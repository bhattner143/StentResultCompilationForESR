#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:36:59 2019

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
#Plotting
#plt.rcParams['figure.figsize'] = (16.0, 10) # set default size of plots #4.2x1.8

plt.style.use('classic')
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['grid.linewidth'] = 0.5
plt.rcParams['grid.linestyle'] = ':'
plt.rcParams['image.interpolation'] = 'nearest'
#plt.rcParams['font.family']='Helvetica'
plt.rcParams['font.size']=5
plt.rcParams['lines.markersize'] = 3
plt.rc('lines', mew=0.5)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['hatch.linewidth'] = 0.5
plt.rcParams["errorbar.capsize"] = 1.5
plt.close("all")


# =============================================================================
# stent_P1491_1:40mm:4Scoops
# =============================================================================
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    
path=GenPath+"Dipankar_Manometry_Stent_P1491_31_07_19/40mm"
name='Mano'
Bolustype='4Scoop'
stent_P1491_1_Mano_4scoop_40mm=stentManometry(path,'stent_P1491_40mm',name)
stent_P1491_1_Mano_4scoop_40mm.find_all()
stent_P1491_1_Mano_4scoop_40mm.FileReading([0,1,2,3,4,5,6,7,8])
stent_P1491_1_Mano_4scoop_40mm.CreateList2byte()
stent_P1491_1_Mano_4scoop_40mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_4scoop_40mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys40mm=stent_P1491_1_Mano_4scoop_40mm.ihArrayRevReshapedDict.keys()

window=[0,0,0,0,0,0,0,0,0,5000,5000,5000,5000,5000,5000,5000,5000,6000]   #use obj.files to define the window 
stent_P1491_1_Mano_4scoop_40mm.FindPeak(12.5,window,400,2)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150,150,150,150,150,150,150 ]
stent_P1491_1_Mano_4scoop_40mm.FindMeanSD(2,rangeDef)
stent_P1491_1_Mano_4scoop_40mm.ComputeGradient()

## =============================================================================
## stent_P1491_1:40mm:4Scoop:Gradient plots
## =============================================================================
#
#FigureNum1=plt.figure(1)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1491_1_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_4Scoop_40mm_20mmps'],
#                  'GradPlot2':stent_P1491_1_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_4scoop_40mm_30mmps'],
#                  'GradPlot3':stent_P1491_1_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_4Scoop_40mm_40mmps_v2'],
#                  'GradPlot4':stent_P1491_1_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4Scoop_40mm_20mmps'],
#                  'GradPlot5':stent_P1491_1_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4scoop_40mm_30mmps_v2'],
#                  'GradPlot6':stent_P1491_1_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4Scoop_40mm_40mmps']} 
#plt.title('P1491_1:40mm:4scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum1,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')
# =============================================================================
# stent_P1491_1:40mm:4Scoop:Max of thresholded gradient plots
# =============================================================================
TimeIndexThreshold=[115,115,115,115,115,115,115,115,115]     
SenIndex=[1]

FileList=['Mano_P1491_1_4Scoop_40mm_20mmps',
          'Mano_P1491_1_4scoop_40mm_30mmps',
          'Mano_P1491_1_4Scoop_40mm_40mmps_v2',
          'Mano_withoutP1491_1_4Scoop_40mm_20mmps',
          'Mano_withoutP1491_1_4scoop_40mm_30mmps_v2',
          'Mano_withoutP1491_1_4Scoop_40mm_40mmps']

stent_P1491_1_Mano_4scoop_40mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1491_1:40mm:6Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1491_19_08_19/40mm/"
name='Mano'

Bolustype='6Scoop'
stent_P1491_1_Mano_6scoop_40mm=stentManometry(path,'stent_P1491_40mm',name)
stent_P1491_1_Mano_6scoop_40mm.find_all()
stent_P1491_1_Mano_6scoop_40mm.FileReading([0,1,2,3,4,5])
stent_P1491_1_Mano_6scoop_40mm.CreateList2byte()
stent_P1491_1_Mano_6scoop_40mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_6scoop_40mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys40mm6scoop=stent_P1491_1_Mano_6scoop_40mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1491_1_Mano_6scoop_40mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_6scoop_40mm.FindMeanSD(3,rangeDef)
stent_P1491_1_Mano_6scoop_40mm.ComputeGradient()

