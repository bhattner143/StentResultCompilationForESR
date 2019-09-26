#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:07:18 2019

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
from numpy.random import rand

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection

import pandas as pd
from intelhex import IntelHex
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.nonparametric.smoothers_lowess import lowess
from dateutil.parser import parse
from scipy.signal import find_peaks,peak_prominences
import random
#from Annotation3DClass import *


def cls():
    print('\n'*50)
#clear Console
cls()

class stentManometry():   

#     columns_new = ['Digital Pressure'] #class attribute
    #Constructor method
    def __init__(self,path,stentName,name):
#        pdb.set_trace()
        self.path = path
        self.stentName=stentName
        self.name=name
        self.currWorkDir=os.getcwd()
        os.chdir(self.path) # whenever we will create an instance of the class, the path will be set for it
        self.ihHexListFinal={}
        self.ihHexList2byte={}
        self.ihHexList2byte2Int={}  
        self.ihHexList2byteReverse={}
        self.ihHexListRev2byte2Int={}
        self.ihArrayRevReshapedDict={}
        self.ihDataFrameRevReshapedDict={}
        self.MeanCycleInfoDict={}
        self.GradMeanCycleInfoDict={}
    # Instance method to find files in the folder
    def find_all(self):
#        pdb.set_trace()
        self.files=[files[index] for root, dirs, files in sorted(os.walk(self.path)) for index in range(len(files)) if self.name in files[index]]
# =============================================================================
# Method: Read Intel hex files and create a dictinonary containing each byte in sequential order
# =============================================================================         
    def FileReading(self,indexFileToRead):
#        pdb.set_trace()
        for index in range(len(indexFileToRead)):
            
            if self.name=='Mano':
               self.filename1=[self.files[indexFileToRead[index]]]#,self.files[indexFileToRead[1]],self.files[indexFileToRead[2]]]           
#               print(self.filename1)
               ih=IntelHex(self.filename1[0])
               ihList=list()
               ihHexList=list()
               for ii in range(len(ih)):
                   ihList.append(ih[ii])
                   ihHexList.append(hex(ihList[ii]))
                   if len(ihHexList[ii])==3:
                       ihHexList[ii]=ihHexList[ii]+'0'
                       
               self.ihHexListFinal[self.filename1[0].split('.')[0]]=ihHexList
               
        #Returning the working directory to the  current working directory      
        os.chdir(self.currWorkDir)
               
# =============================================================================
# Method :Create a dictionary such that each item contains 2 byte
# =============================================================================
    def CreateList2byte(self):
        
        for c,value in enumerate(self.ihHexListFinal):
#            pdb.set_trace()
            ihHexList2byte=list()
            ihHexList2byte2Int=list()                                   
            jj=0     
            for ii in range(len(self.ihHexListFinal[value])):
                if ii%2==0:
                    ihHexList2byte.append(self.ihHexListFinal[value][ii]+\
                                          self.ihHexListFinal[value][ii+1][2:4])
                    ihHexList2byte2Int.append(int(ihHexList2byte[jj],16))
                    jj+=1
            self.ihHexList2byte[value]= ihHexList2byte       
            self.ihHexList2byte2Int[value]= ihHexList2byte2Int 
#               pdb.set_trace()
    
# =============================================================================
# Reverse the bytes and generate a dictionary containing its equivalant unsigned integer value
# =============================================================================
    def CreateListRev2byte2Int(self):
        
        for c,value in enumerate(self.ihHexListFinal):
            
            ihHexList2byteReverse=list()
            ihHexListRev2byte2Int=list()
            for ii in range(len(self.ihHexList2byte[value])):
                    temp=self.ihHexList2byte[value][ii][2:4]
                    ihHexList2byteReverse.append('0x'+self.ihHexList2byte[value][ii][4:6]+temp)
                    ihHexListRev2byte2Int.append(int(ihHexList2byteReverse[ii],16))
                    
            self.ihHexList2byteReverse[value]=ihHexList2byteReverse
            self.ihHexListRev2byte2Int[value]=ihHexListRev2byte2Int
            
