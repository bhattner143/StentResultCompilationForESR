#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:56:41 2019

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

GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting21_05_2019_Dry_bolus_mano/"                    

# =============================================================================
# stent_P1568_2:40mm:4Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_14_08_19/4Scoops/40mm"
name='Mano'

Bolustype='4Scoop'
stent_P1568_2_Mano_4scoop_40mm=stentManometry(path,'stent_P1568_2_40mm',name)
stent_P1568_2_Mano_4scoop_40mm.find_all()
stent_P1568_2_Mano_4scoop_40mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_4scoop_40mm.CreateList2byte()
stent_P1568_2_Mano_4scoop_40mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_4scoop_40mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys40mm4Scoop=stent_P1568_2_Mano_4scoop_40mm.ihArrayRevReshapedDict.keys()

window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]
#window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_4scoop_40mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_4scoop_40mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_4scoop_40mm.ComputeGradient()

## =============================================================================
## stent_P1568_2:40mm:4Scoop:Gradient plots
## =============================================================================
#
#FigureNum1=plt.figure(1)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_20mmps_40mm'],
#                  'GradPlot2':stent_P1568_2_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_30mmps_40mm'],
#                  'GradPlot3':stent_P1568_2_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_40mmps_40mm'],
#                  'GradPlot4':stent_P1568_2_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_20mmps_40mm'],
#                  'GradPlot5':stent_P1568_2_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_30mmps_40mm'],
#                  'GradPlot6':stent_P1568_2_Mano_4scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_40mmps_40mm']} 
#plt.title('P1568_2:40mm:4scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum1,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')

# =============================================================================
# stent_P1568_2:40mm:4Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[145,135,137,137,135,145] 
TimeIndexThreshold=[113,82,104,128,102,120]     
SenIndex=[1]

FileList=['Mano_P1568_2_4Scoop_20mmps_40mm',
          'Mano_P1568_2_4Scoop_30mmps_40mm',
          'Mano_P1568_2_4Scoop_40mmps_40mm',
          'Mano_withoutP1568_2_4Scoop_20mmps_40mm',
          'Mano_withoutP1568_2_4Scoop_30mmps_40mm',
          'Mano_withoutP1568_2_4Scoop_40mmps_40mm']

stent_P1568_2_Mano_4scoop_40mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1568_2:40mm:6Scoops
# =============================================================================

path=GenPath+"Dipankar_Manometry_Stent_P1568_2_09_08_19/40mm"
name='Mano'

Bolustype='6Scoop'
stent_P1568_2_Mano_6scoop_40mm=stentManometry(path,'stent_P1568_2_40mm',name)
stent_P1568_2_Mano_6scoop_40mm.find_all()
stent_P1568_2_Mano_6scoop_40mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_6scoop_40mm.CreateList2byte()
stent_P1568_2_Mano_6scoop_40mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_6scoop_40mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys40mm6Scoop=stent_P1568_2_Mano_6scoop_40mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,24000,0,5000,5000,5000,5000,29000,5000]  #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_6scoop_40mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_6scoop_40mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_6scoop_40mm.ComputeGradient()

## =============================================================================
## stent_P1568_2:40mm:6Scoop:Gradient plots
## =============================================================================
#
#FigureNum2=plt.figure(2)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_20mmps_40mm'],
#                  'GradPlot2':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_30mmps_40mm'],
#                  'GradPlot3':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_40mmps_40mm'],
#                  'GradPlot4':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_40mm'],
#                  'GradPlot5':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_30mmps_40mm'],
#                  'GradPlot6':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_40mmps_40mm']} 
#plt.title('P1568_2:40mm:6scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum2,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')
# =============================================================================
# stent_P1568_2:40mm:6Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[145,135,137,137,135,145] 
TimeIndexThreshold=[130,112,130,130,122,125]     
SenIndex=[1]

