#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:46:19 2022

@author: joaopaulo
"""

import numpy as np
import matplotlib.pyplot as plt


#The portfolio with the highest annualized return

returns1 = ((1+0.5323)**(1/12))-1
vol1 = 0.2703/(12**(0.5))


T1 = 120
count1 = 0
price_list1 = []
start1 = 100

price1 = start1 * (1 + np.random.normal(returns1, vol1))
price_list1.append(price1)

for y in range(T1):
    if count1 == 120:
        break
    price1 = price_list1[count1]* (1 + np.random.normal(returns1, vol1))
    price_list1.append(price1)
    count1 += 1

plt.plot(price_list1)
plt.show()

#The portfolio with the lowest annualized volatility

returns2 = ((1+0.1536)**(1/12))-1
vol2 = 0.1466/(12**(0.5))

T2 = 120
count2 = 0
price_list2 = []
start2 = 100

price2 = start2 * (1 + np.random.normal(returns2, vol2))
price_list2.append(price2)

for y in range(T2):
    if count2 == 120:
        break
    price2 = price_list2[count2]* (1 + np.random.normal(returns2, vol2))
    price_list2.append(price2)
    count2 += 1

plt.plot(price_list2)
plt.show()

#The portfolio with the highest Sharpe ratio

returns3 = ((1+0.4141)**(1/12))-1
vol3 = 0.1932/(12**(0.5))

T3 = 120
count3 = 0
price_list3 = []
start3 = 100

price3 = start3 * (1 + np.random.normal(returns3, vol3))
price_list3.append(price3)

for y in range(T3):
    if count3 == 120:
        break
    price3 = price_list3[count3]* (1 + np.random.normal(returns3, vol3))
    price_list3.append(price3)
    count3 += 1

plt.plot(price_list3)
plt.show()