# =============================================================================
# Create a numpy array and reshape it      
# =============================================================================
    def CreateArrayRevReshaped(self,NumOfCol,CalArray):
        # This method reshapes the array and calibrate the values by using data 
        #genarated from the manometry appratus before the experiments \
        # NumOfCol: Takes the reshape value
        # CalArray: Takes the Catheter pressure sensor calibration values. For proper
        # indexing the first elememt should be 10000
        
#        pdb.set_trace()
        ColumnName=['Time','Wtf','Sensor1','Sensor2','Sensor3','Sensor4','Sensor5']
        for c,value in enumerate(self.ihHexListFinal):
            ihArrayRevReshaped=np.array([])
            ihArrayRevReshaped=np.array(self.ihHexListRev2byte2Int[value])
            # Using python broadcasting
            ihArrayRevReshaped=100*0.133322*np.reshape(ihArrayRevReshaped, \
                (int(len(ihArrayRevReshaped)/NumOfCol), NumOfCol))/CalArray
                                          
                
            temp=np.linspace(0,ihArrayRevReshaped.shape[0]-1,ihArrayRevReshaped.shape[0])  
                                         
            
            self.ihArrayRevReshapedDict[value]=np.vstack((temp.T,ihArrayRevReshaped.T)).T 
            self.ihDataFrameRevReshapedDict[value]=pd.DataFrame(np.vstack((temp.T,ihArrayRevReshaped.T)).T )
            self.ihDataFrameRevReshapedDict[value].columns=ColumnName
            
# =============================================================================
# Find prominient peaks    
# =============================================================================
            
    def FindPeak(self,ht,window,dist,sensorIndex=2):
#        pdb.set_trace()
        self.PeakInformationDict={}
        for c,value in enumerate(self.ihHexListFinal):
            
            peaks, peakHeights = find_peaks(self.ihArrayRevReshapedDict[value][window[c]:window[c+len(self.ihHexListFinal)],sensorIndex]\
                                , height=ht,distance=dist)
            
            self.PeakInformationDict[value]=np.array([peaks+window[c],peakHeights['peak_heights']]).T
            
# =============================================================================
# Find mean and sd of the prominient peak cycles 
# =============================================================================
            
    def FindMeanSD(self,sensorIndex=2,*rangeDef):
#        pdb.set_trace()
        for c,value in enumerate(self.PeakInformationDict):
            RangeInfoArray=np.vstack((self.PeakInformationDict[value][:,0]-rangeDef[0][c],
                       self.PeakInformationDict[value][:,0]+rangeDef[0][c+len(self.PeakInformationDict)])).T
            # Deleting the row containing negative value
            RangeInfoArray=RangeInfoArray[(RangeInfoArray[:,0]>0) & (RangeInfoArray[:,1]>0),:]  
            
            
            # Cycle number,with time, sesnor index
            if RangeInfoArray[-1,1]<self.ihArrayRevReshapedDict[value].shape[0]:
                
                CycleInfoArray=np.zeros((RangeInfoArray.shape[0],int(RangeInfoArray[0,1]-RangeInfoArray[0,0]),3))
            else:
                
                CycleInfoArray=np.zeros((RangeInfoArray.shape[0]-1,int(RangeInfoArray[0,1]-RangeInfoArray[0,0]),3))
                
            for index in range(RangeInfoArray.shape[0]):
                
