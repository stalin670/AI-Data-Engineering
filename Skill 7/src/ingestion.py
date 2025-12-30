import pandas as pd

def load_data():
    orders = pd.read_csv("data/orders.csv")
    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")

    return orders, customers, products
