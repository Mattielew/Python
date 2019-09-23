#-*- coding: utf-8 -*-
#===============================================================================
#         FILE: euler1.py
#        USAGE: Practice
#  DESCRIPTION: Euler1 
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Sat Jul  1 09:01:22 PDT 2017
#     REVISION: ---
#===============================================================================
#project 1 in the euler series 
x = 0
numbers = []
while x < 1001:
    print ('x is (%s)' % x)
    numbers.insert(0,x)
    x = x+1
print(numbers)
sumnum = sum(numbers)
print(sumnum)
