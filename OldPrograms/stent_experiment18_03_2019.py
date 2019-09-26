#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:45:13 2018

@author: dipankarbhattacharya
"""
import os
import pdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
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
        #Read all the files from the directory
#        for root, dirs, self.files in os.walk("."):
#            if 
#               print(self.files)
#        pdb.set_trace()
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
        self.files=[files[index] for root, dirs, files in os.walk(self.path) for index in range(len(files)) if name in files[index]] 
    
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
               
    def FindPeak(self,height):
#        pdb.set_trace()
        peakTimeList=[]
        peaks, peakHeights = find_peaks(self.df1[:,3], height[0])
        peakTime=self.df1[peaks,1]
        peakTimeList=peakTimeList.append(peakTime)
        
        peaks, peakHeights = find_peaks(self.df2[:,3], height[1])
        peakTime=self.df2[peaks,1]
        peakTimeList=peakTimeList.append(peakTime)
        
        peaks, peakHeights = find_peaks(self.df3[:,3], height[2])
        peakTime=self.df3[peaks,1]
        peakTimeList=peakTimeList.append(peakTime)
        return peakTimeList
               
               
    def StentPlotting(self,indexFileToRead,SaveLoc,*PlotWindow):
#        pdb.set_trace()
        plt.rcParams['figure.figsize'] = (8.8, 4.0) # set default size of plots
        plt.rcParams['image.interpolation'] = 'nearest'
        plt.rcParams['image.cmap'] = 'gray'
        plt.figure()
        if self.name=='Flex':
            if len(indexFileToRead)==3:
                if not PlotWindow:  
                    plt.hold(True)
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
             
               plt.hold(True)
               plt.plot(self.df1[2:,1],self.df1[2:,3]-self.df1[2,3],'bo-')
               plt.plot(self.df1[2:-3,1],-self.df1Filter[2:],linewidth=2, linestyle="-", c="r")  # smooth by filter
               plt.hold(False)
               plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
               plt.ylabel('Stent migrartion (mm)',fontsize=10)
               plt.title(r'Horizontal Actuation for wavelength $\lambda$=60 mm and speed $c$=40mm/s',fontsize=10)
               plt.legend(['Unfiltered (Full occulsion)','Filtered (Full occulsion)'],loc='best')
               plt.savefig(SaveLoc,dpi=300)
            elif len(indexFileToRead)==2:
               plt.hold(True)
               plt.plot(self.df1[2:,1],self.df1[2:,3]-self.df1[2,3],'bo-')
               plt.plot(self.df2[2:,1],self.df2[2:,3]-self.df2[2,3],'ko-')
               plt.plot(self.df1[2:-3,1],-self.df1Filter[2:],linewidth=2, linestyle="-", c="r")  # smooth by filter
               plt.plot(self.df2[2:-3,1],-self.df2Filter[2:],linewidth=2, linestyle="-", c="g")  # smooth by filter
               plt.hold(False)
               plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
               plt.ylabel('Stent migrartion (mm)',fontsize=10)
               plt.title(r'Horizontal Actuation for wavelength $\lambda$=60 mm and speed $c$=40mm/s',fontsize=10)
               plt.legend(['Unfiltered (4 Scoops)','Unfiltered (8 Scoops)','Filtered (4 Scoops)',\
                           'Filtered (8 Scoops)'],loc='best')
               plt.savefig(SaveLoc,dpi=300)

# =============================================================================
# Main program begins
# =============================================================================
# =============================================================================
#   Stent P1491_1             
# =============================================================================
#set path
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/DataStentP1491_1CDrySwallow/Set1UnionSet2"
name='Flex'
#path,wavelength,speed,scalingFact,name,Bolustype='Dry'
stent_P1491_1=stent(path,'50mm','30mmps',[1.5,2.0,2.2],name)
stent_P1491_1.find_all(name)
#[1,5,0,4,2,3]
indexFileToRead=[5,0,3]
stent_P1491_1.FileReading(indexFileToRead)
SaveLoc='/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/Plots/StentP1491_1.png'
stent_P1491_1.StentPlotting(indexFileToRead,SaveLoc,[350,400])

# =============================================================================
# Looping through all the stents
# =============================================================================
#stents=[2,4]
stentList=[]
#indexFileToRead=[[],[1,2],[],[0,3]]
#for NumOfStent in stents:
#    path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting17_03_19_Bolus/DataStentP1568_"+str(NumOfStent)+"CBolusSwallow"
#    stent_60mm=stent(path)
#    stent_60mm.find_all(name)
#    stent_60mm.FileReading(indexFileToRead[NumOfStent-1])
#    stent_60mm.FilterData(indexFileToRead[NumOfStent-1])
#    SaveLoc='/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting17_03_19_Bolus/Plots/StentP1568_'+str(NumOfStent)+'.png'
#    stent_60mm.StentPlotting(indexFileToRead[NumOfStent-1],SaveLoc)
#    stentList.append(stent_60mm)
#    stents={"StentP1568_"+str(NumOfStent):stentList[NumOfStent]}

# =============================================================================
# Flex sensor calibration for P1491_1C   
# =============================================================================
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/DataStentP1491_1CDrySwallow/Cal"
pathList=[path]
name='Flex'
#path,wavelength,speed,scalingFact,name,Bolustype='Dry'
FlexSenCal=stent(path,'50mm','30mmps',[1.5,2.0,2.2],name)
FlexSenCal.find_all(name)
FlexSenCal.CalDataReading([73,140])
plt.figure()

plt.plot(FlexSenCal.senCalData[2:,2],FlexSenCal.senCalData[2:,1],'ro')
#plt.plot(FlexSenCal.df1[2:,2],FlexSenCal.df1[2:,1],'bo-')
yy=FlexSenCal.senCalData[2:,1]#-np.mean(FlexSenCal.senCalData[2:,1])
xx=FlexSenCal.senCalData[2:,2]#-np.mean(FlexSenCal.senCalData[2:,2])
deg=1
z=FlexSenCal.LineOfReg(deg,xx,yy)
plt.plot(np.unique(xx), z(np.unique(xx)))

prediction=z.coef[0]*stent_P1491_1.df2[:,2:]+z.coef[1]
plt.figure()
plt.plot(prediction[:,1],'k-')


# =============================================================================
#   Stent P1568_1: Change in Actuation pressure
# =============================================================================
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/DataStentP1568_2CDrySwallow/FlexSensorReadings"
pathList.append(path)
name='Flex'
#path,wavelength,speed,scalingFact,name,Bolustype='Dry'
stent_P1568_1=stent(path,'50mm','40mmps',[1.5,2.0,2.5],name)
stent_P1568_1.find_all(name)
indexFileToRead=[0,1,2]
stent_P1568_1.FileReading(indexFileToRead)
SaveLoc='/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/Plots/StentP1568_1.png'
stent_P1568_1.StentPlotting(indexFileToRead,SaveLoc)
# =============================================================================
# Stent P1568_1: Change in peristalsis speed
# =============================================================================

path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/DataStentP1568_2CDrySwallow/OtherReadings"
pathList.append(path)
stent_P1568_1_50mm=stent(path,'50mm',['20mmps','30mmps','40mmps'],2.5,name)
stent_P1568_1_50mm.find_all(name)
indexFileToRead=[4,9,11]
stent_P1568_1_50mm.FileReading(indexFileToRead)
SaveLoc='/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/Plots/StentP1568_1.png'
stent_P1568_1_50mm.StentPlotting(indexFileToRead,SaveLoc)

#peakTime20mmps=stent_P1568_1_50mm.FindPeak([140,150,100])
#peakTime30mmps=stent_P1568_1_50mm.FindPeak(150)
#peakTime40mmps=stent_P1568_1_50mm.FindPeak(100)
# =============================================================================
# Stent P1568_4: Change in peristalsis speed
# =============================================================================
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/DataStentP1568_4CDrySwallow/FlexSensorReadings"
pathList.append(path)
name='Flex'
stent_P1568_4_50mm=stent(path,'50mm',['20mmps','30mmps','40mmps'],2.5,name)
stent_P1568_4_50mm.find_all(name)
indexFileToRead=[4,9,11]
stent_P1568_4_50mm.FileReading(indexFileToRead)
SaveLoc='/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/Plots/StentP1568_4.png'
stent_P1568_4_50mm.StentPlotting(indexFileToRead,SaveLoc)

path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/DataStentP1568_4CDrySwallow/FlexSensorReadings"
pathList.append(path)
name='Flex'
stent_P1568_4_60mm=stent(path,'60mm',['20mmps','30mmps','40mmps'],2.5,name)
stent_P1568_4_60mm.find_all(name)
indexFileToRead=[16,14,13]  #[0,7,15]
stent_P1568_4_60mm.FileReading(indexFileToRead)
SaveLoc='/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/Plots/StentP1568_4.png'
stent_P1568_4_60mm.StentPlotting(indexFileToRead,SaveLoc)