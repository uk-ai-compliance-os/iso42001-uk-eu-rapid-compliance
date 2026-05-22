> **Status:** Production-Ready Template | **Last Updated:** 2026-05-22 | **Next Review:** 2026-08-22 | **Version:** 1.0.0-PROD
# 🇬🇧 UK INSURTECH AI GOVERNANCE POLICY — PRODUCTION EDITION
## AI Management System (AIMS) | ISO 42001:2023 | EU AI Act (2024/1689) | FCA FG 23/3 | PRA SS2/13

**Document Classification:** CLIENT-FACING / BOARD GOVERNANCE / AUDIT-READY  
**Version:** 2.0.0-PROD  
**Effective Date:** May 19, 2026  
**Jurisdiction:** United Kingdom (England & Wales) | EU Operations (where applicable)  
**Review Cycle:** Quarterly (aligned with actuarial reporting)  
**Document Owner:** Chief Risk Officer (CRO) / Chief Underwriting Officer (CUO)  
**Policy Sponsor:** Board of Directors  
**Contact:** compliance.architect@protonmail.com  

---

## DOCUMENT CONTROL & VERSION HISTORY

| Version | Date | Author | Approver | Change Description | Status |
|---------|------|--------|----------|-------------------|--------|
| 2.0.0 | 2026-05-19 | Governance Architect | Board Chair | Production release — FCA/PRA/EU AI Act tri-aligned | **ACTIVE** |
| 1.1.0 | 2026-05-16 | Compliance Lead | CRO | Added telematics governance and IoT data annex | Superseded |
| 1.0.0 | 2026-05-14 | Actuarial Director | CUO | Initial draft — ISO 42001 baseline | Superseded |

**Next Review:** August 19, 2026  
**Retention:** 7 years post-retirement of all referenced AI systems (FCA SYSC 9.1)  
**Distribution:** Board Portal, Compliance Intranet, Audit Share (read-only), GitHub OS Toolkit  

---

## EXECUTIVE MANDATE

**WHEREAS** the Firm deploys Artificial Intelligence and Machine Learning systems for pricing, underwriting, claims triage, fraud detection, and customer risk profiling;

**WHEREAS** the EU AI Act (2024/1689) classifies insurance pricing and claims AI as **High-Risk** under Annex III, Section 4 (access to essential services);

**WHEREAS** the Financial Conduct Authority (FCA) expects firms to ensure AI systems do not cause consumer harm, produce unfair outcomes, or undermine market integrity (FG 23/3);

**WHEREAS** the Prudential Regulation Authority (PRA) requires operational resilience and model risk management (SS2/13, SS1/23);

**BE IT RESOLVED** that this Policy constitutes the primary governance instrument for all AI systems within the Firm. All employees, contractors, and third-party vendors must adhere to the standards herein. Non-compliance is a disciplinary matter and may trigger regulatory notification.

**Board Resolution Reference:** BOD/2026/AI-001  
**Date of Board Approval:** May 19, 2026

## 🎯 FCA Consumer Duty: The AI Fair Value Test

Under **FCA Consumer Duty rules (PS22/9)**, your AI systems must demonstrate:

| Consumer Duty Outcome | AI Governance Requirement | This Policy Section |
|----------------------|---------------------------|---------------------|
| **Products & Services** | AI features must meet customer needs | §3.3 (Risk Triggers) |
| **Price & Value** | AI pricing must be fair and transparent | §6.1 (Customer Disclosures) |
| **Consumer Understanding** | AI decisions must be explainable | §6.2 (Internal Explainability) |
| **Consumer Support** | Vulnerable customers must be identified | §7.1 (Vulnerable Customer Champion) |

**The FCA's 2026 supervisory priorities include AI-driven pricing. Firms without documented 'fair value' assessments face skilled persons reviews.**

---

## 1. REGULATORY SCOPE & APPLICABILITY MATRIX

### 1.1 Primary Regulatory Frameworks

