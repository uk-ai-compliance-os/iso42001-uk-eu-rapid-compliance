# AI Policy Template — UK Fintech
## ISO 42001 / EU AI Act Aligned | Credit Scoring & Fraud Detection

&gt; **Status:** Draft for customization  
&gt; **Scope:** Organizations using AI/ML for credit decisions, fraud detection, AML monitoring, or algorithmic trading  
&gt; **Regulatory Context:** UK FCA expectations, EU AI Act high-risk (Annex III, Section 5), ICO AI auditing framework

---

## 1. Governance & Accountability

### 1.1 AI Governance Board
- The Board retains ultimate accountability for AI system outcomes affecting customers.
- An AI Risk Committee meets monthly to review model performance, drift, and fairness metrics.
- All high-risk AI decisions require human-in-the-loop (HITL) sign-off.

### 1.2 Roles & Responsibilities
| Role | Responsibility |
|------|----------------|
| Chief Risk Officer | Overall AI risk appetite and policy approval |
| ML Engineering Lead | Technical implementation, monitoring, and drift detection |
| Compliance Lead | Regulatory mapping, audit evidence, and certification maintenance |
| Data Protection Officer | Privacy impact assessments and data governance |

---

## 2. Risk Management (ISO 42001 Annex A / EU AI Act Annex III)

### 2.1 Risk Classification
All AI systems are classified per EU AI Act Annex III:
- **Credit scoring:** High-risk (biometric profiling + access to essential services)
- **Fraud detection:** High-risk if automated decision-making with legal/equivalent effect
- **AML monitoring:** Limited risk (human review required before adverse action)

### 2.2 Risk Assessment Lifecycle
1. **Pre-deployment:** Algorithmic impact assessment (AIA) + bias audit
2. **Deployment:** Real-time monitoring for demographic parity and equalized odds
3. **Post-deployment:** Quarterly model revalidation and fairness reporting

---

## 3. Data Governance (EU AI Act Article 10)

### 3.1 Training Data
- Data provenance logs maintained for all training, validation, and test datasets.
- Bias testing conducted on protected characteristics: age, gender, ethnicity, disability status.
- Synthetic data use documented and justified where real data is insufficient.

### 3.2 Data Quality
- Completeness, accuracy, and timeliness metrics defined per dataset.
- Data cleaning pipelines version-controlled and auditable.

---

## 4. Transparency & Explainability

### 4.1 Customer Communication
- Customers informed when AI is used in credit decisions (Article 52 EU AI Act).
- Right to explanation: Customers may request the main factors influencing an adverse decision.

### 4.2 Internal Documentation
- Model cards maintained for every production AI system.
- SHAP/LIME explanations generated for all adverse automated decisions.

---

## 5. Human Oversight

- All high-risk AI outputs flagged for human review before customer notification.
- Override authority clearly assigned to senior underwriters.
- Annual training for all staff interacting with AI outputs.

---

## 6. Monitoring & Incident Response

### 6.1 Continuous Monitoring
- Model drift detection (PSI, CSI) automated with threshold alerting.
- Fairness metrics reviewed monthly by the AI Risk Committee.

### 6.2 Incident Classification
| Severity | Example | Response |
|----------|---------|--------|
| Critical | Discriminatory outcome proven | System suspension within 1 hour |
| High | Model drift beyond threshold | Human review queue activated |
| Medium | Data quality anomaly | Engineering ticket, 24h fix target |

---

## 7. Third-Party & Vendor AI

- All third-party AI tools (e.g., credit bureaus, fraud platforms) subject to due diligence.
- Vendor contracts include: audit rights, data processing terms, and incident notification SLAs.

---

## 8. Record Keeping & Audit Trail

- All documentation retained for **6 years** post-system retirement.
- Audit trail includes: model versions, training data snapshots, decision logs, and fairness reports.

---

## 9. Review & Update

- This policy reviewed **annually** or upon significant regulatory change.
- Next review date: [INSERT DATE]

---

## 10. Approval

| Role | Name | Date |
|------|------|------|
| Author | [INSERT] | [DATE] |
| Reviewer | [INSERT] | [DATE] |
| Approver (Board/CRO) | [INSERT] | [DATE] |

---

*This template is part of the UK-EU AI Compliance OS. For a fully customized policy aligned to your specific models and data flows, see CONSULTING.md.*
