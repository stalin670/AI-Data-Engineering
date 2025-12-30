import pandas as pd

FEATURE_COLUMNS = ["monthly_usage", "complaints", "tenure"]

def build_features(context):
    row = context.raw_data

    context.features = [
        float(row["monthly_usage"]),
        float(row["complaints"]),
        float(row["tenure"])
    ]

    return context