| Regulation / Standard | Applicability | Control Owner | Evidence Requirement |
|---------------------|---------------|---------------|---------------------|
| **EU AI Act (2024/1689)** | High-risk AI systems (pricing, claims, underwriting); limited-risk (chatbots) | CRO | Conformity assessment file, CE/UKCA marking path |
| **ISO/IEC 42001:2023** | AI Management System (AIMS) certification | Quality & Risk Lead | Internal audit reports, management review minutes |
| **FCA FG 23/3** | Consumer duty, AI transparency, fair value, vulnerability | Compliance Lead | Consumer outcome testing, board fair value attestations |
| **PRA SS2/13** | Model risk management, operational resilience | CRO / CUO | Model inventory, validation sign-offs, stress testing |
| **UK GDPR / DPA 2018** | Lawful processing, automated decision-making, data subject rights | DPO | DPIAs, RoPA, consent records, data breach log |
| **Equality Act 2010** | Prohibited discrimination in pricing, claims, or coverage | HR / Compliance | Bias audit reports, disparate impact analysis |
| **FCA SYSC 9.1** | Record keeping (6-year minimum) | Company Secretary | Audit trails, model versioning logs |
| **ICO AI Guidance** | Explainability, transparency, accountability | DPO | Explanation frameworks, customer communication records |
| **UK AI White Paper** | Pro-innovation, context-specific approach | Head of Innovation | Horizon scanning records, regulatory engagement log |

### 1.2 Scope of AI Systems Covered

**In-Scope (Mandatory Compliance):**
- Insurance pricing and risk-scoring algorithms (motor, home, life, health, commercial)
- Claims triage, prediction, and settlement automation
- Fraud detection and prevention systems
- Underwriting automation and decision support
- Customer risk profiling and segmentation
- Telematics and IoT-based scoring (motor, health, property)
- Large Language Models (LLMs) used for claims correspondence or policy drafting
- Third-party AI embedded in vendor platforms (MGA systems, broker portals, reinsurance pricing)

**Out-of-Scope (But Monitored):**
- Internal IT helpdesk chatbots (no customer data)
- General office productivity AI (email drafting, scheduling)
- Marketing personalisation (provided no pricing/claims impact)

---

## 2. GOVERNANCE ARCHITECTURE — THREE LINES OF DEFENCE

### 2.1 First Line: Development, Deployment & Operations

**Accountable Executive:** Chief Underwriting Officer (CUO)

**Responsibilities:**
- Maintain a complete **AI Model Inventory** with unique identifiers, ownership, and risk tier.
- Ensure all AI systems have **Model Cards** (per ISO 42001 Annex C) before deployment.
- Conduct **pre-deployment bias testing** across protected characteristics (age, disability, gender reassignment, pregnancy/maternity, race, religion/belief, sex, sexual orientation).
- Implement **MLOps pipelines** with version control for data, code, and model weights.
- Monitor **model drift** (Population Stability Index, Characteristic Stability Index) weekly.
- Maintain **training data provenance** logs with source, date, cleansing steps, and label validation.

**Evidence Required:**
- Model Card Register (updated within 24 hours of any model change)
- Pre-Deployment Bias Test Report (signed by Actuarial Director)
- MLOps Pipeline Documentation (Git commit hashes, container IDs)
- Weekly Drift Monitoring Dashboard

### 2.2 Second Line: Risk, Compliance & Consumer Duty

**Accountable Executive:** Chief Risk Officer (CRO)

**Responsibilities:**
- Chair the **AI Governance Committee** (monthly).
- Conduct **quarterly AI risk register reviews**.
- Ensure **EU AI Act conformity assessments** are completed for all high-risk systems.
- Oversee **Data Protection Impact Assessments (DPIAs)** for AI processing personal data.
- Validate **consumer duty outcomes** — fair value, customer understanding, vulnerability detection.
- Maintain regulatory horizon scanning (FCA/PRA guidance, EU AI Act implementing acts).

