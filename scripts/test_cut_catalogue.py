"""Catalogue regression checks for editorial cuts, using small isolated fixtures."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import catalogue


class CutCatalogueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="aim-cut-catalogue-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.patch = patch.object(catalogue, "ROOT", self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.rows = []
        for number in (1, 2, 3):
            identifier = f"{number:03d}"
            file = f"problems/{identifier}-example.md"
            row = {"id": identifier, "title": f"Example {number}", "area": "Example",
                   "file": file, "status": "Open", "last_checked": "2026-01-01"}
            target = "cut_problems/" + file if number == 2 else file
            path = self.root / target
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# {identifier}. Example {number}\n\n**Area:** Example\n"
                            "**Status:** 🔵 OPEN\n**Last checked:** 2026-01-01\n\n"
                            "## Problem statement\n\nA precise question.\n\n"
                            "## Application\n\nA substantive example.\n\n"
                            "## References\n\n[Source](https://example.org/paper)\n\n"
                            "## Status review\n\nOpen as recorded.\n", encoding="utf-8")
            if number != 2:
                self.rows.append(row)
            else:
                self.cut = {k: v for k, v in row.items() if k != "file"}
                self.cut.update(group="example", original_file=file, record=target,
                                reason="User-authorized editorial cutoff", importance=5,
                                scores={"M": 5, "A": 4, "C": 8, "E": 9})
        self.manifest = {"schema_version": 2,
                         "groups": [{"key": "example", "title": "Examples"}],
                         "batches": [{"key": "first", "title": "First", "ids": ["001", "002", "003"]}],
                         "retired": [], "cut": [self.cut]}
        (self.root / "data").mkdir()
        (self.root / "data/example.json").write_text(json.dumps(self.rows), encoding="utf-8")
        self.save()

    def save(self):
        (self.root / "catalogue.json").write_text(json.dumps(self.manifest), encoding="utf-8")

    def test_registered_cut_preserves_gap_and_next_id(self):
        manifest, errors = catalogue.load_manifest()
        self.assertEqual(errors, [])
        entries, errors = catalogue.load_entries(manifest)
        self.assertEqual(errors, [])
        self.assertEqual(catalogue.validate(entries, manifest), [])
        self.assertEqual(catalogue.next_problem_id(manifest), 4)
        opened, presented = catalogue.presentation_records(entries, manifest)
        self.assertEqual([row["id"] for row in opened], ["001", "003"])
        self.assertEqual(presented["retired"], [])
        self.assertNotIn("| 002 |", catalogue.render_catalog(opened, presented))

    def test_missing_cut_record_is_rejected(self):
        (self.root / self.cut["record"]).unlink()
        self.assertTrue(any("invalid cut record" in error for error in catalogue.load_manifest()[1]))

    def test_public_checkout_keeps_cut_registry_without_local_archive(self):
        self.manifest["local_working_directories"] = ["cut_problems"]
        self.save()
        path = self.root / self.cut["record"]
        path.unlink()
        path.parent.rmdir()
        (self.root / "cut_problems").rmdir()
        manifest, errors = catalogue.load_manifest()
        self.assertEqual(errors, [])
        entries, errors = catalogue.load_entries(manifest)
        self.assertEqual(errors, [])
        self.assertEqual(catalogue.validate(entries, manifest, catalogue_only=True), [])
        self.assertEqual(catalogue.next_problem_id(manifest), 4)
        self.assertEqual(manifest["cut"], [self.cut])

    def test_present_local_archive_is_still_strictly_validated(self):
        self.manifest["local_working_directories"] = ["cut_problems"]
        self.save()
        (self.root / self.cut["record"]).unlink()
        self.assertTrue(any("invalid cut record" in e for e in catalogue.load_manifest()[1]))

    def test_public_directories_cannot_be_declared_optional(self):
        self.manifest["local_working_directories"] = ["problems"]
        self.save()
        self.assertTrue(any("invalid local_working_directories" in e
                            for e in catalogue.load_manifest()[1]))

    def test_score_boundary_and_formula_are_checked(self):
        for values in ({"importance": 6}, {"importance": True},
                       {"scores": {"M": 4, "A": 4, "C": 8, "E": 9}}):
            with self.subTest(values=values):
                self.manifest["cut"] = [{**self.cut, **values}]
                self.save()
                self.assertTrue(catalogue.load_manifest()[1])

    def test_unregistered_cut_id_reuse_is_rejected(self):
        entries = [{**row, "group": "example"} for row in self.rows]
        entries.append({**entries[0], "id": "002"})
        self.assertTrue(any("Duplicate ID" in error for error in catalogue.validate(entries, self.manifest)))

    def add_replacement(self):
        file = "problems/002-replacement.md"
        original = self.root / self.cut["record"]
        (self.root / file).write_text(original.read_text(encoding="utf-8").replace(
            "Example 2", "Replacement"), encoding="utf-8")
        row = {"id": "002", "title": "Replacement", "area": "Example", "file": file,
               "status": "Open", "last_checked": "2026-01-01",
               "source_key": "FURTHER-1234567890abcdef"}
        self.rows.append(row)
        self.cut["replacement"] = {"file": file, "source_key": row["source_key"],
                                   "group": "example", "filled_on": "2026-01-01"}
        (self.root / "data/example.json").write_text(json.dumps(self.rows), encoding="utf-8")
        self.save()

    def test_registered_replacement_keeps_archived_identity_and_fills_id(self):
        self.add_replacement()
        manifest, errors = catalogue.load_manifest()
        self.assertEqual(errors, [])
        entries, errors = catalogue.load_entries(manifest)
        self.assertEqual(errors, [])
        self.assertEqual(catalogue.validate(entries, manifest, catalogue_only=True), [])
        self.assertEqual(catalogue.next_problem_id(manifest), 4)
        self.assertIn("Example 2", (self.root / self.cut["record"]).read_text(encoding="utf-8"))

    def test_replacement_must_match_current_identity_and_subject(self):
        self.add_replacement()
        entries = [{**row, "group": "example"} for row in self.rows]
        replacement = next(row for row in entries if row["id"] == "002")
        for values in ({"source_key": "FURTHER-fedcba0987654321"}, {"group": "other"}):
            with self.subTest(values=values):
                changed = [{**row, **values} if row is replacement else row for row in entries]
                self.assertTrue(any("replacement must match" in error
                                    for error in catalogue.validate(changed, self.manifest)))
        missing = [row for row in entries if row["id"] != "002"]
        self.assertTrue(any("replacement must match" in error
                            for error in catalogue.validate(missing, self.manifest)))

    def test_replacement_does_not_allow_duplicate_current_ids(self):
        self.add_replacement()
        entries = [{**row, "group": "example"} for row in self.rows]
        entries.append(dict(entries[-1]))
        self.assertTrue(any("Duplicate ID" in error for error in catalogue.validate(entries, self.manifest)))

    def test_current_and_retained_resolved_records_share_consecutive_ids(self):
        self.add_replacement()
        row = self.rows.pop(0)
        old = self.root / row["file"]
        target = self.root / "research/001-example.md"
        target.parent.mkdir()
        target.write_text(old.read_text(encoding="utf-8").replace("🔵 OPEN", "⚫ WITHDRAWN"), encoding="utf-8")
        old.unlink()
        retired = {key: value for key, value in row.items() if key != "file"}
        retired.update(group="example", status="Withdrawn", record="research/001-example.md", reason="Fixture")
        self.manifest["retired"].append(retired)
        entries = [{**entry, "group": "example"} for entry in self.rows]
        self.assertEqual(catalogue.validate(entries, self.manifest, catalogue_only=True), [])

    def test_new_page_after_retired_id_preserves_current_and_archived_identities(self):
        self.add_replacement()
        # Retire the highest original ID, leaving a gap in current page numbers.
        row = next(item for item in self.rows if item['id'] == '003')
        self.rows.remove(row)
        original = self.root / row['file']
        retained = self.root / 'research/003-example.md'
        retained.parent.mkdir()
        retained.write_text(original.read_text(encoding='utf-8').replace(
            '🔵 OPEN', '⚫ WITHDRAWN'), encoding='utf-8')
        original.unlink()
        retired = {key: value for key, value in row.items() if key != 'file'}
        retired.update(group='example', status='Withdrawn',
                       record='research/003-example.md', reason='Fixture')
        self.manifest['retired'].append(retired)
        before_cut = json.dumps(self.cut, sort_keys=True)
        before_retired = json.dumps(self.manifest['retired'], sort_keys=True)
        before_pages = {p: p.read_bytes() for directory in ('problems', 'cut_problems', 'research')
                        for p in (self.root / directory).rglob('*.md')}
        self.assertEqual(catalogue.next_problem_id(self.manifest), 4)
        template = self.root / self.rows[0]['file']
        (self.root / 'problems/004-new.md').write_text(
            template.read_text(encoding='utf-8').replace('# 001. Example 1', '# 004. New target'),
            encoding='utf-8')
        self.rows.append({'id': '004', 'title': 'New target', 'area': 'Example',
                          'file': 'problems/004-new.md', 'status': 'Open',
                          'last_checked': '2026-01-01'})
        self.manifest['batches'].append({'key': 'new', 'title': 'New', 'ids': ['004']})
        entries = [{**entry, 'group': 'example'} for entry in self.rows]
        self.assertEqual(catalogue.validate(entries, self.manifest, catalogue_only=True), [])
        self.assertEqual(catalogue.next_problem_id(self.manifest), 5)
        self.assertEqual(json.dumps(self.cut, sort_keys=True), before_cut)
        self.assertEqual(json.dumps(self.manifest['retired'], sort_keys=True), before_retired)
        self.assertTrue(all(path.read_bytes() == content for path, content in before_pages.items()))

    def add_editorial_archive(self):
        self.add_replacement()
        current = next(row for row in self.rows if row["id"] == "002")
        record = "cut_problems/problems/002-prior-replacement.md"
        (self.root / record).write_text((self.root / current["file"]).read_text(encoding="utf-8").replace(
            "Replacement", "Former replacement"), encoding="utf-8")
        self.manifest["editorial_archive"] = [{
            "id": "002", "source_key": "FURTHER-abcdef0123456789", "title": "Former replacement",
            "area": "Example", "group": "example", "status": "Open", "last_checked": "2026-01-01",
            "archived_on": "2026-01-01", "reason": "Explicit editorial choice, scores unchanged",
            "record": record, "replacement_file": current["file"],
            "replacement_source_key": current["source_key"], "importance": 8}]
        self.save()

    def test_editorial_archive_does_not_rewrite_threshold_or_duplicate_current_id(self):
        self.add_editorial_archive()
        manifest, errors = catalogue.load_manifest()
        self.assertEqual(errors, [])
        entries, errors = catalogue.load_entries(manifest)
        self.assertEqual(errors, [])
        self.assertEqual(catalogue.validate(entries, manifest, catalogue_only=True), [])
        self.assertEqual(self.cut["importance"], 5)
        self.assertEqual(manifest["editorial_archive"][0]["importance"], 8)
        self.assertEqual(catalogue.next_problem_id(manifest), 4)

    def test_editorial_archive_requires_distinct_replacement_identity(self):
        self.add_editorial_archive()
        self.manifest["editorial_archive"][0]["source_key"] = "FURTHER-1234567890abcdef"
        entries = [{**entry, "group": "example"} for entry in self.rows]
        self.assertTrue(any("distinct current replacement" in error
                            for error in catalogue.validate(entries, self.manifest)))

    def test_catalogue_only_does_not_hide_registered_page_errors(self):
        entries = [{**row, "group": "example"} for row in self.rows]
        draft = self.root / "draft.md"
        draft.write_text("[historical](missing-draft-file.md)\n", encoding="utf-8")
        self.assertEqual(catalogue.validate(entries, self.manifest, catalogue_only=True), [])
        self.assertTrue(catalogue.validate(entries, self.manifest))
        page = self.root / self.rows[0]["file"]
        page.write_text(page.read_text(encoding="utf-8") + "[Broken](missing.md)\n", encoding="utf-8")
        self.assertTrue(catalogue.validate(entries, self.manifest, catalogue_only=True))

    def add_unissued_archive(self):
        path = self.root / 'cut_problems/FURTHER_problems/example/lead-1234567890abcdef.md'
        path.parent.mkdir(parents=True)
        path.write_text('# Archived candidate\n', encoding='utf8')
        self.manifest['further_archive'] = [{
            'source_key': 'FURTHER-1234567890abcdef', 'title': 'Archived candidate',
            'record': path.relative_to(self.root).as_posix(),
            'original_file': 'FURTHER_problems/example/lead-1234567890abcdef.md',
            'reason': 'Matching full announcement', 'status': 'Solution claimed',
            'archived_on': '2026-01-01', 'review': 'catalogue.json'}]
        self.save()

    def test_unissued_archive_does_not_consume_an_id(self):
        self.add_unissued_archive()
        manifest, errors = catalogue.load_manifest()
        self.assertEqual(errors, [])
        self.assertEqual(catalogue.next_problem_id(manifest), 4)

    def test_unissued_archive_cannot_allocate_an_id(self):
        self.add_unissued_archive()
        self.manifest['further_archive'][0]['id'] = '004'
        self.save()
        self.assertTrue(any('must not allocate' in e for e in catalogue.load_manifest()[1]))

    def test_unissued_archive_cannot_be_reintroduced(self):
        self.add_unissued_archive()
        entries = [{**row, 'group': 'example'} for row in self.rows]
        entries[0]['source_key'] = 'FURTHER-1234567890abcdef'
        self.assertTrue(any('cannot also be' in e for e in catalogue.validate(entries, self.manifest, catalogue_only=True)))


class ContentEvidenceUpdateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='aim-evidence-update-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        verifier_path = Path(__file__).resolve().parents[1] / 'cut_problems/verify_cut.py'
        if not verifier_path.is_file():
            self.skipTest('Local-only archive verifier is not part of the public checkout')
        spec = importlib.util.spec_from_file_location(
            'cut_verifier_fixture', verifier_path)
        self.verifier = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.verifier)
        self.path = self.root / 'problem.md'
        old = '# 001. Fixed identity\n\n## Problem statement\n\nFixed target.\n\n## Application\n\nUse.\n'
        new = old + '\n## Status review\n\nDated new evidence.\n'
        self.path.write_text(new, encoding='utf-8')
        self.before = hashlib.sha256(old.encode()).hexdigest()
        self.row = {'sha256_before': self.before,
                    'sha256_after': self.verifier.digest(self.path),
                    'title': '# 001. Fixed identity',
                    'statement_sha256': hashlib.sha256(b'Fixed target.').hexdigest()}
        root_patch = patch.object(self.verifier, 'ROOT', self.root)
        updates_patch = patch.object(self.verifier, 'load_content_updates',
                                     return_value={'problem.md': self.row})
        root_patch.start()
        updates_patch.start()
        self.addCleanup(root_patch.stop)
        self.addCleanup(updates_patch.stop)

    def test_dated_evidence_preserves_the_frozen_hash_chain(self):
        self.assertEqual(self.verifier.updated_content_hash('problem.md', self.before),
                         self.row['sha256_after'])

    def test_incorrect_original_hash_is_rejected(self):
        with self.assertRaises(AssertionError):
            self.verifier.updated_content_hash('problem.md', '0' * 64)

    def test_new_hash_does_not_authorize_a_changed_problem_statement(self):
        self.path.write_text(self.path.read_text(encoding='utf-8').replace(
            'Fixed target.', 'Different target.'), encoding='utf-8')
        self.row['sha256_after'] = self.verifier.digest(self.path)
        with self.assertRaises(AssertionError):
            self.verifier.updated_content_hash('problem.md', self.before)


class ContentEvidenceHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='aim-evidence-history-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        verifier_path = Path(__file__).resolve().parents[1] / 'cut_problems/verify_cut.py'
        if not verifier_path.is_file():
            self.skipTest('Local-only archive verifier is not part of the public checkout')
        spec = importlib.util.spec_from_file_location(
            'cut_history_fixture', verifier_path)
        self.verifier = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.verifier)
        root_patch = patch.object(self.verifier, 'ROOT', self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.first = {'path': 'problem.md', 'sha256_before': 'a' * 64,
                      'sha256_after': 'b' * 64, 'title': '# 001. Fixed identity',
                      'statement_sha256': 'd' * 64}
        self.second = {**self.first, 'sha256_before': 'b' * 64,
                       'sha256_after': 'c' * 64}

    def save(self):
        for directory, payload in (
                ('upstream-integration-2026-11-03',
                 {'schema': 'AIM_AUTHORITATIVE_LOCAL_UPSTREAM_INTEGRATION_V1',
                  'state': 'applied', 'source_updates': [self.first]}),
                ('solution-status-audit-2026-11-03',
                 {'schema': 'AIM_INDIVIDUAL_SOLUTION_STATUS_AUDIT_V1',
                  'canonical_state': 'applied', 'state': 'in_progress',
                  'source_updates': [self.second]})):
            path = self.root / 'research' / directory / 'manifest.json'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload), encoding='utf-8')

    def test_successive_evidence_updates_preserve_the_original_hash(self):
        self.save()
        row = self.verifier.load_content_updates()['problem.md']
        self.assertEqual(row['sha256_before'], 'a' * 64)
        self.assertEqual(row['sha256_after'], 'c' * 64)

    def test_a_broken_intermediate_hash_is_rejected(self):
        self.second['sha256_before'] = '0' * 64
        self.save()
        with self.assertRaises(AssertionError):
            self.verifier.load_content_updates()

    def test_a_changed_identity_cannot_be_hidden_by_a_later_update(self):
        self.second['statement_sha256'] = '0' * 64
        self.save()
        with self.assertRaises(AssertionError):
            self.verifier.load_content_updates()


if __name__ == "__main__":
    unittest.main()
