from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_sales_anomalies(daily_sales):

    sales_df = daily_sales.reset_index()
    sales_df.columns = ["date", "revenue"]

    model = IsolationForest(contamination=0.2)
    model.fit(sales_df[["revenue"]])

    sales_df["anomaly"] = model.predict(sales_df[["revenue"]])

    anomalies = sales_df[sales_df["anomaly"] == -1]

    return anomalies
