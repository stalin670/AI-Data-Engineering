def join_datasets(orders, customers, products):

    df = orders.merge(customers, on="customer_id", how="left")
    df = df.merge(products, on="product_id", how="left")

    return df
