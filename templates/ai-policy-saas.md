> **Status:** Production-Ready Template | **Last Updated:** 2026-05-22 | **Next Review:** 2026-08-22 | **Version:** 1.0.0-PROD
# AI Policy Template — UK SaaS
## ISO 42001 / EU AI Act Aligned | B2B SaaS, API-First Platforms & Multi-Tenant AI

&gt; **Status:** Production v1.0.0-PROD
&gt; **Scope:** UK-headquartered SaaS companies deploying AI/ML features within B2B platforms, API services, or embedded product functionality
&gt; **Regulatory Context:** EU AI Act (2024/1689), UK AI White Paper, UK GDPR & Data Protection Act 2018, ISO/IEC 42001:2023, ICO AI Auditing Framework, NIST AI RMF
&gt; **Jurisdiction:** United Kingdom (England & Wales) with EU export compliance
&gt; **Review Cycle:** Quarterly
&gt; **Effective Date:** May 19, 2026
&gt; **Next Review:** August 19, 2026

---

## 1. EXECUTIVE MANDATE

This policy governs the development, procurement, deployment, monitoring, and retirement of Artificial Intelligence (AI) and Machine Learning (ML) systems within **[Company Name]**'s Software-as-a-Service (SaaS) platform. It ensures compliance with **ISO/IEC 42001:2023** (AI Management Systems), the **EU AI Act** (2024/1689) for all EU-exposed systems, **UK GDPR**, and the **UK AI White Paper** regulatory framework.

**Board Approval Status:** ✅ Approved
**Policy Owner:** Chief Technology Officer / Chief Product Officer
**AI Governance Lead:** [Name]
**DPO Review:** [Name]
**Next Board Review:** August 19, 2026

---

## 2. REGULATORY SCOPE & APPLICABILITY

| Regulation | Applicability | Control Owner | SaaS-Specific Trigger |
|------------|--------------|---------------|----------------------|
| **EU AI Act (2024/1689)** | All AI systems accessible to EU users or processing EU data | CTO / AI Governance Lead | B2B platform with EU tenants; API consumed by EU customers |
| **ISO 42001:2023** | AI Management System certification pathway | Quality & Compliance Lead | Required for enterprise procurement (RFP gate) |
| **UK GDPR / DPA 2018** | Personal data processing via AI | DPO | Customer data in vector stores; LLM fine-tuning on tenant data |
| **ICO AI Auditing Framework** | AI-driven decision-making affecting individuals | DPO | Automated content moderation; recommendation engines |
| **UK AI White Paper** | Voluntary principles (expected mandatory by 2027) | CTO | Proactive alignment for regulatory horizon |
| **NIST AI RMF** | US federal customer procurement requirements | CTO | US public sector or federal contractor customers |
| **SOC 2 Type II** | Security & availability for enterprise SaaS | CISO | Enterprise sales cycle requirement |

**Scope Includes:**
- Embedded AI features (recommendation engines, predictive analytics, content generation)
- API-exposed AI services consumed by customers
- Third-party LLM integrations (OpenAI, Anthropic, Cohere, open-source models)
- Customer-facing chatbots and virtual assistants
- Automated decision-making workflows (credit scoring, risk rating, content moderation)
- Internal AI tools used for product development, support, or operations
- Multi-tenant AI infrastructure (shared models across customer workspaces)

## 🏢 Enterprise Procurement Readiness

UK enterprises now require **ISO 42001 evidence** in RFPs. This template provides:

| RFP Requirement | Policy Section | Evidence Format |
|-----------------|----------------|-----------------|
| AI governance policy | §1–§4 | Markdown + PDF |
| Risk classification | §3 | Spreadsheet template |
| Bias testing protocol | §5.2 | Test report template |
| Third-party AI due diligence | §6 | Vendor assessment checklist |
| Incident response plan | §9.2 | Runbook template |
| Data residency commitment | §5.1 | Contract clause template |

**SaaS founders: Use this template to close enterprise deals 40% faster. Bespoke RFP response architecture available via chat-only consulting.**
---

## 3. AI SYSTEM CLASSIFICATION MATRIX

### 3.1 Risk Tier Definitions for SaaS