#                CycleInfoArray[index,:]=np.arange(RangeInfoArray[index,0],
#                              RangeInfoArray[index,1],dtype=int)
                #Index3=sensor number, 0:sensor1, 1:sensor 2, 2:sensor 3
                if RangeInfoArray[index,1]<self.ihArrayRevReshapedDict[value].shape[0]:
                
                     CycleInfoArray[index,:,0]=self.ihArrayRevReshapedDict[value]\
                         [int(RangeInfoArray[index,0]):int(RangeInfoArray[index,1]),sensorIndex]
                         
                     CycleInfoArray[index,:,1]=self.ihArrayRevReshapedDict[value]\
                         [int(RangeInfoArray[index,0]):int(RangeInfoArray[index,1]),sensorIndex+1]
                         
                     CycleInfoArray[index,:,2]=self.ihArrayRevReshapedDict[value]\
                         [int(RangeInfoArray[index,0]):int(RangeInfoArray[index,1]),sensorIndex+2]
                         
                else:
                    break
                     
            CycleInfoArray=CycleInfoArray.T # After transposing, index 1 is the sensor number
#            pdb.set_trace()
            #Determine mean and create time index
            MeanCycleInfoArray=np.vstack((np.arange(0,CycleInfoArray.shape[1]),
                                          np.mean(CycleInfoArray,axis=2))).T
            # Creating a tuple to enter two arrays at the same dictionary key
            self.MeanCycleInfoDict[value]=(MeanCycleInfoArray,CycleInfoArray)
            
# =============================================================================
# Compute Baseline of  MeanCycleInfoDict and subtract it        
# =============================================================================
    def ComputeBaseline(self):
        self.MeanCycleInfoArrayBaselineSubDict={}
#        pdb.set_trace()
        for c,value in enumerate(self.MeanCycleInfoDict):
            
            BaselineMean=np.mean(self.MeanCycleInfoDict[value][0][0:40],axis=0)
            BaselineMean[0]=0
            
            self.MeanCycleInfoArrayBaselineSubDict[value]=self.MeanCycleInfoDict[value][0]-BaselineMean      
            
# =============================================================================
# Compute a Gradient dictionasry of the MeanCycleInfoDict         
# =============================================================================
    def ComputeGradient(self):
#        pdb.set_trace()
        for c,value in enumerate(self.MeanCycleInfoDict):
            
            GradMeanCycleInfoArray=np.gradient(self.MeanCycleInfoDict\
                      [value][0],
                      self.MeanCycleInfoDict\
                      [value][0][:,0],axis=0)
            
            GradMeanCycleInfoArray[:,0]=self.MeanCycleInfoDict\
                      [value][0][:,0]
            self.GradMeanCycleInfoDict[value]=GradMeanCycleInfoArray
            
# =============================================================================
# Compute maximum of the gradient dictionary upto a specific time index (TimeIndexThreshold) 
# Store the required maximum value of the FileList in a numpy array             
# =============================================================================
    def ComputeMaxGradient(self,TimeIndexThreshold,SenIndex,*FileList):
#        pdb.set_trace()
        self.MaxGradMeanCycleInfoDict={}
        for c,value in enumerate(self.GradMeanCycleInfoDict): 
            self.MaxGradMeanCycleInfoDict[value]=np.amax(self.GradMeanCycleInfoDict[value][0:TimeIndexThreshold[c],:],axis=0).T
#        pdb.set_trace()
        self.StoreMaxGradMeanCycle=np.zeros((len(FileList[0])))
        for c2,value2 in enumerate(FileList[0]):
            self.StoreMaxGradMeanCycle[c2]=self.MaxGradMeanCycleInfoDict[value2][SenIndex]

# =============================================================================
# Compute maximum of the MeanCycleInfoDict dictionary upto a specific time index (TimeIndexThreshold) 
# Store the required maximum value of the FileList in a numpy array             
# =============================================================================
    def ComputeMaxPressure(self,TimeIndexThreshold,SenIndex,*FileList):
#        pdb.set_trace()
        self.MaxPressureMeanCycleInfoDict={}
        for c,value in enumerate(self.MeanCycleInfoArrayBaselineSubDict): 
            self.MaxPressureMeanCycleInfoDict[value]=np.amax(self.MeanCycleInfoArrayBaselineSubDict[value][0:TimeIndexThreshold[c],:],axis=0).T
