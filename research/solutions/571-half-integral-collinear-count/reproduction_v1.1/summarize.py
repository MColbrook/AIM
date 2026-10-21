"""Validate a finished full replay and export per-system performance records."""
import argparse
from collections import Counter
import csv
import io
import json
from pathlib import Path
import statistics
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from check import check
from replay import atomic_json, load_groups


def summarize(directory):
    directory = Path(directory)
    verified = check(directory)
    manifest = json.loads((directory / "run.json").read_text())
    groups = load_groups()
    records = {p.stem: json.loads(p.read_text())
               for p in (directory / "results").glob("*.json")}
    rows = []
    for key, row in sorted(records.items()):
        group = groups[key]
        rows.append({"input_sha256": key,
                     "members": ";".join(f"{m['action']}:{m['index']}" for m in group["members"]),
                     "variables": len(group["input"]["grading"][0]),
                     "inequalities": len(group["input"]["inhom_inequalities"]),
                     "equations": len(group["input"]["inhom_equations"]),
                     "compute_seconds": row["compute_seconds"],
                     "construction_seconds": row["construction_seconds"],
                     "readback_seconds": row["readback_seconds"],
                     "invocation_wall_seconds": row["wall_seconds"],
                     "cpu_seconds_through_readback": row["cpu_seconds"],
                     "peak_rss_bytes": row["peak_rss_bytes"],
                     "status": row["status"]})
    times = sorted(r["compute_seconds"] for r in rows)
    total = sum(times)
    counts = Counter(m["action"] for g in groups.values() for m in g["members"])
    summary = {"verification": verified, "compute_options": manifest["context"]["compute_options"],
               "environment": manifest["context"]["environment"], "workers": manifest["workers"],
               "normaliz_threads_per_worker": 1, "cell_members_by_action": dict(counts),
               "cached_inputs_reused": manifest["cached_inputs_validated"],
               "controller_invocation_wall_seconds": manifest["invocation_wall_seconds"],
               "sum_compute_seconds": total,
               "sum_cpu_seconds_through_readback": sum(r["cpu_seconds_through_readback"] for r in rows),
               "median_compute_seconds": statistics.median(times),
               "p95_compute_seconds": times[int(0.95 * (len(times) - 1))],
               "max_compute_seconds": max(times),
               "max_worker_peak_rss_bytes": max(r["peak_rss_bytes"] for r in rows),
               "top20_fraction_of_compute_time": sum(times[-20:]) / total,
               "slowest10": sorted(rows, key=lambda r: r["compute_seconds"], reverse=True)[:10],
               "timing_scope": "Single fresh whole-workload run; worker CPU is sampled through numerical readback, before environment hashing. Controller wall includes startup, validation, hashing and checkpoint writes. No controlled whole-workload serial/parallel speedup claim.",
               "trust_boundary": "Same trusted Normaliz implementation. These author-side reruns and the receipt checker are not an independent enumeration algorithm, checked simplicial certificates, human review or Lean verification."}
    atomic_json(directory / "verification.json", verified)
    atomic_json(directory / "benchmark.json", summary)
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    (directory / "per_system.csv").write_text(stream.getvalue())
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    result = summarize(args.directory)
    print(json.dumps({k: result[k] for k in ["workers", "cached_inputs_reused",
          "controller_invocation_wall_seconds", "sum_compute_seconds",
          "max_worker_peak_rss_bytes", "top20_fraction_of_compute_time"]}, indent=2))
