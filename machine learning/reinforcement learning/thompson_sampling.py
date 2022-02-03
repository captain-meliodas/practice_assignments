#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:13:34 2021
Thompson Sampling
@author: ankit
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

#you can change N to lesser value like 5000,1000,500 to check whether 
#it is going to find out that add number 4 is having higher clicks

import random

N = len(dataset.index) #total cutomers (#100 passed)
d = len(dataset.columns) #total adds
ads_selected = []

number_of_rewards_1 = [0] * d #number of times ad get clicked
number_of_rewards_0 = [0] * d #number of times ad not get clicked
total_reward = 0

for n in range(N):
    ad = 0
    max_random = 0
    for ad_no in range(d):
        random_beta = random.betavariate(number_of_rewards_1[ad_no] + 1, number_of_rewards_0[ad_no] + 1)
        if(random_beta > max_random):
            max_random = random_beta
            ad = ad_no
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    if reward == 1:
        number_of_rewards_1[ad] += 1
    else:
        number_of_rewards_0[ad] += 1
    
    total_reward += reward

#visualising the results using histogram
plt.hist(ads_selected)
plt.title("Histogram of Ads Selected")
plt.xlabel("Ads")
plt.ylabel("Number of times each ad was selected")
plt.show()