**Evidence Required:**
- AI Risk Register (quarterly, signed by CRO)
- Conformity Assessment Files (per EU AI Act Annex IV)
- DPIA Register (maintained by DPO, reviewed by CRO)
- Consumer Outcome Testing Reports (annual, per FCA Consumer Duty)

### 2.3 Third Line: Internal Audit & Independent Assurance

**Accountable Executive:** Head of Internal Audit

**Responsibilities:**
- Annual **independent audit of the AIMS** against ISO 42001.
- **Red-team exercises** on model inference endpoints (prompt injection, data exfiltration).
- Review of **actuarial sign-offs** and **model validation independence**.
- Report findings directly to the **Audit Committee** of the Board.

**Evidence Required:**
- Annual AIMS Audit Report (ISO 42001 clause-by-clause)
- Red-Team Exercise Findings (remediation tracked in Jira/ServiceNow)
- Audit Committee Minutes (AI-specific section)

---

## 3. AI SYSTEM CLASSIFICATION & RISK TIERING

### 3.1 Risk Classification Matrix

| Tier | Definition | Examples | Approval Authority | EU AI Act Status | FCA/PRA Treatment |
|------|------------|----------|-------------------|------------------|-------------------|
| **Prohibited** | Violates fundamental rights or market integrity | Social scoring for insurance pricing, subliminal techniques to manipulate policyholders | **Board + FCA notification** | Prohibited (Article 5) | Immediate decommission |
| **High-Risk** | Significant impact on policyholder rights, financial outcomes, or safety | Pricing models, claims automation, fraud detection with adverse action, underwriting for life/critical illness | **AI Governance Committee (CRO + CUO + DPO)** | Annex III, Section 4 | Full conformity assessment, ongoing monitoring |
| **Limited Risk** | Transparency obligations; human oversight required | Customer-facing chatbots, policy explanation assistants, FNOL (First Notice of Loss) triage bots | **Head of Customer Operations** | Article 52 | Disclosure requirements only |
| **Minimal Risk** | Internal productivity; no customer impact | Internal document summarisation, training recommendation engines | **IT Director** | N/A | Light-touch monitoring |

### 3.2 Insurance-Specific Risk Triggers

A system **automatically escalates to High-Risk** if it:
- Determines or materially influences **premium pricing** for any policyholder.
- Automates or recommends **claims denial, partial settlement, or fraud flagging**.
- Processes **sensitive data** (health, genetic, biometric, telematics) for underwriting.
- Operates in a **wholesale/reinsurance** context where errors affect cedant solvency.
- Is marketed as **"AI-powered"** to policyholders (heightened transparency duty).

---

## 4. ISO 42001 CONTROL FRAMEWORK — ANNEX A MAPPING

