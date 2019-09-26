# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:57:15 2019

@author: dbha483
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:45:13 2018

@author: dipankarbhattacharya
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.nonparametric.smoothers_lowess import lowess
from dateutil.parser import parse
from scipy.signal import find_peaks
plt.close("all")
import pdb

def cls():
    print('\n'*50)
#clear Console
cls()


class stent:
    def __init__(self, path,wavelength,speed,scalingFact,name,Bolustype='Dry'):
        self.path = path    # instance variable unique to each instance
        self.wavelength=wavelength
        self.speed=speed
        self.scalingFact=scalingFact
        self.Bolustype=Bolustype
        self.name=name
        os.chdir(self.path)
        self.df1=np.array([])
        self.df2=np.array([])
        self.df3=np.array([])
        self.df1Filter=np.array([])
        self.df2Filter=np.array([])
        self.df13Filter=np.array([])
        self.filename1=[]
        self.files=[]
        self.senCalData=np.zeros((1,4))
        self.LineCoeff=[]
    def find_all(self,name):
        self.files=[files[index] for root, dirs, files in sorted(os.walk(self.path)) for index in range(len(files)) if name in files[index]] 
    
    def CalDataReading(self,window):
        for file in self.files:
            df1=pd.read_csv(file, sep=',',header=None)
            self.df1=np.array(df1)
            self.senCalData=np.vstack((self.senCalData,self.df1))
        self.senCalData=self.senCalData[np.argsort(self.senCalData[:, 1])]
        
    def LineOfReg(self,deg,x,y):
        self.LineCoeff=np.poly1d(np.polyfit(x, y, deg))
        z=self.LineCoeff
        return z
#        self.senCalData=self.senCalData[window[0]:window[1],:]
    # Function to read files whose names ares stored in filename1
    def FileReading(self,indexFileToRead):
       if self.name=='Flex':
           self.filename1=[self.files[indexFileToRead[0]],self.files[indexFileToRead[1]],self.files[indexFileToRead[2]]]           
           print(self.filename1)
           df1=pd.read_csv(self.filename1[0], sep=',',header=None)
           self.df1=np.array(df1)
           df2=pd.read_csv(self.filename1[1], sep=',',header=None)
           self.df2=np.array(df2)
           df3=pd.read_csv(self.filename1[2], sep=',',header=None)
           self.df3=np.array(df3)
       elif self.name=='TOF':
           if len(indexFileToRead)==1:
               self.filename1=[self.files[indexFileToRead[0]]]
               df1=pd.read_csv(self.filename1[0], sep=',',header=None)
               self.df1=np.array(df1)
           elif len(indexFileToRead)==2:
    #           pdb.set_trace()
               self.filename1=[self.files[indexFileToRead[0]],self.files[indexFileToRead[1]]]
               df1=pd.read_csv(self.filename1[0], sep=',',header=None)
               self.df1=np.array(df1)
               df2=pd.read_csv(self.filename1[1], sep=',',header=None)
               self.df2=np.array(df2)
           elif len(indexFileToRead)==3:
               self.filename1=[self.files[indexFileToRead[0]],self.files[indexFileToRead[1]],self.files[indexFileToRead[2]]]
               df1=pd.read_csv(self.filename1[0], sep=',',header=None)
               self.df1=np.array(df1)
               df2=pd.read_csv(self.filename1[1], sep=',',header=None)
               self.df2=np.array(df2)
               df3=pd.read_csv(self.filename1[2], sep=',',header=None)
               self.df3=np.array(df3)   
           
          
    def FilterData(self,indexFileToRead):
           from scipy.signal import lfilter
           n = 20 # the larger n is, the smoother curve will be
           b = [1.0 / n] * n
           a = 1
           if len(indexFileToRead)==1:
               self.df1Filter = lfilter(b,a,self.df1[2,3]-self.df1[2:-1,3])
           elif len(indexFileToRead)==2:
               self.df1Filter = lfilter(b,a,self.df1[2,3]-self.df1[2:-1,3])
               self.df2Filter = lfilter(b,a,self.df2[2,3]-self.df2[2:-1,3])
           elif len(indexFileToRead)==3:
               self.df1Filter = lfilter(b,a,self.df1[2,3]-self.df1[2:-1,3])
               self.df2Filter = lfilter(b,a,self.df2[2,3]-self.df2[2:-1,3])
               self.df3Filter = lfilter(b,a,self.df2[2,3]-self.df3[2:-1,3])
               
    def FindPeak(self,height,window,distance,columnIndex=3):
