# 🇬🇧 LEGALTECH AI GOVERNANCE POLICY

**Version:** 1.0.0-PROD  
**Effective Date:** May 18, 2026  
**Jurisdiction:** United Kingdom (England & Wales)  
**Classification:** Client-Facing Governance Document  
**Review Cycle:** Quarterly  
**Owner:** Chief Technology Officer / Money Laundering Reporting Officer (MLRO)  
**Contact:** compliance.architect@protonmail.com

---

## 1. EXECUTIVE MANDATE

This policy governs the development, procurement, deployment, and monitoring of Artificial Intelligence (AI) and Machine Learning (ML) systems within **[Firm Name]**'s legal technology services. It ensures compliance with the **Solicitors Regulation Authority (SRA) Code of Conduct**, **UK GDPR**, **Data Protection Act 2018**, the **EU AI Act** (as applicable to UK exporters), and **ISO/IEC 42001:2023**.

**Board Approval Status:** ✅ Approved  
**Next Review:** August 18, 2026  
**Policy Owner:** Chief Technology Officer

---

## 2. REGULATORY SCOPE & APPLICABILITY

| Regulation | Applicability | Control Owner |
|------------|--------------|---------------|
| **SRA Code of Conduct** | Confidentiality, competence, client care | Compliance Officer for Legal Practice (COLP) |
| **UK GDPR / DPA 2018** | Lawful processing, data subject rights, automated decision-making | Data Protection Officer (DPO) |
| **EU AI Act (2024/1689)** | High-risk AI systems for legal services | Chief Technology Officer (CTO) |
| **ISO 42001:2023** | AI Management System (AIMS) certification | Quality & Risk Lead |
| **Legal Services Act 2007** | Reserved legal activities, unauthorised practice | Managing Partner |
| **Equality Act 2010** | Prohibited discrimination in AI-driven processes | HR / Compliance |

**Scope Includes:** Document review automation, predictive litigation analytics, contract generation LLMs, e-discovery tools, legal research assistants, client intake chatbots, billing optimisation algorithms, and conflict checking systems.

---

## 3. AI SYSTEM CLASSIFICATION MATRIX

### 3.1 Risk Tier Definitions

| Tier | Criteria | Examples | Approval Authority |
|------|----------|----------|-------------------|
| **Prohibited** | Subverts judicial independence, automated legal advice without supervision | Autonomous bail application systems, unsupervised will generation | **Board + SRA** |
| **High-Risk** | Impacts client rights, case outcomes, regulatory reporting, or privilege | Litigation outcome predictors, regulatory filing generators, KYC/AML screening, automated contract review | **MLRO + DPO + COLP** |
| **Limited Risk** | Transparency obligations, human oversight required | Client-facing chatbots, document summarisation tools, intake assistants | **Head of Innovation** |
| **Minimal Risk** | Internal productivity, no client data | Internal scheduling AI, training recommendation engines, IT helpdesk bots | **IT Director** |

### 3.2 Legal-Specific Prohibited Uses

The following AI applications are **expressly prohibited** within **[Firm Name]**:

1. **Autonomous court submissions** — No AI output filed with a court or tribunal without senior solicitor review and signature.
2. **Unsupervised reserved activities** — AI shall not perform reserved legal activities (e.g., exercising rights of audience, conducting litigation, preparing instruments) without human solicitor control (Legal Services Act 2007, s.12).
3. **Sole conflict determination** — AI-driven client conflict checking may flag potential conflicts; final determination rests with the COLP or designated compliance officer.
4. **Discriminatory pricing** — Predictive models for pricing legal services shall not use protected characteristics (race, sex, disability, religion, etc.) as direct or proxy variables (Equality Act 2010).
5. **Training on confidential data** — No client-confidential data used for model training without explicit engagement letter amendment, anonymisation to ICO standards, and DPO sign-off.

---

## 4. GOVERNANCE ARCHITECTURE

### 4.1 Three Lines of Defence

**First Line: Development & Operations**
- AI system owners maintain technical documentation including model cards, training data provenance, and performance benchmarks.
- Bias testing for protected characteristics conducted before deployment and annually thereafter.
- Version control for all model weights, training corpora, and deployment configurations.

**Second Line: Risk & Compliance**
- Quarterly AI risk register reviews chaired by the COLP.
- SRA notification for high-risk deployments where required (SRA Code Rule 2.2).
- EU AI Act conformity assessments for all export-facing or high-risk systems.
- Data Protection Impact Assessments (DPIAs) for AI processing personal data.

**Third Line: Internal Audit**
- Annual independent audit of the AI Management System (AIMS) against ISO 42001.
- Penetration testing of model inference endpoints and API gateways.
- Red-team exercises for prompt injection, data exfiltration, and privilege leakage in legal LLMs.

### 4.2 AI Ethics & Risk Committee

