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
import pdb

def cls():
    print('\n'*50)
#clear Console
cls()


class stent:
    def __init__(self, path):
        self.path = path    # instance variable unique to each instance
        os.chdir(self.path)
        #Read all the files from the directory
        for root, dirs, self.files in os.walk("."):
           for filename in self.files: #not req as for now
               print(filename)
        #pdb.set_trace()
        self.df1=np.array([])
        self.df2=np.array([])
        self.df3=np.array([])
        self.df1Filter=np.array([])
        self.df2Filter=np.array([])
        self.df13Filter=np.array([])
        self.filename1=[]
    # Function to read files whose names ares stored in filename1
    def FileReading(self,indexFileToRead):
       #Import data from  the files
       #self.filename1=[self.files[indexFileToRead[0]],self.files[indexFileToRead[1]]]
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
           n = 8  # the larger n is, the smoother curve will be
           b = [1.0 / n] * n
           a = 1
           if len(indexFileToRead)==1:
               self.df1Filter = lfilter(b,a,self.df1[2,2]-self.df1[2:-1,2])
           elif len(indexFileToRead)==2:
               self.df1Filter = lfilter(b,a,self.df1[2,2]-self.df1[2:-1,2])
               self.df2Filter = lfilter(b,a,self.df2[2,2]-self.df2[2:-1,2])
           elif len(indexFileToRead)==3:
               self.df1Filter = lfilter(b,a,self.df1[2,2]-self.df1[2:-1,2])
               self.df2Filter = lfilter(b,a,self.df2[2,2]-self.df2[2:-1,2])
               self.df3Filter = lfilter(b,a,self.df2[2,2]-self.df3[2:-1,2])
