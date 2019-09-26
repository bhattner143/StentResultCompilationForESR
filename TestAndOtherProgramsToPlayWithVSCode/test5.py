#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:10:12 2019

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
from ClassStentv2 import *

def cls():
    print('\n'*50)
#clear Console
cls()




GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    
path=GenPath+"Dipankar_Manometry_Stent_P1491_05_08_19/"
name='Mano'

#npArray=np.array([np.array(Mano_Stomach_lotofsen.df2)[:,0],\
#             np.array(Mano_Stomach_lotofsen.df2)[:,1],\
#             np.array(Mano_Stomach_lotofsen.df3)[:,1],\
#             np.array(Mano_Stomach_lotofsen.df4)[:,1],\
#             np.array(Mano_Stomach_lotofsen.df5)[:,1]]).T

collectdata1=np.round(AxisParametersForPlotting40mm['IBPSGradientArrayWithStent'],3)
collectdata2=np.round(AxisParametersForPlotting40mm['IBPSGradientArrayWithoutStent'],3)

ColumnNameDict={'With Stent':{'20':{'72':collectdata1[0,0],
                                    '108':collectdata1[0,1],
                                    '144':collectdata1[0,2]},
                              '30':{'72':collectdata1[1,0],
                                    '108':collectdata1[1,1],
                                    '144':collectdata1[1,2]},
                              '40':{'72':collectdata1[2,0],
                                    '108':collectdata1[2,1],
                                    '144':collectdata1[2,2]}},
                                    
                'Without Stent':{'20':{'72':collectdata2[0,0],
                                       '108':collectdata2[0,1],
                                       '144':collectdata2[0,2]},
                              '30':{'72':collectdata2[1,0],
                                    '108':collectdata2[1,1],
                                    '144':collectdata2[1,2]},
                              '40':{'72':collectdata2[2,0],
                                    '108':collectdata2[2,1],
                                    '144':collectdata2[2,2]}}}

 
df=pd.DataFrame(ColumnNameDict)
df.to_csv(path+'CSV/'+\
          stent_P1491_1_Mano_8scoop_40mm.files[0].split('_')[0]+\
          stent_P1491_1_Mano_8scoop_40mm.files[0].split('_')[5].split('.')[0]+\
          '.csv')