#        pdb.set_trace()
        self.StoreMaxPressureMeanCycle=np.zeros((len(FileList[0])))
        for c2,value2 in enumerate(FileList[0]):
            self.StoreMaxPressureMeanCycle[c2]=self.MaxPressureMeanCycleInfoDict[value2][SenIndex]
                            
            
# =============================================================================
# Plotting: static method has been used to make the plot method generic     
# ============================================================================= 

    @staticmethod
    def ManometeryPressurePlotting(ArrayForPlotting,Window,thres,*SenIndex):
#        pdb.set_trace()
        print(type(SenIndex))
        labellist=list()
#        plt.hold(True)
        for c,value in enumerate(SenIndex[0]):
            lines, =plt.plot(ArrayForPlotting[Window[0]:Window[1],0],
                     ArrayForPlotting[Window[0]:Window[1],value]-thres,
                     label='Sensor'+str(value))
            labellist.append('Sensor'+str(value))
#        plt.hold(False)
        plt.legend()
        
    @staticmethod
#The *argw will take any number of positional arguments. In this case *arges will store both sensorindex
# and plot dictionary if we call ManometeryPressurePlottingv(,,,,SenIndex,ArrayForPlotting)
#calling ManometeryPressurePlottingv(,,,,SenIndex,PlotDict=ArrayForPlotting) will store postional arguments in args,
# and keywrod argument PlotDict in kwargs
    def ManometeryPressurePlottingv2(FigureNum,NumOfAxes,Window,thres,*args,**kwargs):
#        pdb.set_trace()
        a,*b=kwargs['PlotDict']
        #Loop through the Axes object (Creating an axes grid)
        j=0
        ax = FigureNum.add_subplot(NumOfAxes[0], NumOfAxes[1],j+1)
        
#        plt.hold(True)
        for i,value1 in enumerate(kwargs['PlotDict']):
            labellist=list()
            for c,value2 in enumerate(args[0]):
             #Loop through each axes to for multiple plot   
                ax.plot(kwargs['PlotDict'][value1][Window[0]:Window[1],0],
                             kwargs['PlotDict'][value1][Window[0]:Window[1],value2]-thres,
                             label='Sensor'+str(value2))
                labellist.append('Sensor'+str(value2))
            plt.legend()

    @staticmethod
#The *argw will take any number of positional arguments. In this case *arges will store both sensorindex
# and plot dictionary if we call ManometeryPressurePlottingv(,,,,SenIndex,ArrayForPlotting)
#calling ManometeryPressurePlottingv(,,,,SenIndex,PlotDict=ArrayForPlotting) will store postional arguments in args,
# and keywrod argument PlotDict in kwargs
    def ManometeryPressurePlottingv3(FigureNum,NumOfAxes,Window,thres,*args,**kwargs):
#        pdb.set_trace()
        # I know it is a very poor implementation
        a,*b=kwargs['PlotDict']
        #Loop through the Axes object (Creating an axes grid)
        for AxesIndex in range(NumOfAxes[0]*NumOfAxes[1]):
            
            ax = FigureNum.add_subplot(NumOfAxes[0], NumOfAxes[1],AxesIndex+1)
            
    #        plt.hold(True)
            for i,value1 in enumerate(kwargs['PlotDict']):
                
                if AxesIndex==0 and i<=1:
                    labellist=list()
                    for c,value2 in enumerate(args[0]):
                     #Loop through each axes to for multiple plot   
                        ax.plot(kwargs['PlotDict'][value1][Window[0]:Window[1],0],
                                     kwargs['PlotDict'][value1][Window[0]:Window[1],value2]-thres)
