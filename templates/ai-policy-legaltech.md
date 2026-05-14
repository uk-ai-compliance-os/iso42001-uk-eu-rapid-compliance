# AI Policy Template — UK Legaltech
## ISO 42001 / EU AI Act Aligned | Contract Analysis, Litigation Prediction & Automated Legal Research

&gt; **Scope:** AI used for legal document review, contract analysis, litigation outcome prediction, e-discovery, or automated legal research  
&gt; **Regulatory Context:** UK AI White Paper, EU AI Act high-risk (Annex III, Section 3 — administration of justice), SRA (Solicitors Regulation Authority) expectations, ICO AI guidance

---

## 1. Governance & Accountability

### 1.1 Legal AI Governance Committee
- Chaired by Managing Partner, General Counsel, or Chief Legal Officer.
- Mandatory inclusion: Data Protection Officer, Compliance Officer, AI Ethics Lead, Senior Practitioner.
- All AI systems affecting client matters or court outcomes require committee approval before deployment.

### 1.2 Roles & Responsibilities
| Role | Responsibility |
|------|----------------|
| Managing Partner / General Counsel | Ultimate accountability for AI use in client matters |
| Head of Legal Innovation | AI tool selection, implementation, and performance monitoring |
| Compliance Officer | Regulatory mapping, SRA Code of Conduct alignment, audit evidence |
| Data Protection Officer | Client data governance, DPIAs, and confidentiality impact |
| Senior Practitioner | Quality control, accuracy review, and professional judgment oversight |

---

## 2. Risk Management (ISO 42001 Annex A / EU AI Act Annex III)

### 2.1 Risk Classification
- **Litigation outcome prediction:** High-risk (EU AI Act Annex III, Section 3 — administration of justice)
- **Contract review / due diligence AI:** High-risk if used for final client advice without human review
- **Legal research / case law search:** Limited risk (transparency obligations only)
- **E-discovery:** High-risk if automated classification affects disclosure obligations or court outcomes

### 2.2 Professional Indemnity & Liability
- AI errors must not compromise solicitor-client privilege or duty of care.
- Professional indemnity insurance explicitly covers AI-assisted advice.
- Clear delineation between "AI-generated draft" and "lawyer-approved final advice."

---

## 3. Data Governance (Client Confidentiality)

### 3.1 Training Data
- **No client matter data** used for training without explicit client consent and Law Society guidance compliance.
- Public case law and legislation are acceptable training sources.
- Third-party legal AI tools must confirm: no client data retention, no model training on uploaded documents.

### 3.2 Data Quality & Provenance
- Legal knowledge cutoff dates clearly documented (law changes; outdated training data = malpractice risk).
- Jurisdiction tagging: AI outputs clearly labeled as applicable to England & Wales, Scotland, NI, or EU law.

---

## 4. Transparency & Client Communication

### 4.1 Client Disclosure
- Clients informed when AI assists in their matter (SRA Code of Conduct Transparency Principle).
- Clear explanation of: what the AI does, what it does not do, and the role of human lawyer review.
- For litigation prediction: Clients advised that predictions are probabilistic, not deterministic.

### 4.2 Court & Opposing Party Disclosure
- Where courts or procedural rules require disclosure of AI use (e.g., e-discovery protocols), disclosure is mandatory.
- No use of AI to generate submissions without human review and signature.

---

## 5. Human Oversight (Legal Professional Judgment)

- **No AI output constitutes legal advice** without qualified lawyer review and sign-off.
- Override mechanism: Senior practitioner may reject AI recommendation; reason documented in matter file.
- For high-risk systems (litigation prediction, contract finalization): Partner-level sign-off required.

---

## 6. Accuracy, Robustness & Hallucination Control

### 6.1 Hallucination Mitigation
- All AI-generated citations verified against primary sources (Legislation.gov.uk, BAILII, Westlaw).
- Automated hallucination detection: Flag outputs containing fabricated cases or statutes.
- Quarterly accuracy audit: Sample 5% of AI-assisted matters for error review.

### 6.2 System Limitations
- AI system capabilities and known limitations documented in "Instructions for Use."
- Staff training on: when to trust AI outputs, when to override, and common failure modes.

---

## 7. Bias & Fairness

- Regular testing for bias in litigation prediction across: case type, client demographics, geography, and court tier.
- Equality Act 2010 compliance: AI must not produce discriminatory outcomes in advice or case assessment.

---

## 8. Record Keeping & Audit Trail

- All AI interactions in client matters logged for **6 years** (SRA record-keeping requirement).
- Audit trail includes: input prompt, AI output, human reviewer identity, modifications made, and final advice version.
- Document retention aligned with matter file retention policies.

---

## 9. Third-Party Legal AI Tools

- Vendor due diligence includes: data processing terms, confidentiality guarantees, and subprocessor disclosure.
- Contracts prohibit vendor from training models on firm or client data.
- Annual vendor re-assessment.

---

## 10. Review & Update

- This policy reviewed **every 6 months** (legaltech moves fast; regulation evolves rapidly).
- Triggered also by: new SRA guidance, EU AI Act implementing acts, or AI-related client complaint.

---

## 11. Approval

| Role | Name | Date |
|------|------|------|
| Author | [INSERT] | [DATE] |
| Reviewer (Compliance) | [INSERT] | [DATE] |
| Approver (Managing Partner/GC) | [INSERT] | [DATE] |

---

*Part of the UK-EU AI Compliance OS. Custom legaltech AI governance frameworks available via chat-only consulting. See CONSULTING.md.*
