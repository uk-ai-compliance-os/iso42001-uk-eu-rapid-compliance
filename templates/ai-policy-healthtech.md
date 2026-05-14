# AI Policy Template — UK Healthtech
## ISO 42001 / EU AI Act Aligned | Clinical Decision Support & Diagnostic AI

&gt; **Scope:** AI used for patient triage, diagnostic imaging analysis, treatment recommendation, or clinical workflow optimization  
&gt; **Regulatory Context:** MHRA Software as Medical Device (SaMD), EU AI Act high-risk (Annex III, Section 1), UK AI White Paper, NHS AI Lab standards

---

## 1. Governance & Accountability

### 1.1 Clinical AI Governance Committee
- Chaired by Chief Medical Officer or equivalent.
- Mandatory inclusion: Clinical Safety Officer, Information Governance Lead, Patient Representative.
- All high-risk clinical AI requires Medical Device conformity assessment (UKCA/CE marking pathway).

### 1.2 Accountability Matrix
| Role | Responsibility |
|------|----------------|
| Chief Medical Officer | Clinical safety and patient outcome accountability |
| Head of AI/ML | Technical validation, performance monitoring, and MLOps |
| Clinical Safety Officer | Hazard logging, safety case maintenance, and incident investigation |
| Quality & Compliance Lead | Regulatory submission, ISO 42001 certification, and audit readiness |

---

## 2. Risk Management (ISO 42001 / EU AI Act / SaMD)

### 2.1 Risk Classification
- **Diagnostic imaging AI:** High-risk (EU AI Act Annex III, Section 1 — medical device)
- **Patient triage/chatbot:** High-risk if directly influencing clinical decisions without HCP review
- **Workflow optimization (scheduling):** Limited risk

### 2.2 Clinical Risk Assessment
- Pre-deployment clinical validation study required for all high-risk systems.
- Performance metrics: Sensitivity, specificity, PPV, NPV, AUC-ROC stratified by demographic group.
- Equality analysis: Disaggregated performance across age, sex, ethnicity, and comorbidity status.

---

## 3. Data Governance (Patient Data)

### 3.1 Data Sources
- NHS data: Processed under Data Processing Agreement with relevant NHS Trust or ICS.
- Private data: Explicit patient consent or legitimate healthcare purpose under UK GDPR.
- All training data subject to Information Governance Review.

### 3.2 Data Quality for Clinical AI
- Label validation by at least 2 independent clinicians (inter-rater reliability &gt; 0.8).
- Data recency requirements: Training data no older than [X] years for rapidly evolving conditions.
- Missing data handling protocols documented.

---

## 4. Transparency & Patient Communication

### 4.1 Patient Information
- Patients informed when AI contributes to their diagnosis or treatment plan.
- Clear distinction between "AI-assisted" and "AI-autonomous" decisions.
- Easy-read patient information sheets for AI-enabled pathways.

### 4.2 Clinician Interface
- AI outputs presented with confidence intervals and known limitations.
- "Uncertainty flags" for out-of-distribution inputs.

---

## 5. Human Oversight (Clinical)

- **No autonomous diagnostic or treatment decisions** without qualified HCP review.
- Override mechanism: Clinician may reject AI recommendation; reason logged.
- Escalation pathway: Disagreement between AI and clinician triggers senior review.

---

## 6. Post-Market Surveillance

### 6.1 Real-World Performance Monitoring
- Continuous monitoring of diagnostic accuracy in deployment environment.
- Quarterly safety reports to Clinical AI Governance Committee.

### 6.2 Vigilance & Incident Reporting
- Adverse incidents reported to MHRA via Yellow Card + internal hazard log.
- Field Safety Corrective Actions (FSCA) implemented within 48 hours for critical risks.

---

## 7. Cybersecurity & Robustness

- Penetration testing annually and upon major architecture change.
- Adversarial input testing for imaging AI.
- Model versioning and rollback capability (revert to previous validated version within 1 hour).

---

## 8. Record Keeping

- Clinical AI documentation retained for **lifetime of device + 10 years** (MHRA requirement).
- Includes: validation studies, risk management file, post-market data, and training records.

---

## 9. Review & Certification

- Annual review or upon: new clinical evidence, software update, or regulatory change.
- ISO 42001 internal audit conducted every 12 months.
- Next review: [INSERT DATE]

---

## 10. Approval

| Role | Name | Date |
|------|------|------|
| Clinical Safety Officer | [INSERT] | [DATE] |
| Chief Medical Officer | [INSERT] | [DATE] |
| Quality & Compliance Lead | [INSERT] | [DATE] |

---

*Part of the UK-EU AI Compliance OS. Custom clinical AI governance architecture available via chat-only consulting. See CONSULTING.md.*
