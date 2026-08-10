# Incident Response RACI

## RACI Definitions

* **R — Responsible:** performs the activity.
* **A — Accountable:** owns the final outcome.
* **C — Consulted:** provides expertise or input.
* **I — Informed:** receives relevant information.

## Responsibility Matrix

| Activity               | Security Analyst | Incident Commander | IT Operations | CISO | Legal / Privacy | HR | Executive Management |
| ---------------------- | ---------------- | ------------------ | ------------- | ---- | --------------- | -- | -------------------- |
| Incident Detection     | R                | I                  | C             | I    | I               | I  | I                    |
| Initial Triage         | R                | A                  | C             | I    | C               | I  | I                    |
| Severity Assessment    | R                | A                  | C             | C    | C               | I  | I                    |
| Incident Declaration   | C                | R/A                | I             | C    | C               | I  | I                    |
| Containment            | R                | A                  | R             | I    | I               | I  | I                    |
| Eradication            | R                | A                  | R             | I    | I               | I  | I                    |
| Recovery               | C                | A                  | R             | I    | I               | I  | I                    |
| Regulatory Assessment  | I                | A                  | I             | A    | R               | I  | I                    |
| External Communication | I                | A                  | I             | A    | R               | I  | C                    |
| Employee Communication | I                | A                  | I             | C    | C               | R  | I                    |
| Executive Escalation   | I                | R                  | I             | A    | C               | I  | I                    |
| Incident Closure       | C                | R                  | C             | A    | C               | I  | I                    |
| Post-Incident Review   | R                | A                  | C             | C    | C               | C  | I                    |
| Lessons Learned        | R                | A                  | C             | C    | C               | C  | I                    |

## Governance Principle

Every significant incident must have:

1. A designated Incident Owner.
2. A designated Incident Commander.
3. A documented severity.
4. A documented escalation path.
5. A clear accountable stakeholder.
6. A documented closure decision.
