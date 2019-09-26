#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:50:37 2019

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
#plt.rcParams['figure.figsize'] = (10.0, 5) # set default size of plots #4.2x1.8

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
stent_P1491_1_Mano_4scoop_40mm.ComputeBaseline()
stent_P1491_1_Mano_4scoop_40mm.ComputeGradient()

 
# =============================================================================
# stent_P1491_1:40mm:4Scoop:Max of thresholded ibps plots
# =============================================================================
#TimeIndexThreshold=[115,115,115,115,115,115,115,115,115] 
TimeIndexThreshold=[130,115,115,115,115,130,115,115,100] 
  
SenIndex=[1]

FileList=['Mano_P1491_1_4Scoop_40mm_20mmps',
          'Mano_P1491_1_4scoop_40mm_30mmps',
          'Mano_P1491_1_4Scoop_40mm_40mmps_v2',
          'Mano_withoutP1491_1_4Scoop_40mm_20mmps',
          'Mano_withoutP1491_1_4scoop_40mm_30mmps_v2',
          'Mano_withoutP1491_1_4Scoop_40mm_40mmps']

stent_P1491_1_Mano_4scoop_40mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)

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
stent_P1491_1_Mano_6scoop_40mm.ComputeBaseline()
stent_P1491_1_Mano_6scoop_40mm.ComputeGradient()



# =============================================================================
# stent_P1491_1:40mm:6Scoop:Max of thresholded ibps plots
# =============================================================================
#TimeIndexThreshold=[92,100,100,87,100,92]  
TimeIndexThreshold=[88,100,100,88,100,88]
 
SenIndex=[1]

FileList=['Mano_P1491_1_6Scoop_20mmps_40mm',
          'Mano_P1491_1_6Scoop_30mmps_40mm',
          'Mano_P1491_1_6Scoop_40mmps_40mm',
          'Mano_withoutP1491_1_6Scoop_20mmps_40mm',
          'Mano_withoutP1491_1_6Scoop_30mmps_40mm',
          'Mano_withoutP1491_1_6Scoop_40mmps_40mm']

stent_P1491_1_Mano_6scoop_40mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)
 
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
stent_P1491_1_Mano_8scoop_40mm.ComputeBaseline()
stent_P1491_1_Mano_8scoop_40mm.ComputeGradient()

# =============================================================================
# stent_P1491_1:40mm:8Scoop:Max of thresholded ibps plots
# =============================================================================
#TimeIndexThreshold=[153,145,147,160,160,160] 
TimeIndexThreshold=[147,120,120,147,147,147]#[92+15,92+15,92+15,123+15,132+15,132+15]  
#l8scoop 20mmps are calibrated to match correct 150,140
SenIndex=[2]

FileList=['Mano_P1491_1_8Scoops_20mmps_40mm',
          'Mano_P1491_1_8Scoop_30mmps_40mm',
          'Mano_P1491_1_8Scoop_40mmps_40mm',
          'Mano_withoutP1491_1_8Scoops_20mmps_40mm',
          'Mano_withoutP1491_1_8Scoops_30mmps_40mm',
          'Mano_withoutP1491_1_8Scoops_40mmps_40mm']

stent_P1491_1_Mano_8scoop_40mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1491_1:40mm:3D Plot
# =============================================================================


FigureNum4=plt.figure(4,figsize=(2.25,1.6))
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting40mm={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSArrayWithStent':np.array([stent_P1491_1_Mano_4scoop_40mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_6scoop_40mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_8scoop_40mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:]]),
                           'IBPSArrayWithoutStent':np.array([stent_P1491_1_Mano_4scoop_40mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:],
                                                                     stent_P1491_1_Mano_6scoop_40mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:],
                                                                  stent_P1491_1_Mano_8scoop_40mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:]])}
ax=stentManometry.ManometryPressure3DPlotting(FigureNum4,NumOfAxes,PlotDict=AxisParametersForPlotting40mm)