| ISO 42001 Clause | Control | Insurance Implementation | Evidence Owner | Frequency |
|------------------|---------|------------------------|----------------|-----------|
| **4.1** | Understanding org & context | Regulatory mapping (FCA/PRA/EU AI Act); market conduct analysis | Compliance Lead | Annual |
| **4.2** | Understanding needs & expectations | Policyholder sentiment analysis; broker feedback; regulator engagement log | Head of Customer Ops | Annual |
| **4.3** | Determining AIMS scope | Scope statement: all in-scope AI systems (see §1.2) | Quality & Risk Lead | Annual |
| **4.4** | AIMS & processes | AIMS manual (this document + annexes) | CRO | Annual |
| **5.1** | Leadership & commitment | Board resolution BOD/2026/AI-001; CEO annual attestation | Company Secretary | Annual |
| **5.2** | Policy | This document | CRO / CUO | Quarterly review |
| **5.3** | Roles & responsibilities | RACI matrix (see §2.1–2.3) | HR / Compliance | Annual |
| **6.1** | Risk assessment | AI Risk Register; model risk framework (PRA SS2/13) | CRO | Quarterly |
| **6.2** | AI risk treatment | Control implementation per risk register | Risk Owners | Ongoing |
| **6.3** | AI system impact assessment | Pre-deployment impact assessment (PIA) template | Compliance Lead | Per deployment |
| **7.1** | Resources | Budget, compute, personnel allocation for AI governance | CFO / CTO | Annual |
| **7.2** | Competence | AI literacy training (see §11); actuarial CPD | HR / L&D | Annual |
| **7.3** | Awareness | All-staff AI governance communications | Compliance Lead | Quarterly |
| **7.4** | Communication | Internal (intranet) and external (customer) comms plans | Marketing / Compliance | Per campaign |
| **7.5** | Documented information | Document control matrix (see top of this file) | Company Secretary | Ongoing |
| **8.1** | Operational planning | AI project gating (see §12) | CUO | Per project |
| **8.2** | AI risk assessment | Integrated into enterprise risk management (ERM) | CRO | Quarterly |
| **8.3** | AI system impact assessment | PIA + actuarial sign-off + fairness testing | Actuarial Director | Per deployment |
| **8.4** | AI system lifecycle | Development → Validation → Deployment → Monitoring → Retirement (see §10) | Head of Data Science | Ongoing |
| **8.5** | Third-party & customer relationships | Vendor due diligence (see §9); broker/MGA AI disclosure | Commercial Director | Per contract |
| **9.1** | Monitoring, measurement, analysis | KPIs: drift incidents, bias findings, customer complaints, model accuracy | Head of Data Science | Monthly |
| **9.2** | Internal audit | Annual AIMS audit (Third Line) | Head of Internal Audit | Annual |
| **9.3** | Management review | Board AI Governance Review (quarterly) | Company Secretary | Quarterly |
| **10.1** | Nonconformity & corrective action | Incident response playbook (see §8); remediation tracking | CRO | Per incident |
| **10.2** | Continual improvement | Post-implementation reviews; model refresh cycles | CUO | Annual |

---

## 5. DATA GOVERNANCE — INSURANCE SPECIFIC

### 5.1 Data Categories & Regulatory Treatment

| Data Category | Source | AI Use | Legal Basis | Retention | Special Controls |
|--------------|--------|--------|-------------|-----------|------------------|
| **Claims history** | Internal systems, TPAs | Pricing, fraud, triage | Legitimate interest / Contract | 6 years post-settlement | Anonymisation for model training |
| **Credit data** | Credit bureaus (e.g., Experian, TransUnion) | Pricing, risk selection | Consent / Legitimate interest | Per DPA with bureau | No use for health/life pricing |
| **Telematics (motor)** | Black box, mobile app, OEM | Usage-based pricing, risk scoring | Explicit consent | Life of policy + 2 years | Driver has right to data portability |
| **Health data** | Medical reports, wearables | Life/critical illness underwriting | Explicit consent (GDPR Article 9) | Per ICO guidelines | Cannot use for non-health lines |
| **IoT (home)** | Smart sensors, leak detectors | Risk scoring, prevention | Contract / Consent | Per device agreement | Cybersecurity hardening |
| **Third-party fraud DBs** | CIFAS, Insurance Fraud Bureau | Fraud detection | Legitimate interest (fraud prevention) | 6 years | Accuracy challenge process |

### 5.2 Training Data Quality Standards

1. **Completeness:** No missing values &gt;5% in any feature used for pricing or claims.
2. **Accuracy:** Source data validated against original policy/claims records quarterly.
3. **Timeliness:** Training data no older than 24 months for fast-moving risks (cyber, gig economy). No older than 60 months for stable risks (property construction).
4. **Representativeness:** Training data must reflect the target population's demographic distribution within ±3% for all protected characteristics. If not, synthetic oversampling or reweighting is mandatory.
5. **Provenance:** Every training dataset has a **Data Lineage Record** (source system, extraction date, transformation steps, responsible data engineer).

### 5.3 Bias Testing Protocol

