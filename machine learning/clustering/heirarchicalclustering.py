#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:39:15 2021
Heirarchical Clustering
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

#using the dendogram method for optimal number of clusters
#linkage=ward means take minimum distance first while creating clusters with different points
import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.title("Dendogram Method")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distance")
plt.show()

#Training the Heirarchical model on the dataset using K = 5 clusters as represented by dendrogram method
from sklearn.cluster import AgglomerativeClustering
hierarchical = AgglomerativeClustering(n_clusters=3, affinity="euclidean", linkage="ward")
y_pred = hierarchical.fit_predict(X) #or you canuse kmeans.fit_predict(X)

print(y_pred)

#visualizing the clusters
plt.scatter(X[y_pred == 0,0],X[y_pred == 0,1],s=100, color="red", label="Cluster 1")
plt.scatter(X[y_pred == 1,0],X[y_pred == 1,1],s=100, color="green", label="Cluster 2")
plt.scatter(X[y_pred == 2,0],X[y_pred == 2,1],s=100, color="blue", label="Cluster 3")
# plt.scatter(X[y_pred == 3,0],X[y_pred == 3,1],s=100, color="yellow", label="Cluster 4")
# plt.scatter(X[y_pred == 4,0],X[y_pred == 4,1],s=100, color="orange", label="Cluster 5")
plt.legend()
plt.show()


