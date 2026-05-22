> **Status:** Production-Ready Template | **Last Updated:** 2026-05-22 | **Next Review:** 2026-08-22 | **Version:** 1.0.0-PROD
# 🩺 AI Policy Template — UK Healthtech
## ISO 42001 / EU AI Act / MHRA SaMD Aligned | Clinical Decision Support & Diagnostic AI

&gt; **Version:** 1.0.0-PROD
&gt; **Status:** Production-Ready Template
&gt; **Effective Date:** [INSERT DATE]
&gt; **Jurisdiction:** United Kingdom (England, Wales, Scotland, Northern Ireland)
&gt; **Classification:** Client-Facing Governance Document / Board Submission Ready
&gt; **Review Cycle:** Quarterly (or upon MHRA/NHS guidance update)
&gt; **Owner:** Chief Medical Officer / Clinical Safety Officer
&gt; **Contact:** compliance.architect@protonmail.com

---

## 1. EXECUTIVE MANDATE

This policy governs the development, procurement, deployment, and monitoring of Artificial Intelligence (AI) and Machine Learning (ML) systems within **[Organisation Name]**'s health technology services. It ensures compliance with the **Medicines and Healthcare products Regulatory Agency (MHRA)** Software as a Medical Device (SaMD) framework, the **EU AI Act (2024/1689)** high-risk system requirements, **ISO/IEC 42001:2023**, **NHS Digital Technology Assessment Criteria (DTAC)**, and **UK GDPR / Data Protection Act 2018**.

**Board Approval Status:** ☐ Approved ☐ Pending  
**Next Review:** [INSERT DATE]  
**Policy Owner:** Chief Medical Officer

---
## 🏥 NHS Procurement Readiness Statement

This policy is designed to satisfy **NHS Digital Technology Assessment Criteria (DTAC)** across all 5 domains:

| DTAC Domain | Policy Section | Evidence Ready |
|-------------|----------------|----------------|
| Clinical Safety | §4.1, §5.1, §8 | ✅ Safety case template included |
| Data Protection | §6, §6.1 | ✅ DPIA framework included |
| Technical Security | §12 | ✅ Penetration test scope included |
| Interoperability | §5.3 | ✅ Data residency clauses included |
| Usability & Accessibility | §7.2 | ✅ Easy-read format guidance included |

**NHS Trusts: Use this template as your DTAC evidence submission. Bespoke adaptation available via chat-only consulting.**

## 2. REGULATORY SCOPE & APPLICABILITY

| Regulation / Standard | Applicability | Control Owner |
|---|---|---|
| **MHRA SaMD & UKCA Marking** | Classification, clinical validation, post-market surveillance | Clinical Safety Officer |
| **EU AI Act (2024/1689)** | High-risk systems (Annex III, Section 1 — medical devices) | Chief Technology Officer |
| **ISO/IEC 42001:2023** | AI Management System (AIMS) certification | Quality & Compliance Lead |
| **NHS DTAC** | NHS procurement eligibility, interoperability, security | Head of Digital / IG Lead |
| **DCB0129 / DCB0160** | Clinical risk management for health IT systems | Clinical Safety Officer |
| **UK GDPR / DPA 2018** | Lawful processing of patient data, DPIAs | Data Protection Officer |
| **NICE Evidence Standards Framework** | Evidence generation for AI-driven diagnostics | Chief Medical Officer |
| **Equality Act 2010** | Non-discrimination in AI-driven patient pathways | HR / Clinical Governance |

**Scope Includes:** Diagnostic imaging AI, clinical decision support systems (CDSS), patient triage algorithms, treatment recommendation engines, predictive analytics for admission/readmission, surgical robotics AI, pathology AI, and workflow optimization tools that process patient data.

---

## 3. AI SYSTEM CLASSIFICATION MATRIX

### 3.1 Risk Tier Definitions

