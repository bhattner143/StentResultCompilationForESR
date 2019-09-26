#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:50:51 2019

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
path=GenPath+"Dipankar_Manometry_Stent_P1568_2_09_08_19/40mm"
name='Mano'

# =============================================================================
# stent_P1568_2:40mm:6Scoops
# =============================================================================

Bolustype='6Scoop'
stent_P1568_2_Mano_6scoop_40mm=stentManometry(path,'stent_P1568_2_40mm',name)
stent_P1568_2_Mano_6scoop_40mm.find_all()
stent_P1568_2_Mano_6scoop_40mm.FileReading([0,1,2,3,4,5])
stent_P1568_2_Mano_6scoop_40mm.CreateList2byte()
stent_P1568_2_Mano_6scoop_40mm.CreateListRev2byte2Int()
stent_P1568_2_Mano_6scoop_40mm.CreateArrayRevReshaped(6,np.array([10000,39112,36380,42660,43900,40060]))

stentDictKeys40mm=stent_P1568_2_Mano_6scoop_40mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,24000,0,5000,5000,5000,5000,29000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_6scoop_40mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_6scoop_40mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_6scoop_40mm.ComputeBaseline()
stent_P1568_2_Mano_6scoop_40mm.ComputeGradient()

# =============================================================================
# stent_P1568_2:40mm:6Scoops: Subplots comparing IBPS and IBPS gradient   
# =============================================================================

NumOfAxes=[2,1]
window=[0,5000]
thres=0
SenIndex=[1] 

FigureNum1=plt.figure(1)
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_40mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_20mmps_40mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_40mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_20mmps_40mm'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_20mmps_40mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_40mm']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum1,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 

FigureNum2=plt.figure(2)
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_40mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_30mmps_40mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_40mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_30mmps_40mm'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_30mmps_40mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_30mmps_40mm']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum2,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 

FigureNum3=plt.figure(3)
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_40mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_40mmps_40mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_40mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_40mmps_40mm'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_40mmps_40mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_40mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_40mmps_40mm']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum3,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 

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
stent_P1568_2_Mano_6scoop_50mm.ComputeBaseline()
stent_P1568_2_Mano_6scoop_50mm.ComputeGradient()     

# =============================================================================
# stent_P1568_2:50mm:6Scoops: Subplots comparing IBPS and IBPS gradient   
# =============================================================================

NumOfAxes=[2,1]
window=[0,5000]
thres=0
SenIndex=[1] 

FigureNum4=plt.figure(4)
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_50mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_20mmps_50mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_50mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_20mmps_50mmv2'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_20mmps_50mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_50mmv2']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum4,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 

FigureNum5=plt.figure(5)
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_50mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_30mmps_50mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_50mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_30mmps_50mm'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_30mmps_50mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_30mmps_50mm']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum5,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 

FigureNum6=plt.figure(6)
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_50mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_40mmps_50mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_50mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_40mmps_50mm'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_40mmps_50mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_40mmps_50mm']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum6,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 

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

stentDictKeys50mm=stent_P1568_2_Mano_6scoop_60mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1568_2_Mano_6scoop_60mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1568_2_Mano_6scoop_60mm.FindMeanSD(3,rangeDef)
stent_P1568_2_Mano_6scoop_60mm.ComputeBaseline()
stent_P1568_2_Mano_6scoop_60mm.ComputeGradient()

# =============================================================================
# stent_P1568_2:60mm:6Scoops: Subplots comparing IBPS and IBPS gradient   
# =============================================================================

NumOfAxes=[2,1]
window=[0,5000]
thres=0
SenIndex=[1] 

FigureNum7=plt.figure(7)
#since I could not find without stent30mmps
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_60mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_20mmps_60mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_60mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_20mmps_60mmv2'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_20mmps_60mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_60mmv2']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum7,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 

FigureNum8=plt.figure(8)
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_60mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_30mmps_60mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_60mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_20mmps_60mm'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_30mmps_60mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_60mm']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum8,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 

FigureNum9=plt.figure(9)
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_60mm.MeanCycleInfoArrayBaselineSubDict['Mano_P1568_2_6Scoop_40mmps_60mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_60mm.MeanCycleInfoArrayBaselineSubDict['Mano_withoutP568_2_6Scoops_40mmps_60mm'],
                  'GradPlot1':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_40mmps_60mm'],
                  'GradPlot2':stent_P1568_2_Mano_6scoop_60mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_40mmps_60mm']} 

stentManometry.ManometeryPressurePlottingv3(FigureNum9,NumOfAxes,window,thres,SenIndex,PlotDict=ArrayForPlotting) 