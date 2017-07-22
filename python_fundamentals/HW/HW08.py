#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW8.py
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
#Tha variablez dawg
x = 'Matthew'
y = 'Crazy'
z = "coffee fiend"
a = "TRUE"
b = "FALSE"
formatter = "%r %r %r %r %r"
formateL = "%s %s %s %s %s "
firmatiL = "%s is a %s %s"
print(formatter %(1,2,3,4,5))
print(formatter %("one","two","three","four","five"))

print(formateL %(a,b,a,a,b))
print(firmatiL %(x,y,z))

