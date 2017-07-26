#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW18.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: This is going to be an example of the functions in python
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

#First we name the function with 'def'
#on the same line as def command we name the function and provide the arguments 
#line 2 enters the mini commands that we eant to create inside the function 
#This takes several arguments(2 actually )
def print_two(*args):
    arg1, arg2 = args
    print("arg 1 : %r, arg2: %r" % (arg1, arg2))

#ok, that *args is actually pointless, instead we could do this : 
def print_two_again(arg1, arg2):
    print("arg 1 : %r, arg2: %r" % (arg1, arg2))

#this just takes one argument 
def print_one(arg1):
    print("arg 1: %r " % (arg1))

#this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Matt", "Moo")
print_two_again("Matteo", "Matwotwo")
print_one("First")
print_none()

