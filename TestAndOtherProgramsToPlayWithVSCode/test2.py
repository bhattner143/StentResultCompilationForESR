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


#def foo(*positional, arg1,**keywords):
#    pdb.set_trace()
#    print("arg1",arg1)
#    print("Positional:", positional)
#    print ("Keywords:", keywords)
#    
#    
#
#foo('zero1',a='one', b='two', c='three')

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)
triangle = signal.sawtooth(2 * np.pi * 5 * t, 0.5)
GradTri=np.gradient(triangle,t)


plt.figure()
plt.plot(t, triangle,'r',t,GradTri,'g')
plt.show()

import numpy
from matplotlib import pyplot

x = numpy.arange(10)
y = numpy.array([5,3,4,2,7,5,4,6,3,2])

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
pyplot.plot(x,y)
for i,j in zip(x,y):
    ax.annotate(str(j),xy=(i,j))

pyplot.show()

#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt
#from numpy.random import rand
#
#m = rand(3,3) # m is an array of (x,y,z) coordinate triplets
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#
#for i in range(len(m)): # plot each point + it's index as text above
#  x = m[i,0]
#  y = m[i,1]
#  z = m[i,2]
#  label = i
#  ax.scatter(x, y, z, color='b')
#  ax.text(x, y, z, '%s' % (label), size=20, zorder=1, color='k')
#
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#
#for angle in range(0, 360):
#  ax.view_init(30, angle)
#  plt.draw()
#  plt.pause(.001)