## =============================================================================
## stent_P1491_1:40mm:6Scoops:Gradient plot
## =============================================================================
#plt.figure(2)
#plt.title('P1491_1:40mm:6scoops')
#
#sensIndex=1
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_20mmps_40mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_30mmps_40mm'],
#                                          [0,5000],0.00,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_40mmps_40mm'],
#                                                          [0,5000],0.00,[sensIndex])
#
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_20mmps_40mm'],
#                                          [0,5000],0.00,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_30mmps_40mm'],
#                                          [0,5000],0.00,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_40mmps_40mm'],
#                                          [0,5000],0.00,[sensIndex])
#   
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])     
    
 #####################################  
# =============================================================================
# stent_P1491_1:40mm:6Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[92,92,92,92,92,92]  
TimeIndexThreshold=[92,100,100,87,100,92]  
#TimeIndexThreshold=[120,120,120,120,120,120]    
SenIndex=[1]

FileList=['Mano_P1491_1_6Scoop_20mmps_40mm',
          'Mano_P1491_1_6Scoop_30mmps_40mm',
          'Mano_P1491_1_6Scoop_40mmps_40mm',
          'Mano_withoutP1491_1_6Scoop_20mmps_40mm',
          'Mano_withoutP1491_1_6Scoop_30mmps_40mm',
          'Mano_withoutP1491_1_6Scoop_40mmps_40mm']

stent_P1491_1_Mano_6scoop_40mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)
 


# =============================================================================
# stent_P1491_1:40mm:8sccops
# =============================================================================
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    
path=GenPath+"Dipankar_Manometry_Stent_P1491_05_08_19/40mm/8Scoops"
name='Mano'
Bolustype='8Scoop'
stent_P1491_1_Mano_8scoop_40mm=stentManometry(path,'stent_P1491_40mm',name)
stent_P1491_1_Mano_8scoop_40mm.find_all()
stent_P1491_1_Mano_8scoop_40mm.FileReading([0,1,2,3,4,5])
stent_P1491_1_Mano_8scoop_40mm.CreateList2byte()
stent_P1491_1_Mano_8scoop_40mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_8scoop_40mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys40mm8scoop=stent_P1491_1_Mano_8scoop_40mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1491_1_Mano_8scoop_40mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_8scoop_40mm.FindMeanSD(3,rangeDef)
stent_P1491_1_Mano_8scoop_40mm.ComputeGradient()

## =============================================================================
## stent_P1491_1:40mm:8Sccop:Gradient plot
## =============================================================================
#FigureNum3=plt.figure(3)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[2]   
#ArrayForPlotting={'GradPlot1':stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoops_20mmps_40mm'],
#                  'GradPlot2':stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_40mm'],
#                  'GradPlot3':stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_40mm'],
#                  'GradPlot4':stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_40mm'],
#                  'GradPlot5':stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_40mm'],
#                  'GradPlot6':stent_P1491_1_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_40mm']} 
#
#plt.title('P1491_1:40mm:8scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum2,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')
# =============================================================================
# stent_P1491_1:40mm:8Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[155,145,155,155,155,155] 
TimeIndexThreshold=[153,145,147,160,160,160]    
SenIndex=[2]

FileList=['Mano_P1491_1_8Scoops_20mmps_40mm',
          'Mano_P1491_1_8Scoop_30mmps_40mm',
          'Mano_P1491_1_8Scoop_40mmps_40mm',
          'Mano_withoutP1491_1_8Scoops_20mmps_40mm',
          'Mano_withoutP1491_1_8Scoops_30mmps_40mm',
          'Mano_withoutP1491_1_8Scoops_40mmps_40mm']

stent_P1491_1_Mano_8scoop_40mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1491_1:40mm:3D Plot
# =============================================================================