FileList=['Mano_P1568_2_6Scoop_20mmps_40mm',
          'Mano_P1568_2_6Scoop_30mmps_40mm',
          'Mano_P1568_2_6Scoop_40mmps_40mm',
          'Mano_withoutP568_2_6Scoops_20mmps_40mm',
          'Mano_withoutP568_2_6Scoops_30mmps_40mm',
          'Mano_withoutP568_2_6Scoops_40mmps_40mm']

stent_P1568_2_Mano_6scoop_40mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1568_2:40mm:8Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_14_08_19/8Scoops/40mm"
name='Mano'

Bolustype='8Scoop'
stent_P1568_2_Mano_8scoop_40mm=stentManometry(path,'stent_P1568_2_40mm',name)
stent_P1568_2_Mano_8scoop_40mm.find_all()
stent_P1568_2_Mano_8scoop_40mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_8scoop_40mm.CreateList2byte()
stent_P1568_2_Mano_8scoop_40mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_8scoop_40mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys40mm8Scoop=stent_P1568_2_Mano_8scoop_40mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_8scoop_40mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_8scoop_40mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_8scoop_40mm.ComputeGradient()

## =============================================================================
## stent_P1568_2:40mm:8Scoop:Gradient plots
## =============================================================================
#
#FigureNum3=plt.figure(3)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_20mmps_40mm'],
#                  'GradPlot2':stent_P1568_2_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_30mmps_40mm'],
#                  'GradPlot3':stent_P1568_2_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_40mmps_40mm'],
#                  'GradPlot4':stent_P1568_2_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_20mmps_40mm'],
#                  'GradPlot5':stent_P1568_2_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_30mmps_40mm'],
#                  'GradPlot6':stent_P1568_2_Mano_8scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_40mmps_40mm']} 
#plt.title('P1568_2:40mm:8scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum3,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')
# =============================================================================
# stent_P1568_2:40mm:8Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[135,110,150,110,135,150]     
TimeIndexThreshold=[88,95,125,95,88,105]   
  
SenIndex=[1]

FileList=['Mano_P1568_2_8Scoop_20mmps_40mm',
          'Mano_P1568_2_8Scoop_30mmps_40mm',
          'Mano_P1568_2_8Scoop_40mmps_40mm',
          'Mano_withoutP568_2_8Scoops_20mmps_40mm',
          'Mano_withoutP568_2_8Scoops_30mmps_40mm',
          'Mano_withoutP568_2_8Scoops_40mmps_40mm']

stent_P1568_2_Mano_8scoop_40mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1568_2:40mm:3D Plot
# =============================================================================


FigureNum4=plt.figure(4)
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting40mm={'Speed':[20,30,40],
                           'ThickenerConcentration':[72,108,144],
                           'IBPSGradientArrayWithStent':np.array([stent_P1568_2_Mano_4scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1568_2_Mano_6scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],                                                                  
                                                                  stent_P1568_2_Mano_8scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:]]),
                            'IBPSGradientArrayWithoutStent':np.array([stent_P1568_2_Mano_4scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                      stent_P1568_2_Mano_6scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                      stent_P1568_2_Mano_8scoop_40mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:]])}
    
stentManometry.ManometryPressure3DPlotting(FigureNum4,NumOfAxes,PlotDict=AxisParametersForPlotting40mm)

# =============================================================================
# stent_P1568_2:50mm:4Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_14_08_19/4Scoops/50mm"
name='Mano'

Bolustype='4Scoop'
stent_P1568_2_Mano_4scoop_50mm=stentManometry(path,'stent_P1568_2_40mm',name)
stent_P1568_2_Mano_4scoop_50mm.find_all()
stent_P1568_2_Mano_4scoop_50mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_4scoop_50mm.CreateList2byte()
stent_P1568_2_Mano_4scoop_50mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_4scoop_50mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys50mm4Scoop=stent_P1568_2_Mano_4scoop_50mm.ihArrayRevReshapedDict.keys()

