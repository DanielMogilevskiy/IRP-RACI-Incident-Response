import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

from utils.risk import calculate_severity
from utils.reporting import (
    add_incident,
    delete_incident,
    incident_exists,
    load_incidents,
    update_incident,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Incident Response Management",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CONSTANTS
# ============================================================

STATUS_OPTIONS = [
    "Open",
    "Investigating",
    "Contained",
    "Eradicated",
    "Recovered",
    "Closed",
]

CATEGORY_OPTIONS = [
    "Phishing",
    "Malware",
    "Account Compromise",
    "Data Breach",
    "Insider Threat",
    "Vulnerability Exploitation",
    "Availability Incident",
    "Third-Party Incident",
]

SEVERITY_ORDER = [
    "Critical",
    "High",
    "Medium",
    "Low",
]

PRIORITY_ORDER = [
    "P1",
    "P2",
    "P3",
    "P4",
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_value(value):
    """Safely format values for display."""

    if pd.isna(value):
        return "N/A"

    if value == "":
        return "N/A"

    return str(value)


def get_status_count(df, status):
    """Return number of incidents with a given status."""

    if df.empty or "status" not in df.columns:
        return 0

    return int((df["status"] == status).sum())


def get_severity_count(df, severity):
    """Return number of incidents with a given severity."""

    if df.empty or "severity" not in df.columns:
        return 0

    return int((df["severity"] == severity).sum())


def safe_dataframe(df):
    """Return a copy prepared for display."""

    if df.empty:
        return df

    display_df = df.copy()

    columns_to_hide = [
        "root_cause",
        "containment_action",
        "resolution_action",
        "lessons_learned",
        "required_stakeholders",
    ]

    existing_columns = [
        column
        for column in columns_to_hide
        if column in display_df.columns
    ]

    if existing_columns:
        display_df = display_df.drop(
            columns=existing_columns
        )

    return display_df


# ============================================================
# LOAD DATA
# ============================================================

incidents = load_incidents()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🛡️ IRP Platform")

    st.caption(
        "GRC Incident Response Management"
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Incident Intake",
            "Incident Register",
            "RACI Matrix",
            "Incident Classification",
            "Escalation Matrix",
            "Post-Incident Review",
        ],
    )

    st.divider()

    st.markdown(
        """
        ### IR Lifecycle

        1. Identification
        2. Triage
        3. Classification
        4. Escalation
        5. Containment
        6. Eradication
        7. Recovery
        8. Closure
        9. Post-Incident Review
        """
    )

    st.divider()

    st.caption(
        "Portfolio Project 5"
    )

    st.caption(
        "Incident Response Plan + RACI"
    )


# ============================================================
# HEADER
# ============================================================

st.title("🛡️ Incident Response Management")
st.caption(
    "GRC Incident Response & RACI Framework"
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.header("📊 Security Incident Dashboard")

    if incidents.empty:

        st.info(
            "No incidents have been recorded yet. "
            "Use Incident Intake to create the first incident."
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Incidents", 0)

        with col2:
            st.metric("Critical", 0)

        with col3:
            st.metric("High", 0)

        with col4:
            st.metric("Open", 0)

    else:

        # ----------------------------------------------------
        # KPI SECTION
        # ----------------------------------------------------

        total_incidents = len(incidents)

        critical_incidents = get_severity_count(
            incidents,
            "Critical",
        )

        high_incidents = get_severity_count(
            incidents,
            "High",
        )

        open_incidents = len(
            incidents[
                incidents["status"].isin(
                    [
                        "Open",
                        "Investigating",
                        "Contained",
                        "Eradicated",
                        "Recovered",
                    ]
                )
            ]
        )

        closed_incidents = get_status_count(
            incidents,
            "Closed",
        )

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(
                "Total Incidents",
                total_incidents,
            )

        with col2:
            st.metric(
                "Critical",
                critical_incidents,
            )

        with col3:
            st.metric(
                "High",
                high_incidents,
            )

        with col4:
            st.metric(
                "Open",
                open_incidents,
            )

        with col5:
            st.metric(
                "Closed",
                closed_incidents,
            )

        st.divider()

        # ----------------------------------------------------
        # SEVERITY DISTRIBUTION
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Incidents by Severity"
            )

            severity_counts = (
                incidents["severity"]
                .value_counts()
                .reindex(
                    SEVERITY_ORDER,
                    fill_value=0,
                )
                .reset_index()
            )

            severity_counts.columns = [
                "Severity",
                "Count",
            ]

            fig = px.bar(
                severity_counts,
                x="Severity",
                y="Count",
                text="Count",
                title="Severity Distribution",
            )

            fig.update_layout(
                xaxis_title="Severity",
                yaxis_title="Incidents",
                showlegend=False,
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
            )

        # ----------------------------------------------------
        # CATEGORY DISTRIBUTION
        # ----------------------------------------------------

        with col2:

            st.subheader(
                "Incidents by Category"
            )

            category_counts = (
                incidents["category"]
                .value_counts()
                .reset_index()
            )

            category_counts.columns = [
                "Category",
                "Count",
            ]

            fig = px.bar(
                category_counts,
                x="Category",
                y="Count",
                text="Count",
                title="Category Distribution",
            )

            fig.update_layout(
                xaxis_title="Category",
                yaxis_title="Incidents",
                showlegend=False,
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
            )

        # ----------------------------------------------------
        # STATUS DISTRIBUTION
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Incidents by Status"
            )

            status_counts = (
                incidents["status"]
                .value_counts()
                .reset_index()
            )

            status_counts.columns = [
                "Status",
                "Count",
            ]

            fig = px.pie(
                status_counts,
                names="Status",
                values="Count",
                title="Incident Lifecycle Status",
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
            )

        # ----------------------------------------------------
        # PRIORITY DISTRIBUTION
        # ----------------------------------------------------

        with col2:

            st.subheader(
                "Incidents by Priority"
            )

            priority_counts = (
                incidents["priority"]
                .value_counts()
                .reindex(
                    PRIORITY_ORDER,
                    fill_value=0,
                )
                .reset_index()
            )

            priority_counts.columns = [
                "Priority",
                "Count",
            ]

            fig = px.bar(
                priority_counts,
                x="Priority",
                y="Count",
                text="Count",
                title="Priority Distribution",
            )

            fig.update_layout(
                xaxis_title="Priority",
                yaxis_title="Incidents",
                showlegend=False,
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
            )

        # ----------------------------------------------------
        # RECENT INCIDENTS
        # ----------------------------------------------------

        st.divider()

        st.subheader(
            "Recent Incidents"
        )

        recent_columns = [
            "incident_id",
            "title",
            "category",
            "severity",
            "priority",
            "status",
            "response_sla",
        ]

        available_columns = [
            column
            for column in recent_columns
            if column in incidents.columns
        ]

        recent_incidents = incidents[
            available_columns
        ].tail(10)

        st.dataframe(
            recent_incidents,
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# INCIDENT INTAKE
# ============================================================

elif page == "Incident Intake":

    st.header("🚨 Incident Intake")

    st.write(
        "Create and assess a security incident using "
        "the risk-based GRC severity engine."
    )

    st.divider()

    # --------------------------------------------------------
    # BASIC INFORMATION
    # --------------------------------------------------------

    st.subheader(
        "1. Incident Information"
    )

    col1, col2 = st.columns(2)

    with col1:

        incident_id = st.text_input(
            "Incident ID",
            value="INC-2026-001",
        )

    with col2:

        category = st.selectbox(
            "Incident Category",
            CATEGORY_OPTIONS,
        )

    title = st.text_input(
        "Incident Title",
        placeholder="Example: Suspected ransomware activity",
    )

    affected_asset = st.text_input(
        "Affected Asset",
        placeholder="Example: Active Directory",
    )

    # --------------------------------------------------------
    # IMPACT ASSESSMENT
    # --------------------------------------------------------

    st.subheader(
        "2. Impact Assessment"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        business_impact = st.selectbox(
            "Business Impact",
            ["Low", "Medium", "High", "Critical"],
        )

        confidentiality = st.selectbox(
            "Confidentiality Impact",
            ["Low", "Medium", "High", "Critical"],
        )

        integrity = st.selectbox(
            "Integrity Impact",
            ["Low", "Medium", "High", "Critical"],
        )

    with col2:

        availability = st.selectbox(
            "Availability Impact",
            ["Low", "Medium", "High", "Critical"],
        )

        data_exposure = st.selectbox(
            "Data Exposure",
            ["Low", "Medium", "High", "Critical"],
        )

        regulatory_impact = st.selectbox(
            "Regulatory Impact",
            ["Low", "Medium", "High", "Critical"],
        )

    with col3:

        financial_impact = st.selectbox(
            "Financial Impact",
            ["Low", "Medium", "High", "Critical"],
        )

        affected_users = st.number_input(
            "Affected Users",
            min_value=0,
            value=1,
            step=1,
        )

    # --------------------------------------------------------
    # SECURITY CONTEXT
    # --------------------------------------------------------

    st.subheader(
        "3. Security Context"
    )

    col1, col2 = st.columns(2)

    with col1:

        privileged_account = st.checkbox(
            "Privileged account involved",
        )

    with col2:

        public_exposure = st.checkbox(
            "Internet / public exposure",
        )

    # --------------------------------------------------------
    # OWNERSHIP
    # --------------------------------------------------------

    st.subheader(
        "4. Governance & Ownership"
    )

    col1, col2 = st.columns(2)

    with col1:

        owner = st.text_input(
            "Incident Owner",
            value="Security Analyst",
        )

    with col2:

        incident_commander = st.text_input(
            "Incident Commander",
            value="Incident Response Lead",
        )

    st.divider()

    # --------------------------------------------------------
    # CREATE INCIDENT
    # --------------------------------------------------------

    if st.button(
        "🔎 Assess & Create Incident",
        type="primary",
        use_container_width=True,
    ):

        if not incident_id.strip():

            st.error(
                "Incident ID is required."
            )

            st.stop()

        if not title.strip():

            st.error(
                "Incident Title is required."
            )

            st.stop()

        if incident_exists(
            incident_id.strip()
        ):

            st.error(
                f"Incident ID {incident_id} already exists."
            )

            st.stop()

        assessment = calculate_severity(
            business_impact=business_impact,
            data_exposure=data_exposure,
            regulatory_impact=regulatory_impact,
            confidentiality=confidentiality,
            integrity=integrity,
            availability=availability,
            affected_users=affected_users,
            privileged_account=privileged_account,
            public_exposure=public_exposure,
            financial_impact=financial_impact,
        )

        severity = assessment["severity"]

        stakeholder_string = ", ".join(
            assessment["stakeholders"]
        )

        now = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        incident = {
            "incident_id": incident_id.strip(),
            "title": title.strip(),
            "category": category,
            "severity": severity,
            "priority": assessment["priority"],
            "severity_score": assessment["score"],
            "response_sla": assessment["response_sla"],
            "status": "Open",
            "detected_at": now,
            "reported_at": now,
            "affected_asset": affected_asset,
            "business_impact": business_impact,
            "confidentiality": confidentiality,
            "integrity": integrity,
            "availability": availability,
            "data_exposure": data_exposure,
            "regulatory_impact": regulatory_impact,
            "financial_impact": financial_impact,
            "affected_users": affected_users,
            "privileged_account": privileged_account,
            "public_exposure": public_exposure,
            "owner": owner,
            "incident_commander": incident_commander,
            "escalation": assessment["escalation"],
            "required_stakeholders": stakeholder_string,
            "root_cause": "",
            "containment_action": "",
            "resolution_action": "",
            "lessons_learned": "",
        }

        add_incident(
            incident
        )

        st.success(
            f"Incident {incident_id} created successfully."
        )

        st.subheader(
            "GRC Assessment Result"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Severity",
                assessment["severity"],
            )

        with col2:
            st.metric(
                "Priority",
                assessment["priority"],
            )

        with col3:
            st.metric(
                "Severity Score",
                assessment["score"],
            )

        with col4:
            st.metric(
                "Response SLA",
                assessment["response_sla"],
            )

        st.warning(
            f"Escalation: {assessment['escalation']}"
        )

        st.info(
            "Required stakeholders: "
            + stakeholder_string
        )


# ============================================================
# INCIDENT REGISTER
# ============================================================

elif page == "Incident Register":

    st.header("📋 Incident Register")

    st.write(
        "Centralized register of security incidents."
    )

    incidents = load_incidents()

    if incidents.empty:

        st.info(
            "No incidents have been recorded yet."
        )

    else:

        # ----------------------------------------------------
        # KPI
        # ----------------------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total",
                len(incidents),
            )

        with col2:

            st.metric(
                "Critical",
                get_severity_count(
                    incidents,
                    "Critical",
                ),
            )

        with col3:

            st.metric(
                "High",
                get_severity_count(
                    incidents,
                    "High",
                ),
            )

        with col4:

            st.metric(
                "Open",
                len(
                    incidents[
                        incidents["status"] != "Closed"
                    ]
                ),
            )

        st.divider()

        # ----------------------------------------------------
        # FILTERS
        # ----------------------------------------------------

        st.subheader(
            "Filters"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            search_term = st.text_input(
                "Search",
                placeholder="Incident ID or title",
            )

        with col2:

            severity_filter = st.multiselect(
                "Severity",
                SEVERITY_ORDER,
            )

        with col3:

            status_filter = st.multiselect(
                "Status",
                STATUS_OPTIONS,
            )

        with col4:

            category_filter = st.multiselect(
                "Category",
                CATEGORY_OPTIONS,
            )

        filtered = incidents.copy()

        if search_term:

            search_term = search_term.lower()

            filtered = filtered[
                filtered["incident_id"]
                .astype(str)
                .str.lower()
                .str.contains(
                    search_term
                )
                |
                filtered["title"]
                .astype(str)
                .str.lower()
                .str.contains(
                    search_term
                )
            ]

        if severity_filter:

            filtered = filtered[
                filtered["severity"].isin(
                    severity_filter
                )
            ]

        if status_filter:

            filtered = filtered[
                filtered["status"].isin(
                    status_filter
                )
            ]

        if category_filter:

            filtered = filtered[
                filtered["category"].isin(
                    category_filter
                )
            ]

        st.subheader(
            f"Results: {len(filtered)}"
        )

        display_df = safe_dataframe(
            filtered
        )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
        )

        # ----------------------------------------------------
        # EXPORT
        # ----------------------------------------------------

        csv_data = filtered.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="⬇️ Export Filtered Register",
            data=csv_data,
            file_name="incident_register.csv",
            mime="text/csv",
        )

        st.divider()

        # ----------------------------------------------------
        # INCIDENT MANAGEMENT
        # ----------------------------------------------------

        st.subheader(
            "Incident Management"
        )

        incident_ids = filtered[
            "incident_id"
        ].astype(str).tolist()

        if incident_ids:

            selected_incident_id = st.selectbox(
                "Select Incident",
                incident_ids,
            )

            selected_rows = incidents[
                incidents["incident_id"].astype(str)
                == selected_incident_id
            ]

            if not selected_rows.empty:

                incident = selected_rows.iloc[0]

                st.markdown(
                    f"### {format_value(incident['incident_id'])}"
                )

                st.write(
                    format_value(
                        incident["title"]
                    )
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.metric(
                        "Severity",
                        format_value(
                            incident["severity"]
                        ),
                    )

                with col2:

                    st.metric(
                        "Priority",
                        format_value(
                            incident["priority"]
                        ),
                    )

                with col3:

                    st.metric(
                        "Score",
                        format_value(
                            incident["severity_score"]
                        ),
                    )

                with col4:

                    st.metric(
                        "Status",
                        format_value(
                            incident["status"]
                        ),
                    )

                st.write(
                    f"**Category:** "
                    f"{format_value(incident['category'])}"
                )

                st.write(
                    f"**Affected Asset:** "
                    f"{format_value(incident['affected_asset'])}"
                )

                st.write(
                    f"**Response SLA:** "
                    f"{format_value(incident['response_sla'])}"
                )

                st.write(
                    f"**Escalation:** "
                    f"{format_value(incident['escalation'])}"
                )

                st.write(
                    f"**Owner:** "
                    f"{format_value(incident['owner'])}"
                )

                st.write(
                    f"**Incident Commander:** "
                    f"{format_value(incident['incident_commander'])}"
                )

                st.divider()

                # ------------------------------------------------
                # STATUS UPDATE
                # ------------------------------------------------

                st.subheader(
                    "Update Incident Status"
                )

                current_status = format_value(
                    incident["status"]
                )

                new_status = st.selectbox(
                    "New Status",
                    STATUS_OPTIONS,
                    index=(
                        STATUS_OPTIONS.index(
                            current_status
                        )
                        if current_status in STATUS_OPTIONS
                        else 0
                    ),
                )

                if st.button(
                    "Update Status",
                    type="primary",
                ):

                    update_incident(
                        selected_incident_id,
                        {
                            "status": new_status,
                        },
                    )

                    st.success(
                        f"Incident {selected_incident_id} "
                        f"updated to {new_status}."
                    )

                    st.rerun()

                st.divider()

                # ------------------------------------------------
                # DELETE
                # ------------------------------------------------

                st.subheader(
                    "Danger Zone"
                )

                confirm_delete = st.checkbox(
                    "I understand that deleting this incident is permanent."
                )

                if st.button(
                    "Delete Incident",
                ):

                    if not confirm_delete:

                        st.error(
                            "Please confirm deletion first."
                        )

                    else:

                        delete_incident(
                            selected_incident_id
                        )

                        st.success(
                            f"Incident {selected_incident_id} deleted."
                        )

                        st.rerun()


# ============================================================
# RACI MATRIX
# ============================================================

elif page == "RACI Matrix":

    st.header("👥 Incident Response RACI")

    st.write(
        "Responsibility and accountability across the incident response lifecycle."
    )

    st.markdown(
        """
        **R — Responsible:** performs the activity.

        **A — Accountable:** owns the final outcome.

        **C — Consulted:** provides expertise or input.

        **I — Informed:** must be kept informed.
        """
    )

    raci_data = {
        "Activity": [
            "Incident Detection",
            "Initial Triage",
            "Severity Assessment",
            "Incident Declaration",
            "Containment",
            "Eradication",
            "Recovery",
            "Regulatory Assessment",
            "External Communication",
            "Employee Communication",
            "Executive Escalation",
            "Incident Closure",
            "Post-Incident Review",
            "Lessons Learned",
        ],
        "Security Analyst": [
            "R",
            "R",
            "R",
            "C",
            "R",
            "R",
            "C",
            "I",
            "I",
            "I",
            "I",
            "C",
            "R",
            "R",
        ],
        "Incident Commander": [
            "I",
            "A",
            "A",
            "R/A",
            "A",
            "A",
            "A",
            "C",
            "C",
            "A",
            "R",
            "R",
            "A",
            "A",
        ],
        "IT Operations": [
            "C",
            "C",
            "C",
            "I",
            "R",
            "R",
            "R",
            "I",
            "I",
            "I",
            "I",
            "C",
            "C",
            "C",
        ],
        "CISO": [
            "I",
            "I",
            "C",
            "C",
            "I",
            "I",
            "I",
            "A",
            "A",
            "C",
            "A",
            "A",
            "C",
            "C",
        ],
        "Legal / Privacy": [
            "I",
            "C",
            "C",
            "C",
            "I",
            "I",
            "I",
            "R",
            "R",
            "C",
            "C",
            "C",
            "C",
            "C",
        ],
        "HR": [
            "I",
            "I",
            "I",
            "I",
            "I",
            "I",
            "I",
            "I",
            "I",
            "R",
            "I",
            "I",
            "C",
            "C",
        ],
        "Executive Management": [
            "I",
            "I",
            "I",
            "I",
            "I",
            "I",
            "I",
            "I",
            "C",
            "I",
            "I",
            "A",
            "I",
            "I",
        ],
    }

    raci_df = pd.DataFrame(
        raci_data
    )

    st.dataframe(
        raci_df,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.info(
        "Governance principle: every significant incident "
        "must have a clearly identified accountable owner."
    )


# ============================================================
# INCIDENT CLASSIFICATION
# ============================================================

elif page == "Incident Classification":

    st.header("🔴 Incident Classification")

    classification_data = {
        "Severity": [
            "Critical",
            "High",
            "Medium",
            "Low",
        ],
        "Priority": [
            "P1",
            "P2",
            "P3",
            "P4",
        ],
        "Description": [
            "Severe business, security or regulatory impact.",
            "Significant business or security impact.",
            "Moderate impact requiring coordinated response.",
            "Limited impact with no significant exposure.",
        ],
        "Response SLA": [
            "Immediate",
            "Within 1 hour",
            "Within 8 hours",
            "Best effort",
        ],
    }

    classification_df = pd.DataFrame(
        classification_data
    )

    st.dataframe(
        classification_df,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader(
        "Classification Criteria"
    )

    st.markdown(
        """
        Severity should consider:

        - Business impact
        - Confidentiality impact
        - Integrity impact
        - Availability impact
        - Data exposure
        - Regulatory impact
        - Financial impact
        - Number of affected users
        - Privileged account involvement
        - Public / internet exposure
        """
    )


# ============================================================
# ESCALATION MATRIX
# ============================================================

elif page == "Escalation Matrix":

    st.header("📢 Escalation Matrix")

    escalation_data = {
        "Severity": [
            "Low",
            "Medium",
            "High",
            "Critical",
        ],
        "Priority": [
            "P4",
            "P3",
            "P2",
            "P1",
        ],
        "Initial Response": [
            "Security Analyst",
            "Security Analyst",
            "Incident Commander",
            "Incident Commander",
        ],
        "Escalation": [
            "Security Team",
            "Incident Commander",
            "CISO + IT Operations",
            "CISO + Executive Management + Legal/Privacy",
        ],
        "Executive Notification": [
            "Not normally required",
            "As required",
            "Required",
            "Immediate",
        ],
    }

    escalation_df = pd.DataFrame(
        escalation_data
    )

    st.dataframe(
        escalation_df,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.subheader(
        "Immediate Escalation Triggers"
    )

    st.markdown(
        """
        Immediate escalation should be considered when an incident involves:

        - Confirmed sensitive data exposure
        - Potential regulatory notification
        - Privileged account compromise
        - Ransomware
        - Major service disruption
        - Significant financial impact
        - Executive or VIP account compromise
        - Material third-party security incident
        - Potential law-enforcement involvement
        """
    )


# ============================================================
# POST-INCIDENT REVIEW
# ============================================================

elif page == "Post-Incident Review":

    st.header("🔍 Post-Incident Review")

    st.write(
        "Complete the review before formally closing a significant incident."
    )

    incidents = load_incidents()

    if incidents.empty:

        st.info(
            "No incidents are available for review."
        )

    else:

        incident_id = st.selectbox(
            "Incident",
            incidents["incident_id"].astype(str).tolist(),
        )

        incident = incidents[
            incidents["incident_id"].astype(str)
            == incident_id
        ].iloc[0]

        st.subheader(
            f"Review: {incident_id}"
        )

        st.write(
            f"**Title:** {format_value(incident['title'])}"
        )

        st.write(
            f"**Severity:** {format_value(incident['severity'])}"
        )

        st.write(
            f"**Status:** {format_value(incident['status'])}"
        )

        st.divider()

        root_cause = st.text_area(
            "Root Cause",
            placeholder="Describe the root cause...",
        )

        what_worked = st.text_area(
            "What Worked Well?",
            placeholder="Describe effective response activities...",
        )

        what_failed = st.text_area(
            "What Failed?",
            placeholder="Describe gaps, delays or control failures...",
        )

        corrective_actions = st.text_area(
            "Corrective Actions",
            placeholder="Describe remediation actions, owners and deadlines...",
        )

        lessons = st.text_area(
            "Lessons Learned",
            placeholder="What should the organization change?",
        )

        if st.button(
            "Complete Post-Incident Review",
            type="primary",
        ):

            update_incident(
                incident_id,
                {
                    "root_cause": root_cause,
                    "containment_action": what_worked,
                    "resolution_action": corrective_actions,
                    "lessons_learned": (
                        lessons
                        + "\n\nWhat failed:\n"
                        + what_failed
                    ),
                    "status": "Closed",
                },
            )

            st.success(
                f"Post-Incident Review completed. "
                f"{incident_id} has been closed."
            )

            st.rerun()