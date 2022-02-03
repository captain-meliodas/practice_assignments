#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:58:52 2021
Simple Linear Regression
@author: ankit
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')

#Matrix of features (Independent variable used for learning)
# iloc -> [rows,columns]
#dataset.iloc[:,:-1] -> provides you the data frame
X = dataset.iloc[:,:-1].values

#dependent variable (To predict)
#getiing all rows but only last column (dependent variable)
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1) 

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_predicted = regressor.predict(X_test)

#compare y_predicted with y_test 

#plotting the training results
plt.scatter(X_train, y_train, color="red") #real salaries in training
plt.plot(X_train,regressor.predict(X_train),color="blue") #predicted salaries in training set
plt.title("Salary Vs Experience (Training Set)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

#plotting the testing results
plt.scatter(X_test, y_test, color="red") #real salaries in training
#no need of replacing X_train and predicted data as X_test will also give the 
#same regression line because it is based on unique equation
plt.plot(X_train,regressor.predict(X_train),color="blue") #predicted salaries in training set
plt.title("Salary Vs Experience (Test Set)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()


