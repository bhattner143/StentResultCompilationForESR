#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:59:49 2019

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


# =============================================================================
# MAIN PROGRAM               
# =============================================================================
style.use('classic')
#Plotting
plt.rcParams['figure.figsize'] = (4.0, 2.5) # set default size of plots #4.2x1.8
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 150
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['grid.linewidth'] = 0.5
plt.rcParams['grid.linestyle'] = ':'
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['font.family']='Helvetica'
plt.rcParams['font.size']=7
plt.rcParams['lines.markersize'] = 3
plt.rc('lines', mew=0.5)
plt.rcParams['lines.linewidth'] = 1
plt.close("all")
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    
path=GenPath+"Dipankar_Manometry_Stent_P1491_05_08_19/40mm/8Scoops"
name='Mano'

# =============================================================================
# stent_P1491_1:40mm:8Scoops
# =============================================================================

Bolustype='8Scoop'
stent_P1491_1_Mano_8scoop_40mm=stentManometry(path,'stent_P1491_40mm',name)
stent_P1491_1_Mano_8scoop_40mm.find_all()
stent_P1491_1_Mano_8scoop_40mm.FileReading([0,1,2,3,4,5])
stent_P1491_1_Mano_8scoop_40mm.CreateList2byte()
stent_P1491_1_Mano_8scoop_40mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_8scoop_40mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys40mm=stent_P1491_1_Mano_8scoop_40mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1491_1_Mano_8scoop_40mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_8scoop_40mm.FindMeanSD(3,rangeDef)
stent_P1491_1_Mano_8scoop_40mm.ComputeGradient()

# =============================================================================
# stent_P1491_1:40mm cycle plots
# =============================================================================

#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoops_20mmps_40mm'],
#                                          [0,5000],0.0,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_20mmps_40mm'],
#                                          [0,5000],0.02,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
#    
#    
#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoop_30mmps_40mm'],
#                                          [0,5000],0.0,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_30mmps_40mm'],
#                                          [0,5000],0.0,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
#    
#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoop_40mmps_40mm'],
#                                                          [0,5000],0.00,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_40mmps_40mm'],
#                                          [46,5000],0.1,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
# =============================================================================
# stent_P1491_1:40mm Mean plots
    #Here the sensor index will be less than the previous plotting because the indexing array has not been considered.
# =============================================================================
plt.figure()
sensIndex=1
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.MeanCycleInfoDict['Mano_P1491_1_8Scoops_20mmps_40mm'][0],
                                          [0,5000],0.0,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_40mm'][0],
                                          [0,5000],0.02,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.MeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_40mm'][0],
                                          [0,5000],0.04,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_40mm'][0],
                                          [0,5000],0.06,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
   
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.MeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_40mm'][0],
                                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_40mm'][0],
                                          [0,5000],0.00,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
    
# =============================================================================
# stent_P1491_1:50mm:Gradient plots      
# =============================================================================
plt.figure()
sensIndex=1
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoops_20mmps_40mm'],
                                          [0,5000],0.0,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_40mm'],
                                          [0,5000],0.00,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_40mm'],
                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_40mm'],
                                          [0,5000],0.00,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
   
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_40mm'],
                                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_40mm'],
                                          [0,5000],0.00,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent'])    

 #####################################  
#plt.close('all') 
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    
path=GenPath+"Dipankar_Manometry_Stent_P1491_05_08_19/50mm/8Scoops"
name='Mano'

# =============================================================================
# stent_P1491_1:50mm:8Scoops
# =============================================================================

Bolustype='8Scoop'
stent_P1491_1_Mano_8scoop_50mm=stentManometry(path,'stent_P1491_50mm',name)
stent_P1491_1_Mano_8scoop_50mm.find_all()
stent_P1491_1_Mano_8scoop_50mm.FileReading([0,1,2,3,4,5])
stent_P1491_1_Mano_8scoop_50mm.CreateList2byte()
stent_P1491_1_Mano_8scoop_50mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_8scoop_50mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys50mm=stent_P1491_1_Mano_8scoop_50mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,4000,0,0,5000,5000,5000,9000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1491_1_Mano_8scoop_50mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_8scoop_50mm.FindMeanSD(3,rangeDef)
stent_P1491_1_Mano_8scoop_50mm.ComputeGradient()
# =============================================================================
# stent_P1491_1:50mm cycle plots
# =============================================================================
#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoop_20mmps_50mm'],
#                                          [0,5000],0.0,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_20mmps_50mm'],
#                                          [0,5000],0.02,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
#    
#    
#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoop_30mmps_50mm'],
#                                          [0,5000],0.0,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_30mmps_50mm'],
#                                          [0,5000],0.0,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
#    
#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoop_40mmps_50mm'],
#                                                          [0,5000],0.00,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_40mmps_50mm'],
#                                          [4000,9000],0.1,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
# =============================================================================
# stent_P1491_1:50mm Mean plots
    #Here the sensor index will be less than the previous plotting because the indexing array has not been considered.