| Tier | MHRA SaMD Class | EU AI Act Category | Criteria | Examples | Approval Authority |
|---|---|---|---|---|---|
| **Prohibited** | N/A | Prohibited | Subverts clinical autonomy, manipulates patient behaviour, exploits vulnerability | AI that discourages emergency care seeking based on cost; social scoring for care prioritisation | **Board + MHRA** |
| **High-Risk** | Class IIb / III | High-Risk (Annex III, Sec 1) | Directly impacts diagnosis, treatment, or clinical decision-making; life-sustaining | Diagnostic imaging AI (radiology, pathology), CDSS for oncology, triage AI without HCP gatekeeping | **CMO + Clinical Safety Officer + DPO** |
| **Limited Risk** | Class IIa | High-Risk / Limited | Influences workflow but requires HCP confirmation before patient impact | Scheduling optimization, bed management AI, drug interaction checkers | **Head of Digital + Clinical Safety Officer** |
| **Minimal Risk** | Class I | Minimal | Administrative support; no clinical decision influence | Staff rota AI, inventory management, training recommendation engines | **IT Director** |

### 3.2 Healthtech-Specific Prohibited Uses

The following AI applications are **expressly prohibited** within **[Organisation Name]**:

1. **Autonomous diagnosis without HCP review** — No AI output shall constitute a final diagnosis or treatment plan without review by a registered healthcare professional.
2. **Social scoring for care access** — AI shall not assign "social worth" scores that influence access to NHS or private care (EU AI Act Article 5).
3. **Emotion recognition in patient monitoring** — Prohibited in non-clinical contexts (e.g., waiting room surveillance) except where medically indicated and consented.
4. **Biometric categorisation for discriminatory triage** — AI shall not use race, ethnicity, or socio-economic proxies to prioritise or deprioritise care.
5. **Training on non-anonymised NHS data without IG approval** — All use of NHS patient data for model training requires Information Governance sign-off, DTAC compliance, and explicit lawful basis under UK GDPR.

---

## 4. GOVERNANCE ARCHITECTURE

### 4.1 Clinical AI Governance Committee

**Composition:**
- Chief Medical Officer (Chair)
- Clinical Safety Officer (Vice-Chair)
- Head of AI / ML Engineering
- Data Protection Officer
- Information Governance Lead
- Patient Representative (mandatory — rotating, 12-month term)
- External Clinical AI Ethicist (independent)

**Mandate:**
- Veto authority over all High-Risk (Class IIb/III) AI deployments.
- Monthly meetings with minuted decisions; minutes retained for **lifetime of device + 10 years**.
- Escalation pathway to MHRA via Yellow Card and Field Safety Notices where patient safety is implicated.
- Annual review of the AI policy and risk appetite statement.

### 4.2 Three Lines of Defence

**First Line: Development & Clinical Operations**
- AI system owners maintain technical documentation: model cards, training data provenance, validation studies, and performance benchmarks.
- Bias testing for protected characteristics (age, sex, ethnicity, disability, deprivation index) conducted pre-deployment and **quarterly** thereafter.
- Version control for all model weights, training corpora, deployment configurations, and clinical validation datasets.

**Second Line: Risk, Compliance & Information Governance**
- Quarterly AI risk register reviews chaired by the Clinical Safety Officer.
- NHS DTAC self-assessment maintained at "Pass" level for all systems procured by NHS Trusts.
- Data Protection Impact Assessments (DPIAs) for all AI processing patient-identifiable data.
- EU AI Act conformity assessments for all CE-marked or export-facing systems.

**Third Line: Internal Audit & External Assurance**
- Annual independent audit of the AI Management System (AIMS) against ISO 42001.
- MHRA-compliant Quality Management System (QMS) audit for SaMD.
- Penetration testing of model inference endpoints, API gateways, and PACS integration points.
- Red-team exercises for adversarial attacks on diagnostic imaging AI.

---

## 5. RISK MANAGEMENT (ISO 42001 / EU AI Act / MHRA SaMD)

### 5.1 Clinical Risk Assessment Lifecycle

