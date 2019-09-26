#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:47:55 2019

@author: dipankarbhattacharya
"""
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
from ClassStent import stent



def cls():
    print('\n'*50)
#clear Console
cls()

class stentManometry(stent):
#    When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    def __init__(self, path,wavelength,speed,scalingFact,name,Bolustype='Dry'):
#The child's __init__() function overrides the inheritance of the parent's __init__() function.        
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:        
         stent.__init__(self,path,wavelength,speed,scalingFact,name,Bolustype='Dry')
#Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
         self.ihList=list()
         self.ihHexList=list()
         self.ihHexList2byte=list()
         self.ihHexList2byte2Int=list()    
         self.ihHexList2byteReverse=list()
         self.ihHexListRev2byte2Int=list()  
         self.ihArrayRevReshaped=np.array([])
# =============================================================================
# Method: Read Intel hex files and create a list containing each byte in sequential order
# =============================================================================         
    def FileReading(self,indexFileToRead):
        if self.name=='Manometry':
           self.filename1=[self.files[indexFileToRead[0]]]#,self.files[indexFileToRead[1]],self.files[indexFileToRead[2]]]           
           print(self.filename1)
           ih=IntelHex(self.filename1[0])
           
           for ii in range(len(ih)):
               self.ihList.append(ih[ii])
               self.ihHexList.append(hex(self.ihList[ii]))
               if len(self.ihHexList[ii])==3:
                   self.ihHexList[ii]=self.ihHexList[ii]+'0'

# =============================================================================
# Method :Create a list such that each item contains 2 byte
# =============================================================================
    def CreateList2byte(self):                                       
        jj=0     
        for ii in range(len(self.ihHexList)):
            if ii%2==0:
                self.ihHexList2byte.append(self.ihHexList[ii]+self.ihHexList[ii+1][2:4])
                self.ihHexList2byte2Int.append(int(self.ihHexList2byte[jj],16))
                jj+=1
                
# =============================================================================
# Reverse the bytes and generate a list containing its equivalant unsigned integer value
# =============================================================================
    def CreateListRev2byte2Int(self):
        for ii in range(len(self.ihHexList2byte)):
                temp=self.ihHexList2byte[ii][2:4]
                self.ihHexList2byteReverse.append('0x'+self.ihHexList2byte[ii][4:6]+temp)
                self.ihHexListRev2byte2Int.append(int(self.ihHexList2byteReverse[ii],16))
                                                    
# =============================================================================
# Create a numpy array and reshape it      
# =============================================================================
    def CreateArrayRevReshaped(self,NumOfCol):
        self.ihArrayRevReshaped=np.array(self.ihHexListRev2byte2Int)/10000
        self.ihArrayRevReshaped=np.reshape(self.ihArrayRevReshaped, (int(len(self.ihArrayRevReshaped)/NumOfCol), NumOfCol))
        temp=np.linspace(0,self.ihArrayRevReshaped.shape[0]-1,self.ihArrayRevReshaped.shape[0])  
#        pdb.set_trace()                                          
        self.df2=np.vstack((temp,self.ihArrayRevReshaped[:,2])).T  
        self.df3=np.vstack((temp,self.ihArrayRevReshaped[:,3])).T  
        self.df1=np.vstack((temp,self.ihArrayRevReshaped[:,1])).T 
# =============================================================================
#  Find prominemnce of the peaks       
# =============================================================================
        
    def FindProminencePEaks(self,window,peak):
#        pdb.set_trace()
        prominences1 = peak_prominences(self.df1[window[0]:window[1],1], peak[0])[0]
        prominences2 = peak_prominences(self.df2[window[0]:window[1],1], peak[2])[0]
        prominences3 = peak_prominences(self.df3[window[0]:window[1],1], peak[4])[0]
        prominences  = [prominences1,prominences2,prominences3]

        return prominences
# =============================================================================
# Design arrays which contains mean, and sd of the cycles having the prominent peaks        
# =============================================================================
    def CalMeanArrayAndSD(self,window,peak,prominences,prominenceVal=[1,1,1],offset=300):

        peak[0]=peak[0][prominences[0]>prominenceVal[0]]
        peak[2]=peak[2][prominences[1]>prominenceVal[1]]
        peak[4]=peak[4][prominences[2]>prominenceVal[2]]
        
        cycleArray1=np.array([peak[0]-offset+window[0],peak[0]+offset+window[0]]).T
        cycleArray2=np.array([peak[2]-offset+window[0],peak[2]+offset+window[0]]).T
        cycleArray3=np.array([peak[4]-offset+window[0],peak[4]+offset+window[0]]).T
        #stent_P1568_4_Mano_8scoop.StentPlotting([2],SaveLoc,cycleArray[14])
        
        df1MeanArray=np.zeros((1,2*offset))
        df2MeanArray=np.zeros((1,2*offset))
        df3MeanArray=np.zeros((1,2*offset))
#        pdb.set_trace()
        
        #For random sampling
        randseq1=random.sample(list(cycleArray1), 10)
        randseq2=random.sample(list(cycleArray2), 10)
        randseq3=random.sample(list(cycleArray3), 10)
        
        for jj in range(10):
#            temp1=np.array([self.df1[cycleArray1[jj,0]:cycleArray1[jj,1],1]])
#            temp2=np.array([self.df2[cycleArray2[jj,0]:cycleArray2[jj,1],1]])
#            temp3=np.array([self.df3[cycleArray3[jj,0]:cycleArray3[jj,1],1]])
            
            temp1=np.array([self.df1[randseq1[jj][0]:randseq1[jj][1],1]])
            temp2=np.array([self.df1[randseq2[jj][0]:randseq2[jj][1],1]])
            temp3=np.array([self.df1[randseq3[jj][0]:randseq3[jj][1],1]])

            
            df1MeanArray=np.vstack((df1MeanArray,temp1))
            df2MeanArray=np.vstack((df2MeanArray,temp2))
            df3MeanArray=np.vstack((df3MeanArray,temp3))
            

        df1MeanArray=df1MeanArray[1:,:]
        df2MeanArray=df2MeanArray[1:,:]
        df3MeanArray=df3MeanArray[1:,:]

        df1Mean=np.mean(df1MeanArray,axis=0)
        df2Mean=np.mean(df2MeanArray,axis=0)
        df3Mean=np.mean(df3MeanArray,axis=0)
        self.dfMeanArray=[df1Mean,df2Mean,df3Mean]
        
        df1SD=np.std(df1MeanArray,axis=0)
        df2SD=np.std(df2MeanArray,axis=0)
        df3SD=np.std(df3MeanArray,axis=0)
        self.dfSD=[df1SD,df2SD,df3SD]


    def StentPlotting(self,indexFileToRead,SaveLoc,*PlotWindow):
        plt.rcParams['figure.figsize'] = (8.8, 4.0) # set default size of plots
        plt.rcParams['image.interpolation'] = 'nearest'
        plt.rcParams['image.cmap'] = 'gray'
        plt.figure()
        if self.name=='Manometry':
            if len(indexFileToRead)==1:
                if not PlotWindow:  
                    plt.hold(True)
                    plt.plot(self.df1[2:,0],(self.df1[2:,3]),'r-')
                    plt.plot(self.df2[2:,0],(self.df2[2:,3]),'g-')
                    plt.plot(self.df3[2:,0],(self.df3[2:1000,3]),'b-')
               
                else:
                    initial=PlotWindow[0][0]
                    final=PlotWindow[0][1]
                    plt.subplot(311)
                    plt.plot(self.df1[initial:final,0],(self.df1[initial:final,1]),'r-')
                    plt.subplot(312)
                    plt.plot(self.df2[initial:final,0],(self.df2[initial:final,1]),'g-')
                    plt.subplot(313)
                    plt.plot(self.df3[initial:final,0],(self.df3[initial:final,1]),'b-')



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
path=GenPath+"Dipankar_Manometry_Stent_P1568_4"
name='Manometry'

# =============================================================================
# =============================================================================
# # stent_P1568_4
# =============================================================================
# =============================================================================

# =============================================================================
# stent_P1568_4:Dry swallow
# =============================================================================
#%%
stent_P1568_4_Mano_Dry=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1568_4_Mano_Dry.find_all(name)
stent_P1568_4_Mano_Dry.FileReading([11])
stent_P1568_4_Mano_Dry.CreateList2byte()
stent_P1568_4_Mano_Dry.CreateListRev2byte2Int()
stent_P1568_4_Mano_Dry.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'Plots/StentP1568_4_Mano_8sccop.png'
#stent_P1568_4_Mano_Dry.StentPlotting([11],SaveLoc,[10000,20000])

#Peak Analysis
peakTime, peak=stent_P1568_4_Mano_Dry.FindPeak([4.0,4.6,4.2],[10000,20000,10000,20000,10000,20000],0,1)
prominences=stent_P1568_4_Mano_Dry.FindProminencePEaks([10000,20000],peak)
stent_P1568_4_Mano_Dry.CalMeanArrayAndSD([10000,20000],peak,prominences,[0.4,1,0.0005],300)

TimeArray=0.05*np.linspace(0,len(stent_P1568_4_Mano_Dry.dfMeanArray[0])-1,len(stent_P1568_4_Mano_Dry.dfMeanArray[0]))
stent_P1568_4_Mano_Dry.df1=np.array([TimeArray,stent_P1568_4_Mano_Dry.dfMeanArray[0]]).T
stent_P1568_4_Mano_Dry.df2=np.array([TimeArray,stent_P1568_4_Mano_Dry.dfMeanArray[1]]).T
stent_P1568_4_Mano_Dry.df3=np.array([TimeArray,stent_P1568_4_Mano_Dry.dfMeanArray[2]]).T
#%%
#stent_P1568_4_Mano_Dry.StentPlotting([2],SaveLoc,[0,600])
# =============================================================================
# stent_P1568_4:4 Scoop
# =============================================================================

Bolustype='4Scoop'
stent_P1568_4_Mano_4scoop=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1568_4_Mano_4scoop.find_all(name)
stent_P1568_4_Mano_4scoop.FileReading([0])
stent_P1568_4_Mano_4scoop.CreateList2byte()
stent_P1568_4_Mano_4scoop.CreateListRev2byte2Int()
stent_P1568_4_Mano_4scoop.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'StentP1568_4_Mano_8sccop.png'
#stent_P1568_4_Mano_4scoop.StentPlotting([0],SaveLoc,[1000,10000])

#Peak Analysis
peakTime, peak=stent_P1568_4_Mano_4scoop.FindPeak([4.0,4,4.2],[1000,10000,1000,10000,1000,10000],0,1)
prominences=stent_P1568_4_Mano_4scoop.FindProminencePEaks([1000,10000],peak)
stent_P1568_4_Mano_4scoop.CalMeanArrayAndSD([1000,9000],peak,prominences,[1,1,0.0005],300)

TimeArray=0.05*np.linspace(0,len(stent_P1568_4_Mano_4scoop.dfMeanArray[0])-1,len(stent_P1568_4_Mano_4scoop.dfMeanArray[0]))
stent_P1568_4_Mano_4scoop.df1=np.array([TimeArray,stent_P1568_4_Mano_4scoop.dfMeanArray[0]]).T
stent_P1568_4_Mano_4scoop.df2=np.array([TimeArray,stent_P1568_4_Mano_4scoop.dfMeanArray[1]]).T
stent_P1568_4_Mano_4scoop.df3=np.array([TimeArray,stent_P1568_4_Mano_4scoop.dfMeanArray[2]]).T
#stent_P1568_4_Mano_4scoop.StentPlotting([2],SaveLoc,[0,600])
# =============================================================================
# stent_P1568_4:8 Scoop
# =============================================================================
Bolustype='8Scoop'
stent_P1568_4_Mano_8scoop=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1568_4_Mano_8scoop.find_all(name)
stent_P1568_4_Mano_8scoop.FileReading([2])
stent_P1568_4_Mano_8scoop.CreateList2byte()
stent_P1568_4_Mano_8scoop.CreateListRev2byte2Int()
stent_P1568_4_Mano_8scoop.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'Plots/StentP1568_4_Mano_8sccop.png'
#stent_P1568_4_Mano_8scoop.StentPlotting([2],SaveLoc,[1000,10000])

#Peak Analysis
peakTime, peak=stent_P1568_4_Mano_8scoop.FindPeak([4.3,4.3,4],[1000,10000,1000,10000,1000,10000],0,1)
prominences=stent_P1568_4_Mano_8scoop.FindProminencePEaks([1000,10000],peak)
stent_P1568_4_Mano_8scoop.CalMeanArrayAndSD([1000,10000],peak,prominences,[1,1,0.1],300)
TimeArray=0.05*np.linspace(0,len(stent_P1568_4_Mano_8scoop.dfMeanArray[0])-1,len(stent_P1568_4_Mano_8scoop.dfMeanArray[0]))
stent_P1568_4_Mano_8scoop.df1=np.array([TimeArray,stent_P1568_4_Mano_8scoop.dfMeanArray[0]]).T
stent_P1568_4_Mano_8scoop.df2=np.array([TimeArray,stent_P1568_4_Mano_8scoop.dfMeanArray[1]]).T
stent_P1568_4_Mano_8scoop.df3=np.array([TimeArray,stent_P1568_4_Mano_8scoop.dfMeanArray[2]]).T
#stent_P1568_4_Mano_8scoop.StentPlotting([2],SaveLoc,[0,600])
    
    
# =============================================================================
# Time Series Analysis
# =============================================================================

stent_P1568_4_Mano_Dry.CreateDataframe([0,600],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
#stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
stent_P1568_4_Mano_Dry.FilterData(6,0.01)

stent_P1568_4_Mano_4scoop.CreateDataframe([0,600],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
#stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
stent_P1568_4_Mano_4scoop.FilterData(6,0.01)

stent_P1568_4_Mano_8scoop.CreateDataframe([0,600],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
#stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
stent_P1568_4_Mano_8scoop.FilterData(6,0.01)


# =============================================================================
# =============================================================================
# # stent_P1568_2
# =============================================================================
# =============================================================================

# =============================================================================
# stent_P1568_2:Dry swallow
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1568_2"
stent_P1568_2_Mano_Dry=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1568_2_Mano_Dry.find_all(name)
stent_P1568_2_Mano_Dry.FileReading([1])
stent_P1568_2_Mano_Dry.CreateList2byte()
stent_P1568_2_Mano_Dry.CreateListRev2byte2Int()
stent_P1568_2_Mano_Dry.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'Plots/StentP1568_4_Mano_8sccop.png' 
#stent_P1568_2_Mano_Dry.StentPlotting([1],SaveLoc,[5000,15000])

#Peak Analysis
peakTime, peak=stent_P1568_2_Mano_Dry.FindPeak([4.3,4.3,4],[5000,15000,5000,15000,5000,15000],0,1)
prominences=stent_P1568_2_Mano_Dry.FindProminencePEaks([5000,15000],peak)
stent_P1568_2_Mano_Dry.CalMeanArrayAndSD([1000,10000],peak,prominences,[1,1,1],300)
TimeArray=0.05*np.linspace(0,len(stent_P1568_2_Mano_Dry.dfMeanArray[0])-1,len(stent_P1568_2_Mano_Dry.dfMeanArray[0]))
stent_P1568_2_Mano_Dry.df1=np.array([TimeArray,stent_P1568_2_Mano_Dry.dfMeanArray[0]]).T
stent_P1568_2_Mano_Dry.df2=np.array([TimeArray,stent_P1568_2_Mano_Dry.dfMeanArray[1]]).T
stent_P1568_2_Mano_Dry.df3=np.array([TimeArray,stent_P1568_2_Mano_Dry.dfMeanArray[2]]).T
#stent_P1568_2_Mano_Dry.StentPlotting([2],SaveLoc,[0,600])

# =============================================================================
# stent_P1568_2:4Scoop
# =============================================================================
Bolustype='4Scoop'
stent_P1568_2_Mano_4scoop=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1568_2_Mano_4scoop.find_all(name)
stent_P1568_2_Mano_4scoop.FileReading([3])
stent_P1568_2_Mano_4scoop.CreateList2byte()
stent_P1568_2_Mano_4scoop.CreateListRev2byte2Int()
stent_P1568_2_Mano_4scoop.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'StentP1568_4_Mano_8sccop.png'
#stent_P1568_2_Mano_4scoop.StentPlotting([3],SaveLoc,[10000,20000])

#Peak Analysis
peakTime, peak=stent_P1568_2_Mano_4scoop.FindPeak([4.0,4.3,4],[10000,20000,10000,20000,10000,20000],0,1)
prominences=stent_P1568_2_Mano_4scoop.FindProminencePEaks([10000,20000],peak)
stent_P1568_2_Mano_4scoop.CalMeanArrayAndSD([10000,20000],peak,prominences,[1,1,1],300)
TimeArray=0.05*np.linspace(0,len(stent_P1568_2_Mano_4scoop.dfMeanArray[0])-1,len(stent_P1568_2_Mano_4scoop.dfMeanArray[0]))
stent_P1568_2_Mano_4scoop.df1=np.array([TimeArray,stent_P1568_2_Mano_4scoop.dfMeanArray[0]]).T
stent_P1568_2_Mano_4scoop.df2=np.array([TimeArray,stent_P1568_2_Mano_4scoop.dfMeanArray[1]]).T
stent_P1568_2_Mano_4scoop.df3=np.array([TimeArray,stent_P1568_2_Mano_4scoop.dfMeanArray[2]]).T
#stent_P1568_2_Mano_4scoop.StentPlotting([2],SaveLoc,[0,600])

# =============================================================================
# stent_P1568_2:8 Scoop
# =============================================================================
Bolustype='8Scoop'
stent_P1568_2_Mano_8scoop=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1568_2_Mano_8scoop.find_all(name)
stent_P1568_2_Mano_8scoop.FileReading([2])
stent_P1568_2_Mano_8scoop.CreateList2byte()
stent_P1568_2_Mano_8scoop.CreateListRev2byte2Int()
stent_P1568_2_Mano_8scoop.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'Plots/StentP1568_4_Mano_8sccop.png'
#stent_P1568_2_Mano_8scoop.StentPlotting([2],SaveLoc,[5000,15000])

#Peak Analysis
peakTime, peak=stent_P1568_2_Mano_8scoop.FindPeak([4.0,4.3,4],[5000,15000,5000,15000,5000,15000],0,1)
prominences=stent_P1568_2_Mano_8scoop.FindProminencePEaks([5000,15000],peak)
stent_P1568_2_Mano_8scoop.CalMeanArrayAndSD([5000,15000],peak,prominences,[1,1,1],300)
TimeArray=0.05*np.linspace(0,len(stent_P1568_2_Mano_8scoop.dfMeanArray[0])-1,len(stent_P1568_2_Mano_8scoop.dfMeanArray[0]))
stent_P1568_2_Mano_8scoop.df1=np.array([TimeArray,stent_P1568_2_Mano_8scoop.dfMeanArray[0]]).T
stent_P1568_2_Mano_8scoop.df2=np.array([TimeArray,stent_P1568_2_Mano_8scoop.dfMeanArray[1]]).T
stent_P1568_2_Mano_8scoop.df3=np.array([TimeArray,stent_P1568_2_Mano_8scoop.dfMeanArray[2]]).T
#stent_P1568_2_Mano_8scoop.StentPlotting([2],SaveLoc,[0,600])

# =============================================================================
# Time Series Analysis
# =============================================================================

stent_P1568_2_Mano_Dry.CreateDataframe([0,600],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
#stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
stent_P1568_2_Mano_Dry.FilterData(6,0.01)

stent_P1568_2_Mano_4scoop.CreateDataframe([0,600],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
#stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
stent_P1568_2_Mano_4scoop.FilterData(6,0.01)

stent_P1568_2_Mano_8scoop.CreateDataframe([0,600],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
#stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
stent_P1568_2_Mano_8scoop.FilterData(6,0.01)



# =============================================================================
# =============================================================================
# # stent_P1491_1
# =============================================================================
# =============================================================================


# =============================================================================
# stent_P1491_1:Dry swallow
# =============================================================================
path=GenPath+"Dipankar_Manometry_Stent_P1491_1"
name='Manometry'



stent_P1491_1_Mano_Dry=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1491_1_Mano_Dry.find_all(name)
stent_P1491_1_Mano_Dry.FileReading([3])
stent_P1491_1_Mano_Dry.CreateList2byte()
stent_P1491_1_Mano_Dry.CreateListRev2byte2Int()
stent_P1491_1_Mano_Dry.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'Plots/StentP1491_4_Mano_Dry.png'
#stent_P1491_1_Mano_Dry.StentPlotting([6],SaveLoc,[17500,18000])

# =============================================================================
# stent_P1491_1:4 Scoop
# =============================================================================
stent_P1491_1_Mano_4scoop=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1491_1_Mano_4scoop.find_all(name)
stent_P1491_1_Mano_4scoop.FileReading([2])
stent_P1491_1_Mano_4scoop.CreateList2byte()
stent_P1491_1_Mano_4scoop.CreateListRev2byte2Int()
stent_P1491_1_Mano_4scoop.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'Plots/StentP1491_4_Mano_4sccop.png'
#stent_P1491_1_Mano_4scoop.StentPlotting([2],SaveLoc,[10500,10700])


# =============================================================================
# stent_P1491_1:6 Scoop
# =============================================================================
stent_P1491_1_Mano_6scoop=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1491_1_Mano_6scoop.find_all(name)
stent_P1491_1_Mano_6scoop.FileReading([0])
stent_P1491_1_Mano_6scoop.CreateList2byte()
stent_P1491_1_Mano_6scoop.CreateListRev2byte2Int()
stent_P1491_1_Mano_6scoop.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'Plots/StentP1491_4_Mano_6sccop.png'
#stent_P1491_1_Mano_6scoop.StentPlotting([0],SaveLoc,[12700,13000])
#
# =============================================================================
# stent_P1491_1:8 Scoop
# =============================================================================
stent_P1491_1_Mano_8scoop=stentManometry(path,'60mm','40mmps',[2.5],name)
stent_P1491_1_Mano_8scoop.find_all(name)
stent_P1491_1_Mano_8scoop.FileReading([1])
stent_P1491_1_Mano_8scoop.CreateList2byte()
stent_P1491_1_Mano_8scoop.CreateListRev2byte2Int()
stent_P1491_1_Mano_8scoop.CreateArrayRevReshaped(6)

SaveLoc=GenPath+'Plots/StentP1491_4_Mano_8sccop.png'
#stent_P1491_1_Mano_8scoop.StentPlotting([1],SaveLoc,[10300,10500])

## =============================================================================
## Time Series Analysis
## =============================================================================
#
#stent_P1491_1_Mano_4scoop.CreateDataframe([11800,12100],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
##stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
#stent_P1491_1_Mano_4scoop.FilterData(6,0.01)
#
#stent_P1491_1_Mano_6scoop.CreateDataframe([14100,14400],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
##stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
#stent_P1491_1_Mano_6scoop.FilterData(6,0.01)
#
#stent_P1491_1_Mano_8scoop.CreateDataframe([13000,13300],ColumnName=['ManometryReading1','ManometryReading2','ManometryReading3'])
##stent_P1568_4_Mano_8scoop.SeasonalDecomposition('Multiplicative')
#stent_P1491_1_Mano_8scoop.FilterData(6,0.01)
##
# =============================================================================
#%% Plotting together
# =============================================================================
#%%
#fig.suptitle('Time Series FIlteration', y=0.95, fontsize=14)
#plt.show()
plt.figure()
stent_P1568_2_Mano_Dry.dataframe['ManometryReading1'].plot(color='r', title='Original Series')
stent_P1568_2_Mano_4scoop.dataframe['ManometryReading1'].plot(color='g', title='Original Series')
stent_P1568_2_Mano_8scoop.dataframe['ManometryReading1'].plot(color='b', title='Original Series')

plt.figure()
stent_P1568_2_Mano_Dry.dataframe['ManometryReading2'].plot(color='r', title='Original Series')
stent_P1568_2_Mano_4scoop.dataframe['ManometryReading2'].plot(color='g', title='Original Series')
stent_P1568_2_Mano_8scoop.dataframe['ManometryReading2'].plot(color='b', title='Original Series')

plt.figure()
stent_P1568_2_Mano_Dry.dataframe['ManometryReading3'].plot(color='r', title='Original Series')
stent_P1568_2_Mano_4scoop.dataframe['ManometryReading3'].plot(color='g', title='Original Series')
stent_P1568_2_Mano_8scoop.dataframe['ManometryReading3'].plot(color='b', title='Original Series')
#%%
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
#%% P1491_1 Plots
plt.figure()
#plt.hold(True)
plt.plot(stent_P1491_1_Mano_4scoop.df1[11800:12100,1])

plt.plot(stent_P1491_1_Mano_6scoop.df1[14100:14400,1])

plt.plot(stent_P1491_1_Mano_8scoop.df1[13000:13300,1])
plt.legend(['4 scoops',\
            '6 scoops',
            '8 scoops']) 

plt.figure()
#plt.hold(True)
plt.plot(stent_P1491_1_Mano_4scoop.df2[11800:12100,1])

plt.plot(stent_P1491_1_Mano_6scoop.df2[14100:14400,1])

plt.plot(stent_P1491_1_Mano_8scoop.df2[13000:13300,1])
plt.legend(['4 scoops',\
            '6 scoops',
            '8 scoops'])  



plt.figure()
#plt.hold(True)
plt.plot(stent_P1491_1_Mano_4scoop.df3[11800:12100,1])

plt.plot(stent_P1491_1_Mano_6scoop.df3[14100:14400,1])

plt.plot(stent_P1491_1_Mano_8scoop.df3[13000:13300,1])
plt.legend(['4 scoops',\
            '6 scoops',
            '8 scoops']) 
plt.show()

#%% P1491_1 gradient Plots mano 1
N=20
Filter8scoopP1491=np.convolve(stent_P1491_1_Mano_8scoop.df1[13000:13300,1], 
                              np.ones((N,))/N, mode='valid')

Grad4scoopP1491=np.gradient(stent_P1491_1_Mano_4scoop.df1[11800:12100,1],
                            stent_P1491_1_Mano_4scoop.df1[11800:12100,0])
Grad6scoopP1491=np.gradient(stent_P1491_1_Mano_6scoop.df1[14100:14400,1],
                            stent_P1491_1_Mano_6scoop.df1[14100:14400,0])
Grad8scoopP1491=np.gradient(Filter8scoopP1491)
plt.figure()
#plt.hold(True)
#plt.plot(stent_P1491_1_Mano_4scoop.df1[11800:12100,1]-3.7)
#
#plt.plot(stent_P1491_1_Mano_6scoop.df1[14100:14400,1]-3.7)

plt.plot(Filter8scoopP1491-3.76)

#plt.plot(Grad4scoopP1491)
#plt.plot(Grad6scoopP1491)
plt.plot(Grad8scoopP1491)

#plt.legend(['P1491_1_Mano_4scoop',\
#            'P1491_1_Mano_6scoop',\
#            'P1491_1_Mano_8scoop',\
#            'Grad_P1491_1_Mano_4scoop',\
#            'Grad_P1491_1_Mano_6scoop',\
#            'Grad_P1491_1_Mano_8scoop']) 
plt.legend(['P1491_1_Mano_8scoop',\
            'Grad_P1491_1_Mano_8scoop']) 
 
 
plt.show()

#%%P1568_4 plots
plt.figure()
#plt.hold(True)
plt.plot(stent_P1568_4_Mano_Dry.df1[:,0],
         stent_P1568_4_Mano_Dry.df1[:,1])

plt.plot(stent_P1568_4_Mano_4scoop.df1[:,0],
         stent_P1568_4_Mano_4scoop.df1[:,1])

plt.plot(stent_P1568_4_Mano_8scoop.df1[:,0],
         stent_P1568_4_Mano_8scoop.df1[:,1])
plt.legend(['Dry',\
            '4 scoops',
            '8 scoops']) 


plt.figure()
#plt.hold(True)
plt.plot(stent_P1568_4_Mano_Dry.df2[:,0],
         stent_P1568_4_Mano_Dry.df2[:,1])

plt.plot(stent_P1568_4_Mano_4scoop.df2[:,0],
         stent_P1568_4_Mano_4scoop.df2[:,1])

plt.plot(stent_P1568_4_Mano_8scoop.df2[:,0],
         stent_P1568_4_Mano_8scoop.df2[:,1])
plt.legend(['Dry',\
            '4 scoops',
            '8 scoops']) 



plt.figure()
#plt.hold(True)
plt.plot(stent_P1568_4_Mano_Dry.df3[:,0],
         stent_P1568_4_Mano_Dry.df3[:,1])

plt.plot(stent_P1568_4_Mano_4scoop.df3[:,0],
         stent_P1568_4_Mano_4scoop.df3[:,1])

plt.plot(stent_P1568_4_Mano_8scoop.df3[:,0],
         stent_P1568_4_Mano_8scoop.df3[:,1])
plt.legend(['Dry',\
            '4 scoops',
            '8 scoops']) 
plt.show()

#%% P1568_4 gradient Manometry sensor 1
Grad4scoopMano1=np.gradient(stent_P1568_4_Mano_4scoop.df1[:,1],stent_P1568_4_Mano_4scoop.df1[:,0])
Grad8scoopMano1=np.gradient(stent_P1568_4_Mano_8scoop.df1[:,1],stent_P1568_4_Mano_8scoop.df1[:,0])
plt.figure()
#plt.hold(True)
plt.plot(stent_P1568_4_Mano_4scoop.df1[:,0],
         stent_P1568_4_Mano_4scoop.df1[:,1]-3.7)
plt.plot(stent_P1568_4_Mano_8scoop.df1[:,0],
         stent_P1568_4_Mano_8scoop.df1[:,1]-3.7)

plt.plot(stent_P1568_4_Mano_4scoop.df1[:,0],Grad4scoopMano1)
plt.plot(stent_P1568_4_Mano_8scoop.df1[:,0],Grad8scoopMano1)
plt.legend(['P1568_4_Mano_4scoop',\
            'P1568_4_Mano_8scoop',\
            'Grad_P1568_4_Mano_4scoop',\
            'Grad_P1568_4_Mano_8scoop']) 
 
plt.show()

#%% P1568_4 gradient Manometry sensor 2
GradDryMano2=np.gradient(stent_P1568_4_Mano_Dry.df1[:,1],stent_P1568_4_Mano_Dry.df1[:,0])
Grad4scoopMano2=np.gradient(stent_P1568_4_Mano_4scoop.df1[:,1],stent_P1568_4_Mano_4scoop.df1[:,0])
Grad8scoopMano2=np.gradient(stent_P1568_4_Mano_8scoop.df1[:,1],stent_P1568_4_Mano_8scoop.df1[:,0])
plt.figure()
#plt.hold(True)
plt.plot(stent_P1568_4_Mano_Dry.df1[:,0],
         stent_P1568_4_Mano_Dry.df1[:,1]-3.7+0.05)
plt.plot(stent_P1568_4_Mano_4scoop.df1[:,0],
         stent_P1568_4_Mano_4scoop.df1[:,1]-3.7)
plt.plot(stent_P1568_4_Mano_8scoop.df1[:,0],
         stent_P1568_4_Mano_8scoop.df1[:,1]-3.7)


plt.plot(stent_P1568_4_Mano_Dry.df1[:,0],GradDryMano2)
plt.plot(stent_P1568_4_Mano_4scoop.df1[:,0],Grad4scoopMano2)
plt.plot(stent_P1568_4_Mano_8scoop.df1 [:,0],Grad8scoopMano2)
plt.legend(['P1568_4_Mano_Dry',\
            'P1568_4_Mano_4scoop',\
            'P1568_4_Mano_8scoop',\
            'Grad_P1568_4_Mano_Dry',\
            'Grad_P1568_4_Mano_4scoop',\
            'Grad_P1568_4_Mano_8scoop']) 
 
plt.show()
#%% P1568_4 gradient Manometry sensor 3
Grad4scoopMano3=np.gradient(stent_P1568_4_Mano_4scoop.df3[:,1],stent_P1568_4_Mano_4scoop.df3[:,0])
Grad8scoopMano3=np.gradient(stent_P1568_4_Mano_8scoop.df3[:,1],stent_P1568_4_Mano_8scoop.df3[:,0])
plt.figure()
#plt.hold(True)
plt.plot(stent_P1568_4_Mano_4scoop.df3[:,0],
         stent_P1568_4_Mano_4scoop.df3[:,1]-3.7)
plt.plot(stent_P1568_4_Mano_8scoop.df3[:,0],
         stent_P1568_4_Mano_8scoop.df3[:,1]-3.7)

plt.plot(stent_P1568_4_Mano_4scoop.df3[:,0],Grad4scoopMano3)
plt.plot(stent_P1568_4_Mano_8scoop.df3 [:,0],Grad8scoopMano3)
plt.legend(['P1568_4_Mano_4scoop',\
            'P1568_4_Mano_8scoop',\
            'Grad_P1568_4_Mano_4scoop',\
            'Grad_P1568_4_Mano_8scoop']) 
 
plt.show()
#%% Gradient comparison of the three manometer sensor
plt.figure()
#plt.hold(True)
plt.plot(stent_P1568_4_Mano_8scoop.df1[:,0],Grad8scoopMano1)
plt.plot(stent_P1568_4_Mano_8scoop.df2 [:,0],Grad8scoopMano2)
plt.plot(stent_P1568_4_Mano_8scoop.df3 [:,0],Grad8scoopMano3)
plt.legend(['Mano1',\
            'Mano2',\
            'MAno3',]) 
#%% P1568_4 gradient Manometry sensor 3
plt.figure()
plt.figure()
#plt.hold(True)
plt.plot(stent_P1568_4_Mano_8scoop.df1[:-48,0],
         stent_P1568_4_Mano_8scoop.df1[48:,1]-3.7)
plt.plot(stent_P1568_4_Mano_8scoop.df3[:,0],
         stent_P1568_4_Mano_8scoop.df3[:,1]-3.7)
plt.legend(['Mano1',\
            'MAno3',])