#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: string.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: Practice with strings and variables 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Mon Jun 26 12:17:47 PDT 2017
#     REVISION: ---
#===============================================================================

lucky = 7 #assigns the number 7 to the string 'lucky' 
print(lucky)

changing = 9 

changing = 15
 
print(changing)
red =5 
blue = 7

print(red + blue)
# we can perform math on strings and variables 

print(red-1) #equivalent to 5-1 ==4 
#A string is simply a list of characters in order 
# 'hello' actually is a list of chars H E L L O referenced together 
# there are no limits to the number of characters you can have in a string 

#There are three ways that you can reference a string in python: 
#single quotes : 'a string'
#double quotes "another type of string"
#triple quotes for longer strings """This is a really long string that Has really, no real limit to it. """"
#single double, or triple quotes 
#You can use backlash commands for escape characters to allow a quotation to be included inside a string
this = "\"This is a real string with quotes\" --Matthew said."
print(this)
x = 'I\'m a var' 
y = 300000
print("I am going to use a changing variable, my name is %r" %(x))
print("I\'m gonna use the same pattern with a different variable, my name is %r" % y)

