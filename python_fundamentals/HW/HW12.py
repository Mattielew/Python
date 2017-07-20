#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW12.py
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
#With the restrucuring of the input command, we can streamline the previous program, less lines are good.
name = input("Name? ")
age = input("how old are you? ")
height = input("how tall are you? ")
weight = input("how much do you weigh? ")

print("Okay %s, so you said you are %s years old, you are %s tall, and you weigh %s" % (name , age , height, weight))