# =============================================================================
plt.figure()
sensIndex=1
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.MeanCycleInfoDict['Mano_P1491_1_8Scoop_20mmps_50mm'][0],
                                          [0,5000],0.0,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_50mm'][0],
                                          [0,5000],0.02,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.MeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_50mm'][0],
                                          [0,5000],0.04,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_50mm'][0],
                                          [0,5000],0.06,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
   
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.MeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_50mm'][0],
                                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_50mm'][0],
                                          [0,5000],0.00,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 

# =============================================================================
# stent_P1491_1:50mm:Gradient plots      
# =============================================================================
plt.figure()
sensIndex=1
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_20mmps_50mm'],
                                          [0,5000],0.0,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_50mm'],
                                          [0,5000],0.0,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_50mm'],
                                          [0,5000],0.0,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_50mm'],
                                          [0,5000],0.0,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
   
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_50mm'],
                                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_50mm'],
                                          [0,5000],0.00,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
        
 #####################################  
#plt.close('all') 
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    
path=GenPath+"Dipankar_Manometry_Stent_P1491_05_08_19/60mm/8Scoops"
name='Mano'

# =============================================================================
# stent_P1491_1:60mm:8Scoops
# =============================================================================

Bolustype='8Scoop'
stent_P1491_1_Mano_8scoop_60mm=stentManometry(path,'stent_P1491_60mm',name)
stent_P1491_1_Mano_8scoop_60mm.find_all()
stent_P1491_1_Mano_8scoop_60mm.FileReading([0,1,2,3,4,5])
stent_P1491_1_Mano_8scoop_60mm.CreateList2byte()
stent_P1491_1_Mano_8scoop_60mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_8scoop_60mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys60mm=stent_P1491_1_Mano_8scoop_60mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,00,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1491_1_Mano_8scoop_60mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_8scoop_60mm.FindMeanSD(3,rangeDef)
stent_P1491_1_Mano_8scoop_60mm.ComputeGradient()

# =============================================================================
# stent_P1491_1:60mm cycle plots
# =============================================================================    
#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoop_20mmps_60mm'],
#                                          [0,5000],0.0,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_20mmps_60mm'],
#                                          [0,5000],0.02,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
#    
#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoop_30mmps_60mm'],
#                                          [0,5000],0.0,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_30mmps_60mm'],
#                                          [0,5000],0.0,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
#    
#plt.figure()
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.ihArrayRevReshapedDict['Mano_P1491_1_8Scoop_40mmps_60mm'],
#                                                          [0,5000],0.00,[3])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.ihArrayRevReshapedDict['Mano_withoutP1491_1_8Scoops_40mmps_60mm'],
#                                          [0,5000],0.1,[3])
#plt.legend(['With Stent',\
#            'Without Stent']) 
# =============================================================================
# stent_P1491_1:60mm Mean plots
    #Here the sensor index will be less than the previous plotting because the indexing array has not been considered.
# =============================================================================
plt.figure()
sensIndex=1
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.MeanCycleInfoDict['Mano_P1491_1_8Scoop_20mmps_60mm'][0],
                                          [0,5000],0.0,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_60mm'][0],
                                          [0,5000],0.1,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.MeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_60mm'][0],
                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_60mm'][0],
                                          [0,5000],0.1,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
   
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.MeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_60mm'][0],
                                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.MeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_60mm'][0],
                                          [0,5000],0.1,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
    
# =============================================================================
# stent_P1491_1:60mm:Gradient plots      
# =============================================================================plt.figure()
sensIndex=1
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_20mmps_60mm'],
                                          [0,5000],0.0,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_60mm'],
                                          [0,5000],0.0,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_60mm'],
                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_60mm'],
                                          [0,5000],0.0,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 
   
    
plt.figure()
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_60mm'],
                                                          [0,5000],0.00,[sensIndex])
stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_60mm'],
                                          [0,5000],0.0,[sensIndex])
plt.legend(['With Stent',\
            'Without Stent']) 