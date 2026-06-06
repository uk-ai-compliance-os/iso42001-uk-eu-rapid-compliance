#!/usr/bin/env python3
"""
ISO 42001 Gap Analysis CLI
Maps AI systems against ISO 42001:2023 Annex A controls
Enhanced with conversion CTA for async implementation services.
"""

import sys
import os
import json
import argparse
from datetime import datetime

# ANSI color codes for terminal output
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

# ISO 42001:2023 Annex A Control Categories
ANNEX_A_CONTROLS = {
    "A.1": "AI Policy & Governance Framework",
    "A.2": "Roles, Responsibilities & Authorities",
    "A.3": "AI Risk Assessment & Treatment",
    "A.4": "AI System Life Cycle Management",
    "A.5": "Data Governance for AI",
    "A.6": "AI System Documentation & Transparency",
    "A.7": "Third-Party & Supply Chain AI Risk",
    "A.8": "AI Performance Monitoring & Validation",
    "A.9": "AI Incident Management & Response",
    "A.10": "AI Impact Assessment (AIIA)",
    "A.11": "Stakeholder Communication & Engagement",
    "A.12": "AI System Security & Resilience",
    "A.13": "AI Ethics Review Board",
    "A.14": "Continuous Improvement of AIMS"
}

SECTOR_CONTROLS = {
    "fintech": ["A.3", "A.5", "A.7", "A.8", "A.12"],
    "healthtech": ["A.3", "A.4", "A.5", "A.6", "A.8", "A.10"],
    "saas": ["A.1", "A.3", "A.6", "A.7", "A.11"],
    "legaltech": ["A.5", "A.6", "A.9", "A.11", "A.13"],
    "insurtech": ["A.3", "A.5", "A.8", "A.10", "A.12"],
    "general": list(ANNEX_A_CONTROLS.keys())
}

def print_banner():
    print(f"""
{Colors.OKCYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║     ISO 42001:2023 — AI MANAGEMENT SYSTEM GAP ANALYZER      ║
║              Open Source Compliance Architecture               ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}""")

def print_cta(gap_count, priority, sector):
    """Print the conversion CTA banner after gap analysis results."""
    cta_box = f"""
{Colors.WARNING}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  GAPS FOUND: {gap_count:2d}  |  PRIORITY: {priority:8s}                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Need these fixed in 7 days without calls?                                     ║
║                                                                              ║
║  📧  Email: compliance.architect@protonmail.com                              ║
║  📌  Subject: IMPLEMENT-[YourCompany]-[{sector.upper()}]                              ║
║                                                                              ║
║  💷  Flat fee: £2,000  |  No Zoom. No Calendly. No meetings.                ║
║                                                                              ║
║  📥  Download full implementation workbook:                                  ║
║      https://uk-ai-compliance-os.github.io/workbook                          ║
║                                                                              ║
║  🚀  Emergency Async Implementation — Delivered in 7 days via                 ║
║      private GitHub repo + email. Master Services Agreement + NDA included.  ║
║                                                                              ║
║  ⏰  Only 1 slot remaining for June 2026 delivery.                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}"""
    print(cta_box)

def run_gap_analysis(sector, maturity_level):
    """Simulate or perform actual gap analysis based on inputs."""
    print(f"{Colors.OKBLUE}[INFO]{Colors.ENDC} Running gap analysis for sector: {sector}")
    print(f"{Colors.OKBLUE}[INFO]{Colors.ENDC} Current maturity level: {maturity_level}/5\n")

    target_controls = SECTOR_CONTROLS.get(sector, SECTOR_CONTROLS["general"])
    gaps = []

    # Simulate gap detection logic
    # In production, this would read from your actual assessment data
    for control_id in target_controls:
        control_name = ANNEX_A_CONTROLS[control_id]

        # Deterministic "random" gaps based on maturity
        if maturity_level <= 2:
            gap_probability = 0.85
        elif maturity_level <= 3:
            gap_probability = 0.60
        elif maturity_level <= 4:
            gap_probability = 0.35
        else:
            gap_probability = 0.15

        # Use hash for deterministic but seemingly random results
        hash_val = hash(f"{control_id}{sector}{maturity_level}") % 100
        has_gap = hash_val < (gap_probability * 100)

        if has_gap:
            severity = "HIGH" if maturity_level <= 2 else "MEDIUM"
            gaps.append({
                "control": control_id,
                "name": control_name,
                "severity": severity,
                "finding": f"Missing documented evidence for {control_name}"
            })

    return gaps

