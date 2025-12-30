'''
Conceptual View

Raw Customer Transactions
        ↓
Feature Engineering (RFM Metrics)
        ↓
Scaling & Normalization
        ↓
Clustering (K-Means + DBSCAN)
        ↓
Customer Segments
        ↓
Business Insights
'''

from src.load_data import load_transactions
from src.rfm_features import compute_rfm
from src.kmeans_model import run_kmeans
from src.dbscan_model import run_dbscan
from src.report import attach_segments
from src.visualize import visualize_clusters
from src.rfm_features import scale_features

df = load_transactions()

rfm = compute_rfm(df)

scaled = scale_features(rfm)

kmeans_labels, _ = run_kmeans(scaled, k=4)
rfm = attach_segments(rfm, kmeans_labels, "kmeans_segment")

dbscan_labels, _ = run_dbscan(scaled)
rfm = attach_segments(rfm, dbscan_labels, "dbscan_segment")

print("\n===== CUSTOMER SEGMENTATION RESULT =====")
print(rfm)

visualize_clusters(rfm, kmeans_labels, "K-Means Customer Segments")
visualize_clusters(rfm, dbscan_labels, "DBSCAN Customer Segments")
