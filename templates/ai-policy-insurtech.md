# AI Policy Template — UK Insurtech
## ISO 42001 / EU AI Act Aligned | Claims Prediction, Underwriting Automation & Fraud Detection

&gt; **Scope:** AI used for insurance pricing, claims triage and prediction, fraud detection, underwriting automation, or customer risk profiling  
&gt; **Regulatory Context:** UK AI White Paper, EU AI Act high-risk (Annex III, Section 4 — access to essential services/insurance), ICO AI guidance, FCA FG 23/3, Prudential Regulation Authority expectations

---

## 1. Governance & Accountability

### 1.1 AI Governance Committee
- Chaired by Chief Underwriting Officer (CUO) or Chief Risk Officer (CRO).
- Mandatory inclusion: Actuarial Director, Compliance Lead, Data Protection Officer, Claims Director.
- All AI models affecting pricing, coverage decisions, or claims outcomes require committee approval.

### 1.2 Roles & Responsibilities
| Role | Responsibility |
|------|----------------|
| Chief Underwriting Officer | Ultimate accountability for AI-driven pricing and risk selection |
| Actuarial Director | Model validation, fairness testing, and actuarial standards compliance |
| Head of Data Science | Model development, deployment, and monitoring |
| Compliance Lead | Regulatory mapping, FCA/PRA alignment, and audit evidence |
| Claims Director | Oversight of claims prediction AI and fraud detection systems |

---

## 2. Risk Management (ISO 42001 Annex A / EU AI Act Annex III)

### 2.1 Risk Classification
- **Insurance pricing / risk scoring:** High-risk (EU AI Act Annex III, Section 4 — access to essential services)
- **Claims triage / prediction:** High-risk if automated decision affects payout or coverage
- **Fraud detection:** High-risk if leads to denial of claim or policy cancellation without human review
- **Customer service chatbot:** Limited risk (transparency obligations only)

### 2.2 Risk Assessment Lifecycle
1. **Pre-deployment:** Actuarial impact assessment + bias testing across protected characteristics
2. **Deployment:** Real-time monitoring for disparate impact and model drift
3. **Post-deployment:** Quarterly fairness review and annual actuarial validation

---

## 3. Data Governance (EU AI Act Article 10)

### 3.1 Training Data
- Data provenance logs for all claims history, pricing data, and third-party data sources (credit, health, driving telematics).
- Bias testing on protected characteristics: age, disability, race, sex, religion/belief.
- No use of health data for non-health insurance without explicit consent (UK GDPR sensitive data rules).

### 3.2 Data Quality
- Completeness and accuracy metrics defined per data source.
- Outlier and anomaly detection in training data to prevent historical bias amplification.
- Telemetrics data (motor, IoT) subject to recency and device calibration validation.

---

## 4. Transparency & Customer Communication

### 4.1 Policyholder Disclosure
- Customers informed when AI contributes to pricing, coverage decisions, or claims outcomes (Article 52 EU AI Act).
- Clear explanation of: data sources used, key factors in pricing, and right to human review.
- For automated claims decisions: Notification must include reason and escalation path.

### 4.2 Internal Documentation
- Model cards maintained for every pricing, underwriting, and claims AI system.
- Actuarial sign-off documented for all model updates and recalibrations.

---

## 5. Human Oversight

- **No fully automated denial of coverage or claims** without qualified underwriter or claims assessor review.
- Override authority: Senior underwriter may override AI pricing recommendation; reason logged.
- Annual training for underwriters, claims handlers, and customer service on AI system capabilities and limitations.

---

## 6. Monitoring & Incident Response

### 6.1 Continuous Monitoring
- Model drift detection for claims frequency, severity, and fraud indicators.
- Fairness metrics reviewed monthly: disparate impact ratio across protected groups must remain within regulatory thresholds.

### 6.2 Incident Classification
| Severity | Example | Response |
|----------|---------|--------|
| Critical | Proven discriminatory pricing or claims denial | Model suspension, regulatory notification within 24h, customer remediation |
| High | Significant model drift affecting reserves | Human review queue, actuarial investigation |
| Medium | Data quality issue in telematics feed | Engineering fix, policyholder notification if affected |

---

## 7. Third-Party Data & Vendor AI

- All third-party data sources (credit bureaus, telematics providers, health data aggregators) subject to due diligence.
- Vendor contracts must include: data accuracy warranties, audit rights, and incident notification SLAs.
- No reliance on "black box" third-party AI for final coverage or claims decisions without internal validation.

---

## 8. Record Keeping & Audit Trail

- All AI model documentation, training data snapshots, and decision logs retained for **6 years** post-model retirement (FCA/PRA record-keeping requirements).
- Audit trail must satisfy both ISO 42001 internal audits and FCA thematic reviews.

---

## 9. Review & Update

- This policy reviewed **every 6 months** (insurance pricing cycles are fast-moving).
- Triggered also by: FCA/PRA guidance updates, significant model refresh, or customer complaint trend.

---

## 10. Approval

| Role | Name | Date |
|------|------|------|
| Author | [INSERT] | [DATE] |
| Reviewer (Actuarial) | [INSERT] | [DATE] |
| Approver (CUO/CRO) | [INSERT] | [DATE] |

---

*Part of the UK-EU AI Compliance OS. Custom insurtech AI governance frameworks available via chat-only consulting. See CONSULTING.md.*