FigureNum4=plt.figure(4)
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting40mm={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSGradientArrayWithStent':np.array([stent_P1491_1_Mano_4scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_6scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_8scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:]]),
                           'IBPSGradientArrayWithoutStent':np.array([stent_P1491_1_Mano_4scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                     stent_P1491_1_Mano_6scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                  stent_P1491_1_Mano_8scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:]])}
stentManometry.ManometryPressure3DPlotting(FigureNum4,NumOfAxes,PlotDict=AxisParametersForPlotting40mm)


# =============================================================================
# stent_P1491_1:50mm:4Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1491_31_07_19/50mm"
name='Mano'

Bolustype='4Scoop'
stent_P1491_1_Mano_4scoop_50mm=stentManometry(path,'stent_P1491_50mm',name)
stent_P1491_1_Mano_4scoop_50mm.find_all()
stent_P1491_1_Mano_4scoop_50mm.FileReading([0,1,2,3,4,5])
stent_P1491_1_Mano_4scoop_50mm.CreateList2byte()
stent_P1491_1_Mano_4scoop_50mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_4scoop_50mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys50mm=stent_P1491_1_Mano_4scoop_50mm.ihArrayRevReshapedDict.keys()

window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
stent_P1491_1_Mano_4scoop_50mm.FindPeak(12.5,window,400,2)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_4scoop_50mm.FindMeanSD(2,rangeDef)
stent_P1491_1_Mano_4scoop_50mm.ComputeGradient()

## =============================================================================
## stent_P1491_1:50mm:4Scoop:Gradient plots    
## =============================================================================
#plt.figure(5)
#plt.title('P1491_1:50mm:4scoops')
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_4scoop_50mm_20mmps'],
#                                          [0,5000],0.0,[1])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_4scoop_50mm_30mmps'],
#                                                          [0,5000],0.00,[1])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_4scoop_50mm_40mmps'],
#                                          [0,5000],0.0,[1])
#
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4scoop_50mm_20mmps'],
#                                          [0,5000],0.0,[1]) 
#
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4scoop_50mm_30mmps'],
#                                          [0,5000],0.0,[1])
#   
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4scoop_50mm_40mmps'],
#                                          [0,5000],0.00,[1])
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps']) 
    
# =============================================================================
# stent_P1491_1:50mm:4Scoop:Max of thresholded gradient plots
# =============================================================================
TimeIndexThreshold=[110,110,110,110,110,110,110,110,110]     
SenIndex=[1]

FileList=['Mano_P1491_1_4scoop_50mm_20mmps',
          'Mano_P1491_1_4scoop_50mm_30mmps',
          'Mano_P1491_1_4scoop_50mm_40mmps',
          'Mano_withoutP1491_1_4scoop_50mm_20mmps',
          'Mano_withoutP1491_1_4scoop_50mm_30mmps',
          'Mano_withoutP1491_1_4scoop_50mm_40mmps']

stent_P1491_1_Mano_4scoop_50mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1491_1:50mm:6Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1491_19_08_19/50mm/"
name='Mano'

Bolustype='6Scoop'
stent_P1491_1_Mano_6scoop_50mm=stentManometry(path,'stent_P1491_50mm',name)
stent_P1491_1_Mano_6scoop_50mm.find_all()
stent_P1491_1_Mano_6scoop_50mm.FileReading([0,1,2,3,4,5])
stent_P1491_1_Mano_6scoop_50mm.CreateList2byte()
stent_P1491_1_Mano_6scoop_50mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_6scoop_50mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys50mm=stent_P1491_1_Mano_6scoop_50mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1491_1_Mano_6scoop_50mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_6scoop_50mm.FindMeanSD(3,rangeDef)
stent_P1491_1_Mano_6scoop_50mm.ComputeGradient()

