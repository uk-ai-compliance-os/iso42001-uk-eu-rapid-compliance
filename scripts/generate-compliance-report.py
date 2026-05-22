#!/usr/bin/env python3
"""
ISO 42001 Compliance Report Generator
UK-EU AI Compliance OS — https://github.com/uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance

This CLI tool reads a JSON configuration file and generates a customised
ISO 42001 compliance readiness report in Markdown format.

Usage:
    python generate-compliance-report.py --config client-config.json --output report.md

The config file must include:
    - company_name
    - sector (fintech|healthtech|legaltech|insurtech|saas)
    - ai_systems_count
    - eu_exposure (yes|no)
    - current_iso_certifications (list)
    - target_date

⚠️ NOTE: This tool generates the REPORT STRUCTURE only. The actual gap analysis,
scoring matrix, and remediation roadmap are customised per engagement and delivered
via private GitHub repository. See CONSULTING.md for bespoke implementation support.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta


def load_config(config_path):
    """Load and validate the client configuration JSON."""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Config file not found: {config_path}")
        print("📋 Create a config file using the template below:")
        print(get_config_template())
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON in config file: {config_path}")
        sys.exit(1)
    
    required_fields = ['company_name', 'sector', 'ai_systems_count', 'eu_exposure', 'target_date']
    missing = [f for f in required_fields if f not in config]
    if missing:
        print(f"❌ Error: Missing required fields in config: {', '.join(missing)}")
        print("📋 Required fields:")
        for field in required_fields:
            print(f"   - {field}")
        sys.exit(1)
    
    valid_sectors = ['fintech', 'healthtech', 'legaltech', 'insurtech', 'saas']
    if config['sector'] not in valid_sectors:
        print(f"❌ Error: Invalid sector '{config['sector']}'. Must be one of: {', '.join(valid_sectors)}")
        sys.exit(1)
    
    return config


def get_config_template():
    """Return a sample configuration file template."""
    return '''
{
    "company_name": "Acme AI Ltd",
    "sector": "fintech",
    "ai_systems_count": 5,
    "eu_exposure": "yes",
    "current_iso_certifications": ["27001"],
    "target_date": "2026-08-02",
    "biggest_fear": "EU AI Act penalties for credit scoring AI"
}
'''


def calculate_days_to_target(target_date_str):
    """Calculate days remaining until target date."""
    try:
        target = datetime.strptime(target_date_str, '%Y-%m-%d')
        today = datetime.now()
        delta = target - today
        return max(delta.days, 0)
    except ValueError:
        return None


def get_sector_risks(sector):
    """Return sector-specific high-risk AI use cases per EU AI Act Annex III."""
    risks = {
        'fintech': [
            'Credit scoring and automated lending decisions (Annex III, Section 5)',
            'Fraud detection with automated account suspension (Annex III, Section 5)',
            'AML monitoring and suspicious activity reporting (Annex III, Section 5)',
            'Algorithmic trading and market manipulation detection (Annex III, Section 5)'
        ],
        'healthtech': [
            'Clinical decision support and diagnostic AI (Annex III, Section 1)',
            'Patient triage and prioritisation systems (Annex III, Section 1)',
            'Medical imaging analysis (Annex III, Section 1)',
            'Drug interaction prediction (Annex III, Section 1)'
        ],
        'legaltech': [
            'Litigation outcome prediction (Annex III, Section 8)',
            'Automated contract review with legal effect (Annex III, Section 8)',
            'Regulatory filing generation (Annex III, Section 8)',
            'Client conflict checking with adverse action (Annex III, Section 8)'
        ],
        'insurtech': [
            'Insurance pricing and risk scoring (Annex III, Section 4)',
            'Claims triage and automated denial (Annex III, Section 4)',
            'Fraud detection leading to policy cancellation (Annex III, Section 4)',
            'Customer risk profiling (Annex III, Section 4)'
        ],
        'saas': [
            'Biometric identification and verification (Annex III, Section 2)',
            'Emotion recognition in workplace (Annex III, Section 3)',
            'Content moderation with legal effect (Annex III, Section 6)',
            'Recruitment and HR screening (Annex III, Section 4)'
        ]
    }
    return risks.get(sector, [])


def get_iso_42001_controls():
    """Return the ISO 42001:2023 controls from Annex A."""
    return [
        ('A.4.1', 'Understanding the organisation and its context', 'Context of the organisation'),
        ('A.4.2', 'Understanding the needs and expectations of interested parties', 'Context of the organisation'),
        ('A.4.3', 'Determining the scope of the AI management system', 'Context of the organisation'),
        ('A.4.4', 'AI management system and its processes', 'Context of the organisation'),
        ('A.5.1', 'Leadership and commitment', 'Leadership'),
        ('A.5.2', 'AI policy', 'Leadership'),
        ('A.5.3', 'Organisational roles, responsibilities and authorities', 'Leadership'),
        ('A.6.1', 'Actions to address risks and opportunities', 'Planning'),
        ('A.6.2', 'AI risk assessment', 'Planning'),
        ('A.6.3', 'AI risk treatment', 'Planning'),
        ('A.6.4', 'AI objectives and planning to achieve them', 'Planning'),
        ('A.7.1', 'Resources', 'Support'),
        ('A.7.2', 'Competence', 'Support'),
        ('A.7.3', 'Awareness', 'Support'),
        ('A.7.4', 'Communication', 'Support'),
        ('A.7.5', 'Documented information', 'Support'),
        ('A.8.1', 'Operational planning and control', 'Operation'),
        ('A.8.2', 'AI system impact assessment', 'Operation'),
        ('A.8.3', 'AI system life cycle', 'Operation'),
        ('A.8.4', 'Data management', 'Operation'),
        ('A.8.5', 'AI system deployment', 'Operation'),
        ('A.8.6', 'Monitoring and measurement of AI systems', 'Operation'),
        ('A.8.7', 'Third-party and customer relationships', 'Operation'),
        ('A.9.1', 'Monitoring, measurement, analysis and evaluation', 'Performance evaluation'),
        ('A.9.2', 'Internal audit', 'Performance evaluation'),
        ('A.9.3', 'Management review', 'Performance evaluation'),
        ('A.10.1', 'Nonconformity and corrective action', 'Improvement'),
        ('A.10.2', 'Continual improvement', 'Improvement'),
    ]


def generate_report(config, output_path):
    """Generate the compliance readiness report."""
    days_remaining = calculate_days_to_target(config['target_date'])
    sector_risks = get_sector_risks(config['sector'])
    controls = get_iso_42001_controls()
    
    report = f"""# ISO 42001 Compliance Readiness Report

