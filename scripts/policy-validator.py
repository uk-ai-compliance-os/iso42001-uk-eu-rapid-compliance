#!/usr/bin/env python3
"""
ISO 42001 Policy Validator
Checks sector-specific AI policy documents for required ISO 42001:2023 clauses.
"""

import argparse
import re
import sys
from pathlib import Path

# ISO 42001 required policy sections mapped to controls
REQUIRED_SECTIONS = {
    "A.4.1": ["life cycle", "planning", "development process", "deployment"],
    "A.4.2": ["design", "testing", "validation", "verification"],
    "A.4.3": ["monitoring", "maintenance", "operation", "continuous improvement"],
    "A.5.1": ["risk assessment", "risk identification", "risk evaluation"],
    "A.5.2": ["impact assessment", "societal impact", "individual impact"],
    "A.5.3": ["legal compliance", "regulatory compliance", "EU AI Act", "applicable law"],
    "A.5.4": ["risk treatment", "mitigation", "residual risk", "risk acceptance"],
    "A.6.1": ["data governance", "data quality", "training data", "data lineage"],
    "A.6.2": ["privacy", "data protection", "GDPR", "personal data"],
    "A.7.1": ["transparency", "explainability", "model card", "decision logic"],
    "A.7.2": ["human oversight", "human-in-the-loop", "override", "escalation"],
    "A.7.3": ["record keeping", "audit trail", "logging", "version control"],
    "A.8.1": ["security", "model security", "adversarial", "access control"],
    "A.8.2": ["acceptable use", "employee training", "misuse", "usage policy"],
    "A.9.1": ["third-party", "vendor", "supply chain", "API", "outsourced"]
}

# Sector-specific mandatory keywords
SECTOR_KEYWORDS = {
    "fintech": ["FCA", "credit scoring", "fraud detection", "AML", "financial", "prudential"],
    "healthtech": ["MHRA", "SaMD", "clinical", "patient safety", "diagnostic", "medical device"],
    "saas": ["data governance", "EU customer", "B2B", "API", "service level"],
    "legaltech": ["SRA", "legal privilege", "confidentiality", "COLP", "COFA", "solicitors"],
    "insurtech": ["FCA", "PRA", "underwriting", "claims", "insurance", "policyholder"]
}


def validate_policy(file_path, sector=None):
    """Validate a policy markdown file against ISO 42001 requirements."""
    path = Path(file_path)

    if not path.exists():
        print(f"[ERROR] File not found: {file_path}")
        sys.exit(1)

    content = path.read_text(encoding="utf-8").lower()

    results = []
    total_controls = len(REQUIRED_SECTIONS)
    compliant_controls = 0

    for control_id, keywords in REQUIRED_SECTIONS.items():
        found = []
        missing = []

        for keyword in keywords:
            if keyword.lower() in content:
                found.append(keyword)
            else:
                missing.append(keyword)

        coverage = len(found) / len(keywords)

        if coverage >= 0.7:
            status = "PASS"
            compliant_controls += 1
        elif coverage >= 0.4:
            status = "WARNING"
        else:
            status = "FAIL"

        results.append({
            "control": control_id,
            "status": status,
            "coverage": int(coverage * 100),
            "found": found,
            "missing": missing
        })

    # Sector-specific checks
    sector_warnings = []
    if sector and sector in SECTOR_KEYWORDS:
        for keyword in SECTOR_KEYWORDS[sector]:
            if keyword.lower() not in content:
                sector_warnings.append(keyword)

    # Overall score
    overall = int((compliant_controls / total_controls) * 100)

    # Print report
    print("=" * 60)
    print(f"ISO 42001 POLICY VALIDATION REPORT")
    print("=" * 60)
    print(f"File: {path.name}")
    print(f"Sector: {sector.upper() if sector else 'Not specified'}")
    print(f"Overall Score: {overall}%")
    print(f"Controls Passed: {compliant_controls}/{total_controls}")
    print("=" * 60)

    for r in results:
        color = "🟢" if r["status"] == "PASS" else "🟡" if r["status"] == "WARNING" else "🔴"
        print(f"\n{color} {r['control']} — {r['status']} ({r['coverage']}% coverage)")

        if r["missing"]:
            print(f"   Missing keywords: {', '.join(r['missing'])}")

    if sector_warnings:
        print(f"\n⚠️  SECTOR-SPECIFIC WARNINGS ({sector.upper()}):")
        for w in sector_warnings:
            print(f"   • Missing: '{w}'")

    print("\n" + "=" * 60)

    if overall >= 80:
        print("✅ POLICY IS AUDIT-READY")
    elif overall >= 60:
        print("⚠️  POLICY NEEDS IMPROVEMENT — Address missing controls before audit")
    else:
        print("❌ POLICY HAS CRITICAL GAPS — Major revision required")

    print("=" * 60)

    return overall


def main():
    parser = argparse.ArgumentParser(
        description="ISO 42001 Policy Validator — Check policy documents for compliance gaps"
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to the policy markdown file to validate"
    )
    parser.add_argument(
        "--sector",
        "-s",
        choices=["fintech", "healthtech", "saas", "legaltech", "insurtech"],
        help="Sector for additional keyword validation"
    )

    args = parser.parse_args()
    score = validate_policy(args.input, args.sector)

    # Exit with error code if critical
    if score < 60:
        sys.exit(1)


if __name__ == "__main__":
    main()