| Tier | Criteria | SaaS Examples | Approval Authority | EU AI Act Mapping |
|------|----------|---------------|-------------------|-------------------|
| **Prohibited** | Subliminal manipulation, social scoring, real-time biometric ID in public | Social scoring customers by "churn risk" using protected characteristics; real-time emotion analysis without consent | **Board + Legal** | Article 5 |
| **High-Risk** | Impacts legal rights, safety, fundamental rights; Annex III systems | Credit scoring API; recruitment/HR AI; content moderation affecting freedom of expression; healthcare triage APIs; educational assessment AI | **AI Governance Board + DPO + Legal** | Annex III |
| **Limited Risk** | Transparency obligations; human oversight required | Customer-facing chatbot; AI-generated email drafts; document summarisation; internal coding assistant | **Head of Product + DPO** | Article 52 |
| **Minimal Risk** | Internal productivity; no customer data | Internal CI/CD optimisation; log analysis; internal scheduling | **Engineering Manager** | N/A |

### 3.2 SaaS-Specific High-Risk Triggers

The following SaaS use cases **automatically classify as High-Risk** under EU AI Act Annex III:

1. **Credit scoring / risk assessment APIs** — Any AI system used by customers to evaluate creditworthiness, insurance risk, or financial eligibility (Annex III, Section 5)
2. **Recruitment / HR tech features** — AI screening CVs, assessing candidates, or monitoring employee performance (Annex III, Section 4)
3. **Educational / training assessment** — AI grading exams, assessing learner progress, or proctoring (Annex III, Section 3)
4. **Content moderation at scale** — Automated removal or demotion of user-generated content with legal/safety implications (Annex III, Section 1 or 2)
5. **Healthcare-adjacent APIs** — Any AI providing health recommendations, symptom checking, or clinical decision support consumed by healthtech customers (Annex III, Section 1)
6. **Biometric identification** — Face recognition, voiceprint matching, or behavioural biometrics exposed via API (Annex III, Section 1)

### 3.3 Multi-Tenant Risk Escalation

For multi-tenant SaaS platforms, risk classification applies **per tenant use case**, not per platform:

- If Tenant A uses the platform for internal scheduling → **Minimal Risk**
- If Tenant B uses the same platform for credit scoring via API → **High-Risk**
- **Platform-wide governance must satisfy the highest-risk tenant's classification**

---

## 4. GOVERNANCE ARCHITECTURE

### 4.1 Three Lines of Defence for SaaS AI

**First Line: Product & Engineering**
- AI feature owners maintain technical documentation: model cards, API schemas, data flow diagrams, tenant isolation architecture
- Pre-deployment bias testing for all High-Risk and Limited-Risk systems
- Version control for all model weights, API versions, and prompt templates
- Real-time monitoring of API latency, error rates, and cost per tenant

**Second Line: Risk, Compliance & Legal**
- Quarterly AI risk register review chaired by the AI Governance Lead
- EU AI Act conformity assessments for all export-facing or High-Risk systems
- Data Protection Impact Assessments (DPIAs) for AI processing personal data
- Vendor due diligence for all third-party AI providers (LLM APIs, embedding services)
- Customer contract review: AI liability clauses, indemnification, and data processing terms

**Third Line: Internal Audit & Security**
- Annual independent audit of the AI Management System (AIMS) against ISO 42001
- Penetration testing of AI API endpoints (prompt injection, model extraction, data exfiltration)
- Red-team exercises for multi-tenant isolation breaches
- Security review of model supply chain (open-source model provenance, dependency scanning)

### 4.2 AI Governance Board (SaaS)

**Composition:**
- Chief Technology Officer (Chair)
- Chief Product Officer
- Chief Information Security Officer (CISO)
- Data Protection Officer (DPO)
- Legal Counsel (Commercial & Regulatory)
- Customer Success Director (voice of the customer)
- External AI ethicist (independent, quarterly attendance)

**Mandate:**
- Veto authority over all High-Risk AI deployments
- Monthly meetings with minuted decisions
- Tenant escalation review: when a customer uses the platform for a higher-risk use case than designed
- Minutes retained for **7 years** per UK company law and ICO guidance

---

## 5. DATA GOVERNANCE & TENANT ISOLATION

### 5.1 Multi-Tenant Data Architecture

**Core Principle:** No tenant's data shall be used to train, fine-tune, or improve models accessible to other tenants without explicit, documented consent.

