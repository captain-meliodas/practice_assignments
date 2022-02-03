#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:25:13 2021
Polynomial Regression
@author: ankit
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')

#Matrix of features (Independent variable used for learning)
# iloc -> [rows,columns]
#dataset.iloc[:,:-1] -> provides you the data frame
X = dataset.iloc[:,1:-1].values

#dependent variable (To predict)
#getiing all rows but only last column (dependent variable)
y = dataset.iloc[:,-1].values

# Training linear regresion on the whole dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

# Training the polynomial Regression model on the whole dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
poly_X = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(poly_X, y)

#Plotting linear regression line
plt.scatter(X, y, color="red")
plt.plot(lin_reg.predict(X), color="blue")
plt.title("Linear Regression")
plt.xlabel("Designation Level")
plt.ylabel("Salary")

#Plotting Polynomial regression line
# plt.scatter(X, y, color="red")
plt.plot(lin_reg2.predict(poly_X), color="green")
plt.title("Polynomial Regression")
plt.xlabel("Designation Level")
plt.ylabel("Salary")

#predicting new data using linear regression (Level = 6.5)
output1 = lin_reg.predict([[6.5]])
#predicting new data using Polynomial Regression (Level = 6.5)
output2 = lin_reg2.predict(poly_reg.fit_transform([[6.5]]))

print(output1,output2)