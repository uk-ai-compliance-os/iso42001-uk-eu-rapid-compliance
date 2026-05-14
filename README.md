# ISO 42001 UK-EU Rapid Compliance Toolkit
### August 2026 EU AI Act Enforcement Ready | UK AI Companies

[![Urgency](https://img.shields.io/badge/DEADLINE-August%202%2C%202026-red)](https://github.com/uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-green)](.)
[![Chat](https://img.shields.io/badge/Contact-Chat%20Only%20%7C%20No%20Calls-purple)](./CONSULTING.md)

&gt; **For UK AI companies with EU customers:** You are legally in scope of the EU AI Act regardless of Brexit. High-risk system enforcement begins **August 2, 2026**. Penalty exposure: up to **€35 million or 7% of global annual turnover**. This toolkit provides the open-source architecture to build your AI Management System (AIMS) and satisfy both ISO 42001 and EU AI Act conformity requirements.

---

## The August 2026 Problem

The EU AI Act's extraterritorial reach applies to UK providers and deployers whose AI systems affect EU citizens or markets. If your AI is used in the EU — even by a third party — you must comply.

**Key deadlines:**
- **August 2, 2026:** Prohibition of unacceptable-risk AI practices + obligations for high-risk systems
- **Ongoing:** Transparency requirements for general-purpose AI models

Most UK AI companies have:
- ❌ No documented AI policy
- ❌ No risk classification against EU AI Act Annex III
- ❌ No ISO 42001-aligned governance structure
- ❌ No technical documentation for conformity assessment

This toolkit closes those gaps in days, not months.

---

## What This Toolkit Provides

A complete, open-source ISO 42001 implementation architecture designed specifically for UK AI companies navigating EU regulatory pressure:

| Component | Purpose |
|-----------|---------|
| `/templates` | Sector-specific AI Policy templates (Fintech, Healthtech, SaaS, Legaltech, Insurtech) |
| `/gap-analysis` | Python CLI tool: automated ISO 42001 / EU AI Act gap assessment |
| `/risk-registers` | Pre-built risk matrices mapped to ISO 42001 Annex A and EU AI Act Annex III |
| `/eu-ai-act-mapping` | Crosswalk: ISO 42001 clauses → EU AI Act articles |
| `/uk-specific` | ICO AI auditing framework + UK AI White Paper alignment |
| `/scripts` | Automation for documentation generation and control tracking |

---

## Who This Is For

- **UK AI SaaS companies** with EU enterprise customers
- **UK Fintech/Insurtech** using AI for credit scoring, fraud detection, or underwriting
- **UK Healthtech** with clinical decision support or diagnostic AI
- **UK Legaltech** deploying automated decision-making systems
- **CTOs, Compliance Leads, and Founders** who need certification-ready documentation without a £100k Big Four engagement

---

## Quick Start (5 Minutes)

### 1. Run the Gap Analysis
```bash
git clone https://github.com/uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance.git
cd iso42001-uk-eu-rapid-compliance/scripts
pip install -r requirements.txt
python gap-analysis-cli.py
