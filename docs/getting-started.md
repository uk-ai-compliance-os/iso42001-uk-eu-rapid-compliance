# Getting Started with the UK-EU AI Compliance OS
&gt; **Time required:** 10 minutes  
&gt; **Who this is for:** Compliance officers, CTOs, founders, and risk managers at UK AI companies  
&gt; **Goal:** Understand what this toolkit provides and decide your next step

---

## What Problem This Solves

You are a UK AI company. You have heard about:
- **ISO 42001:2023** — the new AI Management System standard
- **EU AI Act (2024/1689)** — the law that fines you up to €35 million for non-compliant high-risk AI
- **August 2, 2026** — the enforcement deadline for high-risk systems

You do not have £100,000 for a Big Four consulting firm. You do not have 12 months. You need a documented, audit-ready compliance foundation in weeks, not quarters.

**This toolkit is that foundation.**

---

## What You Get (The 5-Minute Overview)

| Asset | Location | What It Does |
|-------|----------|--------------|
| **Sector AI Policies** | `/templates/` | Copy-paste ready policies for fintech, healthtech, legaltech, insurtech, SaaS |
| **Self-Assessment Checklist** | `/gap-analysis/` | 50 questions. Score yourself. Know your gaps in 30 minutes |
| **Risk Register** | `/risk-registers/` | 15 pre-built AI risks mapped to ISO 42001 and EU AI Act |
| **Certification Roadmap** | `/docs/iso-42001-certification-roadmap.md` | Week-by-week plan from zero to audit-ready |
| **Cost Model** | `/docs/faq-certification-costs.md` | Real numbers: what BSI, LRQA, SGS charge |
| **Regulatory Crosswalk** | `/eu-ai-act-mapping/` | Map EU AI Act Annex III to ISO 42001 controls |
| **UK Body Guide** | `/uk-specific/` | Compare UKAS-accredited certification bodies |
| **Report Generator** | `/scripts/` | Python CLI that generates a gap analysis report from a JSON config |

---

## Your 3 Possible Starting Points

### Path A: "I have no idea where I stand"
1. Open [`gap-analysis/self-assessment-checklist.md`](self-assessment-checklist.md)
2. Answer the 50 yes/no questions
3. Look at your score at the bottom
4. **If below 30:** Email `compliance.architect@protonmail.com` for a diagnostic

### Path B: "I know my sector, I need a policy now"
1. Open your sector template:
   - Fintech → [`/templates/ai-policy-fintech.md`](../templates/ai-policy-fintech.md)
   - Healthtech → [`/templates/ai-policy-healthtech.md`](../templates/ai-policy-healthtech.md)
   - Legaltech → [`/templates/ai-policy-legaltech.md`](../templates/ai-policy-legaltech.md)
   - Insurtech → [`/templates/ai-policy-insurtech.md`](../templates/ai-policy-insurtech.md)
   - SaaS → [`/templates/ai-policy-saas.md`](../templates/ai-policy-saas.md)
2. Replace `[Firm Name]` and `[INSERT]` placeholders with your company details
3. Review with your legal counsel
4. Board approve and publish

### Path C: "I need certification by August 2026"
1. Open [`iso-42001-certification-roadmap.md`](iso-42001-certification-roadmap.md)
2. Check the "Emergency Sprint" section
3. Open [`faq-certification-costs.md`](faq-certification-costs.md) to budget
4. Open [`uk-specific/uk-certification-bodies-guide.md`](../uk-specific/uk-certification-bodies-guide.md) to select a body
5. **Book your certification body slot today** — even if your documentation is incomplete. Slots are filling.

---

## How This Toolkit Is Licensed

Everything in this repository is **MIT licensed**.

- You can copy, modify, and use it commercially without asking
- You can fork it for your own organisation
- You cannot hold the author liable (see [`LICENSE`](../LICENSE))

**The consulting layer is separate.** If you need bespoke adaptation, gap analysis, or certification sprint architecture, that is a paid engagement. See [`CONSULTING.md`](../CONSULTING.md).

---

## Common Questions

**Q: Is this legal advice?**  
A: No. This is compliance architecture and policy templates. Your solicitor must review before board approval.

**Q: Will this guarantee ISO 42001 certification?**  
A: No toolkit can guarantee certification. This toolkit provides the documentation foundation. Certification depends on your implementation evidence and the auditor's judgment.

**Q: I have EU customers but I am not sure if my AI is "high-risk."**  
A: Read [`faq-dual-compliance.md`](faq-dual-compliance.md) and email `compliance.architect@protonmail.com` for a scope diagnostic (£2,500, 48 hours).

**Q: Can I use this if I am not in the UK?**  
A: The templates are UK-focused (SRA, FCA, MHRA, UK GDPR). EU and US adaptations require customisation.

---

## Need Help?

📧 **compliance.architect@protonmail.com**

**What to send:**
- Company name and sector
- Number of AI systems in production
- EU customer exposure (yes/no/unknown)
- Current ISO certifications (if any)
- Target date
- Biggest compliance fear

**What you get back:** 7 diagnostic questions within 4 hours. A flat-fee proposal within 24 hours.

🚫 **No calls. No Calendly. No meetings. Chat-based only.**
