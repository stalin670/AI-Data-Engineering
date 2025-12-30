from sklearn.cluster import KMeans

def run_kmeans(data, k=4):

    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)

    return labels, model
