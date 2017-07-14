#!/usr/bin/env python
#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: dedup.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: dedup a project to remove duplicates  
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
#     REVISION: Tue Jun 20 13:11:19 PDT 2017
#===============================================================================

# -*- coding: iso-8859-15 -*-

import pandas as pd
import numpy as np


# This is going to be a demonstration of the dedupping capabilities in python
# and pandas

print("\nFirst we are going to create some dummy data\n")
#We need to have several rows that have repeating infomration in them 
df = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

print(df)

print("""\nOkay, now that we have some data to work with we are going to be
        dedupping it, we will eliminate the duplicate values of the test row and
        the 'train' row, That way we will only have unique rows. \nNeat.\n""")
df2 = df.drop_duplicates('E')

print(df2 )

