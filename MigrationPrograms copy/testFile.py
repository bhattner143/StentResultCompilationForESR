#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:29:40 2019

@author: dipankarbhattacharya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:14:55 2019

@author: dipankarbhattacharya

"""
#%%
import os
import pdb
import random
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dateutil.parser import parse
from intelhex import IntelHex
from matplotlib import style
from scipy import signal
from scipy.signal import find_peaks, peak_prominences
from sklearn.linear_model import LinearRegression
from statsmodels.nonparametric.smoothers_lowess import lowess
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, kpss

from ClassStentForTOF import *

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

# clear Console
cls()
# =============================================================================
# MAIN PROGRAM
# =============================================================================
# Plotting
plt.rcParams["figure.figsize"] = (2.25, 1.6)  # set default size of plots #4.2x1.8

plt.style.use("classic")
plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["grid.linewidth"] = 0.5
plt.rcParams["grid.linestyle"] = ":"
plt.rcParams["image.interpolation"] = "nearest"
# plt.rcParams['font.family']='Helvetica'
plt.rcParams["font.size"] = 5
plt.rcParams["lines.markersize"] = 3
plt.rc("lines", mew=0.5)
plt.rcParams["lines.linewidth"] = 1
plt.rcParams.update({"errorbar.capsize": 1})
plt.close("all")

#%%
# =============================================================================
# stent_P1491_1:60mm:Dry:various weights
# =============================================================================
GenPath = "/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
path = GenPath + "Dipankar_TOF_Stent_P1491_1_29_08_19/Dry/60mm"
name = "TOF"
Bolustype = "Dry"
stent_P1491_1_Mig_Dry_60mmVW = stentMigration(path, "stent_P1491_60mm", name)
stent_P1491_1_Mig_Dry_60mmVW.find_all()
stent_P1491_1_Mig_Dry_60mmVW.FileReading([0, 1, 2, 3, 4])

stent_P1491_1_Mig_Dry_60mmVW.FindMeanSDAndRelDisp()
stent_P1491_1_Mig_Dry_60mmVW.ComputeGradient()
FileList = [
    "TOF_Dry_60m_40mmps1",
    "TOF_Dry_60m_40mmpsAnchored50g",
    "TOF_Dry_60m_40mmpsAnchored100g",
]

FigureNum1 = plt.figure(num=1, figsize=(2.25, 1.6))

stentMigration.MigrationSubPlotting(
    FigureNum1,
    stent_P1491_1_Mig_Dry_60mmVW.MeanMigrationInfoDict,
    stent_P1491_1_Mig_Dry_60mmVW.GradMeanMigrationInfoDict,
    FileList,
)
FigureNum1.show()
stentMigration.ComputeGradient
# FigureNum1=plt.figure(num=1,figsize=(2.25,1.6))
# stentMigration.MigrationPlotting(FigureNum3,stent_P1491_1_Mig_Dry_60mm.MeanMigrationInfoDict,FileList)
#
#%%
# =============================================================================
# stent_P1491_1:60mm:Dry
# =============================================================================
GenPath = "/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
path = GenPath + "Dipankar_TOF_Stent_P1491_1_29_08_19/Dry/60mmv2"
name = "TOF"
Bolustype = "4Scoop"
stent_P1491_1_Mig_Dry_60mm = stentMigration(path, "stent_P1491_60mm", name)
stent_P1491_1_Mig_Dry_60mm.find_all()
stent_P1491_1_Mig_Dry_60mm.FileReading([0, 1, 2, 3, 4, 5])

stent_P1491_1_Mig_Dry_60mm.FindMeanSDAndRelDisp()
stent_P1491_1_Mig_Dry_60mm.ComputeGradient()

FileList = [
    "TOF_Dry_60m_20mmpsAnchored0g",
    "TOF_Dry_60m_30mmpsAnchored0g",
    "TOF_Dry_60m_40mmpsAnchored0g",
]

FigureNum2 = plt.figure(num=2, figsize=(2.25, 1.6))
stentMigration.MigrationSubPlotting(
    FigureNum2,
    stent_P1491_1_Mig_Dry_60mm.MeanMigrationInfoDict,
    stent_P1491_1_Mig_Dry_60mm.GradMeanMigrationInfoDict,
    FileList,
)
FigureNum2.show()
print(FileList)
#%%
# =============================================================================
# stent_P1491_1:60mm:4Scoop
# =============================================================================
GenPath = "/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
path = GenPath + "Dipankar_TOF_Stent_P1491_1_29_08_19/4Scoop/60mmv2"
name = "TOF"
Bolustype = "4Scoop"
stent_P1491_1_Mig_4Scoop_60mm = stentMigration(path, "stent_P1491_60mm", name)
stent_P1491_1_Mig_4Scoop_60mm.find_all()
stent_P1491_1_Mig_4Scoop_60mm.FileReading([0, 1, 2, 3, 4, 5, 6])

stent_P1491_1_Mig_4Scoop_60mm.FindMeanSDAndRelDisp()
stent_P1491_1_Mig_4Scoop_60mm.ComputeGradient()

FileList = [
    "TOF_4Scoop_60m_20mmpsAnchored0gv4",
    "TOF_4Scoop_60m_30mmpsAnchored0g",
    "TOF_4Scoop_60m_40mmpsAnchored0g",
]

FigureNum3 = plt.figure(num=3, figsize=(2.25, 1.6))
stentMigration.MigrationSubPlotting(
    FigureNum3,
    stent_P1491_1_Mig_4Scoop_60mm.MeanMigrationInfoDict,
    stent_P1491_1_Mig_4Scoop_60mm.GradMeanMigrationInfoDict,
    FileList,
)
FigureNum3.show()
#%%
# =============================================================================
# stent_P1491_1:60mm:6Scoop
# =============================================================================
GenPath = "/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
path = GenPath + "Dipankar_TOF_Stent_P1491_1_29_08_19/6Scoop/60mm"
name = "TOF"
Bolustype = "6Scoop"
stent_P1491_1_Mig_6Scoop_60mm = stentMigration(path, "stent_P1491_60mm", name)
stent_P1491_1_Mig_6Scoop_60mm.find_all()
stent_P1491_1_Mig_6Scoop_60mm.FileReading([0, 1, 2, 3, 4, 5])

stent_P1491_1_Mig_6Scoop_60mm.FindMeanSDAndRelDisp()
stent_P1491_1_Mig_6Scoop_60mm.ComputeGradient()

FileList = [
    "TOF_6Scoop_60m_20mmpsAnchored0g",
    "TOF_6Scoop_60m_30mmpsAnchored0g",
    "TOF_6Scoop_60m_40mmpsAnchored0g",
]

FigureNum4 = plt.figure(4, figsize=(2.25, 1.6))
stentMigration.MigrationSubPlotting(
    FigureNum4,
    stent_P1491_1_Mig_6Scoop_60mm.MeanMigrationInfoDict,
    stent_P1491_1_Mig_6Scoop_60mm.GradMeanMigrationInfoDict,
    FileList,
)
FigureNum4.show()
#%%
# =============================================================================
# stent_P1491_1:60mm:8Scoop
# =============================================================================
GenPath = "/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
path = GenPath + "Dipankar_TOF_Stent_P1491_1_29_08_19/8Scoop/60mm"
name = "TOF"
Bolustype = "8Scoop"
stent_P1491_1_Mig_8Scoop_60mm = stentMigration(path, "stent_P1491_60mm", name)
stent_P1491_1_Mig_8Scoop_60mm.find_all()
stent_P1491_1_Mig_8Scoop_60mm.FileReading([0, 1, 2, 3, 4, 5])

stent_P1491_1_Mig_8Scoop_60mm.FindMeanSDAndRelDisp()
stent_P1491_1_Mig_8Scoop_60mm.ComputeGradient()

FileList = [
    "TOF_8Scoop_60m_20mmpsAnchored0g",
    "TOF_8Scoop_60m_30mmpsAnchored0g",
    "TOF_8Scoop_60m_40mmpsAnchored0g",
]

FigureNum5 = plt.figure(5, figsize=(2.25, 1.6))
stentMigration.MigrationSubPlotting(
    FigureNum5,
    stent_P1491_1_Mig_8Scoop_60mm.MeanMigrationInfoDict,
    stent_P1491_1_Mig_8Scoop_60mm.GradMeanMigrationInfoDict,
    FileList,
)
FigureNum5.show()
#%%
# =============================================================================
# Merge all the dictionaries
# =============================================================================
MergeMeanMigrationInfoDictDry = {
    **stent_P1491_1_Mig_Dry_60mm.MeanMigrationInfoDict,
    **stent_P1491_1_Mig_4Scoop_60mm.MeanMigrationInfoDict,
    **stent_P1491_1_Mig_6Scoop_60mm.MeanMigrationInfoDict,
    **stent_P1491_1_Mig_8Scoop_60mm.MeanMigrationInfoDict,
}

MergeGradMeanMigrationInfoDictDry = {
    **stent_P1491_1_Mig_Dry_60mm.GradMeanMigrationInfoDict,
    **stent_P1491_1_Mig_4Scoop_60mm.GradMeanMigrationInfoDict,
    **stent_P1491_1_Mig_6Scoop_60mm.GradMeanMigrationInfoDict,
    **stent_P1491_1_Mig_8Scoop_60mm.GradMeanMigrationInfoDict,
}
#%%
# =============================================================================
# stent_P1491_1:60mm:20mmps
# =============================================================================


FileList = [
    "TOF_Dry_60m_20mmpsAnchored0g",
    "TOF_4Scoop_60m_20mmpsAnchored0g",
    "TOF_6Scoop_60m_20mmpsAnchored0g",
    "TOF_8Scoop_60m_20mmpsAnchored0g",
]

FigureNum6 = plt.figure(num=6, figsize=(2.25, 1.6))
ax6 = stentMigration.MigrationPlotting(
    FigureNum6, MergeMeanMigrationInfoDictDry, FileList
)
ax6.legend(
    ["No bolus", "72 g.L$^{-1}$", "108 g.L$^{-1}$", "144 g.L$^{-1}$"], prop={"size": 5}
)
plt.show()

#%%
# =============================================================================
# stent_P1491_1:60mm:30mmps
# =============================================================================


FileList = [
    "TOF_Dry_60m_30mmpsAnchored0g",
    "TOF_4Scoop_60m_30mmpsAnchored0g",
    "TOF_6Scoop_60m_30mmpsAnchored0g",
    "TOF_8Scoop_60m_30mmpsAnchored0g",
]

FigureNum7 = plt.figure(num=7, figsize=(2.25, 1.6))
ax7 = stentMigration.MigrationPlotting(
    FigureNum7, MergeMeanMigrationInfoDictDry, FileList
)
ax7.legend(
    ["No bolus", "72 g.L$^{-1}$", "108 g.L$^{-1}$", "144 g.L$^{-1}$"], prop={"size": 5}
)


# FigureNum7=plt.figure(7)
# stentMigration.MigrationSubPlotting(FigureNum7,
#                                    MergeMeanMigrationInfoDictDry,
#                                    MergeGradMeanMigrationInfoDictDry,
#                                    FileList)
#%%
# =============================================================================
# stent_P1491_1:60mm:40mmps
# =============================================================================


FileList = [
    "TOF_Dry_60m_40mmpsAnchored0g",
    "TOF_4Scoop_60m_40mmpsAnchored0g",
    "TOF_6Scoop_60m_40mmpsAnchored0g",
    "TOF_8Scoop_60m_40mmpsAnchored0g",
]

FigureNum8 = plt.figure(num=8, figsize=(2.25, 1.6))
ax8 = stentMigration.MigrationPlotting(
    FigureNum8, MergeMeanMigrationInfoDictDry, FileList
)
ax8.legend(
    ["No bolus", "72 g.L$^{-1}$", "108 g.L$^{-1}$", "144 g.L$^{-1}$"], prop={"size": 5}
)

# =============================================================================
# Marker trajectory from QSR
# =============================================================================
GenPath = "/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/QSRMarkerTrajectory/"
path = GenPath
name = "QSR"
Bolustype = "NA"
QSRMarkerTrajectory = stentMigration(path, "QSRMarkerTrajectory", name)
QSRMarkerTrajectory.find_all()
QSRMarkerTrajectory.FileReading([0])

QSRMarkerArray = QSRMarkerTrajectory.ArrayDict["QSR_experiment_5Q_40mm20mmps_44ms_11"][
    :, [6, 8]
]
QSRMarkerArrayReshape = np.reshape(QSRMarkerArray, (-1, 10), order="F")
QSRMarkerArrayReshapeMean = np.array(
    [
        np.mean(QSRMarkerArrayReshape[:, 0:5], axis=1),
        np.mean(QSRMarkerArrayReshape[:, 6:], axis=1),
    ]
).T


b, a = signal.butter(1, 0.05)
zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b, a, QSRMarkerArray[:, 0], zi=zi * QSRMarkerArray[0, 0])

z2, _ = signal.lfilter(b, a, QSRMarkerArray[:, 1], zi=zi * QSRMarkerArray[0, 1])

QSRMarkerArrayFiltered1 = signal.filtfilt(b, a, QSRMarkerArray[:, 0])
QSRMarkerArrayFiltered2 = signal.filtfilt(b, a, QSRMarkerArray[:, 1])


QSRMarkerArrayGradient = np.gradient(
    QSRMarkerArrayFiltered1, QSRMarkerArrayFiltered2, axis=0
)

X1, Y1 = np.meshgrid(
    QSRMarkerArrayFiltered2[0:610:50], QSRMarkerArrayFiltered1[0:610:50]
)
# X1quiver , Y1quiver = np.meshgrid(QSRMarkerArrayFiltered2[0:5405:200],QSRMarkerArrayFiltered1[0:5405:200])
#
## Define the system of ODEs
## P[0] is prey, P[1] is predator
# def fish(P, t=0):
##    pdb.set_trace()
#    return ([b*P[0]*(1-P[0]/K) - (a*P[0]*P[1])/(1+a*h*P[0]),
#            c*(a*P[0]*P[1])/(1+a*h*P[0]) - d*P[1] ])
## Calculate growth rate at each grid point
# DX1, DY1 = fish([X1quiver[0:20,0:20], Y1quiver[0:20,0:20]])
## Direction at each grid point is the hypotenuse of the prey direction and the
## predator direction.
# M = (np.hypot(DX1, DY1))
# M[ M == 0] = 1.
## Normalize the length of each arrow (optional)
# DX1 /= M
# DY1 /= M
#
# plt.figure()
# plt.title('Trajectories and direction fields')
# """
# This is using the quiver function to plot the field of arrows using DX1 and
# DY1 for direction and M for speed
# """
# Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.plasma)
# plt.xlabel('Prey abundance')
# plt.ylabel('Predator abundance')
##plt.legend(bbox_to_anchor=(1.05, 1.0))
# plt.grid()
# plt.xlim(0, xmax)
# plt.ylim(0, ymax)
# plt.show()


