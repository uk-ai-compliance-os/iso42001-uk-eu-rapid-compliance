**Status:** Production-Ready Template | **Last Updated:** 2026-05-22 | **Next Review:** 2026-08-22 | **Version:** 1.1.0-PROD

# 🇬🇧 LEGALTECH AI GOVERNANCE POLICY

**Version:** 1.1.0-PROD  
**Effective Date:** May 18, 2026  
**Jurisdiction:** United Kingdom (England & Wales)  
**Classification:** Client-Facing Governance Document  
**Review Cycle:** Quarterly  
**Owner:** Chief Technology Officer / Money Laundering Reporting Officer (MLRO)  
**Contact:** compliance.architect@protonmail.com  

---

## 1. EXECUTIVE MANDATE

This policy governs the development, procurement, deployment, and monitoring of Artificial Intelligence (AI) and Machine Learning (ML) systems within **[Firm Name]**'s legal technology services. It ensures compliance with the **Solicitors Regulation Authority (SRA) Standards and Regulations 2022**, **UK GDPR**, **Data Protection Act 2018**, the **EU AI Act (2024/1689)** (as applicable to UK exporters), and **ISO/IEC 42001:2023**.

**Board Approval Status:** ✅ Approved  
**Next Review:** August 18, 2026  
**Policy Owner:** Chief Technology Officer  

---
## ⚖️ SRA 2026 Thematic Review Compliance

The Solicitors Regulation Authority's **2026 Thematic Review on Technology and Innovation** examines:

- Whether firms have documented AI governance (this policy = ✅)
- Whether COLPs understand AI risks (§4.2 = ✅)
- Whether client confidentiality is protected in AI workflows (§5.3 = ✅)
- Whether fee-earners are competent to use AI (§6.2 = ✅)

**Firms submitting this policy to the SRA demonstrate proactive compliance. Firms without documented governance face referral to the Supervision Team.**

## 2. REGULATORY SCOPE & APPLICABILITY

| Regulation / Standard | Applicability | Control Owner |
|---|---|---|
| **SRA Standards and Regulations 2022** | Principles 1–7; Code of Conduct for solicitors; AML Regulations 2017 | COLP / MLRO |
| **UK GDPR / DPA 2018** | Lawful processing; data subject rights; Article 22 automated decision-making | DPO |
| **EU AI Act (2024/1689)** | High-risk AI systems — Annex III, point 1(a) (administration of justice); Articles 6–17, 29, 43, 71–73 | CTO |
| **ISO/IEC 42001:2023** | AI Management System (AIMS) certification | Quality & Risk Lead |
| **Legal Services Act 2007** | Reserved legal activities; unauthorised practice | Managing Partner |
| **Equality Act 2010** | Prohibited discrimination in AI-driven processes | HR / Compliance Lead |
| **CDPA 1988** | Copyright in AI-generated works | Commercial Director |

**EU AI Act High-Risk Classification for Legaltech:**
- **Annex III, point 1(a):** AI systems intended to be used by a judicial authority or on their behalf to assist in the administration of justice (e.g., litigation outcome predictors, sentencing algorithms, case management AI).
- **Annex III, point 1(b):** AI systems intended to be used for influencing the outcome of an election or referendum.
- **Annex III, point 6:** AI systems intended to be used for biometric identification.

*Note: UK legaltech exporting to the EU or processing EU data is in scope regardless of the firm's UK location.*

**UK AI Regulatory Context:** This policy anticipates the UK AI White Paper (March 2023) framework and the proposed UK AI Bill. The UK's sector-based, regulator-led approach (ICO, SRA, FCA, MHRA) is addressed through the Three Lines of Defence model. The firm monitors BSI, UKAS, and DSIT guidance for emerging UK-specific AI assurance requirements.

**Scope Includes:** Document review automation, predictive litigation analytics, contract generation LLMs, e-discovery tools, legal research assistants, client intake chatbots, billing optimisation algorithms, conflict checking systems, and regulatory filing generators.

---

## 3. AI SYSTEM CLASSIFICATION MATRIX