window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]
#window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_4scoop_50mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_4scoop_50mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_4scoop_50mm.ComputeGradient()

## =============================================================================
## stent_P1568_2:50mm:4Scoop:Gradient plots
## =============================================================================
#
#FigureNum5=plt.figure(5)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_20mmps_50mm'],
#                  'GradPlot2':stent_P1568_2_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_30mmps_50mm'],
#                  'GradPlot3':stent_P1568_2_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_40mmps_50mm'],
#                  'GradPlot4':stent_P1568_2_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_20mmps_50mm'],
#                  'GradPlot5':stent_P1568_2_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_30mmps_50mm'],
#                  'GradPlot6':stent_P1568_2_Mano_4scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_40mmps_50mm']} 
#plt.title('P1568_2:50mm:4scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum5,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')

# =============================================================================
# stent_P1568_2:50mm:4Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[145,135,137,137,135,145] 
TimeIndexThreshold=[88,109,115,112,102,88]     
SenIndex=[1]

FileList=['Mano_P1568_2_4Scoop_20mmps_50mm',
          'Mano_P1568_2_4Scoop_30mmps_50mm',
          'Mano_P1568_2_4Scoop_40mmps_50mm',
          'Mano_withoutP1568_2_4Scoop_20mmps_50mm',
          'Mano_withoutP1568_2_4Scoop_30mmps_50mm',
          'Mano_withoutP1568_2_4Scoop_40mmps_50mm']

stent_P1568_2_Mano_4scoop_50mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)



# =============================================================================
# stent_P1568_2:50mm:6Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_09_08_19/50mm"
name='Mano'
Bolustype='6Scoop'
stent_P1568_2_Mano_6scoop_50mm=stentManometry(path,'stent_P1568_2_40mm',name)
stent_P1568_2_Mano_6scoop_50mm.find_all()
stent_P1568_2_Mano_6scoop_50mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_6scoop_50mm.CreateList2byte()
stent_P1568_2_Mano_6scoop_50mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_6scoop_50mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys50mm=stent_P1568_2_Mano_6scoop_50mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_6scoop_50mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_6scoop_50mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_6scoop_50mm.ComputeGradient() 

## =============================================================================
## stent_P1568_2:50mm:6Scoop:Gradient plots
## =============================================================================
#
#FigureNum6=plt.figure(6)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_20mmps_50mm'],
#                  'GradPlot2':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_30mmps_50mm'],
#                  'GradPlot3':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_40mmps_50mm'],
#                  'GradPlot4':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_50mmv2'],
#                  'GradPlot5':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_30mmps_50mm'],
#                  'GradPlot6':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_40mmps_50mm']} 
#plt.title('P1568_2:50mm:6scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum6,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')
# =============================================================================
# stent_P1568_2:50mm:6Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[140,140,140,140,140,140]  
TimeIndexThreshold=[130,130,126,126,130,130]     
SenIndex=[1]

FileList=['Mano_P1568_2_6Scoop_20mmps_50mm',
          'Mano_P1568_2_6Scoop_30mmps_50mm',
          'Mano_P1568_2_6Scoop_40mmps_50mm',
          'Mano_withoutP568_2_6Scoops_20mmps_50mmv2',
          'Mano_withoutP568_2_6Scoops_30mmps_50mm',
          'Mano_withoutP568_2_6Scoops_40mmps_50mm']

stent_P1568_2_Mano_6scoop_50mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1568_2:50mm:8Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_14_08_19/8Scoops/50mm"
name='Mano'

Bolustype='8Scoop'
stent_P1568_2_Mano_8scoop_50mm=stentManometry(path,'stent_P1568_2_50mm',name)
stent_P1568_2_Mano_8scoop_50mm.find_all()
stent_P1568_2_Mano_8scoop_50mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_8scoop_50mm.CreateList2byte()
stent_P1568_2_Mano_8scoop_50mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_8scoop_50mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys50mm=stent_P1568_2_Mano_8scoop_50mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_8scoop_50mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_8scoop_50mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_8scoop_50mm.ComputeGradient()

