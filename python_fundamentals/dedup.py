#-*- coding: utf-8 -*-
#===============================================================================
#         FILE: dedup.py
#        USAGE: ./ 
#  DESCRIPTION: dedup a project to remove duplicates  
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED:  
#     REVISION: Tue Jun 20 13:11:19 PDT 2017
#===============================================================================
import pandas as pd
import numpy as np

# Demonstration of the dedupping capabilities in python and pandas
print("\nFirst we are going to create some dummy data\n")
#We need to have several rows that have repeating infomration in them 
df = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

print(df)

df2 = df.drop_duplicates('E')

print(df2 )

