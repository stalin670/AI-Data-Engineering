from .ingestion import load_data
from .cleaning import clean_orders
from .transform import join_datasets
from .analytics import compute_kpis
from .ai_module import detect_sales_anomalies
from .report import print_report


def run_pipeline():

    orders, customers, products = load_data()

    orders = clean_orders(orders)

    df = join_datasets(orders, customers, products)

    summary, daily_sales = compute_kpis(df)

    anomalies = detect_sales_anomalies(daily_sales)

    print_report(summary, anomalies)
