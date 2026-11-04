# Release Readiness Checklist

This checklist is a decision aid, not an automatic release approval.

## Scope and quality
- [ ] Intended change and acceptance criteria are documented.
- [ ] Affected journeys and dependencies are identified.
- [ ] Smoke tests have recorded results in the target environment.
- [ ] Critical/high-risk test cases have recorded results.
- [ ] Targeted regression is complete for affected areas.
- [ ] Failed, blocked and not-run tests are visible in the report.

## Defects
- [ ] No unresolved critical defects.
- [ ] High-severity defects are fixed or accepted by an authorised owner.
- [ ] Fixes have been retested against original reproduction steps.
- [ ] Regression around each fix is recorded.

## User experience and accessibility
- [ ] Key responsive widths reviewed.
- [ ] Primary keyboard journeys tested.
- [ ] Inputs, validation messages and status indicators are understandable.
- [ ] Content, dates, currency and labels are consistent.

## Data, privacy and integrations
- [ ] Only approved test data was used.
- [ ] Screenshots/logs contain no credentials, tokens or unnecessary personal data.
- [ ] Mocked/simulated integrations are clearly labelled.
- [ ] External integrations are not called working unless tested with permission.

## Decision
- **Recommendation:** Release / Release with known issues / Hold / Not assessed
- **Evidence/report link:**
- **Open risks:**
- **Decision owner:**
- **Date/time:**

Completing this checklist without evidence does not establish that the product is ready to release.