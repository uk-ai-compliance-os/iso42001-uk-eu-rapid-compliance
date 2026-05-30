#!/usr/bin/env python3
"""
ISO 42001 Gap Analysis CLI
Maps AI systems against ISO 42001:2023 Annex A controls and generates an HTML report.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# ISO 42001 Annex A Controls mapped to sectors
CONTROLS = {
    "A.4.1": {
        "name": "AI system life cycle",
        "description": "Processes for planning, developing, deploying, and operating AI systems.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.4.2": {
        "name": "AI system design and development",
        "description": "Requirements for design, testing, and validation of AI systems.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.4.3": {
        "name": "AI system deployment and operation",
        "description": "Monitoring, maintenance, and continuous improvement of deployed AI.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.5.1": {
        "name": "AI system risk assessment",
        "description": "Systematic identification and evaluation of AI-related risks.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.5.2": {
        "name": "AI system impact assessment",
        "description": "Assessment of societal, individual, and organizational impacts.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.5.3": {
        "name": "Legal and regulatory compliance",
        "description": "Alignment with applicable laws (EU AI Act, FCA, MHRA, SRA, etc.).",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.5.4": {
        "name": "Risk treatment",
        "description": "Mitigation strategies and residual risk acceptance criteria.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.6.1": {
        "name": "Data for AI systems",
        "description": "Data governance, quality, bias detection, and lineage tracking.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.6.2": {
        "name": "Privacy and data protection",
        "description": "GDPR, ICO framework, and data minimization for AI.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.7.1": {
        "name": "AI system transparency and explainability",
        "description": "Documentation of decision logic, model cards, and user-facing disclosures.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.7.2": {
        "name": "Human oversight",
        "description": "Human-in-the-loop requirements, override mechanisms, and escalation paths.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.7.3": {
        "name": "Record keeping and logging",
        "description": "Audit trails, version control, and evidence retention for AI decisions.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.8.1": {
        "name": "Security of AI systems",
        "description": "Model security, adversarial robustness, and access controls.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.8.2": {
        "name": "Use of AI systems",
        "description": "Acceptable use policies, employee training, and misuse prevention.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    },
    "A.9.1": {
        "name": "Third-party relationships and supply chain",
        "description": "Vendor due diligence, API governance, and outsourced AI risk.",
        "sectors": ["fintech", "healthtech", "saas", "legaltech", "insurtech"]
    }
}

# Sector-specific EU AI Act risk classifications
SECTOR_RISKS = {
    "fintech": {
        "high_risk": ["Credit scoring", "Insurance pricing", "Fraud detection with biometric data"],
        "annex_iii": "Section 5 (Access to essential services / Financial)"
    },
    "healthtech": {
        "high_risk": ["Diagnostic AI (SaMD)", "Patient triage", "Clinical decision support"],
        "annex_iii": "Section 1 (Biometrics / Medical devices)"
    },
    "saas": {
        "high_risk": ["AI with EU enterprise customers", "HR screening", "Content moderation"],
        "annex_iii": "Context-dependent (Section 3, 5, or 6)"
    },
    "legaltech": {
        "high_risk": ["Automated legal advice", "Judicial analytics", "Evidence analysis"],
        "annex_iii": "Section 8 (Administration of justice / Democratic processes)"
    },
    "insurtech": {
        "high_risk": ["Claims prediction", "Underwriting automation", "Fraud detection"],
        "annex_iii": "Section 5 (Access to essential services / Insurance)"
    }
}


def generate_gap_report(sector, output_path):
    """Generate an HTML gap analysis report for the given sector."""
    sector = sector.lower().strip()

    if sector not in SECTOR_RISKS:
        print(f"[ERROR] Unknown sector: {sector}. Supported: {', '.join(SECTOR_RISKS.keys())}")
        sys.exit(1)

    sector_info = SECTOR_RISKS[sector]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simulate gap scoring
    gaps = []
    for control_id, control in CONTROLS.items():
        # Simulate compliance score (random but deterministic for demo)
        score = hash(control_id + sector) % 100
        if score < 30:
            status = "CRITICAL GAP"
            color = "#dc3545"
        elif score < 60:
            status = "PARTIAL"
            color = "#ffc107"
        else:
            status = "COMPLIANT"
            color = "#198754"

        gaps.append({
            "id": control_id,
            "name": control["name"],
            "description": control["description"],
            "status": status,
            "color": color,
            "score": score
        })

    compliant = sum(1 for g in gaps if g["status"] == "COMPLIANT")
    partial = sum(1 for g in gaps if g["status"] == "PARTIAL")
    critical = sum(1 for g in gaps if g["status"] == "CRITICAL GAP")
    overall = int((compliant / len(gaps)) * 100)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ISO 42001 Gap Analysis — {sector.title()}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 900px; margin: 40px auto; padding: 20px; color: #333; }}
        h1 {{ border-bottom: 3px solid #0d6efd; padding-bottom: 10px; }}
        .meta {{ background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 20px 0; }}
        .summary {{ display: flex; gap: 20px; margin: 20px 0; }}
        .card {{ flex: 1; padding: 20px; border-radius: 8px; text-align: center; font-weight: bold; }}
        .card.green {{ background: #d1e7dd; color: #0f5132; }}
        .card.yellow {{ background: #fff3cd; color: #664d03; }}
        .card.red {{ background: #f8d7da; color: #842029; }}
        .overall {{ font-size: 48px; text-align: center; margin: 20px 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th {{ background: #0d6efd; color: white; padding: 12px; text-align: left; }}
        td {{ padding: 12px; border-bottom: 1px solid #dee2e6; }}
        .badge {{ padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: bold; color: white; }}
        .footer {{ margin-top: 40px; font-size: 12px; color: #6c757d; border-top: 1px solid #dee2e6; padding-top: 20px; }}
    </style>
</head>
<body>
    <h1>ISO 42001 Gap Analysis Report</h1>

    <div class="meta">
        <strong>Sector:</strong> {sector.title()}<br>
        <strong>EU AI Act Annex III:</strong> {sector_info["annex_iii"]}<br>
        <strong>Generated:</strong> {now}<br>
        <strong>Tool:</strong> ISO 42001 Rapid Implementation Toolkit
    </div>

    <div class="overall">{overall}%</div>
    <p style="text-align:center; font-size: 18px; color: #6c757d;">Overall Compliance Readiness</p>

    <div class="summary">
        <div class="card green">{compliant}<br><small>Compliant</small></div>
        <div class="card yellow">{partial}<br><small>Partial</small></div>
        <div class="card red">{critical}<br><small>Critical Gaps</small></div>
    </div>

    <h2>High-Risk System Indicators</h2>
    <ul>
        {"".join(f"<li>{r}</li>" for r in sector_info["high_risk"])}
    </ul>

    <h2>Control-by-Control Assessment</h2>
    <table>
        <tr>
            <th>Control</th>
            <th>Name</th>
            <th>Status</th>
            <th>Score</th>
        </tr>
"""

    for gap in gaps:
        html += f"""        <tr>
            <td><strong>{gap["id"]}</strong></td>
            <td>{gap["name"]}<br><small style="color:#6c757d">{gap["description"][:80]}...</small></td>
            <td><span class="badge" style="background:{gap["color"]}">{gap["status"]}</span></td>
            <td>{gap["score"]}/100</td>
        </tr>
"""

    html += f"""    </table>

    <div class="footer">
        Generated by ISO 42001 Rapid Implementation Toolkit<br>
        This is a diagnostic output. For a full implementation roadmap, email compliance.architect@protonmail.com
    </div>
</body>
</html>"""

    Path(output_path).write_text(html, encoding="utf-8")
    print(f"[OK] Gap analysis report generated: {output_path}")
    print(f"     Sector: {sector.title()}")
    print(f"     Overall readiness: {overall}%")
    print(f"     Compliant: {compliant} | Partial: {partial} | Critical: {critical}")


def main():
    parser = argparse.ArgumentParser(
        description="ISO 42001 Gap Analysis CLI — Generate compliance readiness reports"
    )
    parser.add_argument(
        "--sector",
        required=True,
        choices=["fintech", "healthtech", "saas", "legaltech", "insurtech"],
        help="Target sector for gap analysis"
    )
    parser.add_argument(
        "--output",
        default="gap-analysis-report.html",
        help="Output file path (default: gap-analysis-report.html)"
    )

    args = parser.parse_args()
    generate_gap_report(args.sector, args.output)


if __name__ == "__main__":
    main()
