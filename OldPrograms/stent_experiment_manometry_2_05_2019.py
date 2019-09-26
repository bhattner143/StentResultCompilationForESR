#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:47:55 2019

@author: dipankarbhattacharya
"""
import numpy as np
import matplotlib.pyplot as plt
from intelhex import IntelHex
plt.close("all")
def cls():
    print('\n'*50)
#clear Console
cls()

# =============================================================================
# Read a Intel Hex file
# =============================================================================
#path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/Dipankar_Manometry_Stent_P1568/Manometry_P1568_4C_60mmat40mmps_DrySwallow.hex"
path="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting18_03_2019_Dry_bolus/Dipankar_Manometry_Stent_P1568/Manometry_P1568_4_60mmat40mmps_BolusSwallow_8scoops 05-01-2019 00.hex"
ih = IntelHex(path)

# =============================================================================
# Create a list (ihHexList) containing each byte in sequential order
# =============================================================================
ihList=list()
ihHexList=list()
ihHexList2byte=list()
for ii in range(len(ih)):
    ihList.append(ih[ii])
    ihHexList.append(hex(ihList[ii]))
    if len(ihHexList[ii])==3:
        ihHexList[ii]=ihHexList[ii]+'0'
        
# =============================================================================
# Create a list such that each item contains 2 byte (ihHexList[ii]+ihHexList[ii+1][2:4])
# =============================================================================
ihHexList2byte2Int=list() 
jj=0     
for ii in range(len(ih)):
    if ii%2==0:
        ihHexList2byte.append(ihHexList[ii]+ihHexList[ii+1][2:4])
        ihHexList2byte2Int.append(int(ihHexList2byte[jj],16))
        jj+=1
        
# =============================================================================
# Reverse the byte order (ihHexList2byteReverse), and generate a new list (ihHexListRev2byte2Int) containing its equivalant unsigned integer value
# =============================================================================
ihHexList2byteReverse=list()
ihHexListRev2byte2Int=list() 
for ii in range(len(ihHexList2byte)):
        temp=ihHexList2byte[ii][2:4]
        ihHexList2byteReverse.append('0x'+ihHexList2byte[ii][4:6]+temp)
        ihHexListRev2byte2Int.append(int(ihHexList2byteReverse[ii],16))
        
# =============================================================================
# Create a numpy array (ihArrayReverse) and reshape it (ihArrayRevReshaped)      
# =============================================================================
ihArrayReverse=np.array(ihHexListRev2byte2Int)
cc=6
ihArrayRevReshaped=np.reshape(ihArrayReverse, (int(len(ihArrayReverse)/cc), cc))

plt.rcParams['figure.figsize'] = (8.8, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
plt.figure()
plt.hold(True)
#plt.plot(xxxx[:,1],'r-')
#plt.plot(xxxx[:,2],'g-')
plt.subplot(311)
plt.plot(ihArrayRevReshaped[1000:5000,1],'r-')
plt.subplot(312)
plt.plot(ihArrayRevReshaped[1000:5000,2],'g-')
plt.subplot(313)
plt.plot(ihArrayRevReshaped[1000:5000,3],'b-')

