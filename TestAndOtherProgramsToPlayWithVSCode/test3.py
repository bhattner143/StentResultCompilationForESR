#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 23:06:50 2019

@author: dipankarbhattacharya
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb
import itertools

def cls():
    print('\n'*50)
#clear Console
cls()

X=np.array([20,30,40])
Y=np.array([4,8])
result=zip(X,2)

for item in result:
    print(item)
    
    
    #            pdb.set_trace()    
            TextLoc1=np.array([X[:,0],Y[:,0],Z[:,0]]).T
            TextLoc2=np.array([X[:,1],Y[:,1],Z[:,1]]).T
            TextLoc3=np.array([X[:,2],Y[:,2],Z[:,2]]).T
            
#            for i,j,k in zip(TextLoc1,TextLoc2,TextLoc3):
#                print(i,j,k)
#            pdb.set_trace()
#            for i in range(len(TextLoc1)): # plot each point + it's index as text above
#                  x1 = TextLoc1[i,0]
#                  y1 = TextLoc1[i,1]
#                  z1 = TextLoc1[i,2]
#                
#                  x2 = TextLoc2[i,0]
#                  y2 = TextLoc2[i,1]
#                  z2 = TextLoc2[i,2]
#                  
#                  x3 = TextLoc3[i,0]
#                  y3 = TextLoc3[i,1]
#                  z3 = TextLoc3[i,2]
#                  
#                  label1 = np.round(z1,3)
#                  label2 = np.round(z2,3)
#                  label3 = np.round(z3,3)
#                  
#                  ax.text(x1, y1, z1, '%s' % (label1), size=6, zorder=1, color='k')
#                  ax.text(x2, y2, z2, '%s' % (label2), size=6, zorder=1, color='k')
#                  ax.text(x3, y3, z3, '%s' % (label3), size=6, zorder=1, color='k')
            