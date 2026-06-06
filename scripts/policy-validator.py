#!/usr/bin/env python3
"""
ISO 42001 Policy Validator CLI
Checks sector-specific policies for missing ISO 42001:2023 clauses
Enhanced with conversion CTA for full policy suite delivery.
"""

import sys
import os
import re
import argparse
from datetime import datetime

# ANSI color codes
class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

# ISO 42001:2023 required policy clauses mapped by sector
POLICY_REQUIREMENTS = {
    "fintech": {
        "required_clauses": [
            "AI Risk Appetite Statement",
            "Model Risk Management (MRM) Framework",
            "Algorithmic Trading Controls",
            "Credit Scoring Fairness & Bias Testing",
            "Anti-Money Laundering (AML) AI Validation",
            "FCA FG 23/3 Alignment Declaration",
            "Data Protection Impact Assessment (DPIA)",
            "AI Incident Escalation Matrix",
            "Third-Party AI Vendor Due Diligence",
            "Customer Rights & Explainability Policy"
        ],
        "keywords": [
            "risk appetite", "model risk", "algorithmic trading", "fairness",
            "bias testing", "aml", "fca", "dpia", "incident escalation",
            "third-party", "explainability", "customer rights"
        ]
    },
    "healthtech": {
        "required_clauses": [
            "Clinical Validation & SaMD Classification",
            "MHRA Software as Medical Device Registration",
            "Patient Safety Risk Management (ISO 14971)",
            "Diagnostic AI Performance Monitoring",
            "Healthcare Data Governance (NHS DCB0129)",
            "Clinical Decision Support Transparency",
            "Adverse Event Reporting to MHRA",
            "Algorithm Change Control Procedure",
            "Patient Consent for AI-Assisted Diagnosis",
            "Cybersecurity for Connected Medical Devices"
        ],
        "keywords": [
            "clinical validation", "samd", "mhra", "patient safety", "iso 14971",
            "diagnostic", "nhs", "dcbo129", "adverse event", "change control",
            "patient consent", "cybersecurity"
        ]
    },
    "saas": {
        "required_clauses": [
            "EU AI Act High-Risk System Classification",
            "Subprocessor & AI Vendor List",
            "Customer Data Processing for AI Training",
            "API Abuse Detection & Rate Limiting",
            "Multi-Tenant AI Isolation Controls",
            "Service Level Objectives for AI Features",
            "Model Versioning & Rollback Procedure",
            "User-Facing AI Disclosure Requirements",
            "Data Retention for AI Model Inputs",
            "Cross-Border Data Transfer Safeguards"
        ],
        "keywords": [
            "eu ai act", "high-risk", "subprocessor", "vendor list", "data processing",
            "api abuse", "rate limiting", "multi-tenant", "isolation", "slo",
            "model versioning", "rollback", "disclosure", "data retention", "transfer"
        ]
    },
    "legaltech": {
        "required_clauses": [
            "SRA Code of Conduct AI Competence Requirement",
            "Legal Professional Privilege Preservation",
            "Client Confidentiality in AI Processing",
            "COLP/COFA AI Oversight Responsibilities",
            "AI-Generated Advice Disclaimer & Review",
            "Conflict Check Integration with AI Tools",
            "Billing Transparency for AI-Assisted Work",
            "Document Retention & AI Audit Trail",
            "Law Society Technology Guidance Compliance",
            "AI Bias in Legal Outcomes Monitoring"
        ],
        "keywords": [
            "sra", "competence", "privilege", "confidentiality", "colp", "cofa",
            "oversight", "disclaimer", "review", "conflict check", "billing",
            "transparency", "retention", "audit trail", "law society", "bias"
        ]
    },
    "insurtech": {
        "required_clauses": [
            "FCA/PRA AI Governance Expectations",
            "Claims Prediction Model Fairness Testing",
            "Underwriting Automation Human-in-the-Loop",
            "Pricing Algorithm Discrimination Monitoring",
            "Policyholder Notification of AI Use",
            "Model Risk Management for Actuarial AI",
            "Solvency II Data Quality for AI Inputs",
            "Fraud Detection AI False Positive Handling",
            "Customer Complaint Routing for AI Decisions",
            "AI System Stress Testing & Scenario Analysis"
        ],
        "keywords": [
            "fca", "pra", "claims prediction", "fairness", "underwriting",
            "human-in-the-loop", "pricing", "discrimination", "policyholder",
            "notification", "actuarial", "solvency ii", "fraud detection",
            "false positive", "complaint", "stress testing"
        ]
    },
    "general": {
        "required_clauses": [
            "AI Policy Statement & Strategic Objectives",
            "AI Risk Assessment Procedure",
            "AI System Life Cycle Governance",
            "Data Quality Management for AI",
            "AI Transparency & Explainability Policy",
            "Third-Party AI Risk Management",
            "AI Performance Monitoring & Validation",
            "AI Incident Response & Reporting",
            "AI Ethics Review & Stakeholder Engagement",
            "Continuous Improvement of AI Management System"
        ],
        "keywords": [
            "policy statement", "risk assessment", "life cycle", "data quality",
            "transparency", "explainability", "third-party", "performance",
            "monitoring", "incident response", "ethics", "stakeholder", "improvement"
        ]
    }
}

