def profile_data(df):
    profile = {
        "rows": len(df),
        "columns": len(df.columns),
        "null_counts": df.isnull().sum().to_dict(),
        "unique_counts": df.nunique().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict()
    }
    return profile
