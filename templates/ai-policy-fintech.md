# 🇬🇧 AI Policy Template — UK Fintech
## ISO 42001 / EU AI Act / FCA Handbook Aligned | Credit Scoring, Fraud Detection, AML & Algorithmic Trading

---
**Version:** 1.0.0-PROD
**Effective Date:** [INSERT DATE]
**Jurisdiction:** United Kingdom
**Classification:** Client-Facing Governance Document
**Review Cycle:** Quarterly
**Owner:** Chief Risk Officer / MLRO
**Contact:** compliance.architect@protonmail.com
---

&gt; **Status:** Production-Ready Template v1.0.0 | Last Updated: 2026-05-19
&gt; **Scope:** UK-authorised fintechs using AI/ML for credit decisions, fraud detection, AML monitoring, or algorithmic trading
&gt; **Regulatory Context:** UK FCA Handbook (SYSC, CONC, FG 23/3), FCA Consumer Duty, SMCR, EU AI Act high-risk (Annex III, Section 5), UK GDPR & DPA 2018, ICO AI auditing framework, UK MiFIR / MiFID II (where applicable)

---

## 1. Governance & Accountability

### 1.1 AI Governance Board
- The Board retains ultimate accountability for AI system outcomes affecting customers.
- An AI Risk Committee meets monthly to review model performance, drift, and fairness metrics.
- All high-risk AI decisions require human-in-the-loop (HITL) sign-off.

### 1.2 Roles & Responsibilities
| Role | Responsibility |
|------|----------------|
| Chief Risk Officer (SMF4) | Overall AI risk appetite, model risk governance, and policy approval |
| ML Engineering Lead | Technical implementation, monitoring, and drift detection |
| MLRO / Compliance Lead (SMF17) | AI-driven AML model governance, SAR escalation, FCA notification, and audit evidence |
| Data Protection Officer | Privacy impact assessments (DPIAs) and data governance |
| SMF16 (Compliance Oversight) | Regulatory mapping, Consumer Duty alignment, and certification maintenance |

### 1.3 FCA Consumer Duty & SMCR Accountability

**Consumer Duty Outcome:** AI systems must be designed, tested, and monitored to ensure they do not cause foreseeable harm to retail customers (FCA Consumer Duty Principle, cross-cutting rules).

**Senior Managers and Certification Regime (SMCR):**
| SMF Role | Prescribed Responsibility | AI Accountability |
|----------|---------------------------|-------------------|
| SMF16 (Compliance Oversight) | Compliance with regulatory requirements | AI policy approval and FCA notification |
| SMF17 (MLRO) | AML/CTF compliance | AI-driven AML model oversight and SAR governance |
| SMF24 (Chief Operating Officer) | Operational resilience | AI system downtime and incident impact tolerance |
| SMF4 (Chief Risk Officer) | Risk management framework | AI risk appetite and model risk governance |

**Certification:** All staff with override authority on high-risk AI decisions must be Certified Persons under SMCR.

---

## 2. Risk Management (ISO 42001 Annex A / EU AI Act Annex III / FCA FG 23/3)

### 2.1 Risk Classification
All AI systems are classified per EU AI Act Annex III and FCA guidance:

| System | Risk Tier | Rationale |
|--------|-----------|-----------|
| **Credit scoring / pricing** | High-risk | EU AI Act Annex III, Section 4 (access to essential services); FCA CONC 5.2 (creditworthiness assessment) |
| **Fraud detection** | High-risk | Automated decision-making with legal/equivalent effect; FCA SYSC 3.2.6G |
| **AML monitoring** | High-risk | MLRO-governed; adverse customer action or SAR filing without human review triggers high-risk classification |
| **Algorithmic trading** | High-risk | UK MiFIR / MiFID II; market integrity implications |
| **Customer service chatbot** | Limited risk | Transparency obligations only; no adverse financial impact |

### 2.2 Risk Assessment Lifecycle
1. **Pre-deployment:** Algorithmic impact assessment (AIA) + bias audit + FCA Consumer Duty "foreseeable harm" test
2. **Deployment:** Real-time monitoring for demographic parity, equalized odds, and FCA pricing fairness
3. **Post-deployment:** Quarterly model revalidation, fairness reporting, and SMCR attestation review

---

## 3. Data Governance (EU AI Act Article 10 / UK GDPR / DPA 2018)

### 3.1 Training Data
- Data provenance logs maintained for all training, validation, and test datasets.
- Bias testing conducted on protected characteristics: age, gender, ethnicity, disability status.
- Synthetic data use documented and justified where real data is insufficient.

### 3.2 Data Quality
- Completeness, accuracy, and timeliness metrics defined per dataset.
- Data cleaning pipelines version-controlled and auditable.

### 3.3 UK Data Protection Specifics
- **UK GDPR & DPA 2018:** All AI processing of personal data requires a Data Protection Impact Assessment (DPIA) reviewed and approved by the DPO.
- **ICO "Explaining decisions made with AI":** Adverse automated decisions must be explainable per ICO guidance (not just EU AI Act Article 52).
- **Right to human intervention:** Under DPA 2018 Section 14, data subjects have the right to contest automated decisions and request human review.
- **Credit data:** Processing of personal data for credit scoring must comply with the Consumer Credit Act 1974 and FCA CONC rules.

---

## 4. Transparency & Explainability

