#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW17.py
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


from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print("Copying from %s to %s" %(fromfile, tofile))

input = open(fromfile)
indata = input.read()

print("The input data is %d bytes long" % len(indata))

output = open(tofile, 'w')
output.write(indata)

print("Allright, all done")

output.close
input.close