**Pre-Deployment (Mandatory):**
- **Demographic Parity:** Selection rate disparity across protected groups ≤ 0.05 (5%).
- **Equalised Odds:** True positive rate and false positive rate disparity ≤ 0.05.
- **Calibration:** Predicted probability must align with observed outcomes within ±2% across all demographic segments.
- **Actuarial Sign-Off:** Actuarial Director certifies that bias testing is complete and results are within thresholds.

**Post-Deployment (Ongoing):**
- **Monthly fairness dashboard:** Monitored by AI Governance Committee.
- **Quarterly deep-dive:** Independent review by external actuary (every 4th quarter).
- **Trigger for escalation:** Any protected group shows &gt;0.08 disparity for 2 consecutive months.

---

## 6. TRANSPARENCY, EXPLAINABILITY & CUSTOMER COMMUNICATION

### 6.1 Mandatory Customer Disclosures (FCA Consumer Duty / EU AI Act Art. 52)

| Touchpoint | Disclosure Required | Format | Owner |
|------------|---------------------|--------|-------|
| **Quote journey** | "We use AI to calculate your premium. Key factors include [X, Y, Z]." | Website, email, policy document | Marketing / Compliance |
| **Claims notification** | "Your claim is being assessed with AI assistance. A human reviewer will make the final decision." | Claims portal, letter, email | Claims Director |
| **Fraud investigation** | "We use automated systems to detect fraud. You have the right to request human review." | Letter (before adverse action) | Fraud Manager |
| **Telematics enrolment** | "We collect driving data via [device]. This affects your premium. You can opt out, but your premium may change." | Sign-up flow, app | Customer Ops |
| **Renewal** | "Your premium has been recalculated using updated AI models. Key changes: [factors]." | Renewal letter | Retention Team |

### 6.2 Internal Explainability Requirements

- **Model Cards:** Published internally for every production AI system. Includes: intended use, limitations, training data summary, performance metrics, known failure modes.
- **Global Explanations:** SHAP/LIME values for top 10 features driving model predictions (reviewed by Actuarial Director).
- **Local Explanations:** Available on demand for any individual decision (counterfactual: "Your premium would be £X lower if your no-claims period were Y years longer").
- **Confidence Scores:** Displayed to underwriters/claims handlers (internal use only; never customer-facing without context).

---

## 7. HUMAN OVERSIGHT — THE "UNDERWRITER-IN-THE-LOOP" RULE

### 7.1 Non-Automatable Decisions

The following decisions **require mandatory human review** regardless of AI recommendation:

| Decision Type | Minimum Reviewer | Documentation Required |
|-------------|------------------|------------------------|
| Claims denial (any value) | Senior Claims Handler | Reason for override, AI recommendation vs. human decision |
| Policy cancellation (non-fraud) | Underwriting Manager | Customer circumstances, AI risk score, human rationale |
| Premium increase &gt;25% at renewal | Underwriter | Market comparison, customer history, AI factors |
| Life/critical illness decline | Chief Medical Officer / Senior Underwriter | Medical report review, AI risk score |
| Fraud flag (CIFAS referral) | Fraud Investigation Officer | Evidence review, AI anomaly detection report |
| Vulnerable customer identification | Vulnerable Customer Champion | AI flag + human assessment + support pathway |

### 7.2 Override Authority & Logging

- **Override is a right, not a failure.** Underwriters may override AI recommendations; reason must be logged in the policy/claims management system.
- **Escalation trigger:** Disagreement between AI and human reviewer on High-Risk systems triggers senior review within 4 hours.
- **Training:** All underwriters and claims handlers complete annual "AI Literacy & Override Competence" training (CPD-accredited).

---

## 8. INCIDENT RESPONSE & REGULATORY NOTIFICATION

### 8.1 AI Incident Classification — Insurance Context

