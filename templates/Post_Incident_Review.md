# Post-Incident Review

## Incident Information

| Field              | Value                    |
| ------------------ | ------------------------ |
| Incident ID        | {{ incident_id }}        |
| Incident Title     | {{ title }}              |
| Severity           | {{ severity }}           |
| Priority           | {{ priority }}           |
| Incident Commander | {{ incident_commander }} |
| Closure Date       | {{ closure_date }}       |

---

# 1. Executive Summary

{{ executive_summary }}

---

# 2. What Happened?

{{ incident_summary }}

---

# 3. Root Cause

{{ root_cause }}

---

# 4. Detection

### Detection Method

{{ detection_method }}

### Detection Effectiveness

{{ detection_effectiveness }}

### Detection Gap

{{ detection_gap }}

---

# 5. Response Assessment

## What Worked Well

{{ what_worked }}

## What Did Not Work

{{ what_failed }}

---

# 6. Containment Assessment

{{ containment_assessment }}

---

# 7. Eradication Assessment

{{ eradication_assessment }}

---

# 8. Recovery Assessment

{{ recovery_assessment }}

---

# 9. Governance Assessment

### RACI

Was the RACI model followed?

{{ raci_assessment }}

### Escalation

Was escalation performed according to the escalation matrix?

{{ escalation_assessment }}

### Regulatory Assessment

Was the regulatory/privacy impact assessed?

{{ regulatory_assessment }}

---

# 10. Lessons Learned

{{ lessons_learned }}

---

# 11. Corrective Action Plan

| Action         | Owner         | Priority         | Due Date         | Status         | Evidence         |
| -------------- | ------------- | ---------------- | ---------------- | -------------- | ---------------- |
| {{ action_1 }} | {{ owner_1 }} | {{ priority_1 }} | {{ due_date_1 }} | {{ status_1 }} | {{ evidence_1 }} |
| {{ action_2 }} | {{ owner_2 }} | {{ priority_2 }} | {{ due_date_2 }} | {{ status_2 }} | {{ evidence_2 }} |
| {{ action_3 }} | {{ owner_3 }} | {{ priority_3 }} | {{ due_date_3 }} | {{ status_3 }} | {{ evidence_3 }} |

---

# 12. Control Improvements

Recommended improvements:

* Security controls
* Monitoring
* Access management
* Incident response procedures
* Security awareness
* Vendor controls
* Logging and detection
* Business continuity

---

# 13. Final Assessment

**Incident Response Effectiveness:** {{ effectiveness_rating }}

**Residual Risk:** {{ residual_risk }}

**Further Management Action Required:** {{ management_action }}

---

## Approval

**Incident Commander:** {{ incident_commander }}

**CISO:** {{ ciso }}

**Review Date:** {{ review_date }}
