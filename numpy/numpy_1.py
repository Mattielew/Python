#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: numpy1.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: A demonstration of the capabilities of numpy in python
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

plt.ion()
plt.plot([1.6, 2.7])

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

#Viewing data 
#top records
print(df.head)
#bottom records
print(df.tail)
print('\nprint index of data\n')
print(df.index)

# print just the columns
print(df.columns)
#print just the values 
print(df.values)

print('\nDescriptive Statistics\n')
print('describe creates some simple descriptive statistics about your data-set')
print(df.describe())

print('\nTransposition\n') 
#Transpose your data to have a different view or to export it in a different format
print(df.T)

stacked = df2.stack
print(stacked)

print('\nPivot Tables\n')
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