## {config['company_name']}

**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Sector:** {config['sector'].capitalize()}  
**AI Systems in Production:** {config['ai_systems_count']}  
**EU Customer Exposure:** {config['eu_exposure'].upper()}  
**Target Compliance Date:** {config['target_date']}  
**Days Remaining:** {days_remaining if days_remaining is not None else 'Invalid date'}  

---

## ⚠️ IMPORTANT DISCLAIMER

This report is generated from a **template structure** using the open-source ISO 42001 toolkit.

**What this report contains:**
- Sector-specific risk identification
- ISO 42001 control mapping framework
- Gap identification structure
- Remediation roadmap template

**What this report does NOT contain:**
- ❌ Tailored gap scoring matrix (sector + risk tier + regulatory exposure weighted)
- ❌ Customised remediation sequencing (what to fix first, second, third)
- ❌ Resource estimates (internal hours vs external support needed)
- ❌ Certification body pre-assessment readiness score
- ❌ Regulatory penalty exposure quantification
- ❌ Board-ready presentation deck
- ❌ Auditor response scripts

**These are delivered via bespoke engagement.**

For your tailored compliance architecture:
📧 **compliance.architect@protonmail.com**

---

## 1. Executive Summary

### 1.1 Current State Assessment

| Attribute | Value | Implication |
|-----------|-------|-------------|
| Company | {config['company_name']} | — |
| Sector | {config['sector'].capitalize()} | Determines EU AI Act Annex III risk categories |
| AI Systems | {config['ai_systems_count']} | Scale of compliance effort |
| EU Exposure | {config['eu_exposure'].upper()} | {'CRITICAL: EU AI Act applies directly' if config['eu_exposure'] == 'yes' else 'MODERATE: Monitor EU customer growth'} |
| Target Date | {config['target_date']} | {'URGENT: < 90 days to enforcement' if days_remaining and days_remaining < 90 else 'Manageable timeline'} |
| Current ISO | {', '.join(config.get('current_iso_certifications', ['None']))} | {'Foundation exists for ISO 42001' if config.get('current_iso_certifications') else 'Greenfield implementation required'} |

### 1.2 Key Findings (Template — Customised in Full Engagement)

<!-- CUSTOMISATION REQUIRED: This section contains placeholder findings only.
Actual findings are derived from:
1. Document review (policies, procedures, evidence)
2. Stakeholder interviews (async, via email)
3. System architecture review
4. Regulatory mapping analysis

For tailored findings and prioritised remediation roadmap:
📧 Email: compliance.architect@protonmail.com
💼 Service: EU AI Act Scope Diagnostic (£2,500, 48 hours)
-->

