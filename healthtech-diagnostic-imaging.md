cd ~/Desktop/iso42001-uk-eu-rapid-compliance
mkdir -p examples

cat > examples/healthtech-diagnostic-imaging-diagnostic.md << 'EOF'
# Diagnostic Example: UK Healthtech — Diagnostic Imaging SaaS

## Scenario
MHRA-registered SaMD, NHS Trust pilot, no EU users yet.

## Diagnostic Finding
EU AI Act does not apply (no EU exposure). ISO 42001 recommended for NHS procurement credibility.

## Recommended Path
1. **Scope Diagnostic** (£2,500) — Confirm regulatory applicability
2. **ISO 42001 Rapid Roadmap** (£8,000) — Audit-ready foundation only
3. **Saved £12,000** vs. full AIMS build (not needed without EU exposure)

## Key Documents
- [AI Policy Healthtech](../templates/ai-policy-healthtech.md)
- [Risk Register](../risk-registers/ai-risk-register-template.md)
- [Getting Started Guide](../docs/getting-started.md)

---
*Anonymised diagnostic example. For illustrative purposes only.*
EOF

git add examples/
git commit -m "docs: add healthtech diagnostic example"
git push origin main