## =============================================================================
## stent_P1568_2:50mm:8Scoop:Gradient plots
## =============================================================================
#
#FigureNum7=plt.figure(7)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_20mmps_50mm'],
#                  'GradPlot2':stent_P1568_2_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_30mmps_50mm'],
#                  'GradPlot3':stent_P1568_2_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_40mmps_50mm'],
#                  'GradPlot4':stent_P1568_2_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_20mmps_50mm'],
#                  'GradPlot5':stent_P1568_2_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_30mmps_50mm'],
#                  'GradPlot6':stent_P1568_2_Mano_8scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_40mmps_50mm']} 
#plt.title('P1568_2:50mm:8scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum7,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')
# =============================================================================
# stent_P1568_2:50mm:8Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[140,120,140,120,140,140]     
TimeIndexThreshold=[110,100,106,92,85,106] 
SenIndex=[1]

FileList=['Mano_P1568_2_8Scoop_20mmps_50mm',
          'Mano_P1568_2_8Scoop_30mmps_50mm',
          'Mano_P1568_2_8Scoop_40mmps_50mm',
          'Mano_withoutP568_2_8Scoops_20mmps_50mm',
          'Mano_withoutP568_2_8Scoops_30mmps_50mm',
          'Mano_withoutP568_2_8Scoops_40mmps_50mm']

stent_P1568_2_Mano_8scoop_50mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1568_2:50mm:3D Plot
# =============================================================================


FigureNum7=plt.figure(7)
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting50mm={'Speed':[20,30,40],
                           'ThickenerConcentration':[72,108,144],
                           'IBPSGradientArrayWithStent':np.array([stent_P1568_2_Mano_4scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1568_2_Mano_6scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],     
                                                                  stent_P1568_2_Mano_8scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:]]),
                           'IBPSGradientArrayWithoutStent':np.array([stent_P1568_2_Mano_4scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                     stent_P1568_2_Mano_6scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                     stent_P1568_2_Mano_8scoop_50mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:]])}
stentManometry.ManometryPressure3DPlotting(FigureNum7,NumOfAxes,PlotDict=AxisParametersForPlotting50mm)

# =============================================================================
# stent_P1568_2:60mm:4Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_14_08_19/4Scoops/60mm"
name='Mano'

Bolustype='4Scoop'
stent_P1568_2_Mano_4scoop_60mm=stentManometry(path,'stent_P1568_2_60mm',name)
stent_P1568_2_Mano_4scoop_60mm.find_all()
stent_P1568_2_Mano_4scoop_60mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_4scoop_60mm.CreateList2byte()
stent_P1568_2_Mano_4scoop_60mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_4scoop_60mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys60mm4Scoop=stent_P1568_2_Mano_4scoop_60mm.ihArrayRevReshapedDict.keys()

window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]
#window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_4scoop_60mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_4scoop_60mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_4scoop_60mm.ComputeGradient()

## =============================================================================
## stent_P1568_2:60mm:4Scoop:Gradient plots
## =============================================================================
#
#FigureNum8=plt.figure(8)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_20mmps_60mm'],
#                  'GradPlot2':stent_P1568_2_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_30mmps_60mm'],
#                  'GradPlot3':stent_P1568_2_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_4Scoop_40mmps_60mm'],
#                  'GradPlot4':stent_P1568_2_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_20mmps_60mm'],
#                  'GradPlot5':stent_P1568_2_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_30mmps_60mm'],
#                  'GradPlot6':stent_P1568_2_Mano_4scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP1568_2_4Scoop_40mmps_60mm']} 
#plt.title('P1568_2:60mm:4scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum8,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')

# =============================================================================
# stent_P1568_2:60mm:4Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[145,135,137,137,135,145] 
TimeIndexThreshold=[106,106,115,120,120,104]     
SenIndex=[1]