# =============================================================================
# # =============================================================================
# # stent_P1491_1:50mm:6Scoops:Gradient plot
# # =============================================================================
# plt.figure(6)
# plt.title('P1491_1:50mm:6scoops')
# 
# sensIndex=1
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_20mmps_50mm'],
#                                           [0,5000],0.0,[sensIndex])
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_30mmps_50mm'],
#                                           [0,5000],0.00,[sensIndex])
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_40mmps_50mm'],
#                                                           [0,5000],0.00,[sensIndex])
# 
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_20mmps_50mm'],
#                                           [0,5000],0.00,[sensIndex])
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_30mmps_50mm'],
#                                           [0,5000],0.00,[sensIndex])
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_40mmps_50mm'],
#                                           [0,5000],0.00,[sensIndex])
#    
# plt.legend(['With Stent 20mmps',\
#             'With Stent 30mmps',\
#             'With Stent 40mmps',\
#             'Without Stent 20mmps',\
#             'Without Stent 30mmps',\
#             'Without Stent 40mmps']) 
# 
# =============================================================================
# =============================================================================
# stent_P1491_1:50mm:6Scoop:Max of thresholded gradient plots
# =============================================================================

TimeIndexThreshold=[96,96,96,96,96,96]  
#TimeIndexThreshold=[120,120,120,120,120,120]    
SenIndex=[1]

FileList=['Mano_P1491_1_6Scoop_20mmps_50mm',
          'Mano_P1491_1_6Scoop_30mmps_50mm',
          'Mano_P1491_1_6Scoop_40mmps_50mm',
          'Mano_withoutP1491_1_6Scoop_20mmps_50mm',
          'Mano_withoutP1491_1_6Scoop_30mmps_50mm',
          'Mano_withoutP1491_1_6Scoop_40mmps_50mm']

stent_P1491_1_Mano_6scoop_50mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)
  

# =============================================================================
# stent_P1491_1:50mm:8Scoops
# =============================================================================
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    
path=GenPath+"Dipankar_Manometry_Stent_P1491_05_08_19/50mm/8Scoops"
name='Mano'
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


## =============================================================================
## stent_P1491_1:50mm:8Scoops:Gradient plots    
## =============================================================================
#plt.figure(7)
#plt.title('P1491_1:50mm:8scoops')
#sensIndex=1
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_20mmps_50mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_50mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_50mm'],
#                                                          [0,5000],0.00,[sensIndex])
#
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_50mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_50mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_50mm'],
#                                          [0,5000],0.00,[sensIndex])
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps']) 

# =============================================================================
# stent_P1491_1:50mm:8Scoop:Max of thresholded gradient plots
# =============================================================================
TimeIndexThreshold=[120,103,110,110,110,110]     
#TimeIndexThreshold=[120,96,110,82,101,103] kept previous 
SenIndex=[1]

FileList=['Mano_P1491_1_8Scoop_20mmps_50mm',
          'Mano_P1491_1_8Scoop_30mmps_50mm',
          'Mano_P1491_1_8Scoop_40mmps_50mm',
          'Mano_withoutP1491_1_8Scoops_20mmps_50mm',
          'Mano_withoutP1491_1_8Scoops_30mmps_50mm',
          'Mano_withoutP1491_1_8Scoops_40mmps_50mm']

stent_P1491_1_Mano_8scoop_50mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1491_1:50mm:3D Plot
# =============================================================================


FigureNum8=plt.figure(8)
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting50mm={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSGradientArrayWithStent':np.array([stent_P1491_1_Mano_4scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_6scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_8scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:]]),
                           'IBPSGradientArrayWithoutStent':np.array([stent_P1491_1_Mano_4scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                     stent_P1491_1_Mano_6scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                  stent_P1491_1_Mano_8scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:]])}
stentManometry.ManometryPressure3DPlotting(FigureNum8,NumOfAxes,PlotDict=AxisParametersForPlotting50mm)


# =============================================================================
# stent_P1568_4:60mm:4Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1491_31_07_19/60mm"
name='Mano'

Bolustype='4Scoop'
stent_P1491_1_Mano_4scoop_60mm=stentManometry(path,'stent_P1491_50mm',name)
stent_P1491_1_Mano_4scoop_60mm.find_all()
stent_P1491_1_Mano_4scoop_60mm.FileReading([0,1,2,3,4,5,6,7])
stent_P1491_1_Mano_4scoop_60mm.CreateList2byte()
stent_P1491_1_Mano_4scoop_60mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_4scoop_60mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys60mm=stent_P1491_1_Mano_4scoop_60mm.ihArrayRevReshapedDict.keys()

