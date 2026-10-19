"""Adversarial receipt/cache controls. Fixtures are not computation evidence."""
import copy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import replay
from check import check
from bundle import export_bundle


class ReceiptControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.groups = replay.load_groups()

    def fixture(self, directory, keys=None):
        keys = sorted(self.groups) if keys is None else sorted(keys)
        context = {"data_sha256": replay.digest(replay.DATA),
                   "source_sha256": replay.sources(),
                   "runner_sha256": replay.digest(HERE / "replay.py"),
                   "environment": {"test_fixture_only": True},
                   "compute_options": ["HilbertSeries", "BigInt", "NoGradingDenom"],
                   "requested_inputs": keys}
        result_dir = directory / "results"
        result_dir.mkdir()
        hashes = {}
        for key in keys:
            group = self.groups[key]
            row = {"status": "MATCH", "input_sha256": key,
                   "context_sha256": replay.canonical_hash(context),
                   "environment_sha256": replay.canonical_hash(context["environment"]),
                   "normaliz_threads": 1, "compute_options": context["compute_options"],
                   "series": copy.deepcopy(group["series"]),
                   "grading_readback": copy.deepcopy(group["grading_readback"])}
            path = result_dir / (key + ".json")
            replay.atomic_json(path, row)
            hashes[key] = replay.digest(path)
        manifest = {"context": context, "status": "FULL_REPLAY_MATCHED" if len(keys) == 608
                    else "SUBSET_REPLAY_MATCHED", "failures": [],
                    "completed_inputs": len(keys),
                    "completed_cell_members": sum(len(self.groups[k]["members"]) for k in keys),
                    "result_sha256": hashes}
        replay.atomic_json(directory / "run.json", manifest)
        return manifest

    def test_complete_fixture_checks_without_normaliz(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            with patch.object(replay, "environment", side_effect=RuntimeError("must not import Normaliz")):
                answer = check(directory)
            self.assertEqual((answer["unique_inputs"], answer["cell_members"]), (608, 618))

    def test_missing_result_rejected_even_with_success_label(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            next((directory / "results").glob("*.json")).unlink()
            with self.assertRaisesRegex(ValueError, "Missing"):
                check(directory)

    def test_full_bundle_preserves_all_receipts_and_algebra(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            destination = directory / "bundle.json"
            expected = check(directory)
            self.assertEqual(export_bundle(directory, destination), expected)
            self.assertEqual(check(destination), expected)
            altered = json.loads(destination.read_text())
            altered["results"].pop(next(iter(altered["results"])))
            replay.atomic_json(destination, altered)
            with self.assertRaisesRegex(ValueError, "Missing"):
                check(destination)

    def test_tampered_result_rejected_after_manifest_rehash(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            manifest = self.fixture(directory)
            key = next(iter(manifest["result_sha256"]))
            path = directory / "results" / (key + ".json")
            row = json.loads(path.read_text())
            row["series"][0][0] += 1
            replay.atomic_json(path, row)
            manifest["result_sha256"][key] = replay.digest(path)
            replay.atomic_json(directory / "run.json", manifest)
            with self.assertRaisesRegex(ValueError, "rational function mismatch"):
                check(directory)

    def test_wrong_grade_rejected(self):
        key = next(iter(self.groups))
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            manifest = self.fixture(directory, [key])
            row = json.loads((directory / "results" / (key + ".json")).read_text())
            row["grading_readback"][1] = 2
            with self.assertRaisesRegex(ValueError, "grading mismatch"):
                replay.validate_record(row, self.groups[key], manifest["context"])

    def test_empty_and_explicit_zero_numerators_agree(self):
        key = next(k for k, g in self.groups.items() if not g["series"][0])
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            manifest = self.fixture(directory, [key])
            row = json.loads((directory / "results" / (key + ".json")).read_text())
            row["series"] = [[0], [], 0]
            replay.validate_record(row, self.groups[key], manifest["context"])

    def test_float_is_not_accepted_as_exact_integer_evidence(self):
        key = next(iter(self.groups))
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            manifest = self.fixture(directory, [key])
            row = json.loads((directory / "results" / (key + ".json")).read_text())
            row["series"][0][0] = float(row["series"][0][0])
            with self.assertRaisesRegex(ValueError, "exact integers"):
                replay.validate_record(row, self.groups[key], manifest["context"])

    def test_subset_cannot_claim_complete_coverage(self):
        key = next(iter(self.groups))
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.fixture(directory, [key])
            with self.assertRaisesRegex(ValueError, "subset"):
                check(directory)

    def test_resume_revalidates_and_reuses_completed_result(self):
        key = next(iter(self.groups))
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            manifest = self.fixture(directory, [key])
            args = SimpleNamespace(output=directory, resume=True, only=[key],
                                   workers=1, timeout=60, strategy="default")
            with patch.object(replay, "environment", return_value=manifest["context"]["environment"]), \
                 patch.object(replay, "compute_one", side_effect=RuntimeError("cache must be reused")):
                self.assertEqual(replay.controller(args), 0)

    def test_resume_rejects_different_algorithm_options(self):
        key = next(iter(self.groups))
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            manifest = self.fixture(directory, [key])
            args = SimpleNamespace(output=directory, resume=True, only=[key],
                                   workers=1, timeout=60, strategy="dual")
            with patch.object(replay, "environment", return_value=manifest["context"]["environment"]):
                with self.assertRaisesRegex(ValueError, "identical"):
                    replay.controller(args)

    def test_failed_worker_never_counts_as_complete(self):
        key = next(iter(self.groups))
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "new"
            args = SimpleNamespace(output=directory, resume=False, only=[key],
                                   workers=1, timeout=60, strategy="default")
            failure = {"status": "TIMEOUT", "input_sha256": key}
            with patch.object(replay, "environment", return_value={"test_fixture_only": True}), \
                 patch.object(replay, "compute_one", return_value=failure):
                self.assertEqual(replay.controller(args), 1)
            manifest = json.loads((directory / "run.json").read_text())
            self.assertEqual(manifest["completed_inputs"], 0)
            self.assertEqual(manifest["status"], "INCOMPLETE")
            with self.assertRaisesRegex(ValueError, "finish"):
                check(directory, allow_subset=True)


if __name__ == "__main__":
    unittest.main()