FileList=['Mano_P1568_2_4Scoop_20mmps_60mm',
          'Mano_P1568_2_4Scoop_30mmps_60mm',
          'Mano_P1568_2_4Scoop_40mmps_60mm',
          'Mano_withoutP1568_2_4Scoop_20mmps_60mm',
          'Mano_withoutP1568_2_4Scoop_30mmps_60mm',
          'Mano_withoutP1568_2_4Scoop_40mmps_60mm']

stent_P1568_2_Mano_4scoop_60mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)



# =============================================================================
# stent_P1568_2:60mm:6Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_09_08_19/60mm"
name='Mano'
Bolustype='6Scoop'
stent_P1568_2_Mano_6scoop_60mm=stentManometry(path,'stent_P1568_2_60mm',name)
stent_P1568_2_Mano_6scoop_60mm.find_all()
stent_P1568_2_Mano_6scoop_60mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_6scoop_60mm.CreateList2byte()
stent_P1568_2_Mano_6scoop_60mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_6scoop_60mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys60mm6Scoop=stent_P1568_2_Mano_6scoop_60mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_6scoop_60mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_6scoop_60mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_6scoop_60mm.ComputeGradient()

## =============================================================================
## stent_P1568_2:60mm:6Scoop:Gradient plots
## =============================================================================
#
#FigureNum9=plt.figure(9)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]  
##since 30mmps without stent doesnot exist 
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_20mmps_60mm'],
#                  'GradPlot2':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_30mmps_60mm'],
#                  'GradPlot3':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_40mmps_60mm'],
#                  'GradPlot4':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_60mmv2'],
#                  'GradPlot5':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_60mm'],
#                  'GradPlot6':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_40mmps_60mm']} 
#plt.title('P1568_2:50mm:6scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum9,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')
# =============================================================================
# stent_P1568_2:60mm:6Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[135,135,135,135,135,135]     
TimeIndexThreshold=[128,110,120,128,128,108]
SenIndex=[1]

FileList=['Mano_P1568_2_6Scoop_20mmps_60mm',
          'Mano_P1568_2_6Scoop_30mmps_60mm',
          'Mano_P1568_2_6Scoop_40mmps_60mm',
          'Mano_withoutP568_2_6Scoops_20mmps_60mmv2',
          'Mano_withoutP568_2_6Scoops_20mmps_60mm',
          'Mano_withoutP568_2_6Scoops_40mmps_60mm']

stent_P1568_2_Mano_6scoop_60mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1568_2:60mm:8Scoops
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_14_08_19/8Scoops/60mm"
name='Mano'

Bolustype='8Scoop'
stent_P1568_2_Mano_8scoop_60mm=stentManometry(path,'stent_P1568_2_60mm',name)
stent_P1568_2_Mano_8scoop_60mm.find_all()
stent_P1568_2_Mano_8scoop_60mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_8scoop_60mm.CreateList2byte()
stent_P1568_2_Mano_8scoop_60mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_8scoop_60mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys60mm=stent_P1568_2_Mano_8scoop_60mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_8scoop_60mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_8scoop_60mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_8scoop_60mm.ComputeGradient()

## =============================================================================
## stent_P1568_2:60mm:8Scoop:Gradient plots
## =============================================================================
#
#FigureNum10=plt.figure(9)
#NumOfAxes=[1,1]
#window=[0,5000]
#thres=0
#SenIndex=[1,2]   
#ArrayForPlotting={'GradPlot1':stent_P1568_2_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_20mmps_60mm'],
#                  'GradPlot2':stent_P1568_2_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_30mmps_60mm'],
#                  'GradPlot3':stent_P1568_2_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_8Scoop_40mmps_60mm'],
#                  'GradPlot4':stent_P1568_2_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_20mmps_60mm'],
#                  'GradPlot5':stent_P1568_2_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_30mmps_60mm'],
#                  'GradPlot6':stent_P1568_2_Mano_8scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_8Scoops_40mmps_60mm']} 
#plt.title('P1568_2:50mm:8scoops')  
#stentManometry.ManometeryPressurePlottingv2(FigureNum10,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting)
#plt.legend(['With Stent 20mmps',\
#            'With Stent 30mmps',\
#            'With Stent 40mmps',\
#            'Without Stent 20mmps',\
#            'Without Stent 30mmps',\
#            'Without Stent 40mmps'])  
#plt.ylabel(r'Pressure (Kpa.s$^{-1}$)')
# =============================================================================
# stent_P1568_2:60mm:8Scoop:Max of thresholded gradient plots
# =============================================================================
#TimeIndexThreshold=[150,125,125,150,125,125]  
TimeIndexThreshold=[110,93,84,110,98,113] 
   