| Severity | Definition | Response Time | Notification Required | Evidence Preservation |
|----------|------------|---------------|----------------------|----------------------|
| **Critical** | Discriminatory outcome proven; incorrect advice acted upon by customer; privilege breach; ICO notifiable breach; FCA reportable | **1 hour** | FCA (via RMAR), ICO, affected customer(s), PI insurer, Board Chair | Full model snapshot, training data, decision log, fairness report |
| **High** | Hallucination in policy wording; significant model drift affecting reserves &gt;5%; vendor data breach | **4 hours** | CRO, CUO, DPO, affected customers | Model version, input/output logs, remediation plan |
| **Medium** | Data quality anomaly affecting &lt;100 policies; vendor SLA breach; UI bug in AI interface | **24 hours** | Head of Data Science, CTO | Incident ticket, fix verification |
| **Low** | Non-material inaccuracy; documentation gap; training record missing | **72 hours** | Line manager, Compliance | Corrective action log |

### 8.2 FCA / PRA Notification Protocol

- **FCA:** Any AI incident affecting **consumer harm, market integrity, or prudential soundness** must be assessed for RMAR (Regulatory Incident Report) within 24 hours.
- **PRA:** Any AI incident affecting **solvency calculation, reserving, or reinsurance pricing** must be notified to the PRA supervisory team within 24 hours.
- **ICO:** Personal data breaches involving AI systems (e.g., training data leak, model inversion attack) — 72-hour notification clock starts at detection.

### 8.3 Incident Response Playbook (Summary)

1. **Detect:** Automated monitoring (drift, fairness, security) + human whistleblowing.
2. **Contain:** Suspend model inference if Critical or High. Activate human-only queue.
3. **Assess:** CRO + CUO + DPO convene within 1 hour (Critical) or 4 hours (High).
4. **Notify:** Regulatory notifications per §8.2. Customer notifications per FCA DISP.
5. **Remediate:** Fix root cause, re-validate model, re-train if necessary.
6. **Review:** Post-incident review to AI Governance Committee within 5 business days.
7. **Close:** Evidence archived for 7 years.

---

## 9. THIRD-PARTY AI & VENDOR DUE DILIGENCE

### 9.1 Pre-Procurement Assessment

Before any AI vendor or data provider is onboarded, the Firm must obtain:

| Requirement | Evidence | Reviewer |
|-------------|----------|----------|
| **EU AI Act conformity** | Declaration of conformity (High-Risk) or technical documentation (Limited-Risk) | Compliance Lead |
| **FCA/PRA regulatory status** | Confirmation vendor is FCA-authorised or PRA-regulated (if applicable) | Compliance Lead |
| **SOC 2 Type II** | Report within 12 months | Information Security |
| **ISO 27001** | Valid certificate | Information Security |
| **Model lineage** | Base model ID, training data sources, fine-tuning history | Head of Data Science |
| **Bias audit** | Independent testing across protected characteristics | Actuarial Director |
| **Exit clause** | Data deletion within 30 days of termination; model portability | Commercial / Legal |
| **Insurance** | Professional indemnity ≥ £5m; cyber insurance ≥ £10m | Risk |
| **Data residency** | UK/EU data residency default; TIA for US transfers | DPO |

### 9.2 Contractual Minimums for AI Vendors

1. **IP Indemnity:** Vendor indemnifies against IP claims arising from training data.
2. **Accuracy SLA:** Minimum 95% accuracy on held-out insurance domain test sets; remediation rights if below threshold.
3. **Audit Rights:** Right to inspect model weights, training samples, and validation reports annually.
4. **No Sub-Processing:** Without prior written consent and updated DPIA.
5. **Regulatory Cooperation:** Vendor must assist with FCA, PRA, ICO, or EU AI Act authority inquiries.
6. **No Training on Firm Data:** Contractual warrant that no policyholder/claims data is used for vendor model training.
7. **Privilege Protection:** Where legal advice AI is used, vendor warrants no logging of privileged inputs/outputs.

---

## 10. MODEL GOVERNANCE LIFECYCLE

