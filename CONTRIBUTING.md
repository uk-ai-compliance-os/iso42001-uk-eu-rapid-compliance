# Contributing to UK Legaltech AI Governance

Thank you for improving UK legaltech governance standards.

## How to Contribute

1. **Fork** this repository
2. **Create a branch:** `git checkout -b feat/your-update`
3. **Commit** with clear messages: `docs: clarify SRA notification threshold`
4. **Open a Pull Request** with context on the regulatory or practical issue addressed

## Contribution Standards

- All changes must cite **specific regulatory sources** (SRA guidance, ICO guidance, legislation, ISO clauses).
- No "Draft" or "WIP" language in production-facing documents.
- Bias testing and accessibility considerations must be addressed for any new AI use cases.
- UK jurisdiction focus. EU/US adaptations welcome in separate files (e.g., `legaltech-ai-policy-eu.md`).

## Governance

- **Maintainer:** compliance.architect@protonmail.com
- **Review cycle:** Quarterly aligned with policy review dates

# Navigate to your repo
cd your-repo-name

# Create the file
cat > CONTRIBUTING.md << 'EOF'
# Contributing to UK Legaltech AI Governance

Thank you for improving UK legaltech governance standards.

## How to Contribute

1. **Fork** this repository
2. **Create a branch:** `git checkout -b feat/your-update`
3. **Commit** with clear messages: `docs: clarify SRA notification threshold`
4. **Open a Pull Request** with context on the regulatory or practical issue addressed

## Contribution Standards

- All changes must cite **specific regulatory sources** (SRA guidance, ICO guidance, legislation, ISO clauses).
- No "Draft" or "WIP" language in production-facing documents.
- Bias testing and accessibility considerations must be addressed for any new AI use cases.
- UK jurisdiction focus. EU/US adaptations welcome in separate files (e.g., `legaltech-ai-policy-eu.md`).

## Governance

- **Maintainer:** compliance.architect@protonmail.com
- **Review cycle:** Quarterly aligned with policy review dates
EOF

# Add, commit, push
git add CONTRIBUTING.md
git commit -m "docs: add contribution guidelines"
git push origin main