window=[0,0,0,0,0,0,0,0,5000,5000,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
stent_P1491_1_Mano_4scoop_60mm.FindPeak(12.5,window,400,2)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_4scoop_60mm.FindMeanSD(2,rangeDef)
stent_P1491_1_Mano_4scoop_60mm.ComputeGradient()

## =============================================================================
## stent_P1491_1:60mm:4Sccop:Gradient plot
## =============================================================================
#plt.figure(9)
#plt.title('P1491_1:60mm:4scoops')
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_4Scoop_60mm_20mmps_v2'],
#                                          [0,5000],0.0,[1])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_4scoop_60mm_30mmps'],
#                                                          [0,5000],0.00,[1])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_4Scoop_60mm_40mmps_v2'],
#                                          [0,5000],0.0,[1])
#
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4Scoop_60mm_20mmps'],
#                                          [0,5000],0.0,[1]) 
#
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4scoop_60mm_30mmps'],
#                                          [0,5000],0.0,[1])
#   
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_4Scoop_60mm_40mmps'],
#                                          [0,5000],0.00,[1])
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps']) 
    
# =============================================================================
# stent_P1491_1:60mm:4Scoop:Max of thresholded gradient plots
# =============================================================================
TimeIndexThreshold=[100,100,100,100,100,100,100,100]    
SenIndex=[2]

FileList=['Mano_P1491_1_4Scoop_60mm_20mmps_v2',
          'Mano_P1491_1_4scoop_60mm_30mmps',
          'Mano_P1491_1_4Scoop_60mm_40mmps_v2',
          'Mano_withoutP1491_1_4Scoop_60mm_20mmps',
          'Mano_withoutP1491_1_4scoop_60mm_30mmps',
          'Mano_withoutP1491_1_4Scoop_60mm_40mmps']

stent_P1491_1_Mano_4scoop_60mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1491_1:50mm:6Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1491_19_08_19/60mm/"
name='Mano'

Bolustype='6Scoop'
stent_P1491_1_Mano_6scoop_60mm=stentManometry(path,'stent_P1491_60mm',name)
stent_P1491_1_Mano_6scoop_60mm.find_all()
stent_P1491_1_Mano_6scoop_60mm.FileReading([0,1,2,3,4,5,6,7])
stent_P1491_1_Mano_6scoop_60mm.CreateList2byte()
stent_P1491_1_Mano_6scoop_60mm.CreateListRev2byte2Int()
stent_P1491_1_Mano_6scoop_60mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys50mm=stent_P1491_1_Mano_6scoop_60mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,0,0,5000,5000,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1491_1_Mano_6scoop_60mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_6scoop_60mm.FindMeanSD(3,rangeDef)
stent_P1491_1_Mano_6scoop_60mm.ComputeGradient()

# =============================================================================
# # =============================================================================
# # stent_P1491_1:60mm:6Scoops:Gradient plot
# # =============================================================================
# plt.figure()
# plt.title('P1491_1:50mm:6scoops')
# 
# sensIndex=1
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_20mmps_60mm'],
#                                           [0,5000],0.0,[sensIndex])
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_30mmps_60mm'],
#                                           [0,5000],0.00,[sensIndex])
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_6Scoop_40mmps_60mm'],
#                                                           [0,5000],0.00,[sensIndex])
# 
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_20mmps_60mm'],
#                                           [0,5000],0.00,[sensIndex])
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_30mmps_60mmv2'],
#                                           [0,5000],0.00,[sensIndex])
# stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_6Scoop_40mmps_60mm'],
#                                           [0,5000],0.00,[sensIndex])
#    
# plt.legend(['With Stent 20mmps',\
#             'With Stent 30mmps',\
#             'With Stent 40mmps',\
#             'Without Stent 20mmps',\
#             'Without Stent 30mmps',\
#             'Without Stent 40mmps'])     
#     
# =============================================================================
 #####################################  
  
# =============================================================================
# stent_P1491_1:60mm:6Scoop:Max of thresholded gradient plots
# =============================================================================

#TimeIndexThreshold=[108,100,100,100,100,96,110,96]  
TimeIndexThreshold=[108,106,106,96,96,96,114,108]  
#TimeIndexThreshold=[120,120,120,120,120,120]    
SenIndex=[1]

FileList=['Mano_P1491_1_6Scoop_20mmps_60mm',
          'Mano_P1491_1_6Scoop_30mmps_60mm',
          'Mano_P1491_1_6Scoop_40mmps_60mm',
          'Mano_withoutP1491_1_6Scoop_20mmps_60mm',
          'Mano_withoutP1491_1_6Scoop_30mmps_60mmv2',
          'Mano_withoutP1491_1_6Scoop_40mmps_60mm']

stent_P1491_1_Mano_6scoop_60mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)
  
   
    
