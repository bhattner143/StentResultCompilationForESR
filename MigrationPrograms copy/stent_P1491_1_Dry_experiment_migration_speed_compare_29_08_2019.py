#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:14:55 2019

@author: dipankarbhattacharya
"""

import os
import pdb
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import style
import pandas as pd
from intelhex import IntelHex
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.nonparametric.smoothers_lowess import lowess
from dateutil.parser import parse
from scipy.signal import find_peaks, peak_prominences
import random
from ClassStentForTOF import *


def cls():
    print("\n" * 50)


# clear Console
cls()

# =============================================================================
# MAIN PROGRAM
# =============================================================================
# Plotting
# plt.rcParams['figure.figsize'] = (16.0, 10) # set default size of plots #4.2x1.8

plt.style.use("classic")
# sns.set_style("white")
# sns.set_style("dark")
plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["grid.linewidth"] = 0.5
plt.rcParams["grid.linestyle"] = ":"
plt.rcParams["image.interpolation"] = "nearest"
# plt.rcParams['font.family']='Helvetica'
plt.rcParams["font.size"] = 7
plt.rcParams["lines.markersize"] = 3
plt.rc("lines", mew=0.5)
plt.rcParams["lines.linewidth"] = 1
matplotlib.rcParams.update({"errorbar.capsize": 1})
plt.close("all")


## =============================================================================
## stent_P1491_1:60mm:Dry:various weights
## =============================================================================
# GenPath="/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
# path=GenPath+"Dipankar_TOF_Stent_P1491_1_29_08_19/Dry/60mm"
# name='TOF'
# Bolustype='Dry'
# stent_P1491_1_Mig_Dry_60mmVW=stentMigration(path,'stent_P1491_60mm',name)
# stent_P1491_1_Mig_Dry_60mmVW.find_all()
# stent_P1491_1_Mig_Dry_60mmVW.FileReading([0,1,2,3,4])
#
# stent_P1491_1_Mig_Dry_60mmVW.FindMeanSDAndRelDisp()
# stent_P1491_1_Mig_Dry_60mmVW.ComputeGradient()
#
# FileList=['TOF_Dry_60m_40mmps1',
#          'TOF_Dry_60m_40mmpsAnchored50g',
#          'TOF_Dry_60m_40mmpsAnchored100g']
#
# FigureNum1=plt.figure(1)
# stentMigration.MigrationPlotting(FigureNum1,stent_P1491_1_Mig_Dry_60mmVW.MeanMigrationInfoDict,FileList)
#
# FigureNum2=plt.figure(2)
# stentMigration.MigrationPlotting(FigureNum2,stent_P1491_1_Mig_Dry_60mmVW.GradMeanMigrationInfoDict,FileList)
#
# FigureNum11=plt.figure(11)
#
# stentMigration.MigrationSubPlotting(FigureNum11,
#                                    stent_P1491_1_Mig_Dry_60mmVW.MeanMigrationInfoDict,
#                                    stent_P1491_1_Mig_Dry_60mmVW.GradMeanMigrationInfoDict,
#                                    FileList)

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

FigureNum3 = plt.figure(num=3, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum3, stent_P1491_1_Mig_Dry_60mm.MeanMigrationInfoDict, FileList
)

FigureNum4 = plt.figure(num=4, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum4, stent_P1491_1_Mig_Dry_60mm.GradMeanMigrationInfoDict, FileList
)


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


FigureNum5 = plt.figure(num=5, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum5, stent_P1491_1_Mig_4Scoop_60mm.MeanMigrationInfoDict, FileList
)

FigureNum6 = plt.figure(num=6, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum6, stent_P1491_1_Mig_4Scoop_60mm.GradMeanMigrationInfoDict, FileList
)


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

FigureNum7 = plt.figure(num=7, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum7, stent_P1491_1_Mig_6Scoop_60mm.MeanMigrationInfoDict, FileList
)

FigureNum8 = plt.figure(num=8, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum8, stent_P1491_1_Mig_6Scoop_60mm.GradMeanMigrationInfoDict, FileList
)

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

FigureNum9 = plt.figure(num=9, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum9, stent_P1491_1_Mig_8Scoop_60mm.MeanMigrationInfoDict, FileList
)

FigureNum10 = plt.figure(num=10, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum10, stent_P1491_1_Mig_8Scoop_60mm.GradMeanMigrationInfoDict, FileList
)

## =============================================================================
## stent_P1491_1:60mm:Dry and 4Scoop
## =============================================================================
#
#
# MergeMeanMigrationInfoDictDry4Scoop={**stent_P1491_1_Mig_Dry_60mm.MeanMigrationInfoDict,
#                    **stent_P1491_1_Mig_4Scoop_60mm.MeanMigrationInfoDict}
#
# FileList=['TOF_Dry_60m_40mmps1',
#          'TOF_Dry_60m_40mmpsAnchored50g',
#          'TOF_Dry_60m_40mmpsAnchored100g',
#          'TOF_4Scoop_60m_20mmpsAnchored0g',
#          'TOF_4Scoop_60m_20mmpsAnchored50g',
##          'TOF_4Scoop_60m_20mmpsAnchored100gv2'
##          'TOF_4Scoop_60m_30mmpsAnchored100g',
#          'TOF_4Scoop_60m_40mmpsAnchored100g']
#
# FigureNum3=plt.figure(3)
# stentMigration.MigrationPlotting(FigureNum3,MergeMeanMigrationInfoDictDry4Scoop,FileList)