#        pdb.set_trace()
        peakTimeList=[]
        peakList=[]
        peaks, peakHeights = find_peaks(self.df1[window[0]:window[1],columnIndex], height[0],distance)
        peakTime=self.df1[peaks,1]
        peakTimeList.append(peakTime)
        peakList.append(peaks)
        peakList.append(peakHeights)
        
        peaks, peakHeights = find_peaks(self.df2[window[2]:window[3],columnIndex], height[1],distance)
        peakTime=self.df2[peaks,1]
        peakTimeList.append(peakTime)
        peakList.append(peaks)
        peakList.append(peakHeights)
        
        peaks, peakHeights = find_peaks(self.df3[window[4]:window[5],columnIndex], height[2],distance)
        peakTime=self.df3[peaks,1]
        peakTimeList.append(peakTime)
        peakList.append(peaks)
        peakList.append(peakHeights)
        return peakTimeList,peakList
               
               
    def StentPlotting(self,indexFileToRead,SaveLoc,*PlotWindow):
#        pdb.set_trace()
        plt.rcParams['figure.figsize'] = (8.8, 4.0) # set default size of plots
        plt.rcParams['image.interpolation'] = 'nearest'
        plt.rcParams['image.cmap'] = 'gray'
        plt.figure()
        if self.name=='Flex':
            if len(indexFileToRead)==3:
                if not PlotWindow:  
#                    plt.hold(True)
                    plt.plot(self.df1[2:,0],(self.df1[2:,3]-np.mean(self.df1[2:,3])),'r-')
                    plt.plot(self.df2[2:,0],(self.df2[2:,3]-np.mean(self.df2[2:,3])),'g-')
                    plt.plot(self.df3[2:,0],(self.df3[2:1000,3]-np.mean(self.df3[2:1000,3])),'b-')
               
                else:
                    initial=PlotWindow[0][0]
                    final=PlotWindow[0][1]
                    plt.hold(True)
                    plt.plot(self.df1[initial:final,0],(self.df1[initial:final,3]-np.mean(self.df1[initial:final,3])),'r-')
                    plt.plot(self.df2[initial:final,0],(self.df2[initial:final,3]-np.mean(self.df2[initial:final,3])),'g-')
                    plt.plot(self.df3[initial:final,0],(self.df3[initial:final,3]-np.mean(self.df3[initial:final,3])),'b-')
               
        
        elif self.name=='TOF':
            if len(indexFileToRead)==1:
             
#               plt.hold(True)
               plt.plot(self.df1[2:,1],self.df1[2:,3]-self.df1[2,3],'bo-')
               plt.plot(self.df1[2:-3,1],-self.df1Filter[2:],linewidth=2, linestyle="-", c="r")  # smooth by filter
#               plt.hold(False)
               plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
               plt.ylabel('Stent migrartion (mm)',fontsize=10)
               plt.title(r'Horizontal Actuation for wavelength $\lambda$=60 mm and speed $c$=40mm/s',fontsize=10)
               plt.legend(['Unfiltered (Full occulsion)','Filtered (Full occulsion)'],loc='best')
               plt.savefig(SaveLoc,dpi=300)
            elif len(indexFileToRead)==2:
#               plt.hold(True)
               plt.plot(self.df1[2:,1],self.df1[2:,3]-self.df1[2,3],'bo-')
               plt.plot(self.df2[2:,1],self.df2[2:,3]-self.df2[2,3],'ko-')
               plt.plot(self.df1[2:-3,1],-self.df1Filter[2:],linewidth=2, linestyle="-", c="r")  # smooth by filter
               plt.plot(self.df2[2:-3,1],-self.df2Filter[2:],linewidth=2, linestyle="-", c="g")  # smooth by filter
