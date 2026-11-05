"""Regression checks for diagnostic failures; not tests of the theorem."""
import json
from pathlib import Path
import unittest
from fresh_audit_diagnostics import validate_case

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.row = json.loads(Path(__file__).with_name('fresh_audit_diagnostics.json').read_text())['cases'][0]

    def test_recorded_cases(self):
        rows = json.loads(Path(__file__).with_name('fresh_audit_diagnostics.json').read_text())['cases']
        self.assertEqual(len(rows), 21)
        for row in rows:
            validate_case(row)

    def test_broken_phase_is_rejected(self):
        self.row['phase_error'] = 1.0
        with self.assertRaises(ValueError):
            validate_case(self.row)

    def test_nonfinite_values_are_rejected(self):
        for value in (float('nan'), float('inf'), -float('inf')):
            with self.subTest(value=value):
                self.row['energy_identity_relative'] = value
                with self.assertRaises(ValueError):
                    validate_case(self.row)

    def test_energy_increase_is_rejected(self):
        self.row['energy_ratio'] = 1.01
        with self.assertRaises(ValueError):
            validate_case(self.row)

    def test_mass_decrease_is_rejected(self):
        self.row['mass_ratio'] = 0.99
        with self.assertRaises(ValueError):
            validate_case(self.row)

if __name__ == '__main__':
    unittest.main()
