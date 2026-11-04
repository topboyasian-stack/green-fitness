# Test Plan - Green Fitness Web Demo

**Prepared by:** David Egwu  
**Purpose:** Portfolio test-design artifact  
**Target:** https://green-fitness.pages.dev  
**Source:** https://github.com/topboyasian-stack/green-fitness  
**Status:** Test design drafted; execution status is Not Run unless a dated report is added.

## 1. Objective
Define a risk-based approach to checking the Green Fitness prototype's member, trainer, owner and wellness workflows, responsive rendering, accessibility basics and clear disclosure of simulated functions.

## 2. Product context and constraints
The project README says member switching is a preview control rather than authentication; QR check-in and wearable data are simulated; coaching records use browser local storage; and the prototype is not ready for real member records or payments. Treat these as explicit constraints. Do not enter real personal, payment or health data.

## 3. In scope
- App shell and available role navigation.
- Member dashboard, sample membership card, workout view, exercise completion and feedback where available.
- Trainer roster, programme draft/edit/review/publish flow and feedback review where available.
- Owner attendance/renewal views and clearly illustrative finance figures.
- Wellness meal logging and simulated wearable display where available.
- Same-browser persistence where the design promises local persistence.
- Responsive checks near 320px, 375px, 768px and 1280px.
- Keyboard navigation, visible focus, input labels, heading structure, text alternatives and colour-independent status cues.
- Disclosure that role switching, check-in and telemetry are demo/simulated.

## 4. Out of scope
- Real authentication, secure multi-user authorisation, production-security certification or penetration testing.
- Real payment processing, live QR scanning, real wearable connections, server persistence or cross-device sync.
- Destructive tests, real member records, or any testing without permission.
- Backend/API claims unless an actual interface is exposed and authorised for testing.

## 5. Test approach
1. **Smoke:** load the app and confirm the app shell and navigation are usable.
2. **Functional:** follow the member, trainer, owner and wellness journeys with fictional/demo records.
3. **Negative/boundary:** check empty or invalid values only where a relevant input exists; record absent controls as Blocked rather than inventing a result.
4. **Regression:** recheck the changed workflow and connected paths after a code change.
5. **Responsive:** test narrow mobile, tablet and desktop widths; record actual environment details.
6. **Accessibility:** operate key paths using keyboard only; inspect focus, labels, headings, text alternatives and status cues.
7. **Persistence:** where local storage is intended, refresh in the same browser profile and clearly state local-only limitations.

## 6. Risks and priority

| Risk | Impact | Priority |
|---|---|---|
| Main screen or navigation fails | Blocks core journeys | P1 - High |
| Trainer publishes a wrong/incomplete plan | Member could see unintended programme data | P1 - High |
| Saved state is not reflected after reopening | Confusing/inconsistent demo behaviour | P2 - Medium |
| Simulated integrations appear to be live | Misleads users about product capability | P1 - High |
| Controls overflow at mobile width | Blocks mobile use | P2 - Medium |
| Focus/labels are inaccessible | Blocks or impairs keyboard/screen-reader use | P2 - Medium |

## 7. Entry criteria
- Target URL/source is available and the test scope is understood.
- Browser/version, viewport and build/commit can be recorded.
- Only fictional demo data is used.
- The target environment is authorised for the planned checks.

## 8. Exit criteria
- Every case has a recorded Pass, Fail, Blocked or Not Run status.
- Failures have repeatable steps and safe evidence or a note explaining why evidence is absent.
- High-severity risks, limitations and untested areas are visible in the report.
- Release advice is based on execution evidence, not test design alone.

## 9. Defect workflow
Record a unique ID, title, environment, preconditions, numbered steps, expected result, actual result, impact, severity, priority, evidence and retest result. Severity describes impact; priority describes urgency. Retest fixes using the same reproduction steps and add targeted regression.

## 10. Reporting
Use [the execution report template](../reports/test-execution-report-template.md). This repository includes test design only; it does not imply completed execution or a release approval.