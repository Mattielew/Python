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

print('\nData Creation\n')
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

print('\nData Type Identification\n')
#having specific dtypes
print(df2.dtypes)

print('\nView Commands\n')
#Viewing data 
#top records
print(df.head)
#bottom records
print(df.tail)
print('\nprint index of data\n')
print(df.index)

# print just the columns
print(df.columns)
print('just the values')
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

Data Creation

0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
                   A         B         C         D
2013-01-01 -0.799488  0.614683 -0.013290  0.443529
2013-01-02 -1.189060  1.823170  1.824449  0.760373
2013-01-03 -0.211308  0.487847  1.258179  1.570920
2013-01-04 -0.112495  1.153684 -0.256718 -0.579901
2013-01-05  1.587575 -0.618663 -0.876168  1.415466
2013-01-06  1.013929  0.000324  0.315524  0.970423
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo

Data Type Identification

A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object

View Commands

<bound method NDFrame.head of                    A         B         C         D
2013-01-01 -0.799488  0.614683 -0.013290  0.443529
2013-01-02 -1.189060  1.823170  1.824449  0.760373
2013-01-03 -0.211308  0.487847  1.258179  1.570920
2013-01-04 -0.112495  1.153684 -0.256718 -0.579901
2013-01-05  1.587575 -0.618663 -0.876168  1.415466
2013-01-06  1.013929  0.000324  0.315524  0.970423>
<bound method NDFrame.tail of                    A         B         C         D
2013-01-01 -0.799488  0.614683 -0.013290  0.443529
2013-01-02 -1.189060  1.823170  1.824449  0.760373
2013-01-03 -0.211308  0.487847  1.258179  1.570920
2013-01-04 -0.112495  1.153684 -0.256718 -0.579901
2013-01-05  1.587575 -0.618663 -0.876168  1.415466
2013-01-06  1.013929  0.000324  0.315524  0.970423>

print index of data

DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
Index(['A', 'B', 'C', 'D'], dtype='object')
just the values
[[ -7.99488192e-01   6.14683290e-01  -1.32898717e-02   4.43529391e-01]
 [ -1.18905979e+00   1.82317009e+00   1.82444875e+00   7.60372516e-01]
 [ -2.11307918e-01   4.87847446e-01   1.25817921e+00   1.57091985e+00]
 [ -1.12495397e-01   1.15368355e+00  -2.56717761e-01  -5.79901185e-01]
 [  1.58757462e+00  -6.18663199e-01  -8.76167879e-01   1.41546611e+00]
 [  1.01392913e+00   3.24415789e-04   3.15523883e-01   9.70423118e-01]]

Descriptive Statistics

describe creates some simple descriptive statistics about your data-set
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.048192  0.576841  0.375329  0.763468
std    1.062531  0.855224  0.999970  0.778064
min   -1.189060 -0.618663 -0.876168 -0.579901
25%   -0.652443  0.122205 -0.195861  0.522740
50%   -0.161902  0.551265  0.151117  0.865398
75%    0.732323  1.018933  1.022515  1.304205
max    1.587575  1.823170  1.824449  1.570920

Transposition

   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A   -0.799488   -1.189060   -0.211308   -0.112495    1.587575    1.013929
B    0.614683    1.823170    0.487847    1.153684   -0.618663    0.000324
C   -0.013290    1.824449    1.258179   -0.256718   -0.876168    0.315524
D    0.443529    0.760373    1.570920   -0.579901    1.415466    0.970423
<bound method DataFrame.stack of      A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo>

Pivot Tables

