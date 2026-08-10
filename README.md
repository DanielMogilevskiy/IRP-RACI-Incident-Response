# 🛡️ Incident Response & GRC Management Platform

> **Portfolio Project 5 — Incident Response Plan (IRP) + RACI**

A portfolio-grade **Governance, Risk & Compliance (GRC)** application for managing information security incidents through a structured, risk-based incident response lifecycle.

Built with **Python, Streamlit and Pandas**, the platform combines incident management, severity assessment, escalation governance, RACI responsibilities, regulatory considerations, post-incident review, and GRC control mapping into a single application.

---

## 🚀 Live Demo

**Streamlit:** `COMING SOON`

**GitHub:** `YOUR_GITHUB_REPOSITORY_URL`

---

## 🎯 Project Objective

The objective of this project is to demonstrate how an organization can establish a structured and auditable Incident Response capability.

The platform translates an Incident Response Plan into a practical GRC workflow:

```text
Incident Detection
        ↓
Initial Triage
        ↓
Risk Assessment
        ↓
Severity Classification
        ↓
Priority / SLA
        ↓
Escalation
        ↓
Containment
        ↓
Eradication
        ↓
Recovery
        ↓
Closure
        ↓
Post-Incident Review
        ↓
Corrective Actions
        ↓
Control Improvement
```

---

# 🧩 Key Capabilities

## Incident Management

* Create and track security incidents
* Unique incident identification
* Incident categorization
* Affected asset tracking
* Business impact assessment
* Affected user tracking
* Incident ownership
* Incident Commander assignment
* Incident lifecycle management

## Risk-Based Severity Assessment

The platform evaluates multiple impact dimensions:

* Business Impact
* Confidentiality
* Integrity
* Availability
* Data Exposure
* Regulatory Impact
* Financial Impact
* Affected Users
* Privileged Account Involvement
* Public Exposure

The assessment produces:

```text
Severity
   ↓
Priority
   ↓
Response SLA
   ↓
Escalation Requirements
```

---

# 🚨 Severity & Priority Model

| Severity | Priority | Response SLA   |
| -------- | -------- | -------------- |
| Critical | P1       | Immediate      |
| High     | P2       | Within 1 hour  |
| Medium   | P3       | Within 8 hours |
| Low      | P4       | Best effort    |

Critical incidents may trigger:

* Incident Commander activation
* CISO escalation
* Executive notification
* Legal / Privacy assessment
* Immediate containment
* Continuous response

---

# 👥 RACI Governance

The project implements a formal RACI model covering:

* Detection
* Triage
* Severity assessment
* Incident declaration
* Containment
* Eradication
* Recovery
* Regulatory assessment
* External communication
* Executive escalation
* Closure
* Post-Incident Review

Core roles include:

* Security Analyst
* Incident Commander
* IT Operations
* CISO
* Legal / Privacy
* HR
* Executive Management

The objective is to eliminate ambiguity around **who is Responsible and who is Accountable** during an incident.

---

# 📈 Incident Lifecycle

The application follows a controlled lifecycle:

```text
Open
  ↓
Investigating
  ↓
Contained
  ↓
Eradicated
  ↓
Recovered
  ↓
Closed
```

Lifecycle transitions are validated by application logic rather than allowing arbitrary status changes.

---

# 🔺 Escalation Management

The platform supports risk-based escalation.

Examples of immediate escalation triggers:

* Ransomware
* Sensitive data exposure
* Privileged account compromise
* Critical service disruption
* Significant financial impact
* Potential regulatory notification
* Executive account compromise
* Material third-party incidents

---

# 🔐 GRC & Compliance Alignment

The project is designed around common information security governance practices and demonstrates alignment concepts relevant to:

### ISO/IEC 27001

Examples include:

* Incident management
* Information security event handling
* Responsibilities and accountability
* Evidence and documentation
* Corrective actions
* Monitoring and review
* Control improvement

### GDPR

Where personal data may be involved, the workflow supports:

* Privacy impact assessment
* Regulatory consideration
* Stakeholder escalation
* Documentation of data exposure
* Notification assessment

> This project is a portfolio implementation and does not constitute legal advice or certification evidence.

---

# 🎛️ GRC Control Register

The project includes a control register connecting incident response activities with governance controls.

Example controls:

| Control                         | Purpose                              |
| ------------------------------- | ------------------------------------ |
| Incident Response Plan          | Maintain documented IR capability    |
| Incident Classification         | Apply consistent severity assessment |
| Incident Escalation             | Escalate based on risk               |
| Incident Communication          | Coordinate stakeholders              |
| Evidence Preservation           | Maintain investigation evidence      |
| Post-Incident Review            | Capture lessons learned              |
| Access Review                   | Address access-related weaknesses    |
| Regulatory Assessment           | Evaluate privacy obligations         |
| Third-Party Incident Management | Manage supplier incidents            |
| Incident Metrics                | Monitor response performance         |

---

# 📊 Dashboard

The Streamlit interface provides operational visibility into:

* Total incidents
* Severity distribution
* Priority distribution
* Incident categories
* Incident lifecycle status
* Recent incidents
* Incident trends

The dashboard is designed for both **operational monitoring and management reporting**.

---

# 📝 Post-Incident Review

Significant incidents can be reviewed using a structured PIR process.

The review covers:

