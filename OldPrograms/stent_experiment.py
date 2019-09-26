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
           n = 3  # the larger n is, the smoother curve will be
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
##-----------Stent 3---------------------------------------------
#set path
path="/Users/dipankarbhattacharya/Documents/Spyder Python/Stent testing 25_09_18/DataStentP1491C_3"
# stent 3 40mm
stent3_40mm=stent(path)
indexFileToRead=np.array([10,14])
## Stent 3, Wavelength =40mm
#plot the result
stent3_40mm.FileReading(indexFileToRead)
stent3_40mm.FilterData(indexFileToRead)
plt.figure()
plt.plot(stent3_40mm.df1[2:-16,1],stent3_40mm.df1[2,2]-stent3_40mm.df1[2:-16,2],'bo-',stent3_40mm.df2[2:-1,1],stent3_40mm.df2[2,2]-stent3_40mm.df2[2:-1,2],'ro-')
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'wavelength $\lambda=40 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s'],loc='best')
plt.figure()
plt.hold(True)
plt.plot(stent3_40mm.df1[2:-16,1],stent3_40mm.df1Filter[2:-13],linewidth=2, linestyle="-", c="b",marker="o")  # smooth by filter
plt.plot(stent3_40mm.df2[2:-1,1],stent3_40mm.df2Filter,linewidth=2, linestyle="-", c="r",marker="o")  # smooth by filter
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Filtered stent migrartion (mm)',fontsize=10)
plt.title(r'Peristalsis wavelength $\lambda=40 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s'],loc='best')
fig=plt.figure()
fig.savefig('/Users/dipankarbhattacharya/Documents/Spyder Python/Stent testing 25_09_18/foo.png')
# stent 3 50mm
stent3_50mm=stent(path)
indexFileToRead=np.array([6,12,1])
## Stent 3, Wavelength =50mm
#plot the result
stent3_50mm.FileReading(indexFileToRead)
stent3_50mm.FilterData(indexFileToRead)
plt.figure()
plt.hold(True)
plt.plot(stent3_50mm.df1[2:-1,1],stent3_50mm.df1[2,2]-stent3_50mm.df1[2:-1,2],'bo-',stent3_50mm.df2[2:-1,1],stent3_50mm.df2[2,2]-stent3_50mm.df2[2:-1,2],'ro-',stent3_50mm.df3[2:-1,1],stent3_50mm.df3[2,2]-stent3_50mm.df3[2:-1,2],'ko-')
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'wavelength $\lambda=50 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s'],loc='best')
plt.figure()
plt.hold(True)
plt.plot(stent3_50mm.df1[2:-1,1],stent3_50mm.df1Filter,linewidth=2, linestyle="-", c="b")  # smooth by filter
plt.plot(stent3_50mm.df2[2:-1,1],stent3_50mm.df2Filter,linewidth=2, linestyle="-", c="r")  # smooth by filter
plt.plot(stent3_50mm.df3[2:-1,1],stent3_50mm.df3Filter,linewidth=2, linestyle="-", c="k")  # smooth by filter
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Filtered stent migrartion (mm)',fontsize=10)
plt.title(r'Peristalsis wavelength $\lambda=50 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s','wave speed $c$= 60mm/s'],loc='best')
plt.show()
print('hello')
# stent 3 60mm
stent3_60mm=stent(path)
indexFileToRead=np.array([5,9,11])
## Stent 3, Wavelength =60mm
#plot the result
stent3_60mm.FileReading(indexFileToRead)
stent3_60mm.FilterData(indexFileToRead)
plt.figure()
plt.hold(True)
plt.plot(stent3_60mm.df1[2:-1,1],stent3_60mm.df1[2,2]-stent3_60mm.df1[2:-1,2],'bo-',stent3_60mm.df2[2:-1,1],stent3_60mm.df2[2,2]-stent3_60mm.df2[2:-1,2],'ro-',stent3_60mm.df2[2:-1,1],stent3_60mm.df3[2,2]-stent3_60mm.df3[2:-1,2],'ko-')
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'wavelength $\lambda=60 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s'],loc='best')
plt.figure()
plt.hold(True)
plt.plot(stent3_60mm.df1[2:-1,1],stent3_60mm.df1Filter,linewidth=2, linestyle="-", c="b")  # smooth by filter
plt.plot(stent3_60mm.df2[2:-1,1],stent3_60mm.df2Filter,linewidth=2, linestyle="-", c="r")  # smooth by filter
plt.plot(stent3_60mm.df3[2:-1,1],stent3_60mm.df3Filter,linewidth=2, linestyle="-", c="k")  # smooth by filter
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Filtered stent migrartion (mm)',fontsize=10)
plt.title(r'Peristalsis wavelength $\lambda=60 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s','wave speed $c$= 60mm/s'],loc='best')
plt.show()

