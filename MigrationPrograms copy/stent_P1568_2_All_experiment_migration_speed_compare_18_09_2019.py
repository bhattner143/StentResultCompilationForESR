#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:00:07 2019

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
plt.rcParams["font.size"] = 5
plt.rcParams["lines.markersize"] = 3
plt.rc("lines", mew=0.5)
plt.rcParams["lines.linewidth"] = 1
matplotlib.rcParams.update({"errorbar.capsize": 1})
plt.close("all")

# =============================================================================
# stent_P1568_2:60mm:Dry
# =============================================================================
GenPath = "/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
path = GenPath + "Dipankar_TOF_Stent_P1568_2_18_09_19/Dry/60mm"
name = "TOF"
Bolustype = "Dry"
stent_P1568_2_Mig_Dry_60mm = stentMigration(path, "stent_P1568_2_60mm", name)
stent_P1568_2_Mig_Dry_60mm.find_all()
stent_P1568_2_Mig_Dry_60mm.FileReading([0, 1, 2, 3])

stent_P1568_2_Mig_Dry_60mm.FindMeanSDAndRelDisp()
stent_P1568_2_Mig_Dry_60mm.ComputeGradient()

FileList = [
    "TOF_Dry_60m_20mmpsAnchored0g",
    "TOF_Dry_60m_30mmpsAnchored0g",
    "TOF_Dry_60m_40mmpsAnchored0g",
]

FigureNum3 = plt.figure(num=3, figsize=(2.25, 1.6))
ax1 = stentMigration.MigrationPlotting(
    FigureNum3, stent_P1568_2_Mig_Dry_60mm.MeanMigrationInfoDict, FileList
)
ax1.set(ylim=(-30, 30))

FigureNum4 = plt.figure(num=4, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum4, stent_P1568_2_Mig_Dry_60mm.GradMeanMigrationInfoDict, FileList
)

# =============================================================================
# stent_P1568_2:60mm:4Scoop
# =============================================================================
GenPath = "/Users/dipankarbhattacharya/Documents/Spyder Python/StentResultsCompilation/StentTesting_Migration_TOF/"
path = GenPath + "Dipankar_TOF_Stent_P1568_2_18_09_19/4Scoop/60mm"
name = "TOF"
Bolustype = "4Scoop"
stent_P1568_2_Mig_4Scoop_60mm = stentMigration(path, "stent_P1568_2_60mm", name)
stent_P1568_2_Mig_4Scoop_60mm.find_all()
stent_P1568_2_Mig_4Scoop_60mm.FileReading([0, 1, 2, 3])

stent_P1568_2_Mig_4Scoop_60mm.FindMeanSDAndRelDisp()
stent_P1568_2_Mig_4Scoop_60mm.ComputeGradient()

FileList = [
    "TOF_4Scoop_60m_20mmpsAnchored0gv2",
    "TOF_4Scoop_60m_30mmpsAnchored0g",
    "TOF_4Scoop_60m_40mmpsAnchored0g",
]

FigureNum5 = plt.figure(num=5, figsize=(2.25, 1.6))
ax2 = stentMigration.MigrationPlotting(
    FigureNum5, stent_P1568_2_Mig_4Scoop_60mm.MeanMigrationInfoDict, FileList
)
ax2.set(ylim=(-30, 30))

FigureNum6 = plt.figure(num=6, figsize=(2.25, 1.6))
stentMigration.MigrationPlotting(
    FigureNum6, stent_P1568_2_Mig_4Scoop_60mm.GradMeanMigrationInfoDict, FileList
)

