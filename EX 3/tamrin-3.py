import numpy as np
from sklearn.cluster import KMeans

np.random.seed(0)  
scores = np.random.randint(0, 101, size=(30, 1))  

kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto')
kmeans.fit(scores)


print("Student Scores:")
print(scores.flatten())

print("\nCluster Labels (0 or 1):")
print(kmeans.labels_)

print("\nCluster Centers:")
print(kmeans.cluster_centers_)
