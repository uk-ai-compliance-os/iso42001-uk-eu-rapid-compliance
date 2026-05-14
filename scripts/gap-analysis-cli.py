#!/usr/bin/env python3
"""
ISO 42001 / EU AI Act Gap Analysis CLI
UK-EU AI Compliance OS
Usage: python gap-analysis-cli.py
"""

import json
from datetime import datetime
from pathlib import Path

QUESTIONS = [
    ("org_name", "Organization name: "),
    ("sector", "Sector (fintech/healthtech/saas/legaltech/insurtech/other): "),
    ("ai_systems_count", "Number of AI systems in production: "),
    ("eu_exposure", "Do EU citizens/businesses use your AI? (yes/no/unknown): "),
    ("iso27001", "Do you hold ISO 27001? (yes/no/in-progress): "),
    ("ai_policy_exists", "Do you have a documented AI Policy? (yes/no/draft): "),
    ("risk_assessment_done", "Have you conducted AI risk assessments? (yes/no/partial): "),
    ("human_oversight", "Is human oversight defined for high-risk AI? (yes/no/unclear): "),
    ("data_governance", "Do you have AI-specific data governance procedures? (yes/no): "),
    ("target_date", "Target certification/compliance date (YYYY-MM-DD or 'none'): "),
]

ISO42001_CONTROLS = [
    ("4.1", "Understanding the organization and its context", ["org_name", "sector"]),
    ("4.2", "Understanding the needs and expectations of interested parties", ["eu_exposure"]),
    ("5.1", "Leadership and commitment", ["ai_policy_exists"]),
    ("6.1", "Actions to address risks and opportunities", ["risk_assessment_done"]),
    ("6.2", "AI risk assessment", ["risk_assessment_done", "ai_systems_count"]),
    ("7.5", "Documented information", ["ai_policy_exists"]),
    ("8.1", "Operational planning and control", ["human_oversight"]),
    ("8.2", "AI system impact assessment", ["risk_assessment_done", "eu_exposure"]),
    ("8.3", "AI system design and development", ["data_governance"]),
    ("8.4", "Responsible sourcing of AI systems", ["data_governance"]),
    ("8.5", "AI system deployment", ["human_oversight"]),
    ("8.6", "Monitoring and measurement", ["risk_assessment_done"]),
    ("9.1", "Monitoring, measurement, analysis and evaluation", ["risk_assessment_done"]),
    ("9.2", "Internal audit", ["ai_policy_exists"]),
    ("10.1", "Nonconformity and corrective action", ["risk_assessment_done"]),
]

EU_AI_ACT_ARTICLES = [
    ("Article 9", "Risk management system", ["risk_assessment_done"]),
    ("Article 10", "Data and data governance", ["data_governance"]),
    ("Article 13", "Transparency and provision of information to deployers", ["ai_policy_exists"]),
    ("Article 14", "Human oversight", ["human_oversight"]),
    ("Article 15", "Accuracy, robustness and cybersecurity", ["risk_assessment_done"]),
    ("Article 52", "Transparency obligations for certain AI systems", ["ai_policy_exists"]),
]

def color_status(status):
    if status == "RED":
        return f"\033[91m{status}\033[0m"
    elif status == "AMBER":
        return f"\033[93m{status}\033[0m"
    return f"\033[92m{status}\033[0m"

def main():
    print("=" * 60)
    print("ISO 42001 / EU AI Act Gap Analysis")
    print("UK-EU AI Compliance OS")
    print("=" * 60)
    print()

    answers = {}
    for key, prompt in QUESTIONS:
        answers[key] = input(prompt).strip().lower()

    # Determine scope
    eu_scope = answers["eu_exposure"] in ["yes", "y"]
    high_risk_sectors = answers["sector"] in ["fintech", "healthtech", "legaltech"]
    
    print("\n" + "=" * 60)
    print("SCOPE DETERMINATION")
    print("=" * 60)
    
    if eu_scope:
        print("EU AI Act: \033[91mIN SCOPE\033[0m (extraterritorial application applies)")
    else:
        print("EU AI Act: \033[93mREVIEW REQUIRED\033[0m (downstream use may still trigger obligations)")
    
    if high_risk_sectors:
        print(f"Sector Risk: \033[91mHIGH-RISK LIKELY\033[0m ({answers['sector']} typically Annex III)")
    else:
        print("Sector Risk: \033[93mASSESSMENT REQUIRED\033[0m")

    # ISO 42001 Gap Analysis
    print("\n" + "=" * 60)
    print("ISO 42001 CONTROL GAP ANALYSIS")
    print("=" * 60)
    print(f"{'Control':<<10} {'Status':<<8} {'Title'}")
    print("-" * 60)

    iso_gaps = 0
    for control_id, title, deps in ISO42001_CONTROLS:
        status = "GREEN"
        for dep in deps:
            val = answers.get(dep, "")
            if val in ["no", "none", "unclear", "unknown"]:
                status = "RED"
                iso_gaps += 1
                break
            elif val in ["draft", "partial", "in-progress"]:
                status = "AMBER"
        
        print(f"{control_id:<10} {color_status(status):<<18} {title}")

    # EU AI Act Gap Analysis
    print("\n" + "=" * 60)
    print("EU AI ACT ARTICLE GAP ANALYSIS")
    print("=" * 60)
    print(f"{'Article':<<15} {'Status':<<8} {'Requirement'}")
    print("-" * 60)

    eu_gaps = 0
    for article, title, deps in EU_AI_ACT_ARTICLES:
        status = "GREEN"
        for dep in deps:
            val = answers.get(dep, "")
            if val in ["no", "none", "unclear", "unknown"]:
                status = "RED"
                eu_gaps += 1
                break
            elif val in ["draft", "partial", "in-progress"]:
                status = "AMBER"

        print(f"{article:<15} {color_status(status):<<18} {title}")

    # Summary
    print("\n" + "=" * 60)
    print("EXECUTIVE SUMMARY")
    print("=" * 60)
    print(f"ISO 42001 Gaps: {iso_gaps} RED controls require immediate action")
    print(f"EU AI Act Gaps: {eu_gaps} RED articles require immediate action")
    
    if iso_gaps == 0 and eu_gaps == 0:
        print("\n\033[92mSTATUS: Ready for certification body stage 1 audit\033[0m")
    elif iso_gaps <= 3 and eu_gaps <= 2:
        print("\n\033[93mSTATUS: Foundation exists. Rapid implementation sprint recommended.\033[0m")
    else:
        print("\n\033[91mSTATUS: Critical gaps. August 2026 sprint required immediately.\033[0m")
        print("Recommendation: Engage implementation architect for 14-day emergency build.")

    # Save report
    report = {
        "generated_at": datetime.now().isoformat(),
        "answers": answers,
        "iso_gaps": iso_gaps,
        "eu_gaps": eu_gaps,
        "recommendation": "See Executive Summary above"
    }
    
    output_path = Path(f"gap-analysis-report-{answers['org_name'].replace(' ', '_')}.json")
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\nDetailed report saved to: {output_path}")

if __name__ == "__main__":
    main()
