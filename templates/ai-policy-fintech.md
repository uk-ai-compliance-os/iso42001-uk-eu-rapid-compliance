
> **Status:** Production-Ready Template | **Last Updated:** 2026-05-22 | **Next Review:** 2026-08-22 | **Version:** 1.0.0-PROD
# AI Policy Template — UK Fintech
## 📊 For Leadership: 30-Second Business Case

| Without This Template | With This Template |
|---|---|
| £80k–£150k Big Four engagement | £0 template + £8k–£15k bespoke implementation |
| 6–12 months to documented foundation | 5–10 days to board-ready policy |
| FCA enforcement risk: unlimited fines | Structured conformity assessment path |
| No internal audit capability | Audit-ready templates with evidence requirements |

**Certification-ready AI governance for a fraction of traditional cost, delivered before the FCA's Q3 2026 thematic review.**
## ISO 42001 / EU AI Act Aligned | Credit Scoring & Fraud Detection

&gt; **Status:** Production Template v1.0.0 | Last Updated: 2026-05-22
&gt; **Scope:** Organisations using AI/ML for credit decisions, fraud detection, AML monitoring, or algorithmic trading
&gt; **Regulatory Context:** UK FCA expectations, EU AI Act high-risk (Annex III, Section 5), ICO AI auditing framework
&gt; **⚠️ IMPORTANT:** This is a foundation template. Critical sections marked &lt;!-- CUSTOMISATION REQUIRED --&gt; must be tailored to your specific models and data flows. See CONSULTING.md for bespoke adaptation.

---

## 1. Governance & Accountability

### 1.1 AI Governance Board
- The Board retains ultimate accountability for AI system outcomes affecting customers.
- An AI Risk Committee meets monthly to review model performance, drift, and fairness metrics.
- All high-risk AI decisions require human-in-the-loop (HITL) sign-off.

&lt;!-- CUSTOMISATION REQUIRED: Insert your firm's board structure and AI Risk Committee terms of reference here. For tailored governance architecture mapped to your organisational chart, see CONSULTING.md --&gt;

### 1.2 Roles & Responsibilities
| Role | Responsibility |
|------|----------------|
| Chief Risk Officer | Overall AI risk appetite and policy approval |
| ML Engineering Lead | Technical implementation, monitoring, and drift detection |
| Compliance Lead | Regulatory mapping, audit evidence, and certification maintenance |
| Data Protection Officer | Privacy impact assessments and data governance |

&lt;!-- CUSTOMISATION REQUIRED: Map these roles to actual named individuals in your organisation. For RACI matrix customisation, see CONSULTING.md --&gt;

---

## 2. Risk Management (ISO 42001 Annex A / EU AI Act Annex III)

### 2.1 Risk Classification
All AI systems are classified per EU AI Act Annex III:
- **Credit scoring:** High-risk (biometric profiling + access to essential services)
- **Fraud detection:** High-risk if automated decision-making with legal/equivalent effect
- **AML monitoring:** Limited risk (human review required before adverse action)

&lt;!-- CUSTOMISATION REQUIRED: Classify YOUR specific AI systems. Not sure which risk tier applies? Email compliance.architect@protonmail.com for a formal scope diagnostic (£2,500, 48 hours). --&gt;

### 2.2 Risk Assessment Lifecycle
1. **Pre-deployment:** Algorithmic impact assessment (AIA) + bias audit
2. **Deployment:** Real-time monitoring for demographic parity and equalized odds
3. **Post-deployment:** Quarterly model revalidation and fairness reporting

&lt;!-- CUSTOMISATION REQUIRED: Your firm's specific risk assessment methodology and scoring matrix go here. The scoring matrix is customised per engagement based on your model types, data sources, and customer base. Email compliance.architect@protonmail.com for your tailored assessment. --&gt;

---

## 3. Data Governance (EU AI Act Article 10)

### 3.1 Training Data
- Data provenance logs maintained for all training, validation, and test datasets.
- Bias testing conducted on protected characteristics: age, gender, ethnicity, disability status.
- Synthetic data use documented and justified where real data is insufficient.

&lt;!-- CUSTOMISATION REQUIRED: Document YOUR specific training data sources, provenance chains, and bias testing protocols. For data governance architecture tailored to your data flows, see CONSULTING.md --&gt;

### 3.2 Data Quality
- Completeness, accuracy, and timeliness metrics defined per dataset.
- Data cleaning pipelines version-controlled and auditable.

---

## 4. Transparency & Explainability

### 4.1 Customer Communication
- Customers informed when AI is used in credit decisions (Article 52 EU AI Act).
- Right to explanation: Customers may request the main factors influencing an adverse decision.

