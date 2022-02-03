#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:58:52 2021
/muktiple Linear Regression
@author: ankit
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('50_Startups.csv')

#Matrix of features (Independent variable used for learning)
# iloc -> [rows,columns]
#dataset.iloc[:,:-1] -> provides you the data frame
X = dataset.iloc[:,:-1].values

#dependent variable (To predict)
#getiing all rows but only last column (dependent variable)
y = dataset.iloc[:,-1].values

#encoding string values matrix of fetaures of X (City Name)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# print(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_predicted = regressor.predict(X_test)
#compare y_predicted with y_test
np.set_printoptions(precision=2)
print(len(y_predicted))
result = np.concatenate((y_predicted.reshape(len(y_predicted),1), y_test.reshape(len(y_test),1)),1)
print(result)