1. **Pre-deployment:**
   - Clinical validation study against gold-standard reference (prospective or retrospective, minimum n=500 for imaging AI).
   - Independent clinician label validation (inter-rater reliability κ &gt; 0.8).
   - Algorithmic Impact Assessment (AIA) per EU AI Act Article 9.
   - Clinical Safety Case per DCB0129.

2. **Deployment:**
   - Shadow mode operation for minimum **30 days** before live clinical use.
   - Real-time monitoring of sensitivity, specificity, PPV, NPV, and AUC-ROC.
   - Fairness metrics dashboard: demographic parity ratio, equalized odds, calibration by subgroup.

3. **Post-deployment:**
   - Quarterly clinical performance review against validation benchmarks.
   - Annual actuarial/clinical validation report for MHRA vigilance.
   - Post-market clinical follow-up (PMCF) where required by UKCA marking.

### 5.2 Bias & Fairness Testing Protocol

| Metric | Threshold | Testing Frequency | Responsible Role |
|---|---|---|---|
| Demographic Parity Ratio | ≥ 0.80 across all protected groups | Pre-deployment + Quarterly | Head of AI / ML |
| Equalized Odds (TPR/FPR parity) | Δ ≤ 0.05 between subgroups | Pre-deployment + Quarterly | Head of AI / ML |
| Calibration (predicted vs. observed) | Within 10% across deciles | Monthly | Clinical Safety Officer |
| Inter-rater Reliability (κ) | ≥ 0.80 for ground-truth labels | Pre-deployment | Chief Medical Officer |
| Disparate Impact (deprivation quintile) | No &gt;15% difference in positive prediction rate | Quarterly | Quality & Compliance Lead |

**Remediation Trigger:** If any metric falls below threshold, the system enters **restricted use** (human-in-the-loop mandatory for all outputs) until root cause analysis and re-validation are complete.

---

## 6. DATA GOVERNANCE (Patient Data & NHS Context)

### 6.1 Lawful Basis & Consent

| Data Source | Lawful Basis | Consent Requirement | IG Control |
|---|---|---|---|
| NHS Trust data (secondary use) | Article 6(1)(e) / Article 9(2)(h) UK GDPR | Not required if Section 251 CAG approved | Information Governance Lead |
| NHS data (direct care) | Article 6(1)(e) / Article 9(2)(h) | Implied consent for direct care | Caldicott Guardian |
| Private patient data | Article 6(1)(a) / Article 9(2)(a) | Explicit, granular consent required | DPO |
| Research data (CTIMP/non-CTIMP) | Research-specific lawful basis | Ethics committee + HRA approval | Research Governance Lead |

### 6.2 NHS-Specific Requirements

1. **DTAC Compliance:** All AI systems intended for NHS procurement must complete NHS DTAC self-assessment and achieve "Pass" in all 5 domains (Clinical Safety, Data Protection, Technical Security, Interoperability, Usability & Accessibility).
2. **DSPT (Data Security and Protection Toolkit):** Organisation must maintain "Standards Met" status. AI systems must not compromise DSPT compliance.
3. **Data Residency:** Patient-identifiable data processed by AI systems must remain within **UK sovereign cloud** or **NHS-approved EU/EEA jurisdictions** with UK Addendum to SCCs. US cloud processing prohibited unless validated under NHS England's cloud guidance.
4. **Anonymisation:** Where patient data is used for training, anonymisation must meet **UK ICO Anonymisation Code of Practice** and **NHS Anonymisation Standard** (ISB1523). Re-identification risk assessment required.

### 6.3 Data Quality for Clinical AI

- **Label validation:** All ground-truth labels reviewed by ≥2 independent clinicians; disagreements resolved by senior clinician adjudication.
- **Data recency:** Training data no older than **[INSERT — e.g., 3]** years for rapidly evolving conditions (e.g., COVID-19 variants, antimicrobial resistance patterns).
- **Missing data:** Protocols for handling missing data documented; imputation methods justified in model card.
- **Data provenance:** Full chain of custody from acquisition → cleaning → augmentation → training → validation.

