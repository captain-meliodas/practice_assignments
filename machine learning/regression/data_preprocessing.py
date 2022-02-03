# -*- coding: utf-8 -*-
"""
@Author- Ankit Singh

Data Preprocessing
"""
import numpy as np
import pandas as pd

dataset = pd.read_csv('Data.csv')

#Matrix of features (Independent variable used for learning)
# iloc -> [rows,columns]
#dataset.iloc[:,:-1] -> provides you the data frame
X = dataset.iloc[:,:-1].values

#dependent variable (To predict)
#getiing all rows but only last column (dependent variable)
y = dataset.iloc[:,-1].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:,1:3])
#transform is not inplace so need to re-assgin
X[:,1:3] = imputer.transform(X[:,1:3])

#encoding string values matrix of fetaures of X
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

#encoding dependent variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

#dividing X features matrix in training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1) 

#fitting and transforming training and testing data
#standardisation vs normalisation

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:,1:3] = sc.fit_transform(X_train[:,1:3])
X_test[:,1:3] = sc.transform(X_test[:,1:3])
print(X)
print()
print(X_train)
print(X_test)
# print(y_train)
# print(y_test)
# print()
# print(y)