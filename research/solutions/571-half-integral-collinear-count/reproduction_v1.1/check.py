"""Check complete replay receipts and computed-output algebra without Normaliz."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from replay import (DATA, aggregate_results, canonical_hash, digest, load_groups,
                    sources, validate_record)


def check(output, allow_subset=False):
    if not __debug__:
        raise RuntimeError("Run ordinary Python, without -O")
    output = Path(output)
    if output.is_file():
        bundle = json.loads(output.read_text())
        if bundle["bundle_format_version"] != 1:
            raise ValueError("Unknown replay bundle format")
        manifest = bundle["run"]
        records_in_bundle = bundle["results"]
        manifest_digest = hashlib.sha256(
            (json.dumps(manifest, indent=2) + "\n").encode()).hexdigest()
    else:
        manifest = json.loads((output / "run.json").read_text())
        records_in_bundle = None
        manifest_digest = digest(output / "run.json")
    groups = load_groups()
    context = manifest["context"]
    if context["data_sha256"] != digest(DATA) or context["source_sha256"] != sources():
        raise ValueError("Original data or mathematical source changed")
    if context["runner_sha256"] != digest(HERE / "replay.py"):
        raise ValueError("Replay driver changed")
    selected = context["requested_inputs"]
    if len(selected) != len(set(selected)) or not set(selected) <= set(groups):
        raise ValueError("Invalid requested input list")
    if not allow_subset and set(selected) != set(groups):
        raise ValueError("A subset cannot establish full608 coverage")
    expected_status = "FULL_REPLAY_MATCHED" if len(selected) == 608 else "SUBSET_REPLAY_MATCHED"
    if manifest["status"] != expected_status or manifest["failures"]:
        raise ValueError("Replay did not finish successfully")
    if records_in_bundle is None:
        result_paths = {p.stem: p for p in (output / "results").glob("*.json")}
        records = {key: json.loads(path.read_text()) for key, path in result_paths.items()}
        result_hashes = {key: digest(path) for key, path in result_paths.items()}
    else:
        records = records_in_bundle
        result_hashes = {key: hashlib.sha256(
            (json.dumps(row, indent=2) + "\n").encode()).hexdigest()
            for key, row in records.items()}
    if set(records) != set(selected) or set(manifest["result_sha256"]) != set(selected):
        raise ValueError("Missing, extra or duplicate result")
    for key, row in records.items():
        if result_hashes[key] != manifest["result_sha256"][key]:
            raise ValueError("Result bytes do not match manifest")
        validate_record(row, groups[key], context)
    members = [m for key in records for m in groups[key]["members"]]
    if manifest["completed_inputs"] != len(records) or manifest["completed_cell_members"] != len(members):
        raise ValueError("Coverage counters do not match actual files")
    answer = {"status": expected_status, "unique_inputs": len(records),
              "cell_members": len(members), "data_sha256": context["data_sha256"],
              "context_sha256": canonical_hash(context), "manifest_sha256": manifest_digest,
              "scope": "Checks actual recorded Normaliz results and exact algebra; not a second counting implementation or independent certification"}
    if len(records) == 608:
        if len(members) != 618:
            raise ValueError("Wrong original-cell coverage")
        answer["computed_output_algebra"] = aggregate_results(records, groups)
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--allow-subset", action="store_true")
    args = parser.parse_args()
    print(json.dumps(check(args.output, args.allow_subset), indent=2))
