#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:22:25 2019

@author: dipankarbhattacharya
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb

def cls():
    print('\n'*50)
#clear Console
cls()

import glob
import fnmatch
import pathlib
import os
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting12_02_2019/DataStentP1568_1"
os.chdir(path)
name='TOF'
result = []


#for x in range(len(files)):
#    if name in files[x]:
#        result.append(files[x])
        
        
def ManometeryPressurePlotting(FigureNum,NumOfAxes,Window,thres,*SenIndex,**ArrayForPlotting):
#        pdb.set_trace()
        for i,value1 in enumerate(ArrayForPlotting):
        #Loop through the Axes object (Creating an axes grid)   
            ax = FigureNum.add_subplot(NumOfAxes[0], NumOfAxes[1],i+1)
            labellist=list()
            for c,value2 in enumerate(SenIndex[0]):
             #Loop through each axes to for multiple plot   
                ax.plot(ArrayForPlotting[value1][Window[0]:Window[1],0],
                             ArrayForPlotting[value1][Window[0]:Window[1],value2]-thres,
                             label='Sensor'+str(value2))
                labellist.append('Sensor'+str(value2))
            plt.legend()
        

SenIndex=[1]
Figure1=plt.figure()
ArrayForPlotting={'Plot1':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_30mmps_50mm'],
                  'Plot2':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_50mmv2'],
                  'Plot3':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_P1568_2_6Scoop_30mmps_50mm'],
                  'Plot4':stent_P1568_2_Mano_6scoop_50mm.GradMeanCycleInfoDict['Mano_withoutP568_2_6Scoops_20mmps_50mmv2']}

ManometeryPressurePlotting(Figure1,(2,2),[0,5000],0,[2,3],**ArrayForPlotting)