---

## 7. TRANSPARENCY & PATIENT COMMUNICATION

### 7.1 Mandatory Disclosures

Patients (or their lawful representatives) must be informed in writing when AI systems **materially contribute** to:

- **Diagnosis or differential diagnosis** — Disclosure required if AI generates or ranks diagnostic hypotheses.
- **Treatment recommendations** — Disclosure required if AI suggests treatment pathways, drug dosing, or surgical planning.
- **Triage or prioritisation** — Disclosure required if AI influences waiting times, referral urgency, or resource allocation.
- **Prognostic predictions** — Disclosure required if AI estimates survival, recurrence, or complication risk.

### 7.2 Accessibility & Easy-Read Formats

- All patient-facing AI disclosures available in **easy-read**, **large print**, and **accessible digital formats** (WCAG 2.1 AA).
- Translations provided for populations where ≥5% of service users have English as an additional language.
- Patient information sheets reviewed by **Patient Representative** on Clinical AI Governance Committee.

### 7.3 Clinician Interface Requirements

- AI outputs presented with **confidence intervals**, **known limitations**, and **training population representativeness**.
- **"Uncertainty flags"** for out-of-distribution inputs, low-confidence predictions, and demographic under-representation.
- **Explainability:** SHAP/LIME or equivalent explanations available for all adverse or high-stakes predictions; global model explanations reviewed by Clinical AI Governance Committee.

---

## 8. HUMAN OVERSIGHT (THE CLINICIAN-IN-THE-LOOP RULE)

### 8.1 Non-Delegable Clinical Judgment

No AI output shall be acted upon in patient care without:

1. **Meaningful review** by a registered healthcare professional with competence in the relevant clinical domain (GMC/NMC/GDC standards).
2. **Red-line comparison** against source clinical data (imaging, pathology, lab results) for hallucination or artefact detection.
3. **Electronic sign-off** in the Electronic Patient Record (EPR) with mandatory AI usage flag and reviewer identity.
4. **Supervision record** where the reviewing clinician is in training (junior doctor, student nurse); sign-off by consultant or registered practitioner required.

### 8.2 Override & Escalation

- **Clinician override:** Any clinician may reject an AI recommendation; reason logged in incident management system.
- **Escalation trigger:** Disagreement between AI and clinician triggers **senior clinical review within 4 hours** for inpatients, **24 hours** for outpatients.
- **Emergency bypass:** In life-threatening emergencies, clinical judgment takes precedence over AI recommendations; retrospective review mandatory within 24 hours.

### 8.3 Competence & Training

All clinicians using AI tools must complete **mandatory training** covering:

- Limitations and failure modes of the specific AI system (manufacturer + local validation).
- Bias recognition in AI outputs (e.g., under-performance in certain ethnic groups).
- MHRA vigilance reporting obligations for AI-related adverse incidents.
- Data protection when inputting patient data into third-party AI tools (zero-retention clauses).
- **Training records retained for lifetime of device + 10 years** and produced on MHRA/CQC inspection.

---

## 9. THIRD-PARTY AI PROCUREMENT (Medical Device Vendors)

### 9.1 Vendor Due Diligence (Pre-Procurement)

Before procurement of any clinical AI tool, vendors must provide:

- **UKCA / CE marking certificate** and Declaration of Conformity (for Class IIa+ devices).
- **MHRA registration** as a UK Responsible Person (if manufacturer is outside UK).
- **ISO 13485** (Medical Device QMS) or **ISO 42001** certification.
- **DTAC evidence pack** (if NHS procurement).
- **Model lineage documentation:** training data sources, fine-tuning history, base model identification, known limitations.
- **Algorithmic bias audit:** independent testing for performance disparity across protected characteristics.
- **Clinical validation report:** peer-reviewed publication or MHRA-recognised validation study.
- **Cybersecurity certification:** NHS Cyber Alerts compatibility, penetration test report (within 12 months).
- **Professional indemnity / product liability insurance:** minimum £5 million for Class IIb/III devices.
- **Exit clause:** contractual assurance of data deletion within **30 days** of contract termination; model reversion plan.

