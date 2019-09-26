#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:42:06 2019

@author: dipankarbhattacharya
"""
import os
import pdb
import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from intelhex import IntelHex
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.nonparametric.smoothers_lowess import lowess
from dateutil.parser import parse
from scipy.signal import find_peaks,peak_prominences
import random


def cls():
    print('\n'*50)
#clear Console
cls()
#Make a plotting function

speed=[20,30,40]
stent=[0,1]
wavelength=[40,50,60]
ibpsGrad1=[0.1,0.2,0.3]
ibpsGrad1Array=np.array([[0.0272,0.0217,0.0167],
                        [0.027,0.0248,0.0294]])
    
ibpsGrad2Array=np.array([[0.008,0.0133,0.034],
                        [0.0245,0.025,0.0191]])

BolusCons=[4,8]


X=np.array(speed)
Y=np.array(BolusCons)
Z1=ibpsGrad1Array
Z2=ibpsGrad2Array

X,Y=np.meshgrid(X, Y)


fig = plt.figure()
plt.hold(True)
ax = fig.gca(projection='3d')
surf1 = ax.plot_surface(X, Y, Z1,cmap='viridis',edgecolor='k',
                       linewidth=0, antialiased=False)

scatter1=ax.scatter(X, Y, Z1,c='r')
surf1 = ax.plot_surface(X, Y, Z2,cmap='cool',edgecolor='k',
                       linewidth=0, antialiased=False)
scatter2=ax.scatter(X, Y, Z2,c='g')

ax.xaxis.set_major_locator(plt.MaxNLocator(4))
ax.yaxis.set_major_locator(plt.FixedLocator([4,8]))
ax.view_init(24, 141)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