ax.set_zlabel('Normalized maximum \n intra-bolus pressure' ' (KPa)',size=7)

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
stent_P1491_1_Mano_4scoop_50mm.ComputeBaseline()
stent_P1491_1_Mano_4scoop_50mm.ComputeGradient()

    
# =============================================================================
# stent_P1491_1:50mm:4Scoop:Max of thresholded ibps plots
# =============================================================================
#TimeIndexThreshold=[110,110,110,110,110,110,110,110,110] 
TimeIndexThreshold=[110,110,110,110,110,110,110,110,110]     
SenIndex=[1]

FileList=['Mano_P1491_1_4scoop_50mm_20mmps',
          'Mano_P1491_1_4scoop_50mm_30mmps',
          'Mano_P1491_1_4scoop_50mm_40mmps',
          'Mano_withoutP1491_1_4scoop_50mm_20mmps',
          'Mano_withoutP1491_1_4scoop_50mm_30mmps',
          'Mano_withoutP1491_1_4scoop_50mm_40mmps']

stent_P1491_1_Mano_4scoop_50mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)


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
stent_P1491_1_Mano_6scoop_50mm.ComputeBaseline()
stent_P1491_1_Mano_6scoop_50mm.ComputeGradient()

# =============================================================================
# stent_P1491_1:50mm:6Scoop:Max of thresholded ibps plots
# =============================================================================
#TimeIndexThreshold=[96,96,96,96,96,96] 
TimeIndexThreshold=[96,96,96,96,96,96] 
#TimeIndexThreshold=[120,120,120,120,120,120]    
SenIndex=[1]

FileList=['Mano_P1491_1_6Scoop_20mmps_50mm',
          'Mano_P1491_1_6Scoop_30mmps_50mm',
          'Mano_P1491_1_6Scoop_40mmps_50mm',
          'Mano_withoutP1491_1_6Scoop_20mmps_50mm',
          'Mano_withoutP1491_1_6Scoop_30mmps_50mm',
          'Mano_withoutP1491_1_6Scoop_40mmps_50mm']

stent_P1491_1_Mano_6scoop_50mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)
  

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
stent_P1491_1_Mano_8scoop_50mm.ComputeBaseline()
stent_P1491_1_Mano_8scoop_50mm.ComputeGradient()


# =============================================================================
# stent_P1491_1:50mm:8Scoop:Max of thresholded ibps plots
# =============================================================================
#TimeIndexThreshold=[120,103,110,110,110,110] 
TimeIndexThreshold=[115,105,105,105,105,105]#[120,120,95,95,97,108]    

SenIndex=[1]

FileList=['Mano_P1491_1_8Scoop_20mmps_50mm',
          'Mano_P1491_1_8Scoop_30mmps_50mm',
          'Mano_P1491_1_8Scoop_40mmps_50mm',
          'Mano_withoutP1491_1_8Scoops_20mmps_50mm',
          'Mano_withoutP1491_1_8Scoops_30mmps_50mm',
          'Mano_withoutP1491_1_8Scoops_40mmps_50mm']

stent_P1491_1_Mano_8scoop_50mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)


# =============================================================================
# stent_P1491_1:50mm:3D Plot
# =============================================================================


FigureNum8=plt.figure(8,figsize=(2.25,1.6))
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting50mm={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSArrayWithStent':np.array([stent_P1491_1_Mano_4scoop_50mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_6scoop_50mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_8scoop_50mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:]]),
                           'IBPSArrayWithoutStent':np.array([stent_P1491_1_Mano_4scoop_50mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:],
                                                                     stent_P1491_1_Mano_6scoop_50mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:],
                                                                  stent_P1491_1_Mano_8scoop_50mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:]])}
stentManometry.ManometryPressure3DPlotting(FigureNum8,NumOfAxes,PlotDict=AxisParametersForPlotting50mm)

ax.set_zlabel('Normalized maximum \n intra-bolus pressure' ' (KPa)',size=7)



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
stent_P1491_1_Mano_4scoop_60mm.ComputeBaseline()
stent_P1491_1_Mano_4scoop_60mm.ComputeGradient()