SenIndex=[1]

FileList=['Mano_P1568_2_8Scoop_20mmps_60mm',
          'Mano_P1568_2_8Scoop_30mmps_60mm',
          'Mano_P1568_2_8Scoop_40mmps_60mm',
          'Mano_withoutP568_2_8Scoops_20mmps_60mm',
          'Mano_withoutP568_2_8Scoops_30mmps_60mm',
          'Mano_withoutP568_2_8Scoops_40mmps_60mm']

stent_P1568_2_Mano_8scoop_60mm.ComputeMaxGradient(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1568_2:60mm:3D Plot
# =============================================================================


FigureNum11=plt.figure(11)
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting60mm={'Speed':[20,30,40],
                           'ThickenerConcentration':[72,108,144],
                           'IBPSGradientArrayWithStent':np.array([stent_P1568_2_Mano_4scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1568_2_Mano_6scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1568_2_Mano_8scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[0,:]]),
                           'IBPSGradientArrayWithoutStent':np.array([stent_P1568_2_Mano_4scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                   stent_P1568_2_Mano_6scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:],
                                                                  stent_P1568_2_Mano_8scoop_60mm.StoreMaxGradMeanCycle.reshape((2,-1))[1,:]])}
stentManometry.ManometryPressure3DPlotting(FigureNum11,NumOfAxes,PlotDict=AxisParametersForPlotting60mm)

plt.close('all')
# =============================================================================
# stent_P568_2:Mean 40mm 50mm 60mm:3D Plot
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
Mean40mm50mm60mmWithoutP1491_1Stent = np.load(path2+'P1491_1WithotStentMean40mm50mm60mm.npy')
Std40mm50mm60mmWithoutP1491_1Stent = np.load(path2+'P1491_1WithotStentStd40mm50mm60mm.npy')

Mean40mm50mm60mmWithoutStent[1,:]=Mean40mm50mm60mmWithoutP1491_1Stent[1,:]
Std40mm50mm60mmWithoutStent[1,:]=Std40mm50mm60mmWithoutP1491_1Stent[1,:]

FigureNum13=plt.figure(num=13,figsize=(4.75,2.96))
plt.title('Mean IBPS gradient of 40 mm, 50 mm, and 60 mm wavelength plots')
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlottingAll={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSGradientArrayWithStent':Mean40mm50mm60mmWithStent,
                           'IBPSGradientArrayWithoutStent':Mean40mm50mm60mmWithoutStent}
ax=stentManometry.ManometryPressure3DPlotting(FigureNum13,NumOfAxes,PlotDict=AxisParametersForPlottingAll)
#ax.set_zlabel('20log(Mean IBPS gradient)\n''(KPa.s$^{-1}$)')
ax.set_zlabel('Normalized mean \nIBPS gradient')
ax.view_init(59, -21)

#FigureNum13.savefig(GenPath+'/Plots/StentP568_2Mean40mm50mm60mm.pdf')

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
# Bar Plot
# =============================================================================

#FigureNum15=plt.figure(num=15,figsize=(4.75,2.96))
FigureNum15, ax1 = plt.subplots(num=15,figsize=(2.25,1.6))

