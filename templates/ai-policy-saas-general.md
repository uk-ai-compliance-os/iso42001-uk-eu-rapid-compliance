# AI Policy Template — UK AI SaaS (General Purpose)
## ISO 42001 / EU AI Act Aligned | LLMs, Recommender Systems, and Automation

&gt; **Scope:** General-purpose AI SaaS platforms serving B2B or B2C markets  
&gt; **Regulatory Context:** UK AI White Paper 5 principles, EU AI Act (GPAI + high-risk downstream use), ICO AI guidance, consumer protection

---

## 1. Governance & Accountability

### 1.1 AI Ethics & Governance Board
- Meets quarterly.
- Cross-functional: Engineering, Product, Legal, Customer Success, Executive Sponsor.
- Mandate: Approve new AI features, review incident reports, and set risk appetite.

### 1.2 Roles
| Role | Responsibility |
|------|----------------|
| CTO / VP Engineering | Technical architecture and deployment governance |
| Head of Product | Feature risk assessment and customer communication |
| Legal / Compliance | Regulatory mapping and contract terms |
| Customer Success | Customer complaint triage and escalation |

---

## 2. Risk Management

### 2.1 System Classification
All AI features classified at design stage:
- **Prohibited:** Social scoring, subliminal techniques, exploitation of vulnerabilities → **Not built.**
- **High-risk:** If downstream use includes recruitment, credit, education, law enforcement → **Customer due diligence required.**
- **Limited risk:** Chatbots, deepfakes → **Transparency obligations.**
- **Minimal risk:** Spam filters, spell-check → **Documented but light-touch.**

### 2.2 Risk Register
- Maintained in `/risk-registers/` (see main repo).
- Reviewed monthly.
- Each risk owner assigned and accountable.

---

## 3. Data Governance

### 3.1 Training Data
- No use of customer data for model training without explicit contractual consent.
- Data minimization: Only collect what is necessary for the specified AI purpose.
- Automated PII detection and redaction in training pipelines.

### 3.2 Output Data
- Logging of all high-risk AI outputs for 12 months.
- Customer data segregation: Multi-tenant architecture with no cross-customer model leakage.

---

## 4. Transparency

### 4.1 Customer Contracts
- AI use disclosed in Master Service Agreement (MSA).
- Liability caps adjusted for high-risk AI modules.
- Customer right to audit AI governance documentation (annual, 30 days notice).

### 4.2 End-User Transparency
- AI-generated content clearly labeled.
- For LLMs: System prompts and capabilities described in product documentation.
- For recommenders: Explanation of ranking logic available on request.

---

## 5. Human Oversight

- All high-risk AI outputs subject to sampling review (minimum 5% manual inspection).
- Customer-facing AI: Escalation path to human agent always available.
- Internal AI (e.g., code generation): Human review mandatory before production deployment.

---

## 6. Security & Robustness

- Red-teaming for LLM prompt injection and jailbreaks (quarterly).
- Model output filtering for toxicity, bias, and disinformation.
- Fallback to non-AI workflow if model confidence &lt; threshold.

---

## 7. Third-Party AI (APIs, Foundation Models)

- Vendor risk assessment for all third-party AI APIs (OpenAI, Anthropic, etc.).
- Contractual requirements: Data residency, processing limitations, audit rights.
- No use of consumer-grade APIs for high-risk customer workflows.

---

## 8. Incident Response

| Severity | Trigger | Action |
|----------|---------|--------|
| Critical | Bias causing customer harm | Feature disable, executive notification, customer communication within 4h |
| High | Hallucination in high-stakes output | Manual review queue, model rollback |
| Medium | Performance degradation | Engineering sprint, customer advisory |

---

## 9. Review

- Policy reviewed every 6 months (SaaS velocity).
- Triggered also by: new AI feature launch, regulatory update, or customer incident.

---

## 10. Approval

| Role | Name | Date |
|------|------|------|
| Author | [INSERT] | [DATE] |
| Reviewer | [INSERT] | [DATE] |
| Approver (CTO/CEO) | [INSERT] | [DATE] |

---

*Part of the UK-EU AI Compliance OS. Custom SaaS AI governance frameworks available via chat-only consulting. See CONSULTING.md.*