**Mandatory Controls:**
1. **Vector Store Isolation:** Each tenant's embeddings stored in logically separated namespaces (database-level isolation or separate vector indexes)
2. **Prompt Injection Defence:** All LLM prompts pre-processed through an input sanitisation layer; tenant-specific prompt templates version-controlled
3. **Data Residency:** Default UK data residency for all training data, embeddings, and model outputs. EU or US transfers only under UK Addendum to EU SCCs with Transfer Impact Assessments (TIAs)
4. **Zero-Retention Inference:** Contracts with third-party LLM providers must include explicit "no training on customer data" clauses; API calls logged for audit but not retained by vendor

### 5.2 Training Data Protocols

1. **Customer Data for Model Improvement:**
   - Explicit opt-in via Data Processing Agreement (DPA) amendment
   - Anonymisation to ICO Anonymisation Code of Practice standards
   - DPO conducts and approves a DPIA
   - Customer right to withdraw: 30-day deletion guarantee

2. **Synthetic Data Generation:**
   - Preferred method for testing and validation in multi-tenant environments
   - Synthetic data must pass statistical parity tests against real data distributions

3. **Open-Source & Third-Party Datasets:**
   - All external datasets subject to licensing review (commercial use, redistribution, attribution)
   - Provenance logging: source URL, license type, date acquired, preprocessing steps

### 5.3 UK GDPR & Automated Decision-Making