def print_banner():
    print(f"""
{Colors.OKCYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║     ISO 42001:2023 — POLICY VALIDATOR & COMPLIANCE CHECK    ║
║              Open Source Compliance Architecture               ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}""")

def print_cta(missing_count, sector):
    """Print conversion CTA for missing policy clauses."""
    cta_box = f"""
{Colors.WARNING}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  {missing_count} MISSING ISO 42001 CLAUSES DETECTED IN [{sector.upper()}] POLICY           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Full policy suite with evidence structures available via async delivery.    ║
║                                                                              ║
║  📧  Email: compliance.architect@protonmail.com                              ║
║  📌  Subject: IMPLEMENT-[YourCompany]-[{sector.upper()}]                              ║
║                                                                              ║
║  💷  Flat fee: £2,000  |  No Zoom. No Calendly. No meetings.                ║
║                                                                              ║
║  📦  What you get:                                                           ║
║      • Custom AIMS architecture mapped to your AI systems                    ║
║      • Sector-specific policy suite (tailored, not templated)                ║
║      • Pre-mapped risk register with evidence structures                     ║
║      • Internal audit plan + certification body prep                         ║
║                                                                              ║
║  🚀  Delivered in 7 days via private GitHub repo + email.                   ║
║      Master Services Agreement + Mutual NDA included.                        ║
║                                                                              ║
║  ⏰  Only 1 slot remaining for June 2026 delivery.                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}"""
    print(cta_box)

def load_policy_file(filepath):
    """Load and read policy file content."""
    if not os.path.exists(filepath):
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Policy file not found: {filepath}")
        print(f"{Colors.OKBLUE}[INFO]{Colors.ENDC} Run: python policy-validator.py --help")
        sys.exit(1)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return content.lower()

def validate_policy(content, sector):
    """Check policy for missing required clauses."""
    requirements = POLICY_REQUIREMENTS.get(sector, POLICY_REQUIREMENTS["general"])
    missing = []
    found = []

    for i, clause in enumerate(requirements["required_clauses"]):
        keyword = requirements["keywords"][i] if i < len(requirements["keywords"]) else clause.lower()

        # Check if keyword exists in policy content
        if keyword in content:
            found.append(clause)
        else:
            missing.append({
                "clause": clause,
                "keyword": keyword,
                "severity": "HIGH" if i < 3 else "MEDIUM"  # First 3 are critical
            })

    return found, missing