# =============================================================================
# stent_P1491_1:60mm:8Scoop
# =============================================================================
GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    
path=GenPath+"Dipankar_Manometry_Stent_P1491_05_08_19/60mm/8Scoops"
name='Mano'

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

## =============================================================================
## stent_P1491_1:60mm:Gradient plots    
## =============================================================================
#plt.figure(11)
#plt.title('P1491_1:60mm:8scoops')
#sensIndex=1
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_20mmps_60mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_30mmps_60mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1491_1_8Scoop_40mmps_60mm'],
#                                                          [0,5000],0.00,[sensIndex])
#
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_20mmps_60mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_30mmps_60mm'],
#                                          [0,5000],0.0,[sensIndex])
#stentManometry.ManometeryPressurePlotting(stent_P1491_1_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1491_1_8Scoops_40mmps_60mm'],
#                                          [0,5000],0.00,[sensIndex])
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps']) 

# =============================================================================
# stent_P1491_1:60mm:8Scoop:Max of thresholded gradient plots
# =============================================================================
TimeIndexThreshold=[140,140,140,140,140,140]   
#TimeIndexThreshold=[98,126,98,98,98,98]     
SenIndex=[1]

FileList=['Mano_P1491_1_8Scoop_20mmps_60mm',
          'Mano_P1491_1_8Scoop_30mmps_60mm',
          'Mano_P1491_1_8Scoop_40mmps_60mm',
          'Mano_withoutP1491_1_8Scoops_20mmps_60mm',
          'Mano_withoutP1491_1_8Scoops_30mmps_60mm',
          'Mano_withoutP1491_1_8Scoops_40mmps_60mm']

stent_P1491_1_Mano_8scoop_60mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

    
# =============================================================================
# stent_P1491_1:60mm:3D Plot
# =============================================================================


FigureNum12=plt.figure(12)
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting60mm={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSGradientArrayWithStent':np.array([stent_P1491_1_Mano_4scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_6scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_8scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:]]),
                           'IBPSGradientArrayWithoutStent':np.array([stent_P1491_1_Mano_4scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                     stent_P1491_1_Mano_6scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                  stent_P1491_1_Mano_8scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:]])}
stentManometry.ManometryPressure3DPlotting(FigureNum12,NumOfAxes,PlotDict=AxisParametersForPlotting60mm)


plt.close('all')
# =============================================================================
# stent_P1491_1:Mean 40mm 50mm 60mm:3D Plot
# =============================================================================

Array40mm50mm60mmWithStent=np.array([AxisParametersForPlotting40mm['IBPSGradientArrayWithStent'],
        AxisParametersForPlotting50mm['IBPSGradientArrayWithStent'],
        AxisParametersForPlotting60mm['IBPSGradientArrayWithStent']])

Mean40mm50mm60mmWithStent=np.mean(Array40mm50mm60mmWithStent,axis=0)
Std40mm50mm60mmWithStent=np.std(Array40mm50mm60mmWithStent,axis=0)

Array40mm50mm60mmWithoutStent=np.array([AxisParametersForPlotting40mm['IBPSGradientArrayWithoutStent'],
        AxisParametersForPlotting50mm['IBPSGradientArrayWithoutStent'],
        AxisParametersForPlotting60mm['IBPSGradientArrayWithoutStent']])

