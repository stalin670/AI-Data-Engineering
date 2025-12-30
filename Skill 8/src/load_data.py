import pandas as pd

def load_transactions():
    df = pd.read_csv("data/transactions.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df
