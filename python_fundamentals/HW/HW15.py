#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW15.py
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
script, filename = argv
#reading files 

txt = open(filename)

print("Here is your file %s" %(filename))

print(txt.read())

print("I'll also ask you to type it again:")
file_again = input("> ")

txt_again = open(file_again)


print(txt_again.read())

