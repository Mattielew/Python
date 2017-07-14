#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: ifthen.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: Exploring if then scenarios  
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Tue Jun 27 12:10:44 PDT 2017
#     REVISION: ---
#===============================================================================

#This is going to be a python script for if-then statements
#If-then statements in python can look a little funny, you don't have to explicitly state 'THEN'



z = True
while z == True:
    x = float(input("Please enter an int smaller than one, but greater than zero"))
    if x/3 < .5:
        print("Good job")
        break
    else:
        print("Mmm try again bub")
print("Moving on to the next example..\n")


#While loop 
flag = z 
while (flag)< 5: 
    print(flag)
    flag = flag + 1
print("Goodbye")