#                        labellist.append('Sensor'+str(value2))
#                    plt.legend()
                    plt.legend(['With Stent',\
                                'Without Stent'])
                    
                elif AxesIndex==1 and i>1:
                    for c,value2 in enumerate(args[0]):
                     #Loop through each axes to for multiple plot   
                        ax.plot(kwargs['PlotDict'][value1][Window[0]:Window[1],0],
                                     kwargs['PlotDict'][value1][Window[0]:Window[1],value2]-thres)
#                        labellist.append('Sensor'+str(value2))
                    plt.legend(['With Stent',\
                                'Without Stent'])
                    
                else:
                    continue

        

# =============================================================================
# 3D Plotting
# =============================================================================
    def ManometryPressure3DPlotting(FigureNum,
                                    NumOfAxes,
                                    **kwargs):
        
#        pdb.set_trace()
        ax = FigureNum.add_subplot(111,projection='3d')
        key_list=list(kwargs['PlotDict'].keys())
        Speed=kwargs['PlotDict'][key_list[0]]
        BolusConc=kwargs['PlotDict'][key_list[1]]
        
        X=np.array(Speed)
        Y=np.array(BolusConc)
        X,Y=np.meshgrid(X, Y)
        colormap=['viridis','coolwarm']
        color=['r','g']
        labellist=list()
        
        X1=X.flatten()
        Y1=Y.flatten()
        
        kwargKeys=[value for counter,value in enumerate (kwargs['PlotDict'].keys())]
        
        NormFactor=np.amax(np.array([kwargs['PlotDict'][kwargKeys[2]],
                                    kwargs['PlotDict'][kwargKeys[3]]]))
#        pdb.set_trace()
        for counter,value in enumerate(kwargs['PlotDict']):

            condition=counter==0 or counter==1
            labellist=list()
            if condition:
                continue
            else:
                Z=kwargs['PlotDict'][value]
                Z=20*np.log10(Z)
                #Z=Z/NormFactor
                #ax = FigureNum.gca(projection='3d')
#                ax.plot_wireframe(X, Y, Z, rstride=1,cstride=1,color='k')
                surf = ax.plot_surface(X, Y, Z,cmap=colormap[counter-2],edgecolor='k',
#                               rstride=1,cstride=1,
                               color='r',
                               alpha=0.8,
                               linewidth=0, antialiased=False)
                
#                fake2Dline = mpl.lines.Line2D([0],[0], linestyle="none", c='b', marker = 'o')
                
                scatter=ax.scatter(X, Y, Z,
                                   s=10,
                                   alpha=0.5,
                                   c=color[counter-2],
                                   linewidths=0,
                                   label=str(value).split('y')[1])
                ax.plot_wireframe(X,Y,Z,
                                  rstride=1,cstride=1,
                                  color='k',
                                  lw=1)
                
#                ax.set_zscale('log')
                
                
#                labellist.append(fake2Dline)
                         
            Z1=Z.flatten()
            for x, y, z in zip(X1, Y1, Z1):
                ax.text(x, y, z, '%s' % (np.round(z,3)), size=4, zorder=1, color='k')
                
        ax.set_autoscale_on(True)
        plt.legend()
        
        
        ax.xaxis.set_major_locator(plt.FixedLocator(Speed))
        ax.yaxis.set_major_locator(plt.FixedLocator(BolusConc))
        ax.view_init(11, -141)
        
        ax.set_xlabel(r'Wave speed' '\n(cm.s$^{-1})$',size=5)
        ax.set_ylabel(r'Bolus concentration''\n(g.L$^{-1}$)',size=5)
        ax.set_zlabel(r'Intra-bolus pressure gradient' '(\n KPa.s$^{-1}$)',size=5)
        
        plt.show()
                
        return ax
    
