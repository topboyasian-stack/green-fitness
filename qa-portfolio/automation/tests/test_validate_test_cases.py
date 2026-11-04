import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_test_cases import validate_csv

class TestCaseCsvValidatorTests(unittest.TestCase):
    def test_portfolio_csv_is_valid(self):
        csv_path = Path(__file__).resolve().parents[2] / "test-cases" / "functional-test-cases.csv"
        errors, count = validate_csv(csv_path)
        self.assertEqual(errors, [])
        self.assertGreaterEqual(count, 20)

    def test_duplicate_ids_are_reported(self):
        content = (
            "Test Case ID,Feature,Scenario,Priority,Test Type,Preconditions,Steps,Expected Result,Execution Status,Evidence / Notes\n"
            "TC-1,A,Scenario,High,Smoke,Start,Step,Expected,Not Run,Note\n"
            "TC-1,B,Scenario,Medium,Functional,Start,Step,Expected,Not Run,Note\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.csv"
            path.write_text(content, encoding="utf-8")
            errors, count = validate_csv(path)
        self.assertEqual(count, 2)
        self.assertTrue(any("duplicate Test Case ID" in error for error in errors))

    def test_missing_expected_result_is_reported(self):
        content = (
            "Test Case ID,Feature,Scenario,Priority,Test Type,Preconditions,Steps,Expected Result,Execution Status,Evidence / Notes\n"
            "TC-1,A,Scenario,High,Smoke,Start,Step,,Not Run,Note\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.csv"
            path.write_text(content, encoding="utf-8")
            errors, count = validate_csv(path)
        self.assertEqual(count, 1)
        self.assertTrue(any("Expected Result is blank" in error for error in errors))

if __name__ == "__main__":
    unittest.main()