**Placeholder Findings:**
- [ ] AI governance structure not formally documented
- [ ] Risk classification incomplete for {config['ai_systems_count']} AI systems
- [ ] EU AI Act Annex III mapping not conducted
- [ ] ISO 42001 gap analysis not performed
- [ ] Evidence repository structure not defined

**These are generic placeholders. Your actual gaps will be different.**

---

## 2. Regulatory Scope & Risk Classification

### 2.1 EU AI Act Applicability

**EU Customer Exposure:** {config['eu_exposure'].upper()}

{'**DIRECT APPLICABILITY:** Your AI systems are used by EU citizens/residents. EU AI Act applies in full. You must comply with Annex III high-risk requirements by August 2, 2026.' if config['eu_exposure'] == 'yes' else '**INDIRECT APPLICABILITY:** No current EU customers. Monitor for future expansion. EU AI Act may apply if EU users access your systems.'}

### 2.2 Sector-Specific High-Risk AI Systems (EU AI Act Annex III)

Based on your sector (**{config['sector'].capitalize()}**), the following AI use cases are likely high-risk:

| # | High-Risk Use Case | Annex III Section | Priority |
|---|-------------------|-------------------|----------|
"""
    
    for i, risk in enumerate(sector_risks, 1):
        report += f"| {i} | {risk} | {'Section 5' if config['sector'] == 'fintech' else 'Section 1' if config['sector'] == 'healthtech' else 'Section 8' if config['sector'] == 'legaltech' else 'Section 4' if config['sector'] == 'insurtech' else 'Various'} | 🔴 Critical |\n"
    
    report += f"""

<!-- CUSTOMISATION REQUIRED: This list is sector-generic. Your actual high-risk systems may differ.
For formal scope determination and risk classification:
📧 Email: compliance.architect@protonmail.com
💼 Service: EU AI Act Scope Diagnostic (£2,500, 48 hours)

What you receive:
- Formal scope determination (does EU AI Act apply to YOUR specific systems?)
- Risk tier classification for each AI system (Prohibited / High-risk / Limited-risk / Minimal-risk)
- Regulatory exposure report (penalty exposure quantification)
- 90-day action checklist with week-by-week milestones
-->

---

## 3. ISO 42001:2023 Control Mapping

### 3.1 Control Framework

The following controls from ISO 42001:2023 Annex A are applicable to your organisation:

| Control ID | Control Name | Clause | Status | Evidence |
|------------|-------------|--------|--------|----------|
"""
    
    for code, name, clause in controls:
        report += f"| {code} | {name} | {clause} | ☐ Not Assessed | ☐ Not Available |\n"
    
    report += f"""

<!-- CUSTOMISATION REQUIRED: Each control must be assessed against your specific:
- Policies and procedures
- Evidence and documentation
- Implementation maturity
- Gap severity (Critical / High / Medium / Low)

For control-by-control gap analysis with evidence requirements:
📧 Email: compliance.architect@protonmail.com
💼 Service: ISO 42001 Rapid Implementation Roadmap (£8,000, 10 days)

What you receive:
- Custom AIMS architecture
- Control mapping tailored to your sector
- Policy suite (customised to your systems)
- Internal audit plan
- Certification body pre-assessment prep
-->

---

## 4. Gap Analysis Summary

### 4.1 Gap Identification Matrix (Template)

| Gap ID | Description | ISO 42001 Control | EU AI Act Article | Severity | Status |
|--------|-------------|-------------------|-------------------|----------|--------|
| GAP-001 | AI governance policy not formally approved | A.5.2 | N/A | 🔴 Critical | ☐ Open |
| GAP-002 | AI risk assessment not conducted | A.6.2 | Article 9 | 🔴 Critical | ☐ Open |
| GAP-003 | EU AI Act risk classification incomplete | A.6.1 | Article 6 | 🔴 Critical | ☐ Open |
| GAP-004 | Model cards not maintained | A.7.5 | Article 11 | 🟡 High | ☐ Open |
| GAP-005 | Human oversight protocol not defined | A.8.5 | Article 14 | 🔴 Critical | ☐ Open |
| GAP-006 | Bias testing not conducted | A.8.2 | Article 10 | 🟡 High | ☐ Open |
| GAP-007 | Incident response plan not documented | A.8.1 | Article 62 | 🟡 High | ☐ Open |
| GAP-008 | Third-party AI vendor due diligence incomplete | A.8.7 | Article 25 | 🟢 Medium | ☐ Open |

<!-- CUSTOMISATION REQUIRED: This is a generic gap list. Your actual gaps will be different.
The severity ratings above are NOT calibrated to your specific situation.

For your tailored gap analysis:
📧 Email: compliance.architect@protonmail.com
💼 Service: Full AIMS Build + Certification Sprint (£15,000, 30 days)

