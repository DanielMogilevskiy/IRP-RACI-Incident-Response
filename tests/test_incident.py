from app.utils.incident import (
    INCIDENT_STATUSES,
    SEVERITY_LEVELS,
    build_incident_summary,
    can_transition,
    create_incident_id,
    get_priority,
    get_response_sla,
    is_closed,
    validate_incident,
)


def test_severity_levels():
    assert "Critical" in SEVERITY_LEVELS
    assert "High" in SEVERITY_LEVELS
    assert "Medium" in SEVERITY_LEVELS
    assert "Low" in SEVERITY_LEVELS


def test_incident_statuses():
    assert "Open" in INCIDENT_STATUSES
    assert "Investigating" in INCIDENT_STATUSES
    assert "Contained" in INCIDENT_STATUSES
    assert "Eradicated" in INCIDENT_STATUSES
    assert "Recovered" in INCIDENT_STATUSES
    assert "Closed" in INCIDENT_STATUSES


def test_priority_mapping():
    assert get_priority("Critical") == "P1"
    assert get_priority("High") == "P2"
    assert get_priority("Medium") == "P3"
    assert get_priority("Low") == "P4"


def test_response_sla():
    assert get_response_sla("Critical") == "Immediate"
    assert get_response_sla("High") == "Within 1 hour"
    assert get_response_sla("Medium") == "Within 8 hours"
    assert get_response_sla("Low") == "Best effort"


def test_incident_id_generation():

    existing_ids = [
        "INC-2026-001",
        "INC-2026-002",
        "INC-2026-003",
    ]

    result = create_incident_id(
        2026,
        existing_ids,
    )

    assert result == "INC-2026-004"


def test_first_incident_id():

    result = create_incident_id(
        2026,
        [],
    )

    assert result == "INC-2026-001"


def test_incident_validation():

    incident = {
        "incident_id": "INC-2026-001",
        "title": "Test Incident",
        "category": "Phishing",
        "severity": "High",
        "status": "Open",
    }

    errors = validate_incident(
        incident
    )

    assert errors == []


def test_invalid_incident():

    incident = {
        "incident_id": "",
        "title": "",
        "category": "",
        "severity": "Unknown",
        "status": "Invalid",
    }

    errors = validate_incident(
        incident
    )

    assert len(errors) > 0


def test_lifecycle_transition():

    assert can_transition(
        "Open",
        "Investigating",
    )

    assert can_transition(
        "Investigating",
        "Contained",
    )

    assert can_transition(
        "Contained",
        "Eradicated",
    )

    assert can_transition(
        "Eradicated",
        "Recovered",
    )

    assert can_transition(
        "Recovered",
        "Closed",
    )


def test_invalid_lifecycle_transition():

    assert not can_transition(
        "Open",
        "Closed",
    )

    assert not can_transition(
        "Closed",
        "Investigating",
    )


def test_closed_status():

    assert is_closed("Closed")
    assert not is_closed("Open")


def test_incident_summary():

    incident = {
        "incident_id": "INC-2026-001",
        "title": "Ransomware Incident",
        "category": "Malware",
        "severity": "Critical",
        "status": "Open",
        "affected_asset": "File Server",
        "owner": "Security Analyst",
    }

    summary = build_incident_summary(
        incident
    )

    assert summary["incident_id"] == "INC-2026-001"
    assert summary["severity"] == "Critical"
    assert summary["priority"] == "P1"
    assert summary["response_sla"] == "Immediate"