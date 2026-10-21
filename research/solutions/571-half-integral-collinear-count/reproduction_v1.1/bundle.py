"""Package complete replay records into one inspectable JSON file."""
import argparse
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from check import check
from replay import atomic_json


def export_bundle(directory, destination):
    directory, destination = Path(directory), Path(destination)
    if destination.exists():
        raise FileExistsError("Choose a fresh bundle path")
    before = check(directory)
    document = {"bundle_format_version": 1,
                "run": json.loads((directory / "run.json").read_text()),
                "results": {p.stem: json.loads(p.read_text())
                            for p in sorted((directory / "results").glob("*.json"))}}
    atomic_json(destination, document)
    after = check(destination)
    if before != after:
        raise ValueError("Bundle does not preserve the complete verification report")
    return after


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    print(json.dumps(export_bundle(args.directory, args.destination), indent=2))
