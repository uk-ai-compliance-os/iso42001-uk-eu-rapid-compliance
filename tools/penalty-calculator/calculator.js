/**
 * EU AI Act Penalty Calculator
 * UK-EU AI Compliance OS
 * Calculates penalty exposure based on EU AI Act Article 99
 */

// Configuration
const CONFIG = {
    EUR_TO_GBP: 1.20,           // Exchange rate (update as needed)
    FIXED_PENALTY_EUR: 7500000, // €7.5M fixed penalty
    PERCENTAGE_RATE: 0.015,     // 1.5% of global turnover
    ENFORCEMENT_DATE: new Date('2026-08-02'),
    SECTOR_MULTIPLIERS: {
        fintech: 1.2,
        healthtech: 1.3,
        saas: 1.0,
        legaltech: 1.1,
        insurtech: 1.15,
        other: 1.0
    }
};

// Initialize countdown on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCountdown();
    setInterval(updateCountdown, 86400000); // Update every 24 hours
});

function updateCountdown() {
    const now = new Date();
    const diff = CONFIG.ENFORCEMENT_DATE - now;
    const days = Math.ceil(diff / (1000 * 60 * 60 * 24));
    const daysElement = document.getElementById('daysLeft');
    const banner = document.getElementById('countdownBanner');
    
    if (daysElement) {
        daysElement.textContent = Math.max(0, days);
    }
    
    if (banner && days <= 30) {
        banner.style.background = '#dc3545';
        banner.style.animation = 'pulse 1s infinite';
    }
}

function calculatePenalty() {
    // Get inputs
    const revenue = parseFloat(document.getElementById('revenue').value) || 0;
    const sector = document.getElementById('sector').value;
    const aiSystems = parseInt(document.getElementById('aiSystems').value) || 0;
    const euExposure = document.getElementById('euExposure').value;
    const companySize = document.getElementById('companySize').value;

    // Validation
    if (!revenue || revenue <= 0) {
        showError('Please enter a valid annual revenue');
        return;
    }
    if (!sector) {
        showError('Please select your AI sector');
        return;
    }
    if (!euExposure) {
        showError('Please select your EU exposure level');
        return;
    }
    if (!companySize) {
        showError('Please select your company size');
        return;
    }

    // Calculate base penalty (higher of fixed or percentage)
    const fixedPenaltyGBP = CONFIG.FIXED_PENALTY_EUR * CONFIG.EUR_TO_GBP;
    const percentagePenalty = revenue * CONFIG.PERCENTAGE_RATE;
    let basePenalty = Math.max(fixedPenaltyGBP, percentagePenalty);

    // Apply sector multiplier
    const multiplier = CONFIG.SECTOR_MULTIPLIERS[sector] || 1.0;
    basePenalty = basePenalty * multiplier;

    // Risk classification logic
    const riskData = classifyRisk(sector, aiSystems, euExposure, companySize, revenue);

    // Format currency
    const formatter = new Intl.NumberFormat('en-GB', {
        style: 'currency',
        currency: 'GBP',
        maximumFractionDigits: 0
    });

    // Update DOM
    document.getElementById('penaltyAmount').textContent = formatter.format(basePenalty);
    
    document.getElementById('penaltyDetail').innerHTML = 
        `Based on the <strong>higher</strong> of:<br>` +
        `• Fixed penalty: ${formatter.format(fixedPenaltyGBP)} (€7.5M)<br>` +
        `• 1.5% of global turnover: ${formatter.format(percentagePenalty)}<br>` +
        `• Sector adjustment: ×${multiplier.toFixed(1)}`;
    
    document.getElementById('penaltyLaw').innerHTML = 
        `<strong>Legal basis:</strong> EU AI Act (2024/1689) Article 99 — ` +
        `penalties for non-compliance with high-risk system obligations`;

    // Risk tier
    const riskElement = document.getElementById('riskTier');
    riskElement.textContent = riskData.tier;
    riskElement.className = `risk-tier risk-${riskData.className}`;

    document.getElementById('riskExplanation').innerHTML = riskData.explanation;
    document.getElementById('riskActions').innerHTML = riskData.actions;

    // Update comparison table
    document.getElementById('inactionCost').textContent = formatter.format(basePenalty) + ' penalty';

    // Show results
    const resultsSection = document.getElementById('results');
    resultsSection.classList.remove('hidden');
    
    // Smooth scroll
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Track calculation (for analytics — optional)
    console.log('Penalty calculated:', {
        revenue: revenue,
        sector: sector,
        penalty: basePenalty,
        risk: riskData.tier,
        timestamp: new Date().toISOString()
    });
}

