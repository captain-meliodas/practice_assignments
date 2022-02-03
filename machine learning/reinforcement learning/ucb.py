#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:08:30 2021
Reinforcement Learning
@author: ankit
"""

import pandas as pd
import math
import matplotlib.pyplot as plt

dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

#you can change N to lesser value like 5000,1000,500 to check whether 
#it is going to find out that add number 4 is having higher clicks
N = len(dataset.index) #total cutomers (#100 failed)
d = len(dataset.columns) #total adds

ads_selected = []
number_of_selection = [0] * d
sums_of_rewards = [0] * d
total_reward = 0

#calculating the ucb
for n in range(N):
    ad = 0
    max_upper_bound = 0
    for ad_no in range(d):
        if(number_of_selection[ad_no] > 0):
            average_reward = sums_of_rewards[ad_no] / number_of_selection[ad_no]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / number_of_selection[ad_no])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400 #choosing a highest upperbound if not calculated
        #if upperbound is greater than max upperbound updating the max_upper_bound and
        #selecting the ad
        if(upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            ad = ad_no
        
        ads_selected.append(ad) #creating a list of ads selected
        number_of_selection[ad] += 1 #incrementing the number of times add selected
        
        #selecting the reward from dataset for user n and ad number 'ad'
        #if clicked reward will be 1 if not clicked reward will be 0 according to dataset
        reward = dataset.values[n,ad]
        sums_of_rewards[ad] += reward 

        #--
        total_reward += reward

#visualising the results using histogram
plt.hist(ads_selected)
plt.title("Histogram of Ads Selected")
plt.xlabel("Ads")
plt.ylabel("Number of times each ad was selected")
plt.show()