#               plt.hold(False)
               plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
               plt.ylabel('Stent migrartion (mm)',fontsize=10)
               plt.title(r'Horizontal Actuation for wavelength $\lambda$=60 mm and speed $c$=40mm/s',fontsize=10)
               plt.legend(['Unfiltered (4 Scoops)','Unfiltered (8 Scoops)','Filtered (4 Scoops)',\
                           'Filtered (8 Scoops)'],loc='best')
               plt.savefig(SaveLoc,dpi=300)

# =============================================================================
# Time series analysis
 #Ref:https://www.machinelearningplus.com/time-series/time-series-analysis-python/                   
# =============================================================================
    def CreateDataframe(self,*Window,ColumnName=['Value1','Value2','Value3'],dataArray=np.array([])):
        initial=Window[0][0]
        final=Window[0][1]
        if len(dataArray)==0:  
            self.dataframe = pd.DataFrame({ColumnName[0]:self.df1[initial:final,1],
                                           ColumnName[1]:self.df2[initial:final,1],
                                           ColumnName[2]:self.df3[initial:final,1]})
            self.dataframe.index=pd.DatetimeIndex(freq="w",start=0,periods=final-initial)
            
    def SeasonalDecomposition(self,model):
        if model=='Multiplicative':
            # Multiplicative Decomposition 
            self.dataframeDecomposed = seasonal_decompose(self.dataframe[['ManometryReading1','ManometryReading2','ManometryReading3']], model='multiplicative',extrapolate_trend='freq')
        elif model=='Additive':
            # Additive Decomposition
            self.dataframeDecomposed = seasonal_decompose(self.dataframe[['ManometryReading1','ManometryReading2','ManometryReading3']], model='additive',extrapolate_trend='freq')

        # Plot
        plt.figure()
        plt.rcParams.update({'figure.figsize': (10,10)})
        self.dataframeDecomposed.plot().suptitle(model+'Decompose', fontsize=22)
        plt.show()

    def FilterData(self,MovAvgFilterOrder,LoessSmoothFact):
#            pdb.set_trace()
            # 1. Moving Average
            df_ma1 = self.dataframe.ManometryReading1.rolling(MovAvgFilterOrder, center=True, closed='both').mean()
            df_ma2 = self.dataframe.ManometryReading2.rolling(MovAvgFilterOrder, center=True, closed='both').mean()
            df_ma3 = self.dataframe.ManometryReading3.rolling(MovAvgFilterOrder, center=True, closed='both').mean()
            self.df_ma=pd.concat([df_ma1,df_ma2,df_ma3],axis=1)

            # 2. Loess Smoothing (5% and 15%)
            df_loess1 = pd.DataFrame(lowess(self.dataframe.ManometryReading1, np.arange(len(self.dataframe.ManometryReading1)), frac=LoessSmoothFact)[:, 1], index=self.dataframe.index, columns=['value'])
            df_loess2 = pd.DataFrame(lowess(self.dataframe.ManometryReading2, np.arange(len(self.dataframe.ManometryReading2)), frac=LoessSmoothFact)[:, 1], index=self.dataframe.index, columns=['value'])
            df_loess3 = pd.DataFrame(lowess(self.dataframe.ManometryReading3, np.arange(len(self.dataframe.ManometryReading3)), frac=LoessSmoothFact)[:, 1], index=self.dataframe.index, columns=['value'])
            self.df_loess=pd.concat([df_loess1,df_loess2,df_loess3],axis=1)
            
            fig, axes = plt.subplots(3,1, figsize=(7, 7), sharex=True, dpi=120)
            self.dataframe['ManometryReading1'].plot(ax=axes[0], color='k', title='Original Series')
            df_loess1['value'].plot(ax=axes[1], title='Loess Smoothed')
            df_ma1.plot(ax=axes[2], title='Moving Average (3)')
            fig.suptitle('Time Series FIlteration', y=0.95, fontsize=14)
            plt.show()