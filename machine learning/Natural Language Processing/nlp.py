#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 12:08:47 2021
Natural Language Processing
@author: ankit
"""
import numpy as np
import pandas as pd

#delmiter specifies values spearated by (as tsv is tab separated files)
# quoting = 3 represents ignore the double quotes (") in the text
dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter="\t", quoting=3)

#cleaning the text
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = [] #list that going to contains cleanned text

for i in range(len(dataset.index)):
    #replacing the non-alphabets like quotes and commas with space
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i]) #re.sub replace strings with string provided
    review = review.lower()
    review = review.split()
    
    all_stopwords = stopwords.words('english')
    #removing 'not' stop word
    all_stopwords.remove('not')

    #stemming
    ps = PorterStemmer()
    #getting the root word from each text row
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    #adding those root word separated with space
    review = ' '.join(review)
    corpus.append(review)

#creating Bag Of Words Model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,-1].values

# splitting data into training and testing set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#training the naive bayes model on the training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train,y_train)

#Predicting the Test set Results
y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

#making the confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print()
print(accuracy_score(y_test, y_pred))