### 3.1 Risk Tier Definitions

| Tier | Criteria | Examples | Approval Authority |
|---|---|---|---|
| **Prohibited** | Subverts judicial independence, automated legal advice without supervision | Autonomous bail application systems, unsupervised will generation | **Board + SRA** |
| **High-Risk** | Impacts client rights, case outcomes, regulatory reporting, or privilege | Litigation outcome predictors, regulatory filing generators, KYC/AML screening, automated contract review | **MLRO + DPO + COLP** |
| **Limited Risk** | Transparency obligations, human oversight required | Client-facing chatbots, document summarisation tools, intake assistants | **Head of Innovation** |
| **Minimal Risk** | Internal productivity, no client data | Internal scheduling AI, training recommendation engines, IT helpdesk bots | **IT Director** |

### 3.2 Legal-Specific Prohibited Uses

The following AI applications are **expressly prohibited** within **[Firm Name]**:

1. **Autonomous reserved legal activities** — AI shall not independently exercise rights of audience, conduct litigation, prepare instruments, or perform any reserved legal activity under the Legal Services Act 2007 without real-time human solicitor control and accountability.
2. **Unsupervised reserved activities** — AI shall not perform reserved legal activities (e.g., exercising rights of audience, conducting litigation, preparing instruments) without human solicitor control (Legal Services Act 2007, s.12).
3. **Sole conflict determination** — AI-driven client conflict checking may flag potential conflicts; final determination rests with the COLP or designated compliance officer.
4. **Discriminatory pricing** — Predictive models for pricing legal services shall not use protected characteristics (race, sex, disability, religion, etc.) as direct or proxy variables (Equality Act 2010).
5. **Training on confidential data** — No client-confidential data used for model training without explicit engagement letter amendment, anonymisation to ICO standards, and DPO sign-off.
6. **Subversion of judicial process** — AI shall not be used to generate fabricated authorities, fake case law, or misleading precedents (hallucinated citations) for submission to any court or tribunal.

---

## 4. GOVERNANCE ARCHITECTURE

### 4.1 Three Lines of Defence

**First Line: Development & Operations**
- AI system owners maintain technical documentation including model cards, training data provenance, and performance benchmarks.
- Bias testing for protected characteristics conducted before deployment and annually thereafter.
- Version control for all model weights, training corpora, and deployment configurations.

**Second Line: Risk & Compliance**
- Quarterly AI risk register reviews chaired by the COLP.
- SRA notification for high-risk deployments where required (SRA Code of Conduct for solicitors, Chapter 2 — confidentiality, and Chapter 10 — reporting serious misconduct where public protection is implicated).
- EU AI Act conformity assessments for all export-facing or high-risk systems.
- Data Protection Impact Assessments (DPIAs) for AI processing personal data.

**Third Line: Internal Audit**
- Annual independent audit of the AI Management System (AIMS) against ISO 42001:2023 and review of SRA Standards and Regulations 2022 compliance.
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
- Minutes retained for **7 years** per SRA record-keeping rules (SRA Code of Conduct for solicitors, Chapter 7 — management of your business).
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

1. **Meaningful review** by a solicitor with demonstrable competence in the relevant practice area (SRA Principle 1 — uphold the rule of law and proper administration of justice; SRA Principle 5 — provide a proper standard of service);
2. **Red-line comparison** against source materials, precedents, and statutory provisions for hallucination detection;
3. **Electronic sign-off** in the matter management system with mandatory AI usage flag;
4. **Supervision record** where the reviewing solicitor is a trainee or junior associate (SRA Principle 5 — provide a proper standard of service; SRA Code of Conduct for solicitors, Chapter 7 — management of your business);
5. **Competence verification** that the solicitor has completed the firm's AI competence training (Section 6.2) before being assigned AI-assisted work.

### 6.2 Competence & Training

All fee-earners using AI tools must complete **annual CPD-accredited training** covering:

- Hallucination and confabulation risks in legal Large Language Models (LLMs);
- Bias detection in sentencing, costs, and outcome prediction models;
- SRA competence requirements when delegating work to AI (SRA Principle 1 — uphold the rule of law and proper administration of justice);
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
|---|---|---|---|
| **Critical** | Privilege breach, incorrect advice acted upon by client, SRA reportable conduct, ICO notifiable breach | **1 hour** | SRA, ICO, affected client(s), professional indemnity insurer, Law Society |
| **High** | Hallucination in filed court document, bias detected in client screening, vendor data breach affecting firm data | **4 hours** | COLP, DPO, affected client(s) |
| **Medium** | Model drift degrading accuracy, performance degradation, vendor SLA breach | **24 hours** | Head of Innovation, CTO |
| **Low** | UI bug, non-material inaccuracy, documentation gap | **72 hours** | IT Service Desk |

### 8.2 SRA Notification Protocol

Any AI-related matter that could affect **client trust, public protection, or the reputation of the firm** triggers mandatory COLP notification within **24 hours** (SRA Code of Conduct for solicitors, Chapter 2 — confidentiality, and Chapter 10 — reporting serious misconduct where public protection is implicated).

The COLP shall assess whether the matter is reportable to the SRA under the **SRA Principles** and **Standards and Regulations 2022**, and shall document the rationale for reporting or non-reporting.

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
- **SRA compliance monitoring:** Quarterly review of AI use against SRA Standards and Regulations 2022, Principles 1–7.

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
|---|---|---|---|
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

This document is controlled information under the firm's AI Management System (AIMS) per ISO/IEC 42001:2023, Clause 7.5.

### 13.1 Document Metadata

| Attribute | Value |
|---|---|
| **Document Title** | Legaltech AI Governance Policy |
| **Document Reference** | AIMS-POL-001-LT |
| **Version** | 1.1.0-PROD |
| **Effective Date** | 2026-05-18 |
| **Review Cycle** | Quarterly |
| **Next Review Date** | 2026-08-18 |
| **Document Owner** | Chief Technology Officer |
| **Author** | Governance Lead |
| **Reviewer** | Compliance Officer for Legal Practice (COLP) |
| **Approver** | Managing Partner |
| **Classification** | CONFIDENTIAL — CLIENT-FACING ON REQUEST |
| **Retention Period** | 7 years per SRA record-keeping rules / ISO 42001 Clause 7.5 |
| **Storage Location** | AIMS Document Repository (controlled access) + Board Portal |

### 13.2 Change History

| Version | Date | Author | Change Description | Status |
|---|---|---|---|---|
| **1.1.0** | 2026-05-19 | Governance Lead | Production release — ISO 42001 clause mapping, EU AI Act AIA/FRIA, SRA 2022 alignment, IP/liability, document control per Clause 7.5 | **CURRENT** |
| 1.0.0 | 2026-05-18 | Governance Lead | Initial production release — SRA/ICO/ISO 42001 aligned | SUPERSEDED |
| 0.9.0 | 2026-05-14 | Innovation Team | Internal review and red-team | SUPERSEDED |

### 13.3 Distribution & Access

- **Controlled copies:** Distributed via the firm's AIMS Document Repository with read-only access for all fee-earners and staff.
- **Uncontrolled copies:** Any printed or exported copy is marked "UNCONTROLLED — verify current version at [Firm Name] AIMS repository."
- **Client-facing copies:** Provided under NDA or within engagement letter disclosure provisions.

### 13.4 Review & Approval

- **Planned review:** Quarterly, aligned with AI Ethics & Risk Committee meetings.
- **Trigger review:** Upon regulatory change, serious incident, certification audit finding, or material change to firm AI systems.
- **Approval authority:** AI Ethics & Risk Committee and Managing Partner.
- **Obsolescence:** Superseded versions are archived for 7 years per Clause 7.5.3 and marked "SUPERSEDED — DO NOT USE."

### 13.5 Customisation Instructions (Template Users)

If you are customising this template for your organisation:

