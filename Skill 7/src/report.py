def print_report(summary, anomalies):

    print("\n===== E-COMMERCE KPI SUMMARY =====")
    for k,v in summary.items():
        print(f"{k} : {v}")

    print("\n===== SALES ANOMALY DAYS (AI DETECTED) =====")
    if len(anomalies) == 0:
        print("No unusual sales patterns detected.")
    else:
        print(anomalies[["date","revenue"]])
