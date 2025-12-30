from sklearn.cluster import DBSCAN

def run_dbscan(data):

    model = DBSCAN(eps=1.2, min_samples=2)
    labels = model.fit_predict(data)

    return labels, model