function classifyRisk(sector, aiSystems, euExposure, companySize, revenue) {
    let tier, className, explanation, actions;

    // Determine if high-risk under Annex III
    const isAnnexIII = (
        (sector === 'healthtech' && aiSystems >= 1) ||
        (sector === 'fintech' && aiSystems >= 1) ||
        (aiSystems >= 3 && (euExposure === 'yes' || euExposure === 'platform'))
    );

    if (euExposure === 'no') {
        tier = 'LOW RISK — NO DIRECT EU EXPOSURE';
        className = 'low';
        explanation = 
            `Your current configuration shows no direct EU customer or user exposure. ` +
            `However, <strong>indirect exposure</strong> through cloud providers, payment processors, ` +
            `or platform distribution may still trigger EU AI Act scope. ` +
            `ISO 42001 is strongly recommended for UK procurement credibility (NHS, government contracts).`;
        actions = 
            `<strong>Recommended action:</strong> ` +
            `<a href="mailto:compliance.architect@protonmail.com?subject=Scope%20Diagnostic%20—%20No%20EU%20Exposure">` +
            `Book a £2,500 Scope Diagnostic</a> to confirm regulatory applicability.`;
    } 
    else if (isAnnexIII) {
        tier = 'HIGH RISK — ANNEX III APPLIES';
        className = 'high';
        explanation = 
            `Your AI system(s) fall under <strong>EU AI Act Annex III</strong> high-risk categories. ` +
            `This means:<br>` +
            `• Conformity assessment is <strong>mandatory</strong> before EU market access<br>` +
            `• Your EU customers will require ISO 42001 proof in vendor due diligence<br>` +
            `• Non-compliance after August 2, 2026 exposes you to the full penalty above`;
        actions = 
            `<strong>Urgent action required:</strong> ` +
            `<a href="mailto:compliance.architect@protonmail.com?subject=URGENT%20—%20Annex%20III%20High-Risk%20—%20Need%20Roadmap">` +
            `Get the ISO 42001 Rapid Roadmap (£8,000, 10 days)</a> — audit-ready before enforcement.`;
    } 
    else if (aiSystems >= 1 && (euExposure === 'yes' || euExposure === 'platform')) {
        tier = 'LIMITED RISK — SCOPE CONFIRMATION NEEDED';
        className = 'limited';
        explanation = 
            `You have AI systems with EU exposure, but full Annex III applicability requires ` +
            `detailed scope analysis. Your sector (${sector}) and system count (${aiSystems}) ` +
            `suggest potential high-risk classification.`;
        actions = 
            `<strong>Recommended action:</strong> ` +
            `<a href="mailto:compliance.architect@protonmail.com?subject=Scope%20Diagnostic%20—%20Limited%20Risk%20Classification">` +
            `Start with the £2,500 Scope Diagnostic</a> for formal determination.`;
    } 
    else {
        tier = 'MINIMAL RISK — MONITOR REQUIRED';
        className = 'minimal';
        explanation = 
            `Current indicators suggest minimal direct regulatory exposure. ` +
            `However, AI regulation is evolving rapidly. UK AI White Paper and sector-specific ` +
            `guidance (FCA, MHRA, SRA) may impose additional requirements.`;
        actions = 
            `<strong>Recommended action:</strong> Monitor regulatory changes via ` +
            `<a href="https://github.com/uk-ai-compliance-os/iso42001-uk-eu-rapid-compliance/discussions">GitHub Discussions</a>.`;
    }

    return { tier, className, explanation, actions };
}

function showError(message) {
    // Create or update error display
    let errorDiv = document.getElementById('errorMessage');
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.id = 'errorMessage';
        errorDiv.className = 'error-message';
        document.querySelector('.calculator-form').prepend(errorDiv);
    }
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 5000);
}

// Keyboard support
document.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && e.target.tagName !== 'BUTTON') {
        calculatePenalty();
    }
});
