#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 09:50:49 2021
K-Means Clustering
@author: ankit
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Mall_Customers.csv")

#no dependent variable
#selecting only features which is required
#removing Customer Id and Gender feature from matrix of features
X = dataset.iloc[:,[3,4]].values

#using the elbow method for optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init="k-means++",random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

#Training the K-means model on the dataset using K = 5 clusters as represented by elbow method
kmeans = KMeans(n_clusters=5, init="k-means++",random_state=42)
fitted_data = kmeans.fit(X)
y_pred = fitted_data.predict(X) #or you canuse kmeans.fit_predict(X)

print(y_pred)

#visualizing the clusters
plt.scatter(X[y_pred == 0,0],X[y_pred == 0,1],s=100, color="red", label="Cluster 1")
plt.scatter(X[y_pred == 1,0],X[y_pred == 1,1],s=100, color="green", label="Cluster 2")
plt.scatter(X[y_pred == 2,0],X[y_pred == 2,1],s=100, color="blue", label="Cluster 3")
plt.scatter(X[y_pred == 3,0],X[y_pred == 3,1],s=100, color="yellow", label="Cluster 4")
plt.scatter(X[y_pred == 4,0],X[y_pred == 4,1],s=100, color="orange", label="Cluster 5")

#centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s=300,color="magenta", label="Centroids")
plt.title("Clusters of Customers")
plt.xlabel("Annual Income k($)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