FigureNum9 = plt.figure(num=9, figsize=(2.25, 1.6))
ax = FigureNum9.subplots(1, 1)
ax.plot(QSRMarkerArrayFiltered2[0:610], QSRMarkerArrayFiltered1[0:610], color="#9b1c31")
ax.set_xlabel(r"z-axis displacement (mm)", size=5)
ax.set_ylabel(r"x-axis displacement (mm)", size=5)

# ax.quiver(QSRMarkerArrayFiltered2[0:610:50], QSRMarkerArrayFiltered1[0:610:50], X1, Y1)

ax.annotate(
    "",
    xy=(6.7, 48),
    xycoords="data",
    xytext=(8.7, 45),
    textcoords="data",
    size=5,
    # bbox=dict(boxstyle="round", fc="0.8"),
    arrowprops=dict(
        arrowstyle="simple",
        fc="0.2",
        ec="none",
        #                            patchB=el,
        connectionstyle="arc3,rad=0.3",
    ),
)

# ax[1].plot(QSRMarkerArrayFiltered2[10:50],QSRMarkerArrayGradient[10:50],color='royalblue')
# ax[1].set_xlabel(r'x-axis (mm)',size=5)
# ax[1].set_ylabel(r'y-axis (mm)',size=5)

plt.show()


# FigureNum8=plt.figure(8)
# stentMigration.MigrationSubPlotting(FigureNum8,
#                                    MergeMeanMigrationInfoDictDry,
#                                    MergeGradMeanMigrationInfoDictDry,
#                                    FileList)
## =============================================================================
## stent_P1491_1:60mm:All
## =============================================================================
# GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
# path=GenPath+"Dipankar_TOF_Stent_P1491_1_29_08_19/Allv2/60mm"
# name='TOF'
# Bolustype='All'
# stent_P1491_1_Mig_All_60mm=stentMigration(path,'stent_P1491_60mm',name)
# stent_P1491_1_Mig_All_60mm.find_all()
# stent_P1491_1_Mig_All_60mm.FileReading([0,1,2,3,4,5,6,7,8,9,10,11])
#
# stent_P1491_1_Mig_All_60mm.FindMeanSDAndRelDisp()
# stent_P1491_1_Mig_All_60mm.ComputeGradient()
#
# FileList=['TOF_Dry_60m_20mmpsAnchored0g',
#          'TOF_Dry_60m_30mmpsAnchored0g',
#          'TOF_Dry_60m_40mmpsAnchored0g',
#          'TOF_4Scoop_60m_20mmpsAnchored0gv4',
#          'TOF_4Scoop_60m_30mmpsAnchored0g',
#          'TOF_4Scoop_60m_40mmpsAnchored0g',
#          'TOF_6Scoop_60m_20mmpsAnchored0g',
#          'TOF_6Scoop_60m_30mmpsAnchored0g',
#          'TOF_6Scoop_60m_40mmpsAnchored0g',
#          'TOF_8Scoop_60m_20mmpsAnchored0g',
#          'TOF_8Scoop_60m_30mmpsAnchored0g',
#          'TOF_8Scoop_60m_40mmpsAnchored0g']
#
# ColorChart=['red','green','blue',
#            'cyan','magenta','black',
#            'indigo','khaki','lavender',
#            'maroon','navy','olive']
#
# FigureNum6=plt.figure(6)
# stentMigration.MigrationPlottingWithColor(FigureNum6,
#                                    stent_P1491_1_Mig_All_60mm.MeanMigrationInfoDict,
#                                    #stent_P1491_1_Mig_All_60mm.GradMeanMigrationInfoDict,
#                                    FileList,
#                                    Color=ColorChart)


#%%
