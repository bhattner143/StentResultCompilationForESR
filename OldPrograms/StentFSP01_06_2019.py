#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 12:54:57 2019

@author: dipankarbhattacharya
"""

import pdb
import os
import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from intelhex import IntelHex
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.nonparametric.smoothers_lowess import lowess
from dateutil.parser import parse
from scipy.signal import find_peaks,peak_prominences
import random

from ClassStentForFSP import stent

def cls():
    print('\n'*50)
#clear Console
cls()

# =============================================================================
# MAIN PROGRAM               
# =============================================================================
plt.close("all")
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentForceTesting01_06_2019/"                    
path=GenPath+"FSPComparisonChangeOverlapping2/"
name='FSPBaseLine0'

stent_P1491_1=stent(path,'','',[1,1,1],name)
stent_P1491_1.find_all(name)
df1=pd.read_csv(stent_P1491_1.files[0], sep=',',header=None)
df1=df1[2:]
columns_new = ['Digital Pressure']
df=pd.DataFrame(data=df1.values[:,2],columns=columns_new)

for index in range(len(stent_P1491_1.files)):
    df1=pd.read_csv(stent_P1491_1.files[index], sep=',',header=None)
    df = pd.concat([df, pd.DataFrame(df1.values[2:,3:5], \
                                     columns=['A1_'+stent_P1491_1.files[index][75:],'A2_'+stent_P1491_1.files[index][75:]])],\
                                     axis=1)#73

dfSliced=df[0:268]  #188 
#Area=np.array([100*13*pow(10,-3),100*13*pow(10,-3),\
#               15*13*pow(10,-3),15*13*pow(10,-3),\
#               20*13*pow(10,-3),20*13*pow(10,-3),\
#               40*13*pow(10,-3),40*13*pow(10,-3)])
#Area=np.array([99*13*pow(10,-3),99*13*pow(10,-3),\
#               19*13*pow(10,-3),19*13*pow(10,-3),\
#               39*13*pow(10,-3),39*13*pow(10,-3),\
#               109*13*pow(10,-3),109*13*pow(10,-3),\
#               29*13*pow(10,-3),29*13*pow(10,-3),\
#               89*13*pow(10,-3),89*13*pow(10,-3),\
#               59*13*pow(10,-3),59*13*pow(10,-3),\
#               79*13*pow(10,-3),79*13*pow(10,-3),\
#               69*13*pow(10,-3),69*13*pow(10,-3),\
#               9*13*pow(10,-3),9*13*pow(10,-3),\
#               49*13*pow(10,-3),49*13*pow(10,-3)])
    
Area=np.array([18*13*pow(10,-3),18*13*pow(10,-3),\
               18*13*pow(10,-3),18*13*pow(10,-3),\
               99*13*pow(10,-3),99*13*pow(10,-3),\
               19*13*pow(10,-3),19*13*pow(10,-3),\
               39*13*pow(10,-3),39*13*pow(10,-3),\
               109*13*pow(10,-3),109*13*pow(10,-3),\
               18*13*pow(10,-3),18*13*pow(10,-3),\
               29*13*pow(10,-3),29*13*pow(10,-3),\
               89*13*pow(10,-3),89*13*pow(10,-3),\
               59*13*pow(10,-3),59*13*pow(10,-3),\
               79*13*pow(10,-3),79*13*pow(10,-3),\
               69*13*pow(10,-3),69*13*pow(10,-3),\
               9*13*pow(10,-3),9*13*pow(10,-3),\
               49*13*pow(10,-3),49*13*pow(10,-3)])
    

dfPressure=pd.DataFrame(data=dfSliced.values[:,0],columns=columns_new)
#dff=dfSliced[dfSliced.columns.values[2]]/(dfSliced[dfSliced.columns.values[1]]-dfSliced[dfSliced.columns.values[2]])
#
for ii in range(1,int((len(dfSliced.columns.values)+1)/2)):
#    pdb.set_trace()
    dftemp=dfSliced[dfSliced.columns.values[2*ii]]/(dfSliced[dfSliced.columns.values[2*ii-1]]-dfSliced[dfSliced.columns.values[2*ii]])
    dftemp=dftemp/1#Area[2*ii-1]
    dfPressure=pd.concat([dfPressure,pd.DataFrame(dftemp,columns=[dfSliced.columns.values[2*ii][3:]])],axis=1)
    
plt.rcParams['figure.figsize'] = (8.8, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
matplotlib.rcParams.update({'errorbar.capsize': 2})
#plt.figure()
##fig, axes = plt.subplots(1,1, figsize=(7, 7), sharex=True, dpi=120)
#ax=plt.gca()
#dfPressure.plot(x='Digital Pressure', y='g18mm1.csv',ax=ax,color='r',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g18mm2.csv',ax=ax,color='g',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g18mm3.csv',ax=ax,color='b',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='19mm.csv',ax=ax,color='k',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='9mm.csv',ax=ax,color=(0.9,0.5,0.1),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='18mm4.csv',ax=ax,color='c',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='21mm.csv',ax=ax,color='m',title='Original Series')
##dfPressure.plot(x='Digital Pressure', y='33mm.csv',ax=ax,color='y',title='Original Series')
#plt.show()

#plt.figure()
#fig, axes = plt.subplots(1,1, figsize=(7, 7), sharex=True, dpi=120)
#ax=plt.gca()
#dfPressure.plot(x='Digital Pressure', y='99mm.csv',ax=ax,color='r',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='19mm.csv',ax=ax,color='g',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='39mm.csv',ax=ax,color='b',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g109mm.csv',ax=ax,color='k',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='29mm.csv',ax=ax,color='c',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color='m',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='59mm.csv',ax=ax,color='y',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='79mm.csv',ax=ax,color=(0.7,0.5,0.5),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='69mm.csv',ax=ax,color=(0.7,0.7,0.7),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='9mm.csv',ax=ax,color=(0.2,0.2,0.2),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='49mm.csv',ax=ax,color=(0.5,0.7,0.9),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color=(0.5,0.7,0.9),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g18mm1.csv',ax=ax,color=(0.9,0.5,0.1),title='Original Series')
#plt.show()

plt.figure()
#fig, axes = plt.subplots(1,1, figsize=(7, 7), sharex=True, dpi=120)
ax=plt.gca()
#dfPressure.plot(x='Digital Pressure', y='99mm.csv',ax=ax,color='r',title='Original Series')
dfPressure.plot(x='Digital Pressure', y='19mm.csv',ax=ax,color='r',title='Original Series')
dfPressure.plot(x='Digital Pressure', y='39mm.csv',ax=ax,color='g',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g109mm.csv',ax=ax,color='k',title='Original Series')
dfPressure.plot(x='Digital Pressure', y='29mm.csv',ax=ax,color='b',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color='m',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='59mm.csv',ax=ax,color='y',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='79mm.csv',ax=ax,color=(0.7,0.5,0.5),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='69mm.csv',ax=ax,color=(0.7,0.7,0.7),title='Original Series')
dfPressure.plot(x='Digital Pressure', y='9mm.csv',ax=ax,color='darkred',title='Original Series')
dfPressure.plot(x='Digital Pressure', y='49mm.csv',ax=ax,color='k',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color=(0.5,0.7,0.9),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g18mm1.csv',ax=ax,color='darkblue',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g18mm2.csv',ax=ax,color='c',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g18mm3.csv',ax=ax,color='k',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='18mm4.csv',ax=ax,color='darkcyan',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='21mm.csv',ax=ax,color='m',title='Original Series')
##dfPressure.plot(x='Digital Pressure', y='33mm.csv',ax=ax,color='y',title='Original Series')

plt.show()
###########



dfPressureArray=np.array(dfPressure)
dfMeanPressureArray=np.zeros((1,dfPressureArray.shape[1]))
dfStdPressureArray=dfMeanPressureArray
digitalPressure=np.unique(dfPressureArray[:,0])
for i in range(digitalPressure.shape[0]):
    result = np.where(dfPressureArray == digitalPressure[i])
    print(result[0])
    print(dfPressureArray[result[0],:].mean(axis=0))
    dfMeanPressureArray=np.vstack((dfMeanPressureArray,dfPressureArray[result[0],:].mean(axis=0)))
    dfStdPressureArray=np.vstack((dfStdPressureArray,dfPressureArray[result[0],:].std(axis=0)))

##########

dfStdPressureArray=dfStdPressureArray[:,1:].mean(axis=1)

dfMeanPressureArrayMean=np.array([dfMeanPressureArray[1:,0],\
                                  dfMeanPressureArray[1:,1:].mean(axis=1),\
                                  dfMeanPressureArray[1:,1:].std(axis=1)]).T

df1MeanPressureArray=pd.DataFrame(dfMeanPressureArray[1:,:])
df1MeanPressureArray.columns=dfPressure.columns.values
###########
plt.figure()
plt.plot(dfMeanPressureArrayMean[:,0],dfMeanPressureArrayMean[:,1])
plt.hold(True)
plt.errorbar(dfMeanPressureArrayMean[:,0],dfMeanPressureArrayMean[:,1],
             xerr=dfStdPressureArray[1:],
             yerr=dfMeanPressureArrayMean[:,2], 
             marker='s', mfc='blue',mec='green', ms=2, mew=2,fmt='o',capsize=20, elinewidth=3, markeredgewidth=10)
plt.figure()
#fig, axes = plt.subplots(1,1, figsize=(7, 7), sharex=True, dpi=120)
ax=plt.gca()
#dfPressure.plot(x='Digital Pressure', y='99mm.csv',ax=ax,color='r',title='Original Series')
df1MeanPressureArray.plot(x='Digital Pressure', y='19mm.csv',ax=ax,color='r',title='Original Series')
df1MeanPressureArray.plot(x='Digital Pressure', y='39mm.csv',ax=ax,color='g',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g109mm.csv',ax=ax,color='k',title='Original Series')
df1MeanPressureArray.plot(x='Digital Pressure', y='29mm.csv',ax=ax,color='b',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color='m',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='59mm.csv',ax=ax,color='y',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='79mm.csv',ax=ax,color=(0.7,0.5,0.5),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='69mm.csv',ax=ax,color=(0.7,0.7,0.7),title='Original Series')
df1MeanPressureArray.plot(x='Digital Pressure', y='9mm.csv',ax=ax,color='darkred',title='Original Series')
df1MeanPressureArray.plot(x='Digital Pressure', y='49mm.csv',ax=ax,color='k',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color=(0.5,0.7,0.9),title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='g18mm1.csv',ax=ax,color='darkblue',title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='g18mm2.csv',ax=ax,color='c',title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='g18mm3.csv',ax=ax,color='k',title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='18mm4.csv',ax=ax,color='darkcyan',title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='21mm.csv',ax=ax,color='m',title='Original Series')
##df1MeanPressureArray.plot(x='Digital Pressure', y='33mm.csv',ax=ax,color='y',title='Original Series')


plt.show()
# =============================================================================
# 
# =============================================================================
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentForceTesting01_06_2019/"                    
path=GenPath+"FSPLoadCellBottomHalfAnalysis/"
name='00'

stent_P1491_2=stent(path,'','',[1,1,1],name)
stent_P1491_2.find_all(name)
df40=pd.DataFrame()

for index in range(len(stent_P1491_2.files)):
    df1_40=pd.read_csv(stent_P1491_2.files[index], sep=',',header=None)
    df40 = pd.concat([df40, pd.DataFrame(df1_40.values[2:,3:5], \
                                     columns=['A1_'+stent_P1491_2.files[index][0:],'A2_'+stent_P1491_2.files[index][0:]])],\
                                     axis=1)#73

dfSliced40=df40[0:5]

dfPressure40=pd.DataFrame()
#dff=dfSliced[dfSliced.columns.values[2]]/(dfSliced[dfSliced.columns.values[1]]-dfSliced[dfSliced.columns.values[2]])
#
for ii in range(1,int((len(dfSliced40.columns.values))/2+1)):
#    pdb.set_trace()
    dftemp40=dfSliced40[dfSliced40.columns.values[2*ii-1]]/(dfSliced40[dfSliced40.columns.values[2*ii-2]]-dfSliced40[dfSliced40.columns.values[2*ii-1]])
    dfPressure40=pd.concat([dfPressure40,pd.DataFrame(dftemp40,columns=[dfSliced40.columns.values[2*ii-1][3:]])],axis=1)

dfPressure40Mean=dfPressure40.mean()  
dfPressure40Std=dfPressure40.std() 

WeightList=list()
DistanceList=list()
for index in range(len(dfPressure40.columns.values)):
    WeightList.append(0.001*9.81*int(dfPressure40.columns.values[index][0:3]))
    DistanceList.append(int(dfPressure40.columns.values[index][4:6]))
    
dfWeight=pd.DataFrame(WeightList,columns=['Force'])
dfDistance=pd.DataFrame(DistanceList,columns=['Distance'])  

dfPressure40Mean= pd.concat([pd.DataFrame(np.array(dfPressure40Mean)),dfWeight,dfDistance],axis=1)

dfPressure40MeanArray=np.array(dfPressure40Mean)
dfPressure40MeanArray=dfPressure40MeanArray[dfPressure40MeanArray[:, 1].argsort()]
dfPressure40MeanReshape= dfPressure40MeanArray.T.reshape(-1,4).T
dfPressure40MeanReshapeMean=dfPressure40MeanReshape.mean(axis=0)
dfPressure40MeanReshapeStd=dfPressure40MeanReshape.std(axis=0)[0:3]

dfPressure40MeanReshapeMeanStd= dfPressure40MeanReshapeMean.reshape(-1,3)
dfPressure40MeanReshapeMeanStd=np.vstack((dfPressure40MeanReshapeMeanStd,dfPressure40MeanReshapeStd)).T
#dfPressure40MeanReshapeMeanStd=pd.DataFrame(dfPressure40MeanReshapeMeanStd)
#dfPressure40MeanReshapeMeanStd.columns=['Mean FSP Force','Mean Applied Force','Mean Distance','Std']

dfPressure40Mean['Distance']=1+dfPressure40Mean['Distance']-50
dfPressure40Mean.columns=['Mean','Force','Distance']

plt.figure()
ax=plt.gca()
ax1=dfPressure40Mean.plot.scatter(x='Distance', y=0,ax=ax,color='r',title='Original Series')
ax2=dfPressure40Mean.plot.scatter(x='Distance', y='Force',ax=ax,color='g',title='Original Series')
plt.errorbar(dfPressure40MeanReshapeMeanStd[:,2]+1-50, dfPressure40MeanReshapeMeanStd[:,0],
             dfPressure40MeanReshapeMeanStd[:,3],
             marker='s',mfc='r',mec='k', ms=2, mew=2,fmt='o')
plt.show()

# =============================================================================
# 
# =============================================================================
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentForceTesting01_06_2019/"                    
path=GenPath+"FSPComparisonChangeOverlapping3/"
name='FSPBaseLine40'

stent_P1491_1=stent(path,'','',[1,1,1],name)
stent_P1491_1.find_all(name)
df1_40=pd.read_csv(stent_P1491_1.files[0], sep=',',header=None)
df1_40=df1[2:]
columns_new = ['Digital Pressure']
df40=pd.DataFrame(data=40+df1_40.values[:,2],columns=columns_new)

for index in range(len(stent_P1491_1.files)):
    df1_40=pd.read_csv(stent_P1491_1.files[index], sep=',',header=None)
    df40 = pd.concat([df40, pd.DataFrame(df1_40.values[2:,3:5], \
                                     columns=['A1_'+stent_P1491_1.files[index][75:],'A2_'+stent_P1491_1.files[index][75:]])],\
                                     axis=1)#73

dfSliced40=df40[0:268]
Area=np.array([49*13*pow(10,-3),49*13*pow(10,-3),\
               69*13*pow(10,-3),69*13*pow(10,-3),\
               29*13*pow(10,-3),29*13*pow(10,-3),\
               59*13*pow(10,-3),59*13*pow(10,-3),\
               9*13*pow(10,-3),9*13*pow(10,-3),\
               79*13*pow(10,-3),79*13*pow(10,-3),\
               39*13*pow(10,-3),39*13*pow(10,-3),\
               19*13*pow(10,-3),19*13*pow(10,-3)])
dfPressure40=pd.DataFrame(data=dfSliced40.values[:,0],columns=columns_new)
#dff=dfSliced[dfSliced.columns.values[2]]/(dfSliced[dfSliced.columns.values[1]]-dfSliced[dfSliced.columns.values[2]])
#
for ii in range(1,int((len(dfSliced40.columns.values)+1)/2)):
#    pdb.set_trace()
    dftemp40=dfSliced40[dfSliced40.columns.values[2*ii]]/(dfSliced40[dfSliced40.columns.values[2*ii-1]]-dfSliced40[dfSliced40.columns.values[2*ii]])
    dftemp40=dftemp40/1#Area[2*ii-1]
    dfPressure40=pd.concat([dfPressure40,pd.DataFrame(dftemp40,columns=[dfSliced40.columns.values[2*ii][3:]])],axis=1)
    
plt.show()
plt.figure()
#fig, axes = plt.subplots(1,1, figsize=(7, 7), sharex=True, dpi=120)
ax=plt.gca()
#dfPressure.plot(x='Digital Pressure', y='99mm.csv',ax=ax,color='r',title='Original Series')
dfPressure40.plot(x='Digital Pressure', y='19mm.csv',ax=ax,color='r',title='Original Series')
dfPressure40.plot(x='Digital Pressure', y='39mm.csv',ax=ax,color='g',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g109mm.csv',ax=ax,color='k',title='Original Series')
dfPressure40.plot(x='Digital Pressure', y='29mm.csv',ax=ax,color='b',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color='m',title='Original Series')
#dfPressure40.plot(x='Digital Pressure', y='59mm.csv',ax=ax,color='y',title='Original Series')
#dfPressure40.plot(x='Digital Pressure', y='79mm.csv',ax=ax,color=(0.7,0.5,0.5),title='Original Series')
#dfPressure40.plot(x='Digital Pressure', y='69mm.csv',ax=ax,color=(0.7,0.7,0.7),title='Original Series')
dfPressure40.plot(x='Digital Pressure', y='9mm.csv',ax=ax,color='darkred',title='Original Series')
dfPressure40.plot(x='Digital Pressure', y='49mm.csv',ax=ax,color='k',title='Original Series')
plt.show()

dfPressureArray40=np.array(dfPressure40)
dfMeanPressureArray40=np.zeros((1,dfPressureArray40.shape[1]))
dfStdPressureArray40=np.zeros((1,dfPressureArray40.shape[1]))
digitalPressure40=np.unique(dfPressureArray40[:,0])
for i in range(digitalPressure.shape[0]):
    result40 = np.where(dfPressureArray40 == digitalPressure40[i])
    print(result40[0])
    print(dfPressureArray40[result40[0],:].mean(axis=0))
    dfMeanPressureArray40=np.vstack((dfMeanPressureArray40,dfPressureArray40[result40[0],:].mean(axis=0)))
    dfStdPressureArray40=np.vstack((dfStdPressureArray40,dfPressureArray40[result40[0],:].std(axis=0)))

dfStdPressureArray=dfStdPressureArray[:,1:].std(axis=1)

df1MeanPressureArrayConcatArrayMean=np.array([df1MeanPressureArrayConcatArray[:,0],\
                                  df1MeanPressureArrayConcatArray[:,1:].mean(axis=1),\
                                  df1MeanPressureArrayConcatArray[:,1:].std(axis=1)]).T
    
df1MeanPressureArray40=pd.DataFrame(dfMeanPressureArray40[1:,:])
df1MeanPressureArray40.columns=dfPressure40.columns.values

df1MeanPressureArrayConcat=pd.concat([df1MeanPressureArray, df1MeanPressureArray40[11:]],sort=False)
df1MeanPressureArrayConcatArray=np.array(df1MeanPressureArrayConcat)


plt.figure()
#fig, axes = plt.subplots(1,1, figsize=(7, 7), sharex=True, dpi=120)
ax=plt.gca()
#dfPressure.plot(x='Digital Pressure', y='99mm.csv',ax=ax,color='r',title='Original Series')
df1MeanPressureArrayConcat.plot(x='Digital Pressure', y='19mm.csv',ax=ax,color='r',title='Original Series')
df1MeanPressureArrayConcat.plot(x='Digital Pressure', y='39mm.csv',ax=ax,color='g',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='g109mm.csv',ax=ax,color='k',title='Original Series')
df1MeanPressureArrayConcat.plot(x='Digital Pressure', y='29mm.csv',ax=ax,color='b',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color='m',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='59mm.csv',ax=ax,color='y',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='79mm.csv',ax=ax,color=(0.7,0.5,0.5),title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='69mm.csv',ax=ax,color=(0.7,0.7,0.7),title='Original Series')
df1MeanPressureArrayConcat.plot(x='Digital Pressure', y='9mm.csv',ax=ax,color='darkred',title='Original Series')
df1MeanPressureArrayConcat.plot(x='Digital Pressure', y='49mm.csv',ax=ax,color='k',title='Original Series')
#dfPressure.plot(x='Digital Pressure', y='89mm.csv',ax=ax,color=(0.5,0.7,0.9),title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='g18mm1.csv',ax=ax,color='darkblue',title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='g18mm2.csv',ax=ax,color='c',title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='g18mm3.csv',ax=ax,color='k',title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='18mm4.csv',ax=ax,color='darkcyan',title='Original Series')
#df1MeanPressureArray.plot(x='Digital Pressure', y='21mm.csv',ax=ax,color='m',title='Original Series')
##df1MeanPressureArray.plot(x='Digital Pressure', y='33mm.csv',ax=ax,color='y',title='Original Series')



###########
plt.figure()
plt.errorbar(df1MeanPressureArrayConcatArrayMean[:,0],df1MeanPressureArrayConcatArrayMean[:,1],
             yerr=df1MeanPressureArrayConcatArrayMean[:,2], 
             marker='s', mfc='blue',mec='green', ms=2, mew=2,fmt='-o')
plt.show()