# =============================================================================
# Bar Plotting   
# =============================================================================
    def ManometryPressureBarPlotting(FigureNum,
                                     Mean40mm50mm60mmWithStent,
                                     Std40mm50mm60mmWithStent,
                                     Mean40mm50mm60mmWithoutStent,
                                     Std40mm50mm60mmWithoutStent,
                                     NormFactor,
                                     width=0.25): 

        #FigureNum.set_size_inches(2.25, 1.6)
        ax1 = FigureNum.add_subplot(111)
        

        N = 3
        BolusCon = (72,108,144)
        
        NormMean40mm50mm60mmWithStent=Mean40mm50mm60mmWithStent/NormFactor
        NormStd40mm50mm60mmWithStent=Std40mm50mm60mmWithStent/NormFactor
        
        NormMean40mm50mm60mmWithoutStent=Mean40mm50mm60mmWithoutStent/NormFactor
        NormStd40mm50mm60mmWithoutStent=Std40mm50mm60mmWithoutStent/NormFactor
        
        
        NormBolusMean20mmpsWithStent=list((NormMean40mm50mm60mmWithStent[:,0]))
        NormBolusMean30mmpsWithStent=list((NormMean40mm50mm60mmWithStent[:,1]))
        NormBolusMean40mmpsWithStent=list((NormMean40mm50mm60mmWithStent[:,2]))
        
        NormBolusStd20mmpsWithStent=list((NormStd40mm50mm60mmWithStent[:,0]))
        NormBolusStd30mmpsWithStent=list((NormStd40mm50mm60mmWithStent[:,1]))
        NormBolusStd40mmpsWithStent=list((NormStd40mm50mm60mmWithStent[:,2]))
        
        
        NormBolusMean20mmpsWithoutStent=list((NormMean40mm50mm60mmWithoutStent[:,0]))
        NormBolusMean30mmpsWithoutStent=list((NormMean40mm50mm60mmWithoutStent[:,1]))
        NormBolusMean40mmpsWithoutStent=list((NormMean40mm50mm60mmWithoutStent[:,2]))
        
        
        NormBolusStd20mmpsWithoutStent=list((NormStd40mm50mm60mmWithoutStent[:,0]))
        NormBolusStd30mmpsWithoutStent=list((NormStd40mm50mm60mmWithoutStent[:,1]))
        NormBolusStd40mmpsWithoutStent=list((NormStd40mm50mm60mmWithoutStent[:,2]))
        
        
        ind3 = 2*np.arange(N)-width    # the x locations for the groups
        ind2 = [x - width for x in ind3]
        ind1 = [x - width for x in ind2]
        
        ind4 = 2*np.arange(N)+width    # the x locations for the groups
        ind5 = [x + width for x in ind4]
        ind6 = [x + width for x in ind5]
        
        # the width of the bars: can also be len(x) sequence
        
        colorList=['darkorange','limegreen','lightskyblue']

        p11a= ax1.bar(ind1, NormBolusMean20mmpsWithoutStent, width,
        #             BolusMLMeans20mmps,
#                     yerr=NormBolusStd20mmpsWithoutStent,
                     color=colorList[0])
        p11b= ax1.bar(ind1, NormBolusMean20mmpsWithoutStent, width,
        #             BolusMLMeans20mmps,
#                     yerr=NormBolusStd20mmpsWithoutStent,
                     color='white',
                     hatch='////////')
        
        p11= ax1.bar(ind1, NormBolusMean20mmpsWithoutStent, width,
        #             BolusMLMeans20mmps,
#                     yerr=NormBolusStd20mmpsWithoutStent,
                     color=colorList[0],
                
                     hatch='////////')
        
        p12b= ax1.bar(ind4, NormBolusMean20mmpsWithStent, width,
        #             BolusMLMeans20mmps,
#                     yerr=NormBolusStd20mmpsWithStent,
                     color='white',
                     hatch='\\\\\\\\\\\\\\\\')
                     
        p12= ax1.bar(ind4, NormBolusMean20mmpsWithStent, width,
        #             BolusMLMeans20mmps,
#                     yerr=NormBolusStd20mmpsWithStent,
                     color=colorList[0],
                     hatch='\\\\\\\\\\\\\\\\')             
        
        
        p21a = ax1.bar(ind2, NormBolusMean30mmpsWithoutStent, width,
        #             BolusMLMeans30mmps,
#                      yerr=NormBolusStd30mmpsWithoutStent,
                      color=colorList[1])
