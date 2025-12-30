import json

def log_governance(profile, dq_results, anomalies):
    report = {
        "dataset_profile": profile,
        "dq_rule_results": dq_results,
        "anomaly_count": len(anomalies)
    }

    with open("governance_report.json", "w") as f:
        json.dump(report, f, indent=4)