**Composition:**
- Managing Partner (Chair)
- Data Protection Officer
- Head of Innovation
- External legal technology ethicist (independent)
- Client representative (rotating, annually)

**Mandate:**
- Veto authority over all High-Risk AI deployments.
- Monthly meetings with minuted decisions.
- Minutes retained for **7 years** per SRA record-keeping rules (SRA Code Rule 8.2).
- Escalation pathway to the SRA where public protection is implicated.

---

## 5. DATA GOVERNANCE & CLIENT CONFIDENTIALITY

### 5.1 Training Data Protocols

1. **Client matter data** shall not be used for model training unless:
   - Specific informed consent obtained via engagement letter addendum;
   - Anonymisation meets UK ICO Anonymisation Code of Practice standards;
   - A Data Processing Agreement (DPA) is executed with the cloud/AI provider;
   - DPO conducts and approves a DPIA.

2. **Synthetic data generation** is the preferred method for training legal document classifiers and clause extractors.

3. **Open-source legal datasets** (e.g., BAILII, legislation.gov.uk) are permitted for pre-training and fine-tuning, provided licensing terms are respected and citation standards maintained.

### 5.2 Inference Data Handling

- All client data processed through AI systems encrypted in transit (**TLS 1.3**) and at rest (**AES-256**).
- **Zero-retention inference:** API providers must contractually confirm no model training, fine-tuning, or human review of inputs (contractual clause 12.4).
- **UK data residency default.** EU or US transfers permitted only under the UK Addendum to the EU Standard Contractual Clauses (SCCs), with Transfer Impact Assessments (TIAs) documented.

### 5.3 Legal Professional Privilege Preservation

- All AI-generated drafts, memoranda, or advice documents marked as **"Subject to Legal Professional Privilege — Draft"** until reviewed and approved by the supervising solicitor.
- Metadata scrubbing protocols before document export to prevent training data or prompt leakage.
- Audit logs of all AI-assisted document generation retained for privilege logs and SRA audit trails.
- AI systems processing privileged data must be configured with **no logging of inputs/outputs** to vendor servers where privilege could be waived.

---

## 6. HUMAN OVERSIGHT & ACCOUNTABILITY

### 6.1 The Solicitor-in-the-Loop Rule

No AI output shall be delivered to a client, court, regulator, or third party without:

1. **Meaningful review** by a solicitor with demonstrable competence in the relevant practice area (SRA Code Principle 1);
2. **Red-line comparison** against source materials, precedents, and statutory provisions for hallucination detection;
3. **Electronic sign-off** in the matter management system with mandatory AI usage flag;
4. **Supervision record** where the reviewing solicitor is a trainee or junior associate (SRA Code Principle 5).

### 6.2 Competence & Training

All fee-earners using AI tools must complete **annual CPD-accredited training** covering:

- Hallucination and confabulation risks in legal Large Language Models (LLMs);
- Bias detection in sentencing, costs, and outcome prediction models;
- SRA competence requirements when delegating work to AI (SRA Code Principle 1);
- Privilege preservation in AI-assisted workflows;
- Data protection obligations when inputting client data into third-party AI tools.

**Training records maintained for 7 years** and produced on SRA request.

---

## 7. TRANSPARENCY & CLIENT DISCLOSURE

### 7.1 Mandatory Disclosures

Clients must be informed in writing (engagement letter or supplementary disclosure) when AI systems materially contribute to:

- **Legal advice formulation** — Disclosure required if AI generates substantive advice drafts reviewed by the solicitor.
- **Document review** — Disclosure required for AI-assisted due diligence, disclosure, or e-discovery (per 1,000 pages or matter threshold).
- **Litigation strategy** — Disclosure required if AI recommends settlement values, timeline predictions, or tactical approaches.
- **Billing** — Disclosure required if AI tools are used to scope, predict, or optimise fee estimates.

### 7.2 Explainability Requirements

For all High-Risk systems:

- **Counterfactual explanations** available on client request (e.g., "Why did the model classify this clause as high-risk?").
- **Confidence scores** displayed to the reviewing solicitor (internal use only; not client-facing).
- **Model cards** published internally for all deployed systems, per ISO 42001 Annex C, including intended use, limitations, training data summary, and performance metrics.
- **Global explanations** (SHAP/LIME) for model behaviour available to the AI Ethics Committee.

---

## 8. INCIDENT RESPONSE & REGULATORY NOTIFICATION

### 8.1 AI Incident Classification

| Severity | Definition | Response Time | Notification |
|----------|-----------|---------------|--------------|
| **Critical** | Privilege breach, incorrect advice acted upon by client, SRA reportable conduct, ICO notifiable breach | **1 hour** | SRA, ICO, affected client(s), professional indemnity insurer, Law Society |
| **High** | Hallucination in filed court document, bias detected in client screening, vendor data breach affecting firm data | **4 hours** | COLP, DPO, affected client(s) |
| **Medium** | Model drift degrading accuracy, performance degradation, vendor SLA breach | **24 hours** | Head of Innovation, CTO |
| **Low** | UI bug, non-material inaccuracy, documentation gap | **72 hours** | IT Service Desk |

### 8.2 SRA Notification Protocol

Any AI-related matter that could affect **client trust, public protection, or the reputation of the firm** triggers mandatory COLP notification within **24 hours** (SRA Code Rule 2.2).

The COLP shall assess whether the matter is reportable to the SRA under the **SRA Principles** and **Code of Conduct**, and shall document the rationale for reporting or non-reporting.

---

## 9. THIRD-PARTY AI PROCUREMENT

### 9.1 Vendor Due Diligence

Before procurement of any AI tool or service, vendors must provide:

- **EU AI Act conformity declaration** (for High-Risk systems);
- **SOC 2 Type II** or **ISO 27001** certification;
- **Model lineage documentation** — training data sources, fine-tuning history, base model identification;
- **Algorithmic bias audit** — independent testing for discrimination across protected characteristics;
- **Exit clause** — contractual assurance of data deletion within **30 days** of contract termination;
- **Insurance** — professional indemnity cover of at least £2 million.

### 9.2 Contractual Minimums

All AI vendor contracts must include:

1. **IP indemnity** — Vendor indemnifies against IP infringement claims arising from training data.
2. **Accuracy SLA** — Minimum 95% accuracy on held-out legal domain test sets, with remediation rights.
3. **Audit rights** — Right to inspect model weights, training data samples, and validation reports annually.
4. **No sub-processing** without prior written consent and updated DPIA.
5. **Regulatory cooperation** — Vendor must assist with SRA, ICO, or FCA inquiries.
6. **Privilege protection** — Vendor warrants that no client data is used for training, logged, or accessible to vendor personnel.

---

## 10. CONTINUOUS MONITORING & MODEL GOVERNANCE

### 10.1 Performance Monitoring

- **Drift detection:** Statistical monitoring of input and output distributions (Kolmogorov-Smirnov test, Population Stability Index) — **weekly**.
- **Accuracy benchmarking:** Monthly evaluation against gold-standard legal datasets (e.g., manually annotated contracts, court decisions).
- **Bias auditing:** Quarterly testing for outcome disparities across protected characteristics (demographic parity, equalised odds).
- **Latency & availability:** Real-time monitoring of API response times and uptime (99.9% SLA).

### 10.2 Model Retirement & Sunsetting

AI systems shall be decommissioned when:

- Accuracy falls below **90%** on the validation set for **2 consecutive months**;
- The regulatory environment changes (e.g., new SRA guidance on AI, updated ICO guidance);
- The vendor discontinues security patches, model updates, or technical support;
- A superior replacement system is validated and approved;
- The system is no longer aligned with the firm's risk appetite.

**Sunsetting Procedure:**
1. **90-day notice** to all internal users with migration guidance;
2. **Data migration plan** — all matter data exported to the replacement system or archived;
3. **Audit trail archival** — logs retained for 7 years per SRA requirements;
4. **Vendor data deletion confirmation** — written certification of destruction;
5. **Post-decommissioning review** — lessons learned documented and reported to the AI Ethics Committee.

---

## 11. IMPLEMENTATION ROADMAP

| Phase | Activity | Owner | Deadline |
|-------|----------|-------|----------|
| **Immediate** | Complete AI inventory and risk classification | CTO | June 1, 2026 |
| **30 Days** | Renegotiate vendor DPAs with AI-specific clauses | Commercial Director | June 18, 2026 |
| **60 Days** | Roll out solicitor AI competence training | HR / L&D | July 18, 2026 |
| **90 Days** | Complete ISO 42001 gap analysis | Quality & Risk Lead | August 18, 2026 |
| **120 Days** | External audit readiness assessment | Managing Partner | September 18, 2026 |

---

## 12. GOVERNANCE CONTACT

**Policy Queries & Compliance Support:**  
📧 **compliance.architect@protonmail.com**

**Internal Escalation:**
- **Technical:** Chief Technology Officer
- **Regulatory:** Compliance Officer for Legal Practice (COLP)
- **Data Protection:** Data Protection Officer (DPO)
- **Ethical:** AI Ethics & Risk Committee Chair (Managing Partner)

---

## 13. DOCUMENT CONTROL

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| **1.0.0** | 2026-05-18 | Governance Lead | **Production release** — SRA/ICO/ISO 42001 aligned |
| 0.9.0 | 2026-05-14 | Innovation Team | Internal review and red-team |

**Next Review Date:** August 18, 2026  
**Document Owner:** Chief Technology Officer  
**Approved By:** [Managing Partner Signature]  
**Classification:** CONFIDENTIAL — CLIENT-FACING ON REQUEST  
**Retention:** 7 years per SRA Code Rule 8.2

---

*This policy is a living document. All amendments require approval by the AI Ethics & Risk Committee and the Managing Partner.*