&lt;!-- CUSTOMISATION REQUIRED: Insert your firm's specific customer communication templates and explanation methodologies. For bespoke transparency framework design, see CONSULTING.md --&gt;

### 4.2 Internal Documentation
- Model cards maintained for every production AI system.
- SHAP/LIME explanations generated for all adverse automated decisions.

&lt;!-- CUSTOMISATION REQUIRED: Your model card templates and explainability tool configurations go here. For custom model card generation aligned to your specific models, see CONSULTING.md --&gt;

---

## 5. Human Oversight

- All high-risk AI outputs flagged for human review before customer notification.
- Override authority clearly assigned to senior underwriters.
- Annual training for all staff interacting with AI outputs.

&lt;!-- CUSTOMISATION REQUIRED: Define YOUR human-in-the-loop protocols, escalation matrices, and training curricula. For HITL architecture customised to your underwriting workflows, see CONSULTING.md --&gt;

---

## 6. Monitoring & Incident Response

### 6.1 Continuous Monitoring
- Model drift detection (PSI, CSI) automated with threshold alerting.
- Fairness metrics reviewed monthly by the AI Risk Committee.

&lt;!-- CUSTOMISATION REQUIRED: Your specific monitoring thresholds, alert configurations, and fairness metric definitions go here. For monitoring architecture tailored to your model portfolio, see CONSULTING.md --&gt;

### 6.2 Incident Classification
| Severity | Example | Response |
|----------|---------|----------|
| Critical | Discriminatory outcome proven | System suspension within 1 hour |
| High | Model drift beyond threshold | Human review queue activated |
| Medium | Data quality anomaly | Engineering ticket, 24h fix target |

&lt;!-- CUSTOMISATION REQUIRED: Your firm's incident response playbooks, RACI matrices, and regulatory notification protocols go here. For incident response architecture customised to your operational model, see CONSULTING.md --&gt;

---

## 7. Third-Party & Vendor AI

- All third-party AI tools (e.g., credit bureaus, fraud platforms) subject to due diligence.
- Vendor contracts include: audit rights, data processing terms, and incident notification SLAs.

&lt;!-- CUSTOMISATION REQUIRED: Your vendor due diligence checklist, contract templates, and vendor risk scoring matrix go here. For vendor AI governance architecture tailored to your supplier base, see CONSULTING.md --&gt;

---

## 8. Record Keeping & Audit Trail

- All documentation retained for **6 years** post-system retirement.
- Audit trail includes: model versions, training data snapshots, decision logs, and fairness reports.

&lt;!-- CUSTOMISATION REQUIRED: Your evidence repository structure, retention schedules, and audit trail architecture go here. For audit-ready evidence repository design, see CONSULTING.md --&gt;

---

## 9. Review & Update

- This policy reviewed **annually** or upon significant regulatory change.
- Next review date: [INSERT DATE]

&lt;!-- CUSTOMISATION REQUIRED: Your review calendar, change control process, and version management protocol go here. For policy lifecycle management architecture, see CONSULTING.md --&gt;

---

## 10. Approval

| Role | Name | Date |
|------|------|------|
| Author | [INSERT] | [DATE] |
| Reviewer | [INSERT] | [DATE] |
| Approver (Board/CRO) | [INSERT] | [DATE] |

---

## 🚨 Need This Customised for Your Organisation?

This template provides the regulatory foundation. Every `<!-- CUSTOMISATION REQUIRED -->` section needs tailoring to your specific:

- AI systems and model types
- Data sources and flows
- Organisational structure and roles
- Risk appetite and thresholds
- Vendor ecosystem
- Customer base and geographic exposure

**I offer chat-only, flat-fee compliance architecture:**

| Service | What's Included | Investment | Timeline |
|---------|----------------|------------|----------|
| **EU AI Act Scope Diagnostic** | Formal scope determination, risk classification, regulatory exposure report | £2,500 | 48 hours |
| **ISO 42001 Rapid Roadmap** | Custom AIMS architecture, policy suite, certification prep | £8,000 | 10 days |
| **Full AIMS Build + Cert Sprint** | Complete documentation, evidence repo, board deck, auditor scripts | £15,000 | 30 days |
| **August 2026 Emergency Sprint** | Compressed 14-day delivery for high-risk systems | £20,000 | 14 days |

📧 **Email:** compliance.architect@protonmail.com

**Include in your email:**
- Company name and sector
- Number of AI systems in production
- EU customer exposure (yes/no)
- Biggest compliance fear right now

⏱️ **Response time:** < 4 hours (UK business hours 09:00–18:00 BST)
🚫 **No calls. No Calendly. No meetings. Chat-based only.

---

*This template is part of the UK-EU AI Compliance OS. For a fully customised policy aligned to your specific models and data flows, see CONSULTING.md.*