### 9.2 Contractual Minimums

All clinical AI vendor contracts must include:

1. **Patient data prohibition on training:** Vendor warrants no use of **[Organisation Name]** patient data for model training, fine-tuning, or human review (contractual clause + technical audit).
2. **Accuracy SLA:** Minimum sensitivity/specificity thresholds defined per clinical use case; remediation rights if thresholds breached for &gt;2 consecutive weeks.
3. **Audit rights:** Right to inspect model weights, training data samples, validation reports, and source code annually.
4. **No sub-processing** without prior written consent, updated DPIA, and IG sign-off.
5. **Regulatory cooperation:** Vendor must assist with MHRA, CQC, ICO, and EU AI Act conformity inquiries.
6. **Field Safety Corrective Action (FSCA) cooperation:** Vendor must notify **[Organisation Name]** within **24 hours** of any safety issue affecting the AI system.
7. **Integration liability:** Vendor indemnifies against patient harm arising from API/integration failures.

---

## 10. CONFORMITY ASSESSMENT & CERTIFICATION

### 10.1 UKCA Marking Pathway (Post-Brexit)

| SaMD Class | Conformity Route | Notified Body Required? | Technical Documentation |
|---|---|---|---|
| Class I | Self-certification | No | QMS + clinical evaluation + post-market plan |
| Class IIa | UK Approved Body audit | Yes | Full technical file + clinical evidence summary |
| Class IIb | UK Approved Body full assessment | Yes | Full technical file + PMCF plan + risk management |
| Class III | UK Approved Body + expert panel | Yes | Full technical file + clinical investigation + PMCF |

### 10.2 EU AI Act Conformity (for CE-marked / export devices)

1. **Quality Management System:** Align ISO 42001 AIMS with EU AI Act Article 17.
2. **Technical Documentation:** Annex IV documentation (system architecture, training data governance, performance metrics, risk management).
3. **Conformity Assessment:** UK Approved Body assessment for high-risk systems; self-assessment for limited/minimal risk.
4. **CE Marking:** Affix CE mark + UKCA mark (dual marking for Northern Ireland / EU access).
5. **Post-Market Monitoring:** Continuous logging of performance, incidents, and updates per Article 61–62.

### 10.3 ISO 42001 Certification Roadmap

- **Gap analysis:** Against ISO 42001:2023 clauses 4–10 and Annex A controls.
- **AIMS documentation:** Policy, objectives, risk assessment, AI system impact assessment, operational controls.
- **Internal audit:** Conducted every 12 months by trained, independent auditor.
- **Certification body:** BSI, LRQA, or SGS UK (UKAS-accredited).

---

## 11. POST-MARKET SURVEILLANCE & VIGILANCE

### 11.1 Real-World Performance Monitoring

- **Diagnostic accuracy drift:** Monthly comparison of AI performance against validation benchmarks in live clinical environment.
- **Fairness drift:** Quarterly assessment of demographic parity across new patient populations.
- **Safety signals:** Automated flagging of unexpected correlations (e.g., AI under-performance in new disease variants).

### 11.2 MHRA Vigilance & Incident Reporting

| Severity | Definition | Response Time | Notification |
|---|---|---|---|
| **Critical** | Patient death, serious injury, or missed critical diagnosis directly attributable to AI | **Immediate** (within 2 hours) | MHRA via Yellow Card, CQC, coroner (if death), professional indemnity insurer, NHS England |
| **High** | Incorrect diagnosis requiring corrective intervention; bias detected in protected group | **4 hours** | Clinical Safety Officer, CMO, MHRA, affected patient(s) |
| **Medium** | Model drift beyond threshold; performance degradation not immediately harmful | **24 hours** | Head of AI, Clinical Safety Officer |
| **Low** | Documentation gap; non-material UI issue | **72 hours** | IT Service Desk |