##-----------Pressure Trajectory---------------------------------------------
              # We are determining the pressure trajectory of the 
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/AdcData" 
MaxPressApplied=500
AdcMaxOp=5
PressPerUnitVol=100
#5V in adc is represented by 255, thus step size is 0.019V
# 'y' value of Adc is 0.019y V
StepSize=0.0196
prestraj=stent(path) 
indexFileToRead=np.array([0,1]) 
#pdb.set_trace()
prestraj.FileReading(indexFileToRead)
prestraj.FilterData(indexFileToRead)  
plt.figure()
#plt.plot(prestraj.df2[3:400,2],'b',prestraj.df1[3:400,2],'r')
plt.hold(True)
tempVal=400
#,
time=np.linspace(0,400*0.125,401)
plt.plot(time,(-prestraj.df2Filter[1:tempVal+2]+65)*StepSize*PressPerUnitVol,'k-',time,(-prestraj.df1Filter[1:tempVal+2]+65)*StepSize*PressPerUnitVol,'g-')  # smooth by filter
plt.hold(False)
plt.xlabel(r'Time $t$',fontsize=10)
plt.ylabel('Pressure (kPa)',fontsize=10)
plt.title(r'Chamber Pressure Trajectory/s',fontsize=10)
plt.legend(['Filtered Pressure trajectory 1','Filtered Pressure trajectory 2'],loc='best')
plt.savefig('/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/Plots/PressureTraj.png',dpi=300)                
##-----------Stent 1---------------------------------------------
#set path
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/DataStentP1491C_1"
# stent 1 30mm
stent1_50mm=stent(path)
indexFileToRead=np.array([1,1])
## Stent 1, Wavelength =50mm
#plot the result
stent1_50mm.FileReading(indexFileToRead)
stent1_50mm.FilterData(indexFileToRead)
plt.figure()
plt.plot(stent1_50mm.df1[2:161,1],stent1_50mm.df1[2:161,2]-stent1_50mm.df1[2,2],'bo-')
plt.hold(True)
plt.plot(stent1_50mm.df1[2:158,1],-stent1_50mm.df1Filter[2:158],linewidth=2, linestyle="-", c="r")  # smooth by filter
plt.hold(False)
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'Actuation from top to bottom for wavelength $\lambda$=50 mm and speed $c$=30mm/s',fontsize=10)
plt.legend(['Unfiltered','Filtered'],loc='best')
plt.savefig('/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/Plots/StentP1491C_1.png',dpi=300)
##-----------Stent 2---------------------------------------------
#set path
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/DataStentP1491C_2"
# stent 2 30mm
stent2_50mm=stent(path)
indexFileToRead=np.array([3,6])
## Stent 2, Wavelength =50mm
#plot the result
stent2_50mm.FileReading(indexFileToRead)
stent2_50mm.FilterData(indexFileToRead)
plt.figure()
plt.plot(stent2_50mm.df1[2:161,1],stent2_50mm.df1[2:161,2]-stent2_50mm.df1[2,2],'bo-',stent2_50mm.df2[2:161,1],stent2_50mm.df2[2:161,2]-stent2_50mm.df2[2,2],'ro-')
plt.hold(True)
plt.plot(stent2_50mm.df1[2:50,1],-stent2_50mm.df1Filter[2:50],linewidth=2, linestyle="-", c="c")  # smooth by filter
plt.plot(stent2_50mm.df2[2:69,1],-stent2_50mm.df2Filter[2:69],linewidth=2, linestyle="-", c="g")  # smooth by filter
plt.hold(False)
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'Actuation from top to bottom for wavelength $\lambda$=50 mm and speed $c$=30mm/s',fontsize=10)
plt.legend(['Unfiltered for pressure ','Unfiltered for pressure ','Filtered for pressure','Filtered for pressure'],loc='best')
plt.savefig('/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/Plots/StentP1491C_2.png',dpi=300)
##-----------Stent 3---------------------------------------------
#set path
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/DataStentP1491C_3"
# stent 3 30mm
stent3_50mm=stent(path)
indexFileToRead=np.array([0,15])
## Stent 3, Wavelength =50mm
#plot the result
stent3_50mm.FileReading(indexFileToRead)
stent3_50mm.FilterData(indexFileToRead)
plt.figure()
plt.plot(stent3_50mm.df1[2:51,1],stent3_50mm.df1[2:51,2]-stent3_50mm.df1[2,2],'bo-',stent3_50mm.df2[2:169,1],stent3_50mm.df2[2:169,2]-stent3_50mm.df2[2,2],'ro-')
plt.hold(True)
plt.plot(stent3_50mm.df1[0:50,1],-stent3_50mm.df1Filter[0:50],linewidth=2, linestyle="-", c="c")  # smooth by filter
plt.plot(stent3_50mm.df2[0:50,1],-stent3_50mm.df2Filter[0:50],linewidth=2, linestyle="-", c="g")  # smooth by filter
plt.hold(False)
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'Actuation from top to bottom for wavelength $\lambda$=50 mm and speed $c$=30mm/s',fontsize=10)
plt.legend(['Unfiltered for pressure ','Unfiltered for pressure ','Filtered for pressure','Filtered for pressure'],loc='best')
plt.savefig('/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/Plots/StentP1491C_3.png',dpi=300)


##-----------Stent 4---------------------------------------------
#set path
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/DataStentP1491C_4"
# stent 4 30mm
stent4_50mm=stent(path)
indexFileToRead=np.array([8,6])
## Stent 2, Wavelength =50mm
#plot the result
stent4_50mm.FileReading(indexFileToRead)
stent4_50mm.FilterData(indexFileToRead)
plt.figure()
plt.plot(stent4_50mm.df1[2:51,1],stent4_50mm.df1[2:51,2]-stent4_50mm.df1[2,2],'bo-',stent4_50mm.df2[2:169,1],stent4_50mm.df2[2:169,2]-stent4_50mm.df2[2,2],'ro-')
plt.hold(True)
plt.plot(stent4_50mm.df1[0:48,1],-stent4_50mm.df1Filter[0:48],linewidth=2, linestyle="-", c="c")  # smooth by filter
plt.plot(stent4_50mm.df2[0:167,1],-stent4_50mm.df2Filter[0:167],linewidth=2, linestyle="-", c="g")  # smooth by filter
plt.hold(False)
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'Actuation from top to bottom for wavelength $\lambda$=50 mm and speed $c$=30mm/s',fontsize=10)
plt.legend(['Unfiltered for pressure ','Unfiltered for pressure ','Filtered for pressure','Filtered for pressure'],loc='best')
plt.savefig('/Users/dipankarbhattacharya/Documents/Spyder Python/StentTesting21_01_19/Plots/StentP1491C_4.png',dpi=300)
