# Illustrative Defect-Writing Exercises

**These are hypothetical examples for practicing defect writing. They are not observed Green Fitness defects, are not linked to a real test run, and must not be presented as real bugs found in production.**

## Example A - Hypothetical narrow-screen overflow
- **ID:** EXAMPLE-001 (illustrative only)
- **Title:** [Navigation] A primary action is clipped at a 320px viewport
- **Severity/Priority:** Medium / P2, provisional pending real impact assessment
- **Environment:** Not tested; example only

**Preconditions:** A hypothetical page contains a header and primary action.

**Steps:**
1. Set the viewport to 320px wide.
2. Open the page.
3. Inspect the header and primary action.

**Expected:** The main navigation and primary action fit the viewport and remain usable.

**Actual in this fictional scenario:** The action extends outside the visible viewport.

**Evidence:** None - fictional and not executed.

**Next step on a real product:** Reproduce on a named browser/build, capture a screenshot, check nearby breakpoints and retest after a fix.

## Example B - Hypothetical saved-draft mismatch
- **ID:** EXAMPLE-002 (illustrative only)
- **Title:** [Programme builder] Saved draft displays the previous exercise value after reopening
- **Severity/Priority:** Medium / P2, provisional

**Steps:** Open a sample draft, change one exercise value, save, then reopen.

**Expected:** The latest saved value is displayed.

**Actual in this fictional scenario:** The previous value is displayed.

**Evidence:** None - fictional and not executed.

**Next step on a real product:** Record the field/value, confirm save feedback, preserve evidence and determine whether the behaviour is repeatable.