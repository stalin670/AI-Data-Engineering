'''
Conceptual View
Data Source  →  Ingestion  →  Profiling  →  Quality Rules  →  AI Detection
                                           ↓
                                       Governance Log
                                           ↓
                                      Quality Report

'''
import yaml
from ingestion import load_data
from profiling import profile_data
from dq_rules import apply_rules
from ai_anomaly import detect_anomalies
from lineage import track_lineage
from governance_logger import log_governance
from report_generator import print_report

df = load_data("../data/customers_raw.csv")

profile = profile_data(df)

rules = yaml.safe_load(open("../config/quality_rules.yaml"))["rules"]

dq_results = apply_rules(df, rules)

anomalies = detect_anomalies(df, ["age","salary"])

lineage = track_lineage("customers_raw.csv", "DQ Processing")

log_governance(profile, dq_results, anomalies)

print_report(profile, dq_results, anomalies)

print("\nLineage:", lineage)
