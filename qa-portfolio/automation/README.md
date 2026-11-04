# Test-Case Documentation Validator

A small Python 3 utility using only the standard library. It checks required columns, non-empty fields, unique case IDs, supported priority labels and supported execution statuses.

From this folder's root, run:

    python automation/validate_test_cases.py test-cases/functional-test-cases.csv
    python -m unittest discover -s automation/tests -v

The tool validates documentation structure only. It does not launch a browser, execute the Green Fitness web app or prove that any listed test case passes.