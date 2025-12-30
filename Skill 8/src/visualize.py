import matplotlib.pyplot as plt

def visualize_clusters(rfm, labels, title):

    plt.figure()
    plt.scatter(rfm["frequency"], rfm["monetary"], c=labels)
    plt.xlabel("Frequency")
    plt.ylabel("Monetary Value")
    plt.title(title)
    plt.show()