# =============================================================================
# stent_P1491_1:60mm:4Scoop:Max of thresholded ibps plots
# =============================================================================
#TimeIndexThreshold=[100,100,100,100,100,100,100,100]  
TimeIndexThreshold=[107,107,107,115,100,115,107,107]   
SenIndex=[1]

FileList=['Mano_P1491_1_4Scoop_60mm_20mmps_v2',
          'Mano_P1491_1_4scoop_60mm_30mmps',
          'Mano_P1491_1_4Scoop_60mm_40mmps_v2',
          'Mano_withoutP1491_1_4Scoop_60mm_20mmps',
          'Mano_withoutP1491_1_4scoop_60mm_30mmps',
          'Mano_withoutP1491_1_4Scoop_60mm_40mmps']

stent_P1491_1_Mano_4scoop_60mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)

# =============================================================================
# stent_P1491_1:60mm:6Scoops
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

stentDictKeys60mm=stent_P1491_1_Mano_6scoop_60mm.ihArrayRevReshapedDict.keys()

#window=[0,0,5000,5000]
window=[0,0,0,0,0,0,0,0,5000,5000,5000,5000,5000,5000,5000,5000]   #use obj.files to define the window 
#Enter that sensor index of which you want to find the peaks and than the range can be found according to those peaks
#For better results, choose that sensor which has promininet peaks
stent_P1491_1_Mano_6scoop_60mm.FindPeak(11.5,window,400,3)

rangeDef=[150,150,150,150,150,150,150,150,150,150,150,150,150,150,150,150]
stent_P1491_1_Mano_6scoop_60mm.FindMeanSD(3,rangeDef)
stent_P1491_1_Mano_6scoop_60mm.ComputeBaseline()
stent_P1491_1_Mano_6scoop_60mm.ComputeGradient()

# =============================================================================
# stent_P1491_1:60mm:6Scoop:Max of thresholded ibps plots
# =============================================================================


#TimeIndexThreshold=[108,106,106,96,96,96,114,108]   
TimeIndexThreshold=[107,107,107,96,107,96,107,107]
  
SenIndex=[1]

FileList=['Mano_P1491_1_6Scoop_20mmps_60mm',
          'Mano_P1491_1_6Scoop_30mmps_60mm',
          'Mano_P1491_1_6Scoop_40mmps_60mm',
          'Mano_withoutP1491_1_6Scoop_20mmps_60mm',
          'Mano_withoutP1491_1_6Scoop_30mmps_60mmv2',
          'Mano_withoutP1491_1_6Scoop_40mmps_60mm']

stent_P1491_1_Mano_6scoop_60mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)
  
  
    
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
stent_P1491_1_Mano_8scoop_60mm.ComputeBaseline()
stent_P1491_1_Mano_8scoop_60mm.ComputeGradient()

# =============================================================================
# stent_P1491_1:60mm:8Scoop:Max of thresholded ibps plots
# =============================================================================
#TimeIndexThreshold=[140,140,140,140,140,140]  
TimeIndexThreshold=[140,140,140,120,140,140]   
     
SenIndex=[1]

FileList=['Mano_P1491_1_8Scoop_20mmps_60mm',
          'Mano_P1491_1_8Scoop_30mmps_60mm',
          'Mano_P1491_1_8Scoop_40mmps_60mm',
          'Mano_withoutP1491_1_8Scoops_20mmps_60mm',
          'Mano_withoutP1491_1_8Scoops_30mmps_60mm',
          'Mano_withoutP1491_1_8Scoops_40mmps_60mm']

stent_P1491_1_Mano_8scoop_60mm.ComputeMaxPressure(TimeIndexThreshold,SenIndex,FileList)

    
# =============================================================================
# stent_P1491_1:60mm:3D Plot
# =============================================================================


