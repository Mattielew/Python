#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: numpy1.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: This is going to be a demonstration of the capabilities of numpy in python
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Sun Jul 16 10:06:33 PDT 2017
#     REVISION: ---
#===============================================================================
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


#generating some data to work with 
s = pd.Series([1,3,5,np.nan,6,8])
print(s) 

dates  = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

#cleaner version 
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3]*4,dtype='int32'),
                    'E' : pd.Categorical(['test','train','test','train']),
                    'F' : 'foo' })
print(df2)

#having specific dtypes
print(df2.dtypes)

 