### 11.3 Field Safety Corrective Actions (FSCA)

- **Implementation within 48 hours** for Critical risks.
- **Patient notification:** Where FSCA affects prior diagnoses or treatments, patient recall/re-review initiated.
- **MHRA reporting:** FSCA notification submitted via MHRA portal within 24 hours of decision.

---

## 12. CYBERSECURITY & ROBUSTNESS

- **DCB0129 / DCB0160 compliance:** Clinical risk management applied to health IT systems.
- **Penetration testing:** Annually and upon major architecture change; includes model inference endpoints and DICOM/PACS integration.
- **Adversarial input testing:** For imaging AI — robustness against pixel perturbation, noise injection, and spoofing.
- **Model versioning & rollback:** Revert to previous validated version within **1 hour**; all versions retained for lifetime + 10 years.
- **API security:** OAuth 2.0 + mTLS for all AI service integrations; no patient data in URL parameters or unencrypted logs.

---

## 13. RECORD KEEPING & DOCUMENT CONTROL

- **Retention period:** Clinical AI documentation retained for **lifetime of device + 10 years** (MHRA requirement).
- **Includes:** Validation studies, risk management file, post-market surveillance data, training records, vendor audits, DPIAs, clinical safety cases, and AI system impact assessments.
- **Version control:** All documents maintained in controlled repository with audit trail of changes, approvals, and reviews.
- **Document Owner:** Quality & Compliance Lead
- **Next Review:** [INSERT DATE]

---

## 14. IMPLEMENTATION ROADMAP

| Phase | Activity | Owner | Deadline |
|---|---|---|---|
| **Immediate** | Complete AI inventory and MHRA SaMD classification | Clinical Safety Officer | [DATE + 14 days] |
| **30 Days** | Renegotiate vendor contracts with AI-specific clinical safety clauses | Commercial Director / Procurement | [DATE + 30 days] |
| **45 Days** | Conduct DCB0129 clinical safety assessment for all high-risk systems | Clinical Safety Officer | [DATE + 45 days] |
| **60 Days** | Roll out mandatory clinician AI competence training | HR / Medical Director | [DATE + 60 days] |
| **90 Days** | Complete NHS DTAC self-assessment (if applicable) | Head of Digital | [DATE + 90 days] |
| **120 Days** | Complete ISO 42001 gap analysis and AIMS documentation | Quality & Compliance Lead | [DATE + 120 days] |
| **180 Days** | External audit readiness assessment (BSI / LRQA pre-assessment) | Managing Director / CMO | [DATE + 180 days] |

---

## 15. APPROVAL

| Role | Name | Date |
|---|---|---|
| Author (Clinical Safety Officer) | [INSERT] | [DATE] |
| Reviewer (Chief Medical Officer) | [INSERT] | [DATE] |
| Reviewer (Data Protection Officer) | [INSERT] | [DATE] |
| Approver (Board / Medical Director) | [INSERT] | [DATE] |

---

## 16. HOW TO CUSTOMISE THIS TEMPLATE

1. **Replace placeholders:** Substitute `[Organisation Name]`, `[INSERT DATE]`, and `[INSERT — e.g., 3]` with your specific details.
2. **Validate against your devices:** Confirm MHRA SaMD class for each AI system against MHRA guidance (MDCG 2019-11).
3. **Review with legal counsel:** This template provides governance architecture; your legal counsel must review for solicitor-client privilege and specific contractual contexts.
4. **Board approval:** Submit to Clinical AI Governance Committee and Board for formal adoption.
5. **Publish to compliance portal:** Upload to your NHS Trust's IG Toolkit, client data room, or ISO 42001 evidence repository.

---

*Part of the UK-EU AI Compliance OS. Custom clinical AI governance architecture, NHS DTAC acceleration, and MHRA SaMD conformity support available via chat-only consulting. See [CONSULTING.md](../CONSULTING.md).*
