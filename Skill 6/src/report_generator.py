def print_report(profile, dq_results, anomalies):

    print("\n===== DATASET PROFILE =====")
    print(profile)

    print("\n===== DATA QUALITY RESULTS =====")
    for r in dq_results:
        print(r)

    print("\n===== AI ANOMALY DETECTION =====")
    print(anomalies[["customer_id","age","salary"]])