1. Replace all `[Firm Name]` placeholders with your organisation's legal name.
2. Replace `[Managing Partner Signature]` with actual electronic or wet-ink approval.
3. Update Section 2 Control Owners to match your firm's actual roles.
4. Review Section 3.2 (Prohibited Uses) with your COLP and DPO.
5. Register this document in your own AIMS per ISO 42001 Clause 7.5 with your own document reference number.
6. Conduct a gap analysis against your current AI inventory before declaring "Approved."

---

## 14. INTELLECTUAL PROPERTY & PROFESSIONAL LIABILITY

### 14.1 Ownership of AI-Generated Output

- **Draft Documents:** Raw AI-generated drafts are treated as firm internal working papers. Under UK law (Copyright, Designs and Patents Act 1988, Section 9(3)), works generated by AI without sufficient human creative input may not attract copyright protection. The firm does not represent to clients that raw AI outputs are independently copyrightable.
- **Substantively Revised Work:** Once a solicitor has meaningfully reviewed, corrected, and approved an AI-generated draft, the final work product is firm intellectual property, protected by copyright and legal professional privilege.
- **Client Delivery:** AI-assisted advice delivered to clients is licensed for the specific legal matter only. Reuse, republication, or application to other matters requires a new engagement letter.
- **Third-Party AI Outputs:** Where the firm uses vendor AI tools (e.g., LLM APIs), the firm verifies vendor terms of service to confirm no vendor IP claims over client-facing outputs. Vendor contracts must include explicit IP indemnity (Section 9.2).

### 14.2 Professional Indemnity & Liability Allocation

- **Solicitor Accountability:** The reviewing solicitor retains **full professional responsibility** for all AI-assisted work. AI is a tool, not a delegate. The SRA Standards and Regulations 2022 (Principle 5 — provide a proper standard of service; Principle 7 — comply with legal and regulatory obligations) apply without reduction.
- **Professional Indemnity Insurance:** The firm maintains PI insurance covering AI-assisted advice. The firm notifies its PI insurer of all High-Risk AI deployments. AI use does not diminish the firm's duty of care.
- **Vendor Liability Cap:** Vendor contracts cap liability at a level commensurate with risk (minimum £2 million per claim). The firm does not rely on vendor indemnity as primary protection against client claims.
- **Malpractice & Error:** AI hallucinations, confabulations, bias, or technical errors that result in client loss are firm liabilities. The reviewing solicitor is accountable for detection and correction before delivery.
- **Regulatory Liability:** Breaches of the EU AI Act, UK GDPR, or SRA Standards arising from AI use are firm regulatory liabilities. The COLP and MLRO retain reporting obligations regardless of AI involvement.

### 14.3 Contractual Position with Clients

All engagement letters for AI-assisted matters include:
- Disclosure of AI use (per Section 7.1);
- Confirmation that AI does not replace independent solicitor judgment;
- A statement that the firm retains full professional responsibility;
- Standard limitation of liability clauses adjusted to reflect AI-assisted service delivery;
- Client acknowledgment that AI outputs are reviewed by a solicitor admitted in England & Wales.

---

## 15. AI IMPACT ASSESSMENT (AIA) & FUNDAMENTAL RIGHTS IMPACT ASSESSMENT (FRIA)

### 15.1 Mandatory Trigger

An **AIA** is mandatory before deployment of any High-Risk AI system (EU AI Act Article 9). A **FRIA** is mandatory under Article 29 where the system affects rights under the EU Charter of Fundamental Rights (e.g., access to justice, fair trial, non-discrimination).

### 15.2 AIA Process (Pre-Deployment)

The AIA shall be documented in the AIMS record repository and include:

