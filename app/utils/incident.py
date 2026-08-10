from datetime import datetime
from typing import Dict, List


INCIDENT_STATUSES = [
    "Open",
    "Investigating",
    "Contained",
    "Eradicated",
    "Recovered",
    "Closed",
]


SEVERITY_LEVELS = [
    "Critical",
    "High",
    "Medium",
    "Low",
]


PRIORITY_LEVELS = {
    "Critical": "P1",
    "High": "P2",
    "Medium": "P3",
    "Low": "P4",
}


RESPONSE_SLA = {
    "Critical": "Immediate",
    "High": "Within 1 hour",
    "Medium": "Within 8 hours",
    "Low": "Best effort",
}


def validate_incident(
    incident: Dict,
) -> List[str]:
    """
    Validate the minimum required fields
    for an incident record.
    """

    errors = []

    required_fields = [
        "incident_id",
        "title",
        "category",
        "severity",
        "status",
    ]

    for field in required_fields:
        value = incident.get(field)

        if value is None or str(value).strip() == "":
            errors.append(
                f"Missing required field: {field}"
            )

    severity = incident.get("severity")

    if severity and severity not in SEVERITY_LEVELS:
        errors.append(
            f"Invalid severity: {severity}"
        )

    status = incident.get("status")

    if status and status not in INCIDENT_STATUSES:
        errors.append(
            f"Invalid status: {status}"
        )

    return errors


def create_incident_id(
    year: int | None = None,
    existing_ids: List[str] | None = None,
) -> str:
    """
    Generate a new incident ID.

    Example:
        INC-2026-001
    """

    if year is None:
        year = datetime.now().year

    if existing_ids is None:
        existing_ids = []

    prefix = f"INC-{year}-"

    numbers = []

    for incident_id in existing_ids:
        if str(incident_id).startswith(prefix):
            try:
                number = int(
                    str(incident_id).split("-")[-1]
                )
                numbers.append(number)
            except ValueError:
                continue

    next_number = (
        max(numbers) + 1
        if numbers
        else 1
    )

    return f"{prefix}{next_number:03d}"


def get_priority(
    severity: str,
) -> str:
    """
    Convert severity into incident priority.
    """

    return PRIORITY_LEVELS.get(
        severity,
        "P4",
    )


def get_response_sla(
    severity: str,
) -> str:
    """
    Return the response SLA associated
    with the incident severity.
    """

    return RESPONSE_SLA.get(
        severity,
        "Best effort",
    )


def is_closed(
    status: str,
) -> bool:
    """
    Determine whether an incident is closed.
    """

    return status == "Closed"


def can_transition(
    current_status: str,
    new_status: str,
) -> bool:
    """
    Validate incident lifecycle transitions.
    """

    allowed_transitions = {
        "Open": [
            "Investigating",
        ],
        "Investigating": [
            "Contained",
            "Closed",
        ],
        "Contained": [
            "Eradicated",
        ],
        "Eradicated": [
            "Recovered",
        ],
        "Recovered": [
            "Closed",
        ],
        "Closed": [],
    }

    return new_status in allowed_transitions.get(
        current_status,
        [],
    )


def build_incident_summary(
    incident: Dict,
) -> Dict:
    """
    Create a standardized incident summary
    for reporting and dashboards.
    """

    severity = incident.get(
        "severity",
        "Low",
    )

    return {
        "incident_id": incident.get(
            "incident_id",
            "",
        ),
        "title": incident.get(
            "title",
            "",
        ),
        "severity": severity,
        "priority": get_priority(
            severity
        ),
        "response_sla": get_response_sla(
            severity
        ),
        "status": incident.get(
            "status",
            "Open",
        ),
        "category": incident.get(
            "category",
            "",
        ),
        "affected_asset": incident.get(
            "affected_asset",
            "",
        ),
        "owner": incident.get(
            "owner",
            "",
        ),
    }