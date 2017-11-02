
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pand
#loads the data in as raw_data
raw_data = pand.read_csv('Customers.csv')
X = raw_data.iloc[:, [3, 4]].values  #Loading the column 2 and 4 values i.e income and spending score into X
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 40) #Generating 5 clusters using K-Mean and setting random_state as 40
y_kmeans = kmeans.fit_predict(X)
#Plotting the clusters on the graph with respective colors
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'magenta', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'red', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'cyan', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'green', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'blue', label = 'Cluster 5')
#Plotting the centroids of clusters with yellow color to identify.
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers data')
plt.xlabel('Annual Income in K$')
plt.ylabel('Spending score 1-100')
plt.legend()
plt.show()