N = 3
BolusCon = (72,108,144)

#BolusMLMeans = (10, 5, 3)
#BolusMLMeans20mmps=(10, 5, 3.33)
#BolusMLMeans30mmps=(10, 5, 3.12)
#BolusMLMeans40mmps=(10, 5, 2.78)
NormBolusMLMeans20mmps=(10, 5, 3.33)
NormBolusMLMeans30mmps=(10, 5, 3.12)
NormBolusMLMeans40mmps=(10, 5, 2.78)

NormBolusGradientMean20mmps=list((Mean40mm50mm60mmWithStent[:,0]/np.amax(Mean40mm50mm60mmWithStent)))
NormBolusGradientMean30mmps=list((Mean40mm50mm60mmWithStent[:,1]/np.amax(Mean40mm50mm60mmWithStent)))
NormBolusGradientMean40mmps=list((Mean40mm50mm60mmWithStent[:,2]/np.amax(Mean40mm50mm60mmWithStent)))
#BolusGradientMean20mmps=list((Mean40mm50mm60mmWithStent[:,0]/0.08))
#BolusGradientMean30mmps=list((Mean40mm50mm60mmWithStent[:,1]/0.08))
#BolusGradientMean40mmps=list((Mean40mm50mm60mmWithStent[:,2]/0.08))
#menStd = (2, 3, 4, 1, 2)
#womenStd = (3, 5, 2, 3, 3)
width = 0.12 
ind1 = np.arange(N)    # the x locations for the groups
ind2 = [x + width for x in ind1]
ind3 = [x + width for x in ind2]

      # the width of the bars: can also be len(x) sequence

#p11 = plt.bar(ind1, NormBolusMLMeans20mmps, width,
#              color='tab:blue')
p12 = ax1.bar(ind1, NormBolusMLMeans20mmps, width,
#             NormBolusMLMeans20mmps,
             color='darkorange')

#p21 = plt.bar(ind2, NormBolusMLMeans30mmps, width,
#              color='tab:red')
p22 = ax1.bar(ind2, NormBolusMLMeans30mmps, width,
#             NormBolusMLMeans30mmps,
             color='limegreen')

#p31 = plt.bar(ind3, NormBolusMLMeans40mmps, width,
#              color='tab:green')
p32 = ax1.bar(ind3, NormBolusMLMeans40mmps, width,
#             NormBolusMLMeans40mmps,
             color='lightskyblue')

plt.xlabel(r'Bolus concentration (g.L$^{-1}$)',size=5)
ax1.xaxis.labelpad = 10
plt.ylabel('Transported bolus volume (ml)',size=5)

plt.xticks([])

ax1.annotate('72', xy=(0.2825, 0.07),xycoords='figure fraction', 
                     xytext=(0.2825,0.005), textcoords='figure fraction',
            fontsize=5, ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-[, widthB=1.5, lengthB=0.5', lw=0.5))
        
ax1.annotate('108', xy=(0.5425, 0.07),xycoords='figure fraction', 
             xytext=(0.5425,0.005), textcoords='figure fraction',
    fontsize=5, ha='center', va='bottom',
    arrowprops=dict(arrowstyle='-[, widthB=1.5, lengthB=0.5', lw=0.5))

ax1.annotate('144', xy=(0.8025, 0.07),xycoords='figure fraction', 
             xytext=(0.8025,0.005), textcoords='figure fraction',
            fontsize=5, ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-[, widthB=1.5, lengthB=0.5', lw=0.5))
ax1.set_ylim([0,12])


#plt.yticks(np.arange(0, 81, 10))
plt.legend((p12[0], p22[0],p32[0]), ('20 mm.s$^{-1}$', '30 mm.s$^{-1}$', '40 mm.s$^{-1}$'))


#plt.show()
#bars = [r for r in ax1.get_children() if type(r)==Rectangle]
#colors = [c.get_facecolor() for c in bars[:-1]] # I think the last Rectangle is the background.
