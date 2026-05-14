#!/usr/bin/env python3
"""
MLflow Governance Hook for ISO 42001 Audit Trails
UK-EU AI Compliance OS

Auto-logs ML experiment parameters, metrics, and artifacts
in ISO 42001-compliant format for audit evidence.

Usage:
    import mlflow_governance_hook as gov
    gov.log_experiment_run(
        model_name="credit_risk_v2",
        version="2.1.0",
        parameters={"max_depth": 12, "n_estimators": 500},
        metrics={"auc_roc": 0.847, "demographic_parity": 0.023},
        training_data_hash="sha256:a1b2c3...",
        dataset_provenance="internal_crm_2026_q1.csv"
    )
"""

import json
import hashlib
import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class GovernanceLogger:
    """
    ISO 42001 compliant experiment logger.
    Generates audit-ready JSON records per Clause 7.5 (Documented Information)
    and Clause 8.3 (AI system design and development).
    """
    
    def __init__(self, output_dir: str = "governance_logs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.run_id = self._generate_run_id()
        
    def _generate_run_id(self) -> str:
        timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        return f"aims_run_{timestamp}"
    
    def _hash_artifact(self, content: bytes) -> str:
        return f"sha256:{hashlib.sha256(content).hexdigest()}"
    
    def log_experiment_run(
        self,
        model_name: str,
        version: str,
        parameters: Dict[str, Any],
        metrics: Dict[str, float],
        training_data_hash: str,
        dataset_provenance: str,
        bias_audit_results: Optional[Dict[str, float]] = None,
        human_oversight_approved: bool = False,
        approver: Optional[str] = None,
        notes: Optional[str] = None
    ) -> str:
        """
        Log a complete experiment run in ISO 42001 audit format.
        
        Returns the run_id for reference in AIMS documentation.
        """
        
        record = {
            "run_id": self.run_id,
            "timestamp_utc": datetime.datetime.utcnow().isoformat(),
            "iso_42001_clause": ["7.5", "8.3", "8.6"],
            "eu_ai_act_article": ["Article 10", "Article 11", "Article 15"],
            
            "model_identity": {
                "name": model_name,
                "version": version,
                "run_id": self.run_id
            },
            
            "design_and_development": {
                "parameters": parameters,
                "hyperparameter_search_method": notes or "manual",
                "development_environment": "documented_in_aims_manual"
            },
            
            "data_governance": {
                "training_data_hash": training_data_hash,
                "dataset_provenance": dataset_provenance,
                "data_quality_check": "documented_in_data_governance_procedure"
            },
            
            "performance_validation": {
                "metrics": metrics,
                "validation_methodology": "stratified_k_fold",
                "test_set_holdout": "documented_in_validation_plan"
            },
            
            "fairness_and_bias": {
                "bias_audit_results": bias_audit_results or {"status": "pending"},
                "protected_characteristics_tested": ["age", "gender", "ethnicity"],
                "fairness_threshold": "demographic_parity < 0.05"
            },
            
            "human_oversight": {
                "approval_required": True,
                "approved": human_oversight_approved,
                "approver": approver,
                "approval_timestamp": datetime.datetime.utcnow().isoformat() if human_oversight_approved else None
            },
            
            "audit_trail": {
                "log_format_version": "1.0",
                "integrity_hash": None,  # Computed below
                "retention_years": 6
            }
        }
        
        # Compute integrity hash for tamper evidence
        record_json = json.dumps(record, sort_keys=True)
        record["audit_trail"]["integrity_hash"] = self._hash_artifact(record_json.encode())
        
        # Save to file
        output_file = self.output_dir / f"{self.run_id}.json"
        with open(output_file, "w") as f:
            json.dump(record, f, indent=2)
        
        print(f"[GOVERNANCE] ISO 42001 audit record saved: {output_file}")
        print(f"[GOVERNANCE] Run ID: {self.run_id}")
        print(f"[GOVERNANCE] Integrity: {record['audit_trail']['integrity_hash']}")
        
        if not human_oversight_approved:
            print("[WARNING] Human oversight not recorded. ISO 42001 Clause 8.5 requires HITL sign-off before deployment.")
        
        return self.run_id


# Example usage for documentation
if __name__ == "__main__":
    logger = GovernanceLogger()
    
    # Example: Credit scoring model training run
    run_id = logger.log_experiment_run(
        model_name="credit_risk_classifier",
        version="2.1.0",
        parameters={
            "algorithm": "xgboost",
            "max_depth": 12,
            "n_estimators": 500,
            "learning_rate": 0.05
        },
        metrics={
            "auc_roc": 0.847,
            "precision": 0.812,
            "recall": 0.789,
            "demographic_parity": 0.023,
            "equalized_odds": 0.041
        },
        training_data_hash="sha256:a1b2c3d4e5f6789012345678901234567890abcdef",
        dataset_provenance="internal_crm_extract_2026_q1_v3.csv",
        bias_audit_results={
            "gender_parity": 0.018,
            "age_fairness": 0.031,
            "ethnicity_equalized_odds": 0.042
        },
        human_oversight_approved=True,
        approver="Dr. Sarah Chen, Chief Risk Officer",
        notes="Production candidate for EU market deployment. Fairness audit passed all thresholds."
    )
    
    print(f"\nExample complete. In production, store {run_id} in your AIMS configuration management database.")
