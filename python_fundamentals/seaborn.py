##!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: seaborn.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: seaborn exploration  
#
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED:  
#     REVISION: Wed Jun 21 08:21:45 PDT 2017
#===============================================================================
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "distributions")))

x = np.random.normal(size=100)
sns.distplot(x)