### 10.1 Phase Gate Framework

| Phase | Gate Criteria | Sign-Off | Documentation |
|-------|--------------|----------|---------------|
| **1. Concept** | Business case; regulatory scope; risk tier | Business Owner | AI Project Charter |
| **2. Development** | Data quality validated; bias testing plan; MLOps pipeline ready | Head of Data Science | Dev environment spec; Git repo |
| **3. Validation** | Actuarial validation; fairness testing; security review; DPIA | Actuarial Director + DPO + CISO | Validation report; PIA |
| **4. Deployment** | AI Governance Committee approval; monitoring dashboard live; human oversight trained | CUO + CRO | Deployment sign-off |
| **5. Monitoring** | Weekly drift; monthly fairness; quarterly actuarial review | Head of Data Science | Monitoring logs |
| **6. Refresh** | Annual revalidation; or triggered by data shift, regulatory change | Actuarial Director | Refresh report |
| **7. Retirement** | Business case for sunsetting; data migration; audit trail archive | CUO | Retirement plan |

### 10.2 Model Retirement & Sunsetting

A model **must be decommissioned** when:
- Accuracy falls below 90% on validation set for 2 consecutive months.
- Regulatory environment changes (e.g., new FCA guidance on pricing fairness).
- Vendor discontinues support, security patches, or model updates.
- Superior replacement validated and approved.
- System no longer aligned with Firm risk appetite.

**Sunsetting Procedure:**
1. **90-day notice** to all internal users with migration guidance.
2. **Data migration plan:** All policy/claims data exported to replacement or archived.
3. **Audit trail archival:** Logs retained for 7 years (FCA SYSC 9.1).
4. **Vendor data deletion confirmation:** Written certification of destruction.
5. **Post-retirement review:** Lessons learned to AI Governance Committee.

---

## 11. COMPETENCE, TRAINING & CULTURE

### 11.1 Mandatory AI Literacy Programme

| Role | Training Module | Frequency | CPD Hours | Owner |
|------|----------------|-----------|-----------|-------|
| **Board / NEDs** | AI Governance for Insurance Directors | Annual | 4 | Company Secretary |
| **CRO / CUO / CISO** | Model Risk & Regulatory Horizon | Quarterly | 2 | Compliance |
| **Actuaries** | Fairness Testing & Algorithmic Bias | Annual | 8 | Actuarial Director |
| **Underwriters** | AI Override Competence; Telematics Interpretation | Annual | 4 | CUO |
| **Claims Handlers** | AI Triage Interpretation; Vulnerability Flags | Annual | 4 | Claims Director |
| **Data Scientists** | MLOps Governance; ISO 42001 Requirements | Annual | 8 | Head of Data Science |
| **Customer Service** | AI Disclosure Scripts; Complaint Escalation | Annual | 2 | Head of Customer Ops |
| **Compliance / Risk** | EU AI Act; FCA FG 23/3; PRA SS2/13 | Quarterly | 4 | Compliance Lead |

### 11.2 Training Records

- All training completions logged in HR system.
- Records retained for **7 years** (SRA-equivalent standard adapted for insurance).
- Available for FCA skilled persons review or ISO 42001 audit on demand.

---

## 12. IMPLEMENTATION ROADMAP — AUGUST 2026 SPRINT