FigureNum12=plt.figure(12,figsize=(2.25,1.6))
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlotting60mm={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSArrayWithStent':np.array([stent_P1491_1_Mano_4scoop_60mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_6scoop_60mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:],
                                                                  stent_P1491_1_Mano_8scoop_60mm.StoreMaxPressureMeanCycle.reshape((2,-1))[0,:]]),
                           'IBPSArrayWithoutStent':np.array([stent_P1491_1_Mano_4scoop_60mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:],
                                                                     stent_P1491_1_Mano_6scoop_50mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:],
                                                                  stent_P1491_1_Mano_8scoop_60mm.StoreMaxPressureMeanCycle.reshape((2,-1))[1,:]])}
stentManometry.ManometryPressure3DPlotting(FigureNum12,NumOfAxes,PlotDict=AxisParametersForPlotting60mm)

ax.set_zlabel('Normalized maximum \n intra-bolus pressure' ' (KPa)',size=7)

# =============================================================================
# stent_P1491_1:Mean 40mm 50mm 60mm:3D Plot
# =============================================================================

Array40mm50mm60mmWithStent=np.array([AxisParametersForPlotting40mm['IBPSArrayWithStent'],
        AxisParametersForPlotting50mm['IBPSArrayWithStent'],
        AxisParametersForPlotting60mm['IBPSArrayWithStent']])

Mean40mm50mm60mmWithStent=np.mean(Array40mm50mm60mmWithStent,axis=0)
Std40mm50mm60mmWithStent=np.std(Array40mm50mm60mmWithStent,axis=0)

Array40mm50mm60mmWithoutStent=np.array([AxisParametersForPlotting40mm['IBPSArrayWithoutStent'],
        AxisParametersForPlotting50mm['IBPSArrayWithoutStent'],
        AxisParametersForPlotting60mm['IBPSArrayWithoutStent']])

Mean40mm50mm60mmWithoutStent=np.mean(Array40mm50mm60mmWithoutStent,axis=0)
Std40mm50mm60mmWithoutStent=np.std(Array40mm50mm60mmWithoutStent,axis=0)

#Making a common Mean40mm50mm60mmWithoutStent and Std40mm50mm60mmWithoutStent
# for P1491_1 and P1568_4
path2=GenPath+'ArraySaveForBarPlotting/'
Mean40mm50mm60mmWithoutP1568_4Stent = np.load(path2+'P1568_4WithotStentMean40mm50mm60mmIBPS.npy')
#Std40mm50mm60mmWithoutP1491_1Stent = np.load(path2+'P1491_1WithotStentStd40mm50mm60mm.npy')

Mean40mm50mm60mmWithoutStent=Mean40mm50mm60mmWithoutP1568_4Stent
#Std40mm50mm60mmWithoutStent[1,:]=Std40mm50mm60mmWithoutP1491_1Stent[1,:]

# =============================================================================
# 
# =============================================================================

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



FigureNum13=plt.figure(num=13,figsize=(2.25,1.6))
plt.title('Mean IBPS of 40 mm, 50 mm, and 60 mm wavelength plots')
NumOfAxes=[1,1] #Defining the subplot grid
AxisParametersForPlottingAll={'Speed':[20,30,40],
                           'BolusViscosity':[72,108,144],
                           'IBPSArrayWithStent':Mean40mm50mm60mmWithStent,
                           'IBPSArrayWithoutStent':Mean40mm50mm60mmWithoutStent}
ax=stentManometry.ManometryPressure3DPlotting(FigureNum13,NumOfAxes,PlotDict=AxisParametersForPlottingAll)
#ax.set_zlabel('20log(Mean IBPS gradient)\n''(KPa.s$^{-1}$)')
ax.set_zlabel('Normalized IBPS')
#plt.close('all')
# =============================================================================
# stent_P1491_1:Mean 40mm 50mm 60mm:bar Plot
# =============================================================================

FigureNum14=plt.figure(num=14,figsize=(2.25,1.6))

axbar=stentManometry.ManometryPressureBarPlotting(FigureNum14,
                                                  Mean40mm50mm60mmWithStent,
                                                  Std40mm50mm60mmWithStent,
                                                  Mean40mm50mm60mmWithoutStent,
                                                  Std40mm50mm60mmWithoutStent,
                                                  NormFactor=np.amax(Mean40mm50mm60mmWithoutStent))



