#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: conversions.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: conversions  
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED:  
#     REVISION: Wed Jun 21 08:13:01 PDT 2017
#===============================================================================



print("This is a regular old integer")
x = 2
print(x)

print("Now let's convert that integer into a floating point number.")
x = float(x)
print(x)
print("neat")

print("Now, how about a byte?")
x = bytes([2])
print(x)


print("""Now, what if I wasn't sure about the type that I was making?")
print("I could tae a look at the data type of a variable that I have assigned by
        examining it with the type() command.""")

print(type(x))