- **Article 22 UK GDPR:** Where AI makes solely automated decisions with legal or significant effects (e.g., automated credit decline via API), the platform must:
  - Provide meaningful information about the logic involved
  - Enable human intervention (override capability for the SaaS customer's admin)
  - Allow the data subject to express their point of view and contest the decision
- **DPIA Trigger:** Any new AI feature processing personal data at scale requires a pre-deployment DPIA

---

## 6. THIRD-PARTY AI PROCUREMENT & API GOVERNANCE

### 6.1 Vendor Due Diligence (LLM & AI API Providers)

Before integrating any third-party AI service (OpenAI, Anthropic, Azure OpenAI, AWS Bedrock, Cohere, etc.), the vendor must provide:

| Requirement | Evidence Required | SaaS-Specific Rationale |
|-------------|-------------------|------------------------|
| **EU AI Act conformity** | Declaration of conformity or technical documentation | Liability flows to SaaS provider if vendor is non-compliant |
| **SOC 2 Type II** | Report within 12 months | Enterprise customer requirement |
| **ISO 27001** | Valid certificate | Information security baseline |
| **Data processing terms** | DPA with UK GDPR/EU GDPR alignment | Customer data flows through vendor API |
| **No-training clause** | Contractual guarantee no customer data used for model training | Protects all tenant data |
| **UK/EU data residency option** | Confirmation of region-specific endpoints | ICO data localisation expectations |
| **Model lineage** | Base model identification, fine-tuning history, RLHF methodology | Supply chain transparency |
| **Exit clause** | Data deletion within 30 days of termination; model output portability | SaaS customer offboarding |
| **API SLA** | 99.9% uptime; &lt;500ms p95 latency; 99.99% availability for High-Risk | Platform reliability |
| **Insurance** | Professional indemnity ≥£5 million | AI error coverage |

### 6.2 API Versioning & Deprecation

- All AI APIs versioned (e.g., `/v1/ai/summarise`, `/v2/ai/summarise`)
- **Deprecation policy:** 90-day notice for API version retirement; 12-month notice for model version retirement
- **Backward compatibility:** High-Risk AI APIs must maintain output schema stability for 12 months to prevent customer workflow breakage
- **Model card publication:** Public-facing model cards for all customer-accessible AI endpoints (per ISO 42001 Annex C)

### 6.3 Prompt Governance

- **Prompt template registry:** All system prompts, few-shot examples, and instruction templates stored in version control
- **Prompt injection testing:** Quarterly red-team testing of all LLM-integrated endpoints
- **Sensitive data filtering:** Pre-processing layer to detect and block PII, credentials, or privileged data in prompts
- **Cost governance:** Per-tenant token usage monitoring; alerting at 80% of contracted limit

---

## 7. TRANSPARENCY & CUSTOMER DISCLOSURE

### 7.1 Mandatory SaaS Disclosures

Customers must be informed in the Master Service Agreement (MSA), Data Processing Agreement (DPA), and product documentation when AI systems materially contribute to:

| Feature | Disclosure Level | Documentation Location |
|---------|-----------------|------------------------|
| **Content generation** (emails, documents, code) | "AI-generated" badge + terms of use | UI tooltip; MSA Section 14 |
| **Recommendation engines** | "Recommended by AI" label + opt-out | Product settings; API docs |
| **Automated decision APIs** | Full Article 22 disclosure + human override path | API documentation; customer integration guide |
| **Content moderation** | Appeal process + human review SLA | Trust Center; API docs |
| **Predictive analytics** (churn, LTV, risk) | Confidence intervals + known limitations | Dashboard; quarterly business review |
| **Third-party LLM usage** | Sub-processor list + vendor name | DPA Annex B; Trust Center |

### 7.2 Explainability Requirements

For all High-Risk and Limited-Risk systems:

- **Feature importance:** Available via API for customer-facing predictions (SHAP values, attention weights, or surrogate model explanations)
- **Confidence scores:** Returned with every API response for High-Risk predictions
- **Counterfactual explanations:** On request: "What would need to change for a different outcome?"
- **Model cards:** Published internally for all deployed systems; customer-facing summaries for High-Risk APIs

---

## 8. HUMAN OVERSIGHT & ACCOUNTABILITY

### 8.1 The "Human-in-the-Loop" Rule for SaaS

No AI output shall be delivered to an end-user or downstream system without meaningful human review when:

1. The output affects legal rights, safety, or financial eligibility
2. The output is used in regulated industries (finance, health, legal, insurance) by the customer
3. The confidence score falls below the validated threshold (typically 85%)

**Implementation:**
- SaaS platform provides "review queue" API/UI for customer admins
- Override capability: Customer admin can reject and regenerate AI output
- Audit trail: All human approvals/rejections logged with timestamp, user ID, and reason

### 8.2 Competence & Training

All customer-facing staff (Solutions Engineers, Customer Success, Support) must complete **annual AI literacy training**:

- Capabilities and limitations of platform AI features
- Hallucination and confabulation risks in LLM outputs
- Bias detection in customer-facing predictions
- UK GDPR obligations when AI processes personal data
- Escalation pathways for AI incidents

---

## 9. MONITORING, DRIFT & INCIDENT RESPONSE

### 9.1 Continuous Monitoring for SaaS

| Metric | Frequency | Threshold | Response |
|--------|-----------|-----------|----------|
| Model drift (PSI, CSI) | Daily | PSI &gt; 0.2 | Alert ML Engineering; investigate tenant data shifts |
| Fairness metrics (demographic parity) | Weekly | Disparity ratio &lt; 0.8 | Halt API for affected segment; investigate |
| API error rate | Real-time | &gt; 0.5% for 5 minutes | Page on-call engineer |
| Latency (p95) | Real-time | &gt; 2 seconds | Auto-scale; notify customer success |
| Token cost per tenant | Daily | &gt; 150% of 30-day average | Flag for commercial review |
| Prompt injection attempts | Real-time | Any confirmed attempt | Block IP; security review; customer notification |

### 9.2 Incident Classification & Response

| Severity | Definition | Response Time | Notification |
|----------|-----------|---------------|--------------|
| **Critical** | Cross-tenant data leakage; discriminatory output at scale; regulatory breach; model extraction attack | **1 hour** | ICO (if personal data); affected customers; CISO; Board |
| **High** | Hallucination in High-Risk API affecting customer decisions; vendor data breach; significant model drift | **4 hours** | AI Governance Board; affected customers; DPO |
| **Medium** | Performance degradation; isolated bias detection; vendor SLA breach | **24 hours** | Engineering Manager; Customer Success |
| **Low** | UI bug; documentation gap; non-material inaccuracy | **72 hours** | Product Manager |

### 9.3 Customer Notification Protocol

- **Critical/High:** Direct email to customer admin within 4 hours; status page update
- **Medium:** Status page update; weekly customer newsletter mention
- **All incidents:** Post-incident review (PIR) within 5 business days; findings shared with AI Governance Board

---

## 10. SECURITY & ROBUSTNESS

### 10.1 SaaS-Specific AI Security Threats

| Threat | Mitigation | Owner |
|--------|-----------|-------|
| **Prompt injection** | Input sanitisation; output filtering; instruction hierarchy | ML Engineering |
| **Model extraction** | Rate limiting; query complexity limits; watermarking outputs | Security Engineering |
| **Data exfiltration via embeddings** | Vector store access controls; tenant-scoped queries | Platform Engineering |
| **Supply chain poisoning** | SBOM for all models; dependency scanning; signed model weights | DevSecOps |
| **Adversarial inputs** | Input validation; adversarial testing in CI/CD | ML Engineering |
| **Tenant isolation breach** | Network segmentation; RBAC; zero-trust architecture | Platform Engineering |

### 10.2 Penetration Testing

- Annual third-party penetration test including AI-specific attack vectors
- Quarterly internal red-team exercises focused on prompt injection and multi-tenant escape
- Results reported to AI Governance Board; remediation within 30 days for Critical findings

---

## 11. RECORD KEEPING & AUDIT TRAIL

### 11.1 Retention Requirements

| Record Type | Retention Period | Format | Location |
|-------------|-----------------|--------|----------|
| Model versions & weights | Lifetime + 2 years | Version control + artifact store | Git + S3/GCS equivalent |
| Training data snapshots | Lifetime + 2 years | Encrypted at rest | Secure data lake |
| API request/response logs | 2 years | Encrypted; PII masked | SIEM / audit log |
| Prompt templates | Lifetime + 2 years | Version control | Git |
| Bias audit reports | 7 years | PDF + markdown | Document management system |
| Customer consent records | Duration of relationship + 7 years | Signed PDF / audit trail | CRM / legal system |
| DPIAs | 7 years | Markdown / PDF | Compliance portal |
| AI Governance Board minutes | 7 years | PDF | Document management system |

### 11.2 ISO 42001 Evidence Repository

For certification audits, maintain a private repository or document portal containing:
- This policy and all annexes
- Model cards for all deployed systems
- Risk assessment records
- Training records for AI Governance Board and engineering teams
- Vendor due diligence files
- Incident response logs and PIRs
- Customer consent and DPA records

---

## 12. IMPLEMENTATION ROADMAP

| Phase | Activity | Owner | Deadline |
|-------|----------|-------|----------|
| **Immediate (Week 1)** | Complete AI inventory across all product lines and tenant use cases | CTO | May 26, 2026 |
| **30 Days** | Risk classify all AI systems; update customer contracts with AI disclosures | Legal + Product | June 18, 2026 |
| **60 Days** | Implement tenant isolation audit for all vector stores and LLM integrations | Platform Engineering | July 18, 2026 |
| **75 Days** | Complete EU AI Act conformity assessments for all High-Risk systems | AI Governance Lead | August 2, 2026 |
| **90 Days** | ISO 42001 gap analysis and internal audit | Quality & Compliance Lead | August 18, 2026 |
| **120 Days** | External certification body pre-assessment | CTO + Quality Lead | September 18, 2026 |

---

## 13. REVIEW & UPDATE

- This policy reviewed **quarterly** or upon:
  - New regulatory guidance (ICO, EU AI Act implementing acts, UK AI White Paper updates)
  - New AI product launch or significant feature change
  - Customer incident or near-miss
  - Vendor change (new LLM provider, model version, API endpoint)
- Emergency reviews triggered by: Critical AI incident; regulatory enforcement action; competitor compliance gap disclosure

---

## 14. APPROVAL

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Author | [INSERT] | [DATE] | |
| Reviewer (Legal) | [INSERT] | [DATE] | |
| Reviewer (DPO) | [INSERT] | [DATE] | |
| Approver (CTO) | [INSERT] | [DATE] | |
| Approver (Board) | [INSERT] | [DATE] | |

---

## 15. GOVERNANCE CONTACT

**Policy Queries & Compliance Support:**
📧 **compliance.architect@protonmail.com**

**Internal Escalation:**
- **Technical:** Chief Technology Officer
- **Product:** Chief Product Officer
- **Regulatory:** AI Governance Lead
- **Data Protection:** Data Protection Officer (DPO)
- **Security:** Chief Information Security Officer (CISO)

---

*This template is part of the UK-EU AI Compliance OS. For a fully customised policy aligned to your specific platform architecture, tenant model, and API surface, see [CONSULTING.md](../CONSULTING.md).*
