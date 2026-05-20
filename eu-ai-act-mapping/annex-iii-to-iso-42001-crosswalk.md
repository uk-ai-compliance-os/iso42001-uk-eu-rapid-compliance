# EU AI Act Annex III → ISO 42001:2023 Crosswalk
&gt; **Purpose:** Map high-risk AI system categories to ISO 42001 controls for dual compliance.  
&gt; **For:** UK AI companies with EU market exposure

| EU AI Act Annex III Section | High-Risk Domain | ISO 42001:2023 Clause / Annex A Control | Compliance Action |
|-----------------------------|------------------|------------------------------------------|-------------------|
| **Section 1** | Biometric identification & categorisation | A.5 (Risk assessment), A.7 (Human oversight) | Conduct DPIA + bias audit + HITL protocol |
| **Section 2** | Critical infrastructure management (water, gas, electricity) | A.5, A.6 (Data governance), A.9 (Internal audit) | Safety case + continuous monitoring + third-party validation |
| **Section 3** | Education & vocational training (admission, assessment) | A.5, A.8 (Transparency), A.7 | Fairness testing + explainability docs + appeals process |
| **Section 4** | Employment, workers management, self-employment (recruitment, promotion) | A.5, A.7, A.8 | Bias audit across protected characteristics + human review + disclosure |
| **Section 5** | Access to essential services (credit scoring, insurance, benefits) | A.5, A.6, A.7, A.8 | Full AIA + data provenance + override authority + Article 52 notice |
| **Section 6** | Law enforcement (risk assessment, evidence evaluation) | A.5, A.6, A.7, A.9 | National security exemptions review + accuracy thresholds + audit trail |
| **Section 7** | Migration, asylum, border control | A.5, A.7, A.8 | Fundamental rights impact assessment + human-in-the-loop mandatory |
| **Section 8** | Administration of justice & democratic processes | A.5, A.7, A.8, A.9 | Highest oversight standard + explainability + independent validation |

---

## Key Mapping Notes

### Risk Management (Art. 9 EU AI Act ↔ ISO 42001 A.5)
- EU AI Act requires "continuous, iterative" risk management.
- ISO 42001 A.5 provides the management system framework for this.
- **Gap:** ISO 42001 does not prescribe specific bias tests. You must add domain-specific fairness metrics.

### Data Governance (Art. 10 EU AI Act ↔ ISO 42001 A.6)
- Both require training data suitability, representativeness, and error handling.
- **Gap:** EU AI Act explicitly bans use of sensitive data (Art. 10(5)) unless strictly necessary. ISO 42001 is silent on this — add explicit prohibition in your policy.

### Human Oversight (Art. 14 EU AI Act ↔ ISO 42001 A.7)
- EU AI Act: overseers must have "competence, authority, resources."
- ISO 42001 A.7: defines roles and responsibilities.
- **Gap:** Add training records and competence matrices to prove oversight capability.

### Transparency (Art. 52 EU AI Act ↔ ISO 42001 A.8)
- EU AI Act: user must know they are interacting with AI.
- ISO 42001 A.8: communication and disclosure.
- **Gap:** Article 52 requires specific formatting and timing of notices. Add this to your template.

---

## How to Use This Crosswalk

1. Identify your Annex III section(s).
2. Read the mapped ISO 42001 controls.
3. Check your current documentation against both columns.
4. Where there is a "Gap," create a policy amendment or evidence item.
5. Present this crosswalk to your certification body auditor — it demonstrates regulatory breadth.

---

**Need a bespoke crosswalk for your specific AI system?**  
📧 `compliance.architect@protonmail.com`  
Sector-specific mapping delivered in 48 hours. Chat-only.