#        
        p21 = ax1.bar(ind2, NormBolusMean30mmpsWithoutStent, width,
        #             BolusMLMeans30mmps,
#                      yerr=NormBolusStd30mmpsWithoutStent,
                      color=colorList[1],
                      hatch='////////')
        
        p22 = ax1.bar(ind5, NormBolusMean30mmpsWithStent, width,
        #             BolusMLMeans30mmps,
#                      yerr=NormBolusStd30mmpsWithStent,
                      color=colorList[1],
                      hatch='\\\\\\\\\\\\\\\\')
        
        p31a = ax1.bar(ind3, NormBolusMean40mmpsWithoutStent, width,
        #             BolusMLMeans40mmps,
#                      yerr=NormBolusStd40mmpsWithoutStent,
                      color=colorList[2])
        p31 = ax1.bar(ind3, NormBolusMean40mmpsWithoutStent, width,
        #             BolusMLMeans40mmps,
#                      yerr=NormBolusStd40mmpsWithoutStent,
                      color=colorList[2],
                      hatch='////////')
        p32 = ax1.bar(ind6, NormBolusMean40mmpsWithStent, width,
        #             BolusMLMeans40mmps,
#                      yerr=NormBolusStd40mmpsWithStent,
                      color=colorList[2],
                      hatch='\\\\\\\\\\\\\\\\')
        
        
        
        ax1.set_xlabel(r'Bolus concentration (g.L$^{-1}$)',size=5)
        ax1.set_ylabel('Normalized mean IBPS gradient' '',size=5)
        ax1.set_ylim([0,1.2])
        ax1.xaxis.labelpad = 10
#        pdb.set_trace()
#        plt.xticks([2*r  for r in range(N)], ['72', '104', '144'])
        plt.xticks([])
        
        xtickslocs=ax1.get_xticks()
        ymin, _ = ax1.get_ylim()
        
        ax1XtickLocinPixels=ax1.transData.transform([(xtick, ymin) for xtick in xtickslocs])
#        ax1XtickLocinPixels=ax1XtickLocinPixels/300;
        
        print(ax1XtickLocinPixels)
#        pdb.set_trace()
        
        ax1.annotate('72', xy=(0.2525, 0.07),xycoords='figure fraction', 
                     xytext=(0.2525,0.005), textcoords='figure fraction',
            fontsize=5, ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-[, widthB=3.8, lengthB=0.5', lw=0.5))
        
        ax1.annotate('108', xy=(0.5125, 0.07),xycoords='figure fraction', 
                     xytext=(0.5125,0.005), textcoords='figure fraction',
            fontsize=5, ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-[, widthB=3.8, lengthB=0.5', lw=0.5))
        
        ax1.annotate('144', xy=(0.7725, 0.07),xycoords='figure fraction', 
                     xytext=(0.7725,0.005), textcoords='figure fraction',
            fontsize=5, ha='center', va='bottom',
            arrowprops=dict(arrowstyle='-[, widthB=3.8, lengthB=0.5', lw=0.5))

        #(0.2525,0)
        #plt.yticks(np.arange(0, 81, 10))
        ax1.legend((p11a[0], p21a[0],p31a[0],p11b[0],p12b[0]), 
                   ('20 mm.s$^{-1}$', '30 mm.s$^{-1}$', '40 mm.s$^{-1}$','Without stent','With stent'),
#                   bbox_to_anchor=(0., 1.02, 1., .202),
                   ncol=1,
#                   mode="expand", 
                   borderaxespad=0,
                   handlelength=1,
                   labelspacing=0.1,
                   columnspacing=0.2,
                   loc=0)
        plt.show()
        
        return ax1
