from pathlib import Path

import pandas as pd


# ============================================================
# DATA CONFIGURATION
# ============================================================

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "incidents.csv"
)


COLUMNS = [
    "incident_id",
    "title",
    "category",
    "severity",
    "priority",
    "severity_score",
    "response_sla",
    "status",
    "detected_at",
    "reported_at",
    "affected_asset",
    "business_impact",
    "confidentiality",
    "integrity",
    "availability",
    "data_exposure",
    "regulatory_impact",
    "financial_impact",
    "affected_users",
    "privileged_account",
    "public_exposure",
    "owner",
    "incident_commander",
    "escalation",
    "required_stakeholders",
    "root_cause",
    "containment_action",
    "resolution_action",
    "lessons_learned",
]


# ============================================================
# LOAD INCIDENTS
# ============================================================

def load_incidents() -> pd.DataFrame:
    """
    Load incidents from the CSV register.

    Returns:
        pandas DataFrame containing all incidents.
    """

    if not DATA_FILE.exists():
        return pd.DataFrame(columns=COLUMNS)

    try:
        df = pd.read_csv(DATA_FILE)
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return pd.DataFrame(columns=COLUMNS)

    if df.empty:
        return pd.DataFrame(columns=COLUMNS)

    # Make sure all expected columns exist.
    for column in COLUMNS:
        if column not in df.columns:
            df[column] = ""

    # Keep the expected column order.
    df = df[COLUMNS]

    return df


# ============================================================
# SAVE INCIDENTS
# ============================================================

def save_incidents(df: pd.DataFrame) -> None:
    """
    Save the incident register to CSV.
    """

    DATA_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Make sure all expected columns exist.
    for column in COLUMNS:
        if column not in df.columns:
            df[column] = ""

    df = df[COLUMNS]

    df.to_csv(
        DATA_FILE,
        index=False,
    )


# ============================================================
# CHECK INCIDENT ID
# ============================================================

def incident_exists(
    incident_id: str,
) -> bool:
    """
    Check whether an incident ID already exists.
    """

    df = load_incidents()

    if df.empty:
        return False

    incident_ids = (
        df["incident_id"]
        .astype(str)
        .str.strip()
    )

    return incident_id.strip() in incident_ids.values


# ============================================================
# ADD INCIDENT
# ============================================================

def add_incident(
    incident: dict,
) -> pd.DataFrame:
    """
    Add a new incident to the register.
    """

    incident_id = str(
        incident.get(
            "incident_id",
            "",
        )
    ).strip()

    if not incident_id:
        raise ValueError(
            "Incident ID is required."
        )

    if incident_exists(incident_id):
        raise ValueError(
            f"Incident ID {incident_id} already exists."
        )

    df = load_incidents()

    new_incident = {}

    for column in COLUMNS:
        new_incident[column] = incident.get(
            column,
            "",
        )

    new_row = pd.DataFrame(
        [new_incident]
    )

    df = pd.concat(
        [
            df,
            new_row,
        ],
        ignore_index=True,
    )

    save_incidents(df)

    return df


# ============================================================
# UPDATE INCIDENT
# ============================================================

def update_incident(
    incident_id: str,
    updates: dict,
) -> pd.DataFrame:
    """
    Update an existing incident.
    """

    df = load_incidents()

    if df.empty:
        return df

    mask = (
        df["incident_id"]
        .astype(str)
        .str.strip()
        == incident_id.strip()
    )

    if not mask.any():
        return df

    for column, value in updates.items():

        if column in COLUMNS:
            df.loc[
                mask,
                column,
            ] = value

    save_incidents(df)

    return df


# ============================================================
# DELETE INCIDENT
# ============================================================

def delete_incident(
    incident_id: str,
) -> pd.DataFrame:
    """
    Delete an incident from the register.
    """

    df = load_incidents()

    if df.empty:
        return df

    df = df[
        df["incident_id"]
        .astype(str)
        .str.strip()
        != incident_id.strip()
    ]

    save_incidents(df)

    return df