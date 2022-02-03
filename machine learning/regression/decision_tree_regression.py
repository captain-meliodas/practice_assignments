#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:30:23 2021
Decision Tree Regression
@author: ankit
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# print(regressor.predict([[6.5],[6.2],[15]]))

#visualizing the DecessionTree Regression
plt.scatter(X,y, color="red")
plt.plot(X, regressor.predict(X), color="blue")
plt.title("Decision Tree Regression")
plt.xlabel("Designation Level")
plt.ylabel("Salary")
plt.show()

# Visualising the Decision Tree Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title("Decision Tree Regression")
plt.xlabel("Designation Level")
plt.ylabel("Salary")
plt.show()

