import pandas as pd
def clean_orders(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["quantity"] * df["price"]
    df = df.drop_duplicates()
    return df
