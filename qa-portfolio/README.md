# David Egwu - QA Portfolio

**Focus:** Software Quality Assurance | Manual Testing | Web & Workflow Validation | Data Quality

This folder contains a risk-based test plan, 26 structured test cases, defect-reporting examples, accessibility and release checklists, a test execution report template, and a small Python utility that validates test-case documentation.

**Portfolio folder:** https://github.com/topboyasian-stack/green-fitness/tree/qa-portfolio/qa-portfolio

- Candidate: David Egwu, Lagos, Nigeria
- Email: davidegwu5@gmail.com
- Phone: +234 815 619 6053
- LinkedIn: https://linkedin.com/in/david-egwu
- GitHub profile: https://github.com/topboyasian-stack
- Demo under test design: https://green-fitness.pages.dev
- Source project: https://github.com/topboyasian-stack/green-fitness

## Portfolio contents

| Area | Artifact | What it demonstrates |
|---|---|---|
| Planning | [Test plan](plans/green-fitness-web-app-test-plan.md) | Scope, risks, assumptions, entry/exit criteria |
| Test design | [Functional test cases](test-cases/functional-test-cases.csv) | Traceable scenarios, priorities, expected results |
| Defect management | [Bug report template](bug-reports/bug-report-template.md) | Reproducible reporting, evidence, severity and priority |
| Defect writing | [Illustrative exercises](bug-reports/illustrative-practice-examples.md) | Examples clearly labelled hypothetical |
| Accessibility | [Responsive/accessibility checklist](checklists/accessibility-responsive-checklist.md) | Keyboard, labels, focus, viewport checks |
| Release quality | [Release checklist](checklists/release-readiness.md) | Risk-based release decisions |
| Reporting | [Execution report template](reports/test-execution-report-template.md) | Results, limitations and recommendation |
| Lightweight automation | [CSV validator](automation/validate_test_cases.py) | Documentation-structure validation |

## Test status and honesty

**The 26 test cases are designed test cases, not evidence that the app has been tested.** All are marked `Not Run`. The sample defect examples are hypothetical writing exercises, not observed defects and must not be represented as real findings. The Python script validates documentation only; it does not execute the website.

The Green Fitness project README states that people, financial figures and telemetry are fictional; check-in and wearable data are simulations; browser local storage is not secure multi-user storage; and the prototype is not ready for real member records or payments. These constraints are explicitly included in the test plan.

## Run the documentation checks

From this folder, run `python automation/validate_test_cases.py test-cases/functional-test-cases.csv`, then `python -m unittest discover -s automation/tests -v`.

## QA approach

Understand requirements and risks; design positive, negative and boundary tests; execute only in an authorised environment; capture reproducible evidence; report defects clearly; retest fixes; run focused regression; and keep verified observations separate from assumptions.