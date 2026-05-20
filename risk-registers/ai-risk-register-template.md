# AI Risk Register Template
&gt; **Aligned to:** ISO 42001:2023 Annex A & EU AI Act (2024/1689)  
&gt; **For:** UK AI companies preparing for August 2026 enforcement

| Risk ID | Risk Description | ISO 42001 Clause | EU AI Act Article | Likelihood | Impact | Risk Owner | Mitigation Status |
|---------|------------------|------------------|-------------------|------------|--------|------------|-------------------|
| R001 | Algorithmic bias in credit/insurance decisions leading to discriminatory outcomes | A.5 | Art. 10, Annex III.5 | High | Critical | CRO / CUO | ⬜ Open |
| R002 | Model drift degrading clinical diagnostic accuracy below safe threshold | A.5 | Art. 10, Annex III.1 | Medium | Critical | CMO / Clinical Safety Officer | ⬜ Open |
| R003 | Hallucination in legal AI generates incorrect advice acted upon by client | A.5 | Art. 52 | High | Critical | COLP / DPO | ⬜ Open |
| R004 | Vendor API change breaks AI pipeline with no rollback capability | A.6 | Art. 8 | Medium | High | CTO | ⬜ Open |
| R005 | Training data contains unconsented personal data (UK GDPR breach) | A.6 | Art. 10 | High | Critical | DPO | ⬜ Open |
| R006 | Lack of human oversight in automated hiring / HR AI decisions | A.7 | Art. 14, Annex III.4 | High | Critical | HR Director | ⬜ Open |
| R007 | EU customer uses UK SaaS AI without conformity assessment documentation | A.8 | Art. 16, Art. 22 | High | Critical | Compliance Lead | ⬜ Open |
| R008 | Prompt injection attack extracts confidential client data from legal LLM | A.5 | Art. 15 | Medium | Critical | CISO / CTO | ⬜ Open |
| R009 | Inability to explain AI decision to regulator or affected individual | A.8 | Art. 13, Art. 52 | Medium | High | Compliance Lead | ⬜ Open |
| R010 | Third-party AI vendor loses SOC 2 / ISO 27001 certification | A.6 | Art. 8 | Low | High | Procurement / Risk | ⬜ Open |
| R011 | Post-deployment adversarial input manipulates fraud detection model | A.5 | Art. 15 | Medium | High | Head of ML | ⬜ Open |
| R012 | AI system classified as "minimal risk" is later reclassified as "high-risk" by regulator | A.5 | Art. 6 | Medium | Critical | Compliance Lead | ⬜ Open |
| R013 | Insufficient audit trail for SRA / FCA / ICO investigation | A.9 | Art. 11 | High | High | COLP / Compliance | ⬜ Open |
| R014 | Data residency violation: EU patient data processed in non-compliant jurisdiction | A.6 | Art. 10 | Medium | Critical | DPO | ⬜ Open |
| R015 | August 2026 deadline passes with no conformity assessment or ISO 42001 evidence | A.10 | Art. 71 | High | Critical | CEO / Board | ⬜ Open |

---

## How to Use This Template

1. **Copy** this file into your own repository.
2. **Replace** `[Risk Owner]` names with your actual roles.
3. **Score** Likelihood and Impact using your internal methodology (1–5 or Low/Med/High).
4. **Close** mitigation tasks and attach evidence (policy docs, test results, audit logs).
5. **Review** monthly until certification audit.

---

**Custom risk architecture for your specific AI systems:**  
📧 `compliance.architect@protonmail.com`  
Flat-fee gap analysis delivered in 48 hours. Chat-only.
