'''
Raw E-Commerce Data  →  Ingestion  →  Cleaning  →  Transformations
                                                    ↓
                                      Analytics Layer (KPIs, Metrics)
                                                    ↓
                                 AI Layer (Forecast + Anomaly Detection)
                                                    ↓
                                     Automated Insights & Reports
'''
from src.pipeline import run_pipeline

if __name__ == "__main__":
    run_pipeline()
