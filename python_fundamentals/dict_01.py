#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: dict.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: dictionaries 
#
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED:  
#     REVISION: Tue Jun 20 13:10:50 PDT 2017
#===============================================================================

#Dictionaries in python

mystuff = {"one":"Spiderman","two":300000,"three":"tres","four":"Apples","five":5}

print(mystuff['one'])
#this behaves differently than the way that typical lists do.

print("mystuff['two'] :",mystuff['two'])
#you can edit sections from a dictionary with a

#Dict keys are immutatble, meaning you cannot change them dynamically 

#this is how you delete from a dictionary
del mystuff['four']
print(mystuff)

print(len(mystuff))

dict = mystuff.copy()
print(dict)
del dict['five']
print(dict)
print(mystuff)
#Copies are not the same thing as clones, if you change the copy then you change
#just that version, and what if you change the origin?

print(dict.keys)

dict.update(mystuff)
print(mystuff)


dict_1 = {'foo' : 100, 'bar' : 200, 'baz' : 300}
ser_3 = Series(dict_1)
print(ser_3)


