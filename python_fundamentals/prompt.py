#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: prompt.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: prompt  
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
#     REVISION: Wed Jun 21 08:18:13 PDT 2017
#===============================================================================

x = int(input("Please enter a value:"))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print('Zero')
elif x == 1:
    print("Uno")
else:
    print("More")

