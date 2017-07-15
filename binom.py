# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:29:11 2017

@author: 235914
"""
from  scipy.stats import binom
import matplotlib.pyplot as plt
win_base = 1000000
return_listlist = []
best_game = []
for percent in range(0,10000):
    return_list = []
    for i in range(1,51):
        win_amount = win_base-10000*i
        win_chance = sum(binom.pmf(range(i,2*i), 2*i-1, percent/10000.0))
        expected_return = win_amount * win_chance
        return_list.append((i,expected_return))
        #print i*2-1,',',i,',', win_chance,',', win_amount,',', expected_return
    best_game.append(max(return_list, key=lambda x: x[1])[0])
    return_listlist.append(return_list)

 
print best_game

'''
for i,rList in enumerate(return_listlist):
    plt.plot(rList)
    print best_game[i]
    
    
'''

x1 = range(0,10000)
x = []
for item in x1:
    x.append(item/100.0)
    
plt.plot(x, best_game)


# win_chance = sum(binom.pmf(range(i,2*i), 2*i-1, percent/100))