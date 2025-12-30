from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df, cols):

    subset = df[cols]

    # rows which are valid for model
    valid_rows = subset.dropna()

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(valid_rows)

    predictions = model.predict(valid_rows)

    # create default column = 0 (no anomaly)
    df["anomaly"] = 0

    # assign predictions only to valid rows
    df.loc[valid_rows.index, "anomaly"] = -predictions

    anomalies = df[df["anomaly"] == 1]

    return anomalies
