import pandas as pd
from sklearn.preprocessing import StandardScaler

def compute_rfm(df):

    reference_date = df["order_date"].max()

    rfm = df.groupby("customer_id").agg({
        "order_date": lambda x: (reference_date - x.max()).days,
        "order_id": "count",
        "amount": "sum"
    })

    rfm.columns = ["recency", "frequency", "monetary"]

    return rfm.reset_index()

def scale_features(rfm):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(rfm[["recency","frequency","monetary"]])
    return scaled