| Phase | Activity | Owner | Deadline | Deliverable |
|-------|----------|-------|----------|-------------|
| **Immediate (Week 1)** | Complete AI inventory and risk classification | CUO | May 26, 2026 | AI Model Inventory v1.0 |
| **Sprint 1 (Week 2)** | Finalise EU AI Act conformity assessments for High-Risk systems | Compliance Lead | Jun 2, 2026 | Conformity Assessment Files |
| **Sprint 2 (Week 3–4)** | Renegotiate vendor DPAs with AI-specific clauses | Commercial Director | Jun 16, 2026 | Updated Contract Register |
| **Sprint 3 (Week 5–6)** | Roll out AI literacy training (all roles) | HR / L&D | Jun 30, 2026 | Training Completion Report |
| **Sprint 4 (Week 7–8)** | Complete ISO 42001 gap analysis; begin evidence collection | Quality & Risk Lead | Jul 14, 2026 | Gap Analysis Report |
| **Sprint 5 (Week 9–10)** | Internal audit readiness assessment | Head of Internal Audit | Jul 28, 2026 | Pre-Audit Findings |
| **Sprint 6 (Week 11–12)** | Board presentation; certification body selection | CRO / CUO | Aug 11, 2026 | Certification Sprint Plan |
| **Go-Live** | AIMS fully operational; external audit scheduled | Board | Aug 18, 2026 | ISO 42001 Stage 1 Audit |

---

## 13. BOARD REPORTING TEMPLATE

**Quarterly AI Governance Dashboard (for Board Pack)**

| Metric | Target | Actual | Trend | RAG |
|--------|--------|--------|-------|-----|
| AI systems in production | — | [X] | — | — |
| High-Risk systems with current conformity assessment | 100% | [X]% | ↑/↓ | 🟢/🟡/🔴 |
| Bias tests completed (pre-deployment) | 100% | [X]% | ↑/↓ | 🟢/🟡/🔴 |
| Drift incidents this quarter | 0 | [X] | ↑/↓ | 🟢/🟡/🔴 |
| Customer complaints citing AI unfairness | &lt;5 | [X] | ↑/↓ | 🟢/🟡/🔴 |
| Training completion rate | 100% | [X]% | ↑/↓ | 🟢/🟡/🔴 |
| Vendor AI due diligence completion | 100% | [X]% | ↑/↓ | 🟢/🟡/🔴 |
| Days to next regulatory deadline | — | [X] | ↓ | 🟢/🟡/🔴 |

**Narrative:** [CRO provides 3-paragraph summary of AI risk landscape, regulatory changes, and strategic recommendations.]

---

## 14. GOVERNANCE CONTACTS & ESCALATION

**Policy Queries & Compliance Support:**  
📧 **compliance.architect@protonmail.com**  
⏱️ **Response time:** &lt; 4 hours (UK business hours 09:00–18:00 BST)

**Internal Escalation Pathway:**
- **Technical / Model Issues:** Chief Underwriting Officer (CUO)
- **Regulatory / FCA-PRA:** Chief Risk Officer (CRO)
- **Data Protection / ICO:** Data Protection Officer (DPO)
- **Information Security:** Chief Information Security Officer (CISO)
- **Consumer Duty / Fair Value:** Head of Customer Operations
- **Audit / Assurance:** Head of Internal Audit

---

## 15. APPROVAL & ATTESTATION

**This Policy is approved by the Board of Directors and is effective immediately.**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Author** | Governance Architect | [INSERT] | 2026-05-19 |
| **Reviewer (Actuarial)** | Actuarial Director | [INSERT] | [DATE] |
| **Reviewer (Compliance)** | Compliance Lead | [INSERT] | [DATE] |
| **Reviewer (Legal)** | General Counsel | [INSERT] | [DATE] |
| **Approver (Risk)** | Chief Risk Officer (CRO) | [INSERT] | [DATE] |
| **Approver (Underwriting)** | Chief Underwriting Officer (CUO) | [INSERT] | [DATE] |
| **Final Approver** | Board Chair | [INSERT] | [DATE] |

**Classification:** CONFIDENTIAL — BOARD GOVERNANCE  
**Retention:** 7 years per FCA SYSC 9.1  
**Next Review:** August 19, 2026

---

*This policy is a living document. All amendments require approval by the AI Governance Committee and the Board of Directors.*

*Part of the UK-EU AI Compliance OS. For bespoke adaptation to your underwriting platforms, claims systems, or telematics stacks, see [CONSULTING.md](CONSULTING.md) for chat-only implementation architecture.*