##-----------Stent 4---------------------------------------------
#set path
path2="/Users/dipankarbhattacharya/Documents/Spyder Python/Stent testing 25_09_18/DataStentP1491C_4"
# stent 3 40mm
stent4_40mm=stent(path2)
indexFileToRead=np.array([5,0])
## Stent 3, Wavelength =40mm
#plot the result
stent4_40mm.FileReading(indexFileToRead)
stent4_40mm.FilterData(indexFileToRead)
plt.figure()
plt.plot(stent4_40mm.df1[2:-1,1],stent4_40mm.df1[2,2]-stent4_40mm.df1[2:-1,2],'bo-',stent4_40mm.df2[2:-1,1],stent4_40mm.df2[2,2]-stent4_40mm.df2[2:-1,2],'ro-')
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'wavelength $\lambda=40 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s'],loc='best')
plt.figure()
plt.hold(True)
plt.plot(stent4_40mm.df1[2:-1,1],stent4_40mm.df1Filter,linewidth=2, linestyle="-", c="b")  # smooth by filter
plt.plot(stent4_40mm.df2[2:-1,1],stent4_40mm.df2Filter,linewidth=2, linestyle="-", c="r")  # smooth by filter
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Filtered stent migrartion (mm)',fontsize=10)
plt.title(r'Peristalsis wavelength $\lambda=40 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s'],loc='best')
plt.show()
# stent 3 50mm
stent4_50mm=stent(path2)
indexFileToRead=np.array([11,9])
## Stent 3, Wavelength =40mm
#plot the result
stent4_50mm.FileReading(indexFileToRead)
stent4_50mm.FilterData(indexFileToRead)
plt.figure()
plt.plot(stent4_50mm.df1[2:-1,1],stent4_50mm.df1[2,2]-stent4_50mm.df1[2:-1,2],'bo-',stent4_50mm.df2[2:-1,1],stent4_50mm.df2[2,2]-stent4_50mm.df2[2:-1,2],'ro-')
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'wavelength $\lambda=50 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s'],loc='best')
plt.figure()
plt.hold(True)
plt.plot(stent4_50mm.df1[2:-1,1],stent4_50mm.df1Filter,linewidth=2, linestyle="-", c="b")  # smooth by filter
plt.plot(stent4_50mm.df2[2:-1,1],stent4_50mm.df2Filter,linewidth=2, linestyle="-", c="r")  # smooth by filter
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Filtered stent migrartion (mm)',fontsize=10)
plt.title(r'Peristalsis wavelength $\lambda=50 mm$',fontsize=10)
plt.legend(['wave speed $c$= 20mm/s','wave speed $c$= 40mm/s'],loc='best')
plt.show()
# stent 3 60mm
stent4_60mm=stent(path2)
indexFileToRead=np.array([10])
## Stent 3, Wavelength =40mm
#plot the result
stent4_60mm.FileReading(indexFileToRead)
stent4_60mm.FilterData(indexFileToRead)
plt.figure()
plt.plot(stent4_60mm.df1[2:-1,1],stent4_60mm.df1[2,2]-stent4_60mm.df1[2:-1,2],'bo-')
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Stent migrartion (mm)',fontsize=10)
plt.title(r'wavelength $\lambda=50 mm$',fontsize=10)
plt.legend(['wave speed $c$= 40mm/s'],loc='best')
plt.figure()
plt.hold(True)
plt.plot(stent4_60mm.df1[2:-1,1],stent4_60mm.df1Filter,linewidth=2, linestyle="-", c="b")  # smooth by filter
plt.xlabel(r'Peristalsis cycle $n_c$',fontsize=10)
plt.ylabel('Filtered stent migrartion (mm)',fontsize=10)
plt.title(r'Peristalsis wavelength $\lambda=50 mm$',fontsize=10)
plt.legend(['wave speed $c$= 40mm/s'],loc='best')
plt.show()