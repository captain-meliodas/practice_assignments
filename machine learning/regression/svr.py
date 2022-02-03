#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:15:07 2021
Support Vector Regression
@author: ankit
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

#reshapping the vector to column
y = y.reshape(len(y),1)

#feature scaling for svr
#need to scale both label and independent variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

#training the model using svr with kernel rbf
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X,y)

#predicting a new value
#in svm we have used feature scaling so therefore we have to scale the input on same scale
#scaling the input for prediction
scaled_inp = sc_X.transform([[8]])
scaled_label = regressor.predict(scaled_inp)

#reversing the scaled label(output) to original scale
original_output = sc_y.inverse_transform(scaled_label)

#visualizing the SVR
plt.scatter(sc_X.inverse_transform(X),sc_y.inverse_transform(y), color="red")
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X)), color="blue")
plt.title("Support Vector Regression")
plt.xlabel("Designation Level")
plt.ylabel("Salary")
plt.show()

# print(X)
print("new label predicted for 6.5 level designation---",original_output)
# print(y)
