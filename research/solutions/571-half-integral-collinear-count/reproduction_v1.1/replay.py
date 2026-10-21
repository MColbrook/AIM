"""Checkpointed fresh Normaliz replay; expected answers stay in the controller."""
import argparse
import concurrent.futures
import contextlib
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import tempfile
import threading
import time

HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
DATA = PACKAGE / "numerical_case/exact_series.json"
sys.path.insert(0, str(PACKAGE / "src"))
sys.path.insert(0, str(PACKAGE / "numerical_case"))
from exact_algebra import rational_equal, verify_all_action_sums
from verify import verify

PREFIX = "NORMALIZ_REPLAY_RESULT="
STOP = threading.Event()
CHILDREN = {}
CHILD_LOCK = threading.Lock()


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_hash(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def atomic_json(path, value):
    path = Path(path)
    fd, temporary = tempfile.mkstemp(prefix="." + path.name, dir=path.parent)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump(value, stream, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def sources():
    names = ["src/chain_models.py", "src/exact_algebra.py", "numerical_case/verify.py"]
    return {name: digest(PACKAGE / name) for name in names}


def environment():
    import PyNormaliz
    import PyNormaliz_cpp
    site = Path(PyNormaliz.__file__).parent
    native = [Path(PyNormaliz_cpp.__file__)]
    native += sorted((site / "pynormaliz.dylibs").glob("*.dylib"))
    native += sorted((site / "pynormaliz.libs").glob("*.so*"))
    return {"python": sys.version, "implementation": platform.python_implementation(),
            "system": platform.system(), "machine": platform.machine(),
            "pynormaliz": importlib.metadata.version("PyNormaliz"),
            "wrapper_sha256": digest(PyNormaliz.__file__),
            "native_sha256": {p.name: digest(p) for p in native},
            "compiled_normaliz_minor_version": "not exposed by this binding; binary hashes identify the actual implementation"}


def load_groups():
    verify()  # Reconstruct every input, grading and cell assignment first.
    document = json.loads(DATA.read_text())
    return {g["input_sha256"]: g for g in document["groups"]}


def validate_record(row, group, context):
    """Recheck cache contents rather than trusting a stored success boolean."""
    if row["context_sha256"] != canonical_hash(context):
        raise ValueError("Replay context mismatch")
    if row["input_sha256"] != canonical_hash(group["input"]):
        raise ValueError("Input hash mismatch")
    if row.get("status") != "MATCH" or row.get("normaliz_threads") != 1:
        raise ValueError("Unsuccessful or incorrectly threaded result")
    if row["environment_sha256"] != canonical_hash(context["environment"]):
        raise ValueError("Worker software environment mismatch")
    series = row["series"]
    if (not isinstance(series, list) or len(series) != 3
            or not isinstance(series[0], list)
            or not isinstance(series[1], list)
            or any(type(v) is not int for v in series[0] + series[1] + [series[2]])
            or series[2] < 0 or any(v <= 0 for v in series[1])):
        raise ValueError("A series must contain exact integers and positive denominator degrees")
    expected_grade = [group["input"]["grading"][0] + [0], 1]
    if row["grading_readback"] != expected_grade:
        raise ValueError("Original grading mismatch")
    # Normaliz represents the zero series with an empty numerator. Accept an
    # explicit zero numerator too, regardless of its otherwise irrelevant shift.
    actual = [series[0] or [0], series[1], series[2]]
    expected = group["series"]
    expected = [expected[0] or [0], expected[1], expected[2]]
    if not rational_equal(actual, expected):
        raise ValueError("Entire rational function mismatch")
    if row["compute_options"] != context["compute_options"]:
        raise ValueError("Computation options mismatch")


def aggregate_results(records, groups):
    action_records = {name: [] for name in ("identity", "H", "V", "HV")}
    for key, row in records.items():
        for member in groups[key]["members"]:
            action_records[member["action"]].append(row["series"])
    return verify_all_action_sums(action_records)


def worker():
    """Only constraints and options enter this process; no expected series."""
    request = json.load(sys.stdin)
    resource.setrlimit(resource.RLIMIT_CPU, (math.ceil(request["timeout"]),
                                           math.ceil(request["timeout"]) + 2))
    import PyNormaliz as nmz
    nmz.NmzSetNumberOfNormalizThreads(1)
    payload = request["input"]
    start = time.monotonic()
    cone = nmz.Cone(**{k: v for k, v in payload.items() if v})
    built = time.monotonic()
    if not cone.Compute(*request["options"]) or not cone.IsComputed("HilbertSeries"):
        raise RuntimeError("Normaliz did not compute a Hilbert series")
    computed = time.monotonic()
    series, grade = cone.HilbertSeries(), cone.Grading()
    done = time.monotonic()
    usage = resource.getrusage(resource.RUSAGE_SELF)
    rss = usage.ru_maxrss * (1 if sys.platform == "darwin" else 1024)
    row = {"input_sha256": canonical_hash(payload), "series": series,
           "grading_readback": grade, "normaliz_threads": 1,
           "environment_sha256": canonical_hash(environment()),
           "compute_options": request["options"], "worker_pid": os.getpid(),
           "seconds": done - start, "cpu_seconds": usage.ru_utime + usage.ru_stime,
           "construction_seconds": built - start, "compute_seconds": computed - built,
           "readback_seconds": done - computed, "peak_rss_bytes": rss}
    print(PREFIX + json.dumps(row), flush=True)


def compute_one(key, group, context, timeout):
    command = [sys.executable, "-B", str(HERE / "replay.py"), "--worker"]
    env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1",
               MKL_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
    request = {"input": group["input"], "options": context["compute_options"],
               "timeout": timeout}
    start = time.monotonic()
    with CHILD_LOCK:
        if STOP.is_set():
            return {"status": "INTERRUPTED", "input_sha256": key}
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True, env=env,
                                   start_new_session=True)
        CHILDREN[process.pid] = process
    try:
        try:
            stdout, stderr = process.communicate(json.dumps(request), timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate()
            return {"status": "TIMEOUT", "input_sha256": key,
                    "wall_seconds": time.monotonic() - start,
                    "stdout": stdout, "stderr": stderr, "timeout_seconds": timeout}
        if process.returncode:
            return {"status": "ERROR", "input_sha256": key, "exit_code": process.returncode,
                    "wall_seconds": time.monotonic() - start, "stdout": stdout, "stderr": stderr}
        lines = [line[len(PREFIX):] for line in stdout.splitlines() if line.startswith(PREFIX)]
        if len(lines) != 1:
            raise ValueError("Missing or repeated worker result")
        row = json.loads(lines[0])
        row.update(status="MATCH", context_sha256=canonical_hash(context),
                   wall_seconds=time.monotonic() - start, finished_utc=utc(),
                   stderr=stderr, stdout_before_result="\n".join(
                       line for line in stdout.splitlines() if not line.startswith(PREFIX)))
        validate_record(row, group, context)
        return row
    except Exception as error:
        return {"status": "ERROR", "input_sha256": key,
                "error": repr(error), "wall_seconds": time.monotonic() - start}
    finally:
        with CHILD_LOCK:
            CHILDREN.pop(process.pid, None)


def stop_children():
    with CHILD_LOCK:
        for process in CHILDREN.values():
            if process.poll() is None:
                with contextlib.suppress(ProcessLookupError):
                    os.killpg(process.pid, signal.SIGTERM)


def controller(args):
    if not __debug__:
        raise RuntimeError("Run ordinary Python, without -O")
    if args.workers < 1 or not math.isfinite(args.timeout) or args.timeout <= 0:
        raise ValueError("Positive workers and finite positive per-system timeout required")
    groups = load_groups()
    selected = sorted(set(args.only) if args.only else groups)
    if not selected or not set(selected) <= set(groups):
        raise ValueError("Unknown or empty input selection")
    options = ["HilbertSeries", "BigInt", "NoGradingDenom"]
    if args.strategy == "dual":
        options.append("DualMode")
    context = {"data_sha256": digest(DATA), "source_sha256": sources(),
               "runner_sha256": digest(HERE / "replay.py"),
               "environment": environment(), "compute_options": options,
               "requested_inputs": selected}
    output = args.output.resolve()
    if output.exists() and not args.resume:
        raise FileExistsError("Output exists; use --resume to validate and continue it")
    if args.resume and not output.exists():
        raise FileNotFoundError("Resume directory does not exist")
    output.mkdir(parents=True, exist_ok=True)
    with (output / ".controller.lock").open("a+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("Another controller owns this output directory") from None
        return run_locked(args, output, groups, selected, context)


def run_locked(args, output, groups, selected, context):
    results_dir = output / "results"
    attempts_dir = output / "attempts"
    results_dir.mkdir(exist_ok=True)
    attempts_dir.mkdir(exist_ok=True)
    manifest_path = output / "run.json"
    if args.resume:
        manifest = json.loads(manifest_path.read_text())
        if manifest["context"] != context:
            raise ValueError("Resume requires identical inputs, source, software and options")
    else:
        manifest = {"schema_version": 1, "created_utc": utc(), "context": context,
                    "evidence_scope": "Author-side fresh Normaliz replay; not independent human or formal certification",
                    "target_unique_inputs": 608, "target_cell_members": 618}
    records = {}
    for path in sorted(results_dir.glob("*.json")):
        key = path.stem
        if key not in selected or key in records:
            raise ValueError("Unexpected or duplicate cached input")
        row = json.loads(path.read_text())
        validate_record(row, groups[key], context)
        records[key] = row
    pending = sorted(set(selected) - set(records),
                     key=lambda k: (-len(groups[k]["input"]["grading"][0]), k))
    reused = len(records)
    failures = []
    start = time.monotonic()
    STOP.clear()
    previous_handlers = {sig: signal.signal(sig, lambda *_: STOP.set())
                         for sig in (signal.SIGINT, signal.SIGTERM)}

    def save_progress(status):
        with CHILD_LOCK:
            pids = sorted(CHILDREN)
        manifest.update(status=status, updated_utc=utc(), workers=args.workers,
                        timeout_seconds=args.timeout, controller_pid=os.getpid(),
                        worker_pids=pids, requested_inputs=len(selected),
                        completed_inputs=len(records),
                        completed_cell_members=sum(len(groups[k]["members"]) for k in records),
                        cached_inputs_validated=reused, failures=failures,
                        invocation_wall_seconds=time.monotonic() - start,
                        result_sha256={k: digest(results_dir / (k + ".json")) for k in sorted(records)})
        atomic_json(manifest_path, manifest)

    try:
        save_progress("RUNNING")
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            active = {}
            while pending or active:
                if STOP.is_set():
                    stop_children()
                while pending and len(active) < args.workers and not STOP.is_set() and not failures:
                    key = pending.pop(0)
                    active[pool.submit(compute_one, key, groups[key], context, args.timeout)] = key
                if not active:
                    break
                done, _ = concurrent.futures.wait(active, timeout=1,
                         return_when=concurrent.futures.FIRST_COMPLETED)
                for future in done:
                    key = active.pop(future)
                    row = future.result()
                    attempt = attempts_dir / (key + "-" + str(time.time_ns()) + ".json")
                    atomic_json(attempt, row)
                    if row["status"] == "MATCH":
                        atomic_json(results_dir / (key + ".json"), row)
                        records[key] = row
                    else:
                        failures.append({"input_sha256": key, "status": row["status"],
                                         "attempt": attempt.name})
                    print(json.dumps({"completed": len(records), "requested": len(selected),
                                      "input_sha256": key, "status": row["status"],
                                      "seconds": row.get("seconds")}), flush=True)
                if done or int(time.monotonic() - start) % 10 == 0:
                    save_progress("RUNNING")
        if len(records) == len(selected) and not failures:
            if len(selected) == 608:
                manifest["computed_output_algebra"] = aggregate_results(records, groups)
                status = "FULL_REPLAY_MATCHED"
            else:
                status = "SUBSET_REPLAY_MATCHED"
        else:
            status = "INTERRUPTED" if STOP.is_set() else "INCOMPLETE"
        save_progress(status)
        print(json.dumps({"status": status, "completed": len(records),
                          "requested": len(selected), "failures": len(failures)}), flush=True)
        return 0 if status in ("FULL_REPLAY_MATCHED", "SUBSET_REPLAY_MATCHED") else 1
    finally:
        stop_children()
        for sig, handler in previous_handlers.items():
            signal.signal(sig, handler)


def main():
    if sys.argv[1:] == ["--worker"]:
        worker()
        return 0
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--timeout", type=float, default=900,
                        help="Per-system wall and CPU limit in seconds; failures remain incomplete")
    parser.add_argument("--strategy", choices=("default", "dual"), default="default")
    parser.add_argument("--only", action="append", metavar="INPUT_SHA256",
                        help="Select a subset for diagnostics; never reports full coverage")
    parser.add_argument("--resume", action="store_true")
    return controller(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