* Root cause
* Detection effectiveness
* Response effectiveness
* Containment
* Eradication
* Recovery
* RACI effectiveness
* Escalation effectiveness
* Regulatory assessment
* Lessons learned
* Corrective actions
* Control improvements
* Residual risk

---

# 🧪 Testing

The project includes automated tests covering core incident-management logic.

Test coverage includes:

* Severity mapping
* Priority mapping
* Response SLA
* Incident ID generation
* Input validation
* Lifecycle transitions
* Closure logic
* Incident summaries

Run the tests with:

```bash
python -m pytest
```

Expected result:

```text
12 passed
```

---

# 🏗️ Project Structure

```text
Incident-Response/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── data/
│   │   ├── incidents.csv
│   │   ├── stakeholders.csv
│   │   └── controls.csv
│   │
│   └── utils/
│       ├── __init__.py
│       ├── incident.py
│       ├── reporting.py
│       └── risk.py
│
├── docs/
│   ├── IRP.md
│   ├── RACI.md
│   ├── SEVERITY_MATRIX.md
│   ├── ESCALATION_MATRIX.md
│   ├── INCIDENT_LIFECYCLE.md
│   └── POST_INCIDENT_REVIEW.md
│
├── templates/
│   ├── Incident_Communication.md
│   ├── Incident_Report.md
│   └── Post_Incident_Review.md
│
├── tests/
│   └── test_incident.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# ⚙️ Technology Stack

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python     | Application logic        |
| Streamlit  | Web application          |
| Pandas     | Data management          |
| Plotly     | Data visualization       |
| Pytest     | Automated testing        |
| CSV        | Lightweight data storage |
| Markdown   | GRC documentation        |

---

# 💻 Local Installation

## 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd Incident-Response
```

## 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run tests

```bash
python -m pytest
```

## 5. Start the application

```bash
streamlit run app/app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

# 🔎 Example Incident Scenarios

The application can be used to model scenarios such as:

### Ransomware

```text
Critical
→ P1
→ Immediate response
→ CISO escalation
→ Executive notification
→ Legal / Privacy assessment
```

### Privileged Account Compromise

```text
High / Critical
→ P1/P2
→ Incident Commander
→ IT Operations
→ CISO
→ Access review
→ Evidence preservation
```

### Phishing

```text
Low / Medium / High
→ Risk-based classification
→ Investigation
→ Credential reset
→ Monitoring
→ Lessons learned
```

### Data Exposure

```text
Potential breach
→ Impact assessment
→ Privacy assessment
→ Legal review
→ Regulatory consideration
→ Corrective actions
```

---

# 📚 Documentation

Detailed governance documentation is available in `/docs`.

| Document                  | Purpose                  |
| ------------------------- | ------------------------ |
| `IRP.md`                  | Incident Response Plan   |
| `RACI.md`                 | Roles and accountability |
| `SEVERITY_MATRIX.md`      | Severity methodology     |
| `ESCALATION_MATRIX.md`    | Escalation rules         |
| `INCIDENT_LIFECYCLE.md`   | Incident lifecycle       |
| `POST_INCIDENT_REVIEW.md` | PIR methodology          |

Templates are available in `/templates`.

---

# 🛡️ Security Considerations

This application is designed as a **portfolio and educational GRC project**.

It does not connect to production SIEM, EDR, ticketing, identity, or cloud infrastructure.

No real personal, confidential, or production security data should be entered into the demo environment.

For production use, the application would require additional controls including:

* Authentication
* Authorization / RBAC
* Secure database storage
* Encryption
* Audit logging
* Secrets management
* Backup and recovery
* Input sanitization
* Secure deployment configuration
* Monitoring
* Formal change management

---

# 🔮 Future Improvements

Potential future enhancements include:

* PostgreSQL database
* Role-Based Access Control
* Authentication
* Immutable audit trail
* SIEM integration
* EDR integration
* Email / Teams / Slack notifications
* Automated evidence collection
* SLA breach alerts
* Corrective Action Register
* Risk Register integration
* Vendor incident workflow
* Business Impact Analysis integration
* API layer
* Automated compliance reporting
* ISO 27001 control mapping
* GDPR breach workflow automation

---

# 🎓 Portfolio Skills Demonstrated

This project demonstrates practical knowledge of:

* Governance, Risk & Compliance
* Incident Response Governance
* Risk Assessment
* Incident Classification
* Severity Modeling
* Escalation Management
* RACI
* Security Governance
* Regulatory Assessment
* GDPR considerations
* ISO 27001 concepts
* Control Management
* Evidence Management
* Post-Incident Review
* Corrective Action Management
* KPI / Dashboard Design
* Python
* Streamlit
* Data Management
* Automated Testing
* Git / GitHub
* Technical Documentation

---

# ⚠️ Disclaimer

This project is an independent portfolio project created for educational and demonstration purposes.

It is not an official ISO/IEC 27001 implementation, certification, legal opinion, or substitute for professional incident response or regulatory advice.

---

## Author

**Cybersecurity / GRC Portfolio**

Built as part of a structured cybersecurity GRC portfolio covering:

1. ISO 27001 Checklist & Automation
2. Risk Heatmap
3. Asset Register
4. GDPR Data Mapping
5. **Incident Response Plan + RACI**
6. Vendor Risk Assessment
7. BIA + RTO/RPO

---

⭐ If this project is useful for learning GRC, feel free to explore the repository and documentation.
