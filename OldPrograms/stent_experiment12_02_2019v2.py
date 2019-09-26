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
plt.close("all")
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
#        for root, dirs, self.files in os.walk("."):
#            if 
#               print(self.files)
        #pdb.set_trace()
        self.df1=np.array([])
        self.df2=np.array([])
        self.df3=np.array([])
        self.df1Filter=np.array([])
        self.df2Filter=np.array([])
        self.df13Filter=np.array([])
        self.filename1=[]
        self.files=[]
        
    def find_all(self,name):
        self.files=[files[index] for root, dirs, files in os.walk(self.path) for index in range(len(files)) if name in files[index]] 
        
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
           n = 20 # the larger n is, the smoother curve will be
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
               
               
    def StentPlotting(self,indexFileToRead,SaveLoc):
        plt.rcParams['figure.figsize'] = (8.8, 4.0) # set default size of plots
        plt.rcParams['image.interpolation'] = 'nearest'
        plt.rcParams['image.cmap'] = 'gray'
        plt.figure()
        if len(indexFileToRead)==1:
         
           plt.hold(True)
           plt.plot(self.df1[2:,1],self.df1[2:,2]-self.df1[2,2],'bo-')
           plt.plot(self.df1[2:-3,1],-self.df1Filter[2:],linewidth=2, linestyle="-", c="r")  # smooth by filter
           plt.hold(False)
           plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
           plt.ylabel('Stent migrartion (mm)',fontsize=10)
           plt.title(r'Actuation from top to bottom for wavelength $\lambda$=50 mm and speed $c$=30mm/s',fontsize=10)
           plt.legend(['Unfiltered (Full occulsion)','Filtered (Full occulsion)'],loc='best')
           plt.savefig(SaveLoc,dpi=300)
        elif len(indexFileToRead)==2:
           plt.hold(True)
           plt.plot(self.df1[2:,1],self.df1[2:,2]-self.df1[2,2],'bo-')
           plt.plot(self.df2[2:,1],self.df2[2:,2]-self.df2[2,2],'ko-')
           plt.plot(self.df1[2:-3,1],-self.df1Filter[2:],linewidth=2, linestyle="-", c="r")  # smooth by filter
           plt.plot(self.df2[2:-3,1],-self.df2Filter[2:],linewidth=2, linestyle="-", c="g")  # smooth by filter
           plt.hold(False)
           plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
           plt.ylabel('Stent migrartion (mm)',fontsize=10)
           plt.title(r'Actuation from top to bottom for wavelength $\lambda$=50 mm and speed $c$=30mm/s',fontsize=10)
           plt.legend(['Unfiltered (Half occulsion)','Unfiltered (Full occulsion)','Filtered (Half occulsion)',\
                       'Filtered (Full occulsion)'],loc='best')
           plt.savefig(SaveLoc,dpi=300)
##-----------Stent 2---------------------------------------------
##-----------Stent 1---------------------------------------------
#set path
           
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting12_02_2019/DataStentP1568_1"
name='TOF'

# =============================================================================
# Looping through all the stents
# =============================================================================
stentList=[]
indexFileToRead=[[1,0],[0,1],[0,1],[0],[0]]
for NumOfStent in range(5):
    path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting12_02_2019/DataStentP1568_"+str(NumOfStent+1)
    stent_50mm=stent(path)
    stent_50mm.find_all(name)
    stent_50mm.FileReading(indexFileToRead[NumOfStent])
    stent_50mm.FilterData(indexFileToRead[NumOfStent])
    SaveLoc='/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting12_02_2019/Plots/StentP1568_'+str(NumOfStent+1)+'.png'
    stent_50mm.StentPlotting(indexFileToRead[NumOfStent],SaveLoc)
    stentList.append(stent_50mm)
    stents={"StentP1568_"+str(NumOfStent+1):stentList[NumOfStent]}
    
#stents={"StentP1568_1":stentList[0],
#        "StentP1568_2":stentList[1],
#        "StentP1568_3":stentList[2],
#        "StentP1568_4":stentList[3],
#        "StentP1568_5":stentList[4]}
