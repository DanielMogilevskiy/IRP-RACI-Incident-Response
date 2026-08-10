SEVERITY_LEVELS = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Critical": 4,
}


def calculate_severity(
    business_impact: str,
    data_exposure: str,
    regulatory_impact: str,
    confidentiality: str,
    integrity: str,
    availability: str,
    affected_users: int,
    privileged_account: bool,
    public_exposure: bool,
    financial_impact: str,
) -> dict:
    """
    Calculate incident severity using multiple impact factors.

    Returns:
        A dictionary containing score, severity, priority,
        escalation level, response SLA and required stakeholders.
    """

    score = 0

    # Core impact factors
    score += SEVERITY_LEVELS.get(business_impact, 1)
    score += SEVERITY_LEVELS.get(data_exposure, 1)
    score += SEVERITY_LEVELS.get(regulatory_impact, 1)

    # CIA impact
    score += SEVERITY_LEVELS.get(confidentiality, 1)
    score += SEVERITY_LEVELS.get(integrity, 1)
    score += SEVERITY_LEVELS.get(availability, 1)

    # Financial impact
    score += SEVERITY_LEVELS.get(financial_impact, 1)

    # Affected users
    if affected_users >= 1000:
        score += 4
    elif affected_users >= 100:
        score += 3
    elif affected_users >= 10:
        score += 2
    else:
        score += 1

    # Privileged account compromise
    if privileged_account:
        score += 3

    # Internet/public exposure
    if public_exposure:
        score += 2

    # Severity thresholds
    if score >= 30:
        severity = "Critical"
    elif score >= 22:
        severity = "High"
    elif score >= 14:
        severity = "Medium"
    else:
        severity = "Low"

    # Response priority
    priority_map = {
        "Low": "P4",
        "Medium": "P3",
        "High": "P2",
        "Critical": "P1",
    }

    # Response SLA
    sla_map = {
        "Low": "Best effort",
        "Medium": "Within 8 hours",
        "High": "Within 1 hour",
        "Critical": "Immediate",
    }

    # Escalation level
    escalation_map = {
        "Low": "Security Team",
        "Medium": "Incident Commander",
        "High": "CISO + IT Operations",
        "Critical": "CISO + Executive Management + Legal/Privacy",
    }

    # Required stakeholders
    stakeholder_map = {
        "Low": [
            "Security Analyst",
        ],
        "Medium": [
            "Security Analyst",
            "Incident Commander",
        ],
        "High": [
            "Security Analyst",
            "Incident Commander",
            "CISO",
            "IT Operations",
        ],
        "Critical": [
            "Security Analyst",
            "Incident Commander",
            "CISO",
            "Executive Management",
            "Legal / Privacy",
            "IT Operations",
        ],
    }

    return {
        "score": score,
        "severity": severity,
        "priority": priority_map[severity],
        "response_sla": sla_map[severity],
        "escalation": escalation_map[severity],
        "stakeholders": stakeholder_map[severity],
    }