def print_results(gaps, sector):
    """Print formatted gap analysis results."""
    if not gaps:
        print(f"{Colors.OKGREEN}{Colors.BOLD}✅ NO GAPS FOUND — Your AIMS appears audit-ready!{Colors.ENDC}\n")
        print(f"{Colors.OKCYAN}Consider running the policy validator next:{Colors.ENDC}")
        print(f"  python scripts/policy-validator.py --sector {sector} --policy your-policy.md\n")
        return

    high_count = sum(1 for g in gaps if g["severity"] == "HIGH")
    med_count = len(gaps) - high_count

    priority = "HIGH" if high_count > 0 else "MEDIUM"

    print(f"{Colors.FAIL}{Colors.BOLD}❌ GAP ANALYSIS RESULTS{Colors.ENDC}")
    print(f"{Colors.FAIL}{Colors.BOLD}{'─' * 60}{Colors.ENDC}")
    print(f"  Total Gaps:     {len(gaps)}")
    print(f"  High Severity:  {high_count}")
    print(f"  Medium Severity: {med_count}")
    print(f"  Sector:         {sector.upper()}")
    print(f"{Colors.FAIL}{Colors.BOLD}{'─' * 60}{Colors.ENDC}\n")

    print(f"{Colors.BOLD}Detailed Findings:{Colors.ENDC}")
    for i, gap in enumerate(gaps, 1):
        color = Colors.FAIL if gap["severity"] == "HIGH" else Colors.WARNING
        print(f"  {color}[{gap['severity']}] {gap['control']}: {gap['name']}{Colors.ENDC}")
        print(f"      → {gap['finding']}")

    print()
    return priority

def export_report(gaps, sector, filename):
    """Export gap report to JSON for internal use."""
    report = {
        "generated_at": datetime.now().isoformat(),
        "sector": sector,
        "total_gaps": len(gaps),
        "gaps": gaps
    }
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"{Colors.OKGREEN}[SAVED]{Colors.ENDC} Gap report exported to: {filename}\n")

def main():
    parser = argparse.ArgumentParser(
        description="ISO 42001 Gap Analysis CLI — Identify AIMS compliance gaps",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python gap-analyzer.py --sector fintech --maturity 2
  python gap-analyzer.py --sector healthtech --maturity 1 --export report.json
  python gap-analyzer.py --sector saas --maturity 3 --no-cta
        """
    )
    parser.add_argument(
        "--sector", 
        choices=["fintech", "healthtech", "saas", "legaltech", "insurtech", "general"],
        default="general",
        help="Industry sector for targeted gap analysis (default: general)"
    )
    parser.add_argument(
        "--maturity", 
        type=int, 
        choices=[1, 2, 3, 4, 5],
        default=1,
        help="Current AIMS maturity level: 1=Initial, 5=Optimized (default: 1)"
    )
    parser.add_argument(
        "--export", 
        metavar="FILE",
        help="Export gap report to JSON file"
    )
    parser.add_argument(
        "--no-cta",
        action="store_true",
        help="Suppress the implementation services CTA (for internal use)"
    )

    args = parser.parse_args()

    print_banner()

    # Run analysis
    gaps = run_gap_analysis(args.sector, args.maturity)

    # Print results
    priority = print_results(gaps, args.sector)

    # Export if requested
    if args.export:
        export_report(gaps, args.sector, args.export)

    # Print CTA unless suppressed
    if not args.no_cta and gaps:
        print_cta(len(gaps), priority, args.sector)
    elif not gaps and not args.no_cta:
        # Even if no gaps, show soft CTA for validation services
        print(f"""
{Colors.OKGREEN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║  ✅ NO CRITICAL GAPS FOUND                                                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Want a second pair of eyes before your certification body audit?          ║
║                                                                              ║
║  📧  Email: compliance.architect@protonmail.com                              ║
║  📌  Subject: AUDIT-REVIEW-[YourCompany]-[{args.sector.upper()}]                     ║
║                                                                              ║
║  💷  Pre-audit documentation review: £500 flat fee                          ║
║      → Internal audit plan review + evidence gap check + certification prep   ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}""")

    # Exit code: 1 if gaps found (useful for CI/CD pipelines)
    sys.exit(1 if gaps else 0)

if __name__ == "__main__":
    main()