### 4.1 Customer Communication
- Customers informed when AI is used in credit decisions (Article 52 EU AI Act; FCA CONC 5.2).
- Right to explanation: Customers may request the main factors influencing an adverse decision.
- **FCA Consumer Duty:** Explanations must be "understandable" to the target customer (not just technical staff).

### 4.2 Internal Documentation
- Model cards maintained for every production AI system.
- SHAP/LIME explanations generated for all adverse automated decisions.
- **SMCR attestation:** Model cards must be signed off by the accountable SMF before deployment.

---

## 5. Human Oversight

- All high-risk AI outputs flagged for human review before customer notification.
- Override authority clearly assigned to senior underwriters or MLRO (for AML).
- Annual training for all staff interacting with AI outputs, including SMCR-certified competence requirements.
- **No fully automated adverse action** without qualified human review (credit denial, account closure, SAR filing).

---

## 6. Monitoring & Incident Response

### 6.1 Continuous Monitoring
- Model drift detection (PSI, CSI) automated with threshold alerting.
- Fairness metrics reviewed monthly by the AI Risk Committee.
- FCA impact tolerance monitoring: AI system downtime must not breach operational resilience thresholds.

### 6.2 Incident Classification & FCA Notification

| Severity | Definition | Response Time | FCA Notification |
|----------|------------|---------------|------------------|
| **Critical** | Discriminatory outcome proven, systemic consumer harm, or market abuse | Automated decision suspension within 1 hour; system review within 4 hours | FCA via REPO / INREP within 24 hours |
| **High** | Model drift beyond tolerance affecting pricing or eligibility | Human review queue activated; MLRO notified within 4 hours | FCA if impact tolerance breached |
| **Medium** | Data quality anomaly or vendor SLA breach | Engineering ticket; 24h fix target | Internal log only |
| **Low** | UI bug or non-material inaccuracy | 72h fix target | No external notification |

**Operational Resilience:** All AI systems must have defined impact tolerances per FCA PS21/3. Breach of tolerance triggers the incident response protocol above.

---

## 7. Third-Party AI & FCA Outsourcing (SYSC 8 / SYSC 13)

### 7.1 Regulatory Scope
Any AI service that is "material" to the firm's operations (including cloud ML platforms, credit bureau APIs, and fraud detection services) is classified as **outsourcing** under FCA SYSC 8.

### 7.2 Due Diligence Requirements
Before procurement, vendors must provide:
- **FCA outsourcing certificate:** Confirmation that the arrangement complies with SYSC 8.1 and the firm maintains adequate access to data and audit rights.
- **Operational resilience attestation:** Vendor's impact tolerance and self-assessment per FCA PS21/3.
- **Exit strategy:** Contractual right to retrieve all training data, model weights, and decision logs within 30 days of termination.
- **No sub-outsourcing** without prior written consent and updated risk assessment.

### 7.3 Cloud AI Governance
- **UK data residency default:** AI inference and training must occur in UK or EEA regions unless a Transfer Impact Assessment (TIA) is approved.
- **Zero-retention clause:** Cloud providers must contractually confirm no use of firm data for model training or fine-tuning.
- **SOC 2 Type II + ISO 27001:** Minimum security standards for all AI vendors.

---

## 8. Record Keeping & Audit Trail

- All documentation retained for **6 years** post-system retirement (FCA SYSC 9).
- Audit trail includes: model versions, training data snapshots, decision logs, fairness reports, and SMCR attestation records.
- **FCA readiness:** All records must be producible within 72 hours of an FCA information request or skilled persons review (s.166 FSMA).

---

## 9. Review & Update

- This policy reviewed **quarterly** (aligned with FCA SMCR attestation cycles) or upon significant regulatory change.
- **Trigger events:** New FCA guidance (e.g., FG updates), EU AI Act implementing acts, ICO enforcement action, or material model refresh.
- Next review date: [INSERT DATE]

---

## 10. Approval

| Role | Name | Date |
|------|------|------|
| Author | [INSERT] | [DATE] |
| Reviewer (MLRO / SMF17) | [INSERT] | [DATE] |
| Approver (Board / CRO / SMF4) | [INSERT] | [DATE] |

---

## 11. Algorithmic Trading AI (UK MiFIR / MiFID II)

**Scope:** AI used for trade execution, order routing, or market-making.

### 11.1 Governance
- **Algo testing:** All trading algorithms must be tested in a non-live environment for a minimum period before deployment (FCA SYSC 18.5).
- **Kill switch:** Immediate ability to disable the algorithm without human intervention. Kill switch tested quarterly.
- **Market abuse monitoring:** AI-generated orders must be screened for patterns indicative of market manipulation (Market Abuse Regulation).

### 11.2 Record Keeping
- Full audit trail of all AI-generated orders, including: input signals, model version, decision logic, and execution timestamp.
- Retention: **5 years** per UK MiFIR Article 25.

---

## How to Customise This Template

1. **Replace placeholders:** Substitute `[Firm Name]` and `[INSERT]` fields with your authorised firm name and SMF names.
2. **Validate against FCA Handbook:** Have your SMF16 (Compliance Oversight) review against current SYSC, CONC, Consumer Duty, and FG 23/3 rules.
3. **Board approval:** Obtain signed approval from the Board, CRO (SMF4), and MLRO (SMF17) before publishing to your compliance portal.
4. **Legal review:** This template is not legal advice. Engage independent FCA regulatory counsel before filing or deploying.

---

*This template is part of the UK-EU AI Compliance OS. For a fully customised policy aligned to your specific models, data flows, and FCA permissions, see [CONSULTING.md](../CONSULTING.md).*
