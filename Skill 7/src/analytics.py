def compute_kpis(df):

    summary = {
        "total_orders": len(df),
        "total_revenue": df["revenue"].sum(),
        "unique_customers": df["customer_id"].nunique(),
        "top_category": df.groupby("category")["revenue"].sum().idxmax()
    }

    daily_sales = df.groupby("order_date")["revenue"].sum()

    return summary, daily_sales