Mean40mm50mm60mmWithoutStent=np.mean(Array40mm50mm60mmWithoutStent,axis=0)
Std40mm50mm60mmWithoutStent=np.std(Array40mm50mm60mmWithoutStent,axis=0)

#Making a common Mean40mm50mm60mmWithoutStent and Std40mm50mm60mmWithoutStent
# for P1491_1 and P1568_4

path2=GenPath+'ArraySaveForBarPlotting/'
Mean40mm50mm60mmWithoutP1568_4Stent = np.load(path2+'P1568_4WithotStentMean40mm50mm60mm.npy')
Std40mm50mm60mmWithoutP1568_4Stent = np.load(path2+'P1568_4WithotStentStd40mm50mm60mm.npy')

Mean40mm50mm60mmWithoutStent[[2],:]=Mean40mm50mm60mmWithoutP1568_4Stent[[2],:]
Std40mm50mm60mmWithoutStent[[2],:]=Std40mm50mm60mmWithoutP1568_4Stent[[2],:]


FigureNum13=plt.figure(num=13,figsize=(2.25,1.6))
plt.title('Mean IBPS gradient of 40 mm, 50 mm, and 60 mm wavelength plots')
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlottingAll={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSGradientArrayWithStent':Mean40mm50mm60mmWithStent,
                           'IBPSGradientArrayWithoutStent':Mean40mm50mm60mmWithoutStent}
ax=stentManometry.ManometryPressure3DPlotting(FigureNum13,NumOfAxes,PlotDict=AxisParametersForPlottingAll)
ax.set_zlabel('20log(Mean IBPS gradient)\n''(KPa.s$^{-1}$)')
#ax.set_zlabel('Normalized IBPS gradient')
#ax.view_init(5, -57)
#from mpl_toolkits.mplot3d import axes3d
## rotate the axes and update
#for angle in range(0, 360):
##    pdb.set_trace()
#    ax.view_init(30, angle)
#    plt.pause(.1)

#FigureNum13.savefig(GenPath+'/Plots/StentP1491_1Mean40mm50mm60mm.pdf')

# =============================================================================
# stent_P1491_1:Mean 40mm 50mm 60mm:bar Plot
# =============================================================================

FigureNum14=plt.figure(num=14,figsize=(2.25,1.6))

axbar=stentManometry.ManometryPressureBarPlotting(FigureNum14,
                                                  Mean40mm50mm60mmWithStent,
                                                  Std40mm50mm60mmWithStent,
                                                  Mean40mm50mm60mmWithoutStent,
                                                  Std40mm50mm60mmWithoutStent,
                                                  NormFactor=np.amax(Mean40mm50mm60mmWithStent))


# =============================================================================
# Rotating the plot
# =============================================================================
#ax.view_init(elev=20., azim=i*4)
# Animate

#    plt.draw()
#    plt.pause(.0001)

#from matplotlib import animation
#FigureNum14=plt.figure(14)
#ax1 = Axes3D(FigureNum14)
#plt.title('Mean IBPS gradient of 40 mm, 50 mm, and 60 mm wavelength plots')

#def init():
#    # Plot the surface.
#    NumOfAxes=[1,1] #Defining the subplot grid
#    AxisParametersForPlottingAll={'Speed':[20,30,40],
#                           'BolusViscosity':[72,108,144],
#                           'IBPSGradientArrayWithStent':Mean40mm50mm60mmWithStent,
#                           'IBPSGradientArrayWithoutStent':Mean40mm50mm60mmWithoutStent}
#    ax=stentManometry.ManometryPressure3DPlotting(FigureNum14,NumOfAxes,PlotDict=AxisParametersForPlottingAll)
#    ax.set_zlabel(r'Mean intra-bolus pressure gradient (KPa.s$^{-1}$)')
#    
#    return FigureNum14,
#
#def animate(i):
#    # azimuth angle : 0 deg to 360 deg
#    ax1.view_init(elev=10, azim=i*4)
#    return FigureNum14,
#
## Animate
#ani = animation.FuncAnimation(FigureNum14, animate, init_func=init,
#                               frames=90, interval=50, blit=True)
