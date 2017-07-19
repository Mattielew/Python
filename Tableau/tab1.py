#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: tab1.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: 
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
import csv

f = open('/Mattie/Documents/Github/Python/Tableau/cameras.csv') 

csv_f = csv.reader(f)

for row in csv_f:
    print(row)

f.close() 


str = "(40.714353, -74.005973)"
tuple(float(x) for x in str.strip('()').split(','))

print(str)