def print_results(found, missing, sector, filepath):
    """Print formatted validation results."""
    total = len(found) + len(missing)

    print(f"{Colors.BOLD}📄 Policy File:{Colors.ENDC} {filepath}")
    print(f"{Colors.BOLD}🏭 Sector:{Colors.ENDC} {sector.upper()}")
    print(f"{Colors.BOLD}📊 Total Clauses Checked:{Colors.ENDC} {total}\n")

    if not missing:
        print(f"{Colors.OKGREEN}{Colors.BOLD}✅ ALL CLAUSES PRESENT — Policy appears comprehensive!{Colors.ENDC}\n")
        print(f"{Colors.OKCYAN}Next steps:{Colors.ENDC}")
        print(f"  1. Run gap-analyzer.py to check implementation evidence")
        print(f"  2. Prepare for certification body pre-assessment\n")
        return

    high_count = sum(1 for m in missing if m["severity"] == "HIGH")

    print(f"{Colors.FAIL}{Colors.BOLD}❌ VALIDATION RESULTS{Colors.ENDC}")
    print(f"{Colors.FAIL}{Colors.BOLD}{'─' * 60}{Colors.ENDC}")
    print(f"  Clauses Found:    {len(found)}/{total}")
    print(f"  Clauses Missing:  {len(missing)}/{total}")
    print(f"  Critical Gaps:    {high_count}")
    print(f"{Colors.FAIL}{Colors.BOLD}{'─' * 60}{Colors.ENDC}\n")

    print(f"{Colors.BOLD}✅ Found Clauses:{Colors.ENDC}")
    for clause in found:
        print(f"  {Colors.OKGREEN}✓{Colors.ENDC} {clause}")

    print(f"\n{Colors.BOLD}❌ Missing Clauses:{Colors.ENDC}")
    for gap in missing:
        color = Colors.FAIL if gap["severity"] == "HIGH" else Colors.WARNING
        icon = "🔴" if gap["severity"] == "HIGH" else "🟡"
        print(f"  {color}{icon} [{gap['severity']}] {gap['clause']}{Colors.ENDC}")
        print(f"      Expected keyword: \"{gap['keyword']}\"")

    print()
    return len(missing)

def export_validation_report(found, missing, sector, filepath, output_file):
    """Export validation report to text file."""
    with open(output_file, 'w') as f:
        f.write(f"ISO 42001 Policy Validation Report\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write(f"Sector: {sector}\n")
        f.write(f"File: {filepath}\n")
        f.write(f"─" * 60 + "\n\n")

        f.write(f"CLAUSES FOUND: {len(found)}\n")
        for clause in found:
            f.write(f"  [PASS] {clause}\n")

        f.write(f"\nCLAUSES MISSING: {len(missing)}\n")
        for gap in missing:
            f.write(f"  [{gap['severity']}] {gap['clause']}\n")
            f.write(f"    Expected: {gap['keyword']}\n")

        if missing:
            f.write(f"\n\nRECOMMENDATION:\n")
            f.write(f"This policy requires {len(missing)} additional clauses to meet\n")
            f.write(f"ISO 42001:2023 requirements for {sector} sector.\n")
            f.write(f"Consider professional policy drafting services.\n")

    print(f"{Colors.OKGREEN}[SAVED]{Colors.ENDC} Validation report exported to: {output_file}\n")

def main():
    parser = argparse.ArgumentParser(
        description="ISO 42001 Policy Validator — Check for missing compliance clauses",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python policy-validator.py --policy docs/ai-policy-fintech.md --sector fintech
  python policy-validator.py --policy policy.md --sector healthtech --export report.txt
  python policy-validator.py --policy policy.md --sector saas --no-cta
        """
    )
    parser.add_argument(
        "--policy",
        required=True,
        help="Path to your AI policy markdown file to validate"
    )
    parser.add_argument(
        "--sector",
        choices=["fintech", "healthtech", "saas", "legaltech", "insurtech", "general"],
        default="general",
        help="Industry sector for targeted validation (default: general)"
    )
    parser.add_argument(
        "--export",
        metavar="FILE",
        help="Export validation report to text file"
    )
    parser.add_argument(
        "--no-cta",
        action="store_true",
        help="Suppress the implementation services CTA (for internal use)"
    )

    args = parser.parse_args()

    print_banner()

    # Load policy
    content = load_policy_file(args.policy)

    # Validate
    found, missing = validate_policy(content, args.sector)

    # Print results
    missing_count = print_results(found, missing, args.sector, args.policy)

    # Export if requested
    if args.export:
        export_validation_report(found, missing, args.sector, args.policy, args.export)

    # Print CTA unless suppressed
    if not args.no_cta and missing:
        print_cta(missing_count, args.sector)
    elif not missing and not args.no_cta:
        # Soft CTA for audit prep
        print(f"""
{Colors.OKGREEN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║  ✅ POLICY VALIDATION PASSED                                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Policy looks solid. Want a certification-ready review before audit?         ║
║                                                                              ║
║  📧  Email: compliance.architect@protonmail.com                              ║
║  📌  Subject: AUDIT-PREP-[YourCompany]-[{args.sector.upper()}]                       ║
║                                                                              ║
║  💷  Pre-audit policy review + evidence check: £500 flat fee                ║
║      → 3-day async review with annotated policy + gap fix list               ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}""")

    # Exit code: 1 if missing clauses found
    sys.exit(1 if missing else 0)

if __name__ == "__main__":
    main()
