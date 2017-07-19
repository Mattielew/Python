#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: pandas1.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: Demo of pandas  
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED:  
#     REVISION: ---
#===============================================================================


ser1 = Series([ 1,1,2,-3,-5, 8, 13])
print(ser1)

ser_2 = Series([1, 1, 2, -3, -5],index=['a', 'b', 'c', 'd', 'e'])

print(ser_2)
