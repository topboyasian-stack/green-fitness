#!/usr/bin/env python3
"""Validate QA test-case CSV structure; this does not execute the application."""
import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = [
    "Test Case ID", "Feature", "Scenario", "Priority", "Test Type",
    "Preconditions", "Steps", "Expected Result", "Execution Status", "Evidence / Notes"
]
VALID_PRIORITIES = {"High", "Medium", "Low"}
VALID_STATUSES = {"Not Run", "Pass", "Fail", "Blocked"}

def validate_csv(path):
    errors = []
    try:
        with Path(path).open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                return ["CSV has no header row."], 0
            missing = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
            if missing:
                return ["Missing required columns: " + ", ".join(missing)], 0
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        return [f"Cannot read/parse CSV: {exc}"], 0
    if not rows:
        errors.append("CSV contains no test cases.")
    seen = set()
    for line, row in enumerate(rows, start=2):
        case_id = (row.get("Test Case ID") or "").strip()
        if not case_id:
            errors.append(f"Line {line}: Test Case ID is blank.")
        elif case_id in seen:
            errors.append(f"Line {line}: duplicate Test Case ID {case_id}.")
        seen.add(case_id)
        for col in REQUIRED_COLUMNS:
            if not (row.get(col) or "").strip():
                errors.append(f"Line {line}: {col} is blank.")
        priority = (row.get("Priority") or "").strip()
        if priority not in VALID_PRIORITIES:
            errors.append(f"Line {line}: invalid Priority {priority!r}.")
        status = (row.get("Execution Status") or "").strip()
        if status not in VALID_STATUSES:
            errors.append(f"Line {line}: invalid Execution Status {status!r}.")
    return errors, len(rows)

def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) != 1:
        print("Usage: python validate_test_cases.py <test-cases.csv>")
        return 2
    errors, count = validate_csv(argv[0])
    if errors:
        print(f"Validation FAILED: {len(errors)} issue(s) across {count} test case(s).")
        for error in errors:
            print("- " + error)
        return 1
    print(f"Validation PASSED: {count} test case(s); required fields are present and statuses are valid.")
    print("Note: this checks documentation structure only, not application behaviour.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())