1. **System Description:** Intended purpose, capabilities, limitations, foreseeable misuse, and context of use in the UK legal sector.
2. **Risk Identification:** Map risks to Annex III category and ISO 42001 Annex A controls. Include adversarial risks (prompt injection, data poisoning).
3. **Data Governance Review:** Verify training data quality, representativeness, and absence of prohibited data (Article 10). Document data provenance and cleaning pipelines.
4. **Bias & Fairness Testing:** Test across all Equality Act 2010 protected characteristics with defined pass/fail thresholds (demographic parity ratio ≥ 0.8; equalised odds difference ≤ 0.05).
5. **Human Oversight Design:** Define oversight measures per Article 14 — natural persons must effectively oversee the system, interpret outputs, and override decisions.
6. **Cybersecurity & Robustness Assessment:** Adversarial testing, penetration testing of inference endpoints, and robustness validation per Article 15.
7. **Transparency Documentation:** Draft instructions for use (Article 13) and customer-facing disclosures (Article 52).
8. **Stakeholder Consultation:** Include affected parties (clients, court users, vulnerable groups, pro bono representatives).
9. **Mitigation & Residual Risk Plan:** Document compensating controls for risks that cannot be eliminated.
10. **Sign-off:** Approved by AI Ethics & Risk Committee and documented in AIMS records before deployment.

### 15.3 FRIA Process (Where Fundamental Rights Are Affected)

Where the AI system affects rights under the EU Charter (e.g., Article 47 — effective remedy; Article 21 — non-discrimination):

1. Identify affected rights and severity of impact.
2. Assess likelihood of impact on vulnerable groups (litigants in person, protected parties, children).
3. Design mitigation measures (human-in-the-loop, appeal pathways, alternative non-AI processes).
4. Establish post-deployment monitoring for rights impact.
5. Report findings to Board and attach to AIMS management review records.

### 15.4 Review & Maintenance

- AIAs and FRIAs are reviewed upon any material change to the AI system architecture, training data, or intended purpose.
- Annual review as part of AIMS management review (ISO 42001 Clause 9.3).
- Triggered review upon: regulatory change, serious incident, or certification audit finding.

---

## APPENDIX A: ISO/IEC 42001:2023 CLAUSE MAPPING

This policy implements the following ISO 42001:2023 management system clauses:

| ISO 42001 Clause | Clause Title | Policy Section |
|---|---|---|
| 4.1 | Understanding the organization and its context | Section 2 (Regulatory Scope & Applicability) |
| 4.2 | Understanding the needs and expectations of interested parties | Section 2 (Stakeholder mapping) |
| 4.3 | Determining the scope of the AIMS | Section 2 (Scope Includes) |
| 4.4 | AIMS and its processes | Section 4 (Governance Architecture) |
| 5.1 | Leadership and commitment | Section 1 (Executive Mandate) |
| 5.2 | AI policy | This document (Section 1) |
| 5.3 | Organizational roles, responsibilities and authorities | Section 4.1 (Three Lines of Defence) |
| 6.1 | Actions to address risks and opportunities | Section 3 (AI System Classification Matrix) |
| 6.2 | AIMS objectives and planning to achieve them | Section 11 (Implementation Roadmap) |
| 7.1 | Resources | Section 4.2 (Committee composition) |
| 7.2 | Competence | Section 6.2 (Training) |
| 7.3 | Awareness | Section 6.2 (Training) |
| 7.4 | Communication | Section 7 (Transparency & Client Disclosure) |
| 7.5 | Documented information | Section 13 (Document Control) |
| 8.1 | Operational planning and control | Section 10 (Continuous Monitoring) |
| 8.2 | AI risk assessment | Section 3 (Risk Tiers) |
| 8.3 | AI impact assessment | Section 15 (AIA & FRIA Process) |
| 8.4 | AI system lifecycle | Section 10.2 (Model Retirement & Sunsetting) |
| 9.1 | Monitoring, measurement, analysis and evaluation | Section 10.1 (Performance Monitoring) |
| 9.2 | Internal audit | Section 4.1 (Third Line — Internal Audit) |
| 9.3 | Management review | Section 4.2 (AI Ethics & Risk Committee) |
| 10.1 | Nonconformity and corrective action | Section 8 (Incident Response) |
| 10.2 | Continual improvement | Section 11 (Implementation Roadmap) |
| 10.3 | Preventive action | Section 3.2 (Legal-Specific Prohibited Uses) |

*This mapping demonstrates conformity with the ISO 42001:2023 management system structure and is subject to certification body review.*

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

*This policy is a living document. All amendments require approval by the AI Ethics & Risk Committee and the Managing Partner.*