What you receive:
- Complete documentation set (policies, procedures, templates)
- Evidence repository structure
- 2 rounds of async review and refinement
- Board presentation deck
- Auditor response scripts
- Certification body pre-assessment readiness score
-->

---

## 5. Remediation Roadmap (Template)

### 5.1 Suggested Timeline (Not Calibrated)

| Phase | Activities | Duration | Target Completion |
|-------|-----------|----------|-----------------|
| Phase 1: Foundation | Governance structure, risk classification, policy framework | Weeks 1–2 | [DATE] |
| Phase 2: Documentation | Policy suite, procedures, evidence templates | Weeks 3–4 | [DATE] |
| Phase 3: Implementation | Control implementation, evidence collection | Weeks 5–8 | [DATE] |
| Phase 4: Validation | Internal audit, gap closure, pre-assessment | Weeks 9–10 | [DATE] |
| Phase 5: Certification | Certification body engagement, audit | Weeks 11–12 | [DATE] |

<!-- CUSTOMISATION REQUIRED: This timeline is generic and NOT calibrated to:
- Your current maturity level
- Your resource availability (internal team size and capacity)
- Your target certification date ({config['target_date']})
- Your sector-specific requirements
- Your certification body availability

For a realistic, achievable timeline:
📧 Email: compliance.architect@protonmail.com
💼 Service: ISO 42001 Rapid Implementation Roadmap (£8,000, 10 days)

What you receive:
- Week-by-week implementation plan
- Resource allocation (internal vs external)
- Milestone definitions and acceptance criteria
- Risk-adjusted timeline (buffer for delays)
- Certification body selection and booking strategy
-->

---

## 6. Next Steps

### 6.1 Immediate Actions (This Week)

1. **Confirm regulatory scope** — Does EU AI Act apply to YOUR specific AI systems?
2. **Validate risk classification** — Are your AI systems correctly tiered?
3. **Assess current maturity** — What documentation and evidence already exists?
4. **Define target state** — What does "compliant" look like for your organisation?

### 6.2 Get Your Tailored Assessment

This report is a **starting point**. To move from "template" to "certification-ready":

| Service | What's Included | Investment | Timeline |
|---------|----------------|------------|----------|
| **EU AI Act Scope Diagnostic** | Formal scope determination, risk classification, regulatory exposure report, 90-day action checklist | £2,500 | 48 hours |
| **ISO 42001 Rapid Roadmap** | Custom AIMS architecture, control mapping, policy suite, internal audit plan, certification body pre-assessment prep | £8,000 | 10 days |
| **Full AIMS Build + Cert Sprint** | Complete documentation set, evidence repository structure, 2 rounds of async review, board presentation deck, auditor response scripts | £15,000 | 30 days |
| **August 2026 Emergency Sprint** | For high-risk systems with < 90 days to enforcement. Everything in Full Build, compressed to 14-day delivery with daily async check-ins. | £20,000 | 14 days |

📧 **Email:** compliance.architect@protonmail.com

**Include in your email:**
- This report (attach or link)
- Your answers to the 7 diagnostic questions (see CONSULTING.md)
- Your biggest compliance fear right now

⏱️ **Response time:** < 4 hours during UK business hours (09:00–18:00 BST)
🚫 **No calls. No Calendly. No meetings. Chat-based only.**

---

*This report was generated using the UK-EU AI Compliance OS open-source toolkit.*
*For a fully customised compliance architecture, see CONSULTING.md.*
"""
    
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"✅ Report generated: {output_path}")
    print(f"📊 Company: {config['company_name']}")
    print(f"🏢 Sector: {config['sector'].capitalize()}")
    print(f"🤖 AI Systems: {config['ai_systems_count']}")
    print(f"🇪🇺 EU Exposure: {config['eu_exposure'].upper()}")
    print(f"📅 Days Remaining: {days_remaining if days_remaining is not None else 'N/A'}")
    print(f"\n⚠️  This is a TEMPLATE report. For tailored analysis, see CONSULTING.md")


def main():
    parser = argparse.ArgumentParser(
        description='ISO 42001 Compliance Report Generator — UK-EU AI Compliance OS'
    )
    parser.add_argument(
        '--config', '-c',
        required=True,
        help='Path to client configuration JSON file'
    )
    parser.add_argument(
        '--output', '-o',
        default='compliance-report.md',
        help='Output path for generated report (default: compliance-report.md)'
    )
    
    args = parser.parse_args()
    
    print("🔧 UK-EU AI Compliance OS — Report Generator")
    print("=" * 50)
    
    config = load_config(args.config)
    generate_report(config, args.output)
    
    print("\n✨ Done!")


if __name__ == '__main__':
    main()
