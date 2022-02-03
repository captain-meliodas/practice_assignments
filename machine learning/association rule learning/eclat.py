#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:39:15 2021
Association Rule (Eclat)
@author: ankit
"""

import pandas as pd

dataset = pd.read_csv("Market_Basket_Optimisation.csv", header=None)

#creating a list of transactions for training the Apriori model
transactions = []
for row in range(len(dataset.index)):
    transactions.append([str(dataset.values[row,column]) for column in range(len(dataset.columns))])

# Training the Apriori model on the dataset
from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

## Displaying the first results coming directly from the output of the apriori function
results = list(rules)
print(results)

## Putting the results well organised into a Pandas DataFrame
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    return list(zip(lhs, rhs, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support'])

## Displaying the results non sorted
print(resultsinDataFrame)
print("======================")

## Displaying the results sorted by descending lifts
print(resultsinDataFrame.nlargest(n = 10, columns = 'Support'))