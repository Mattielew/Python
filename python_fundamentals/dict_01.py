#-*- coding: utf-8 -*-
#===============================================================================
#         FILE: dictionary.py
#        USAGE: practice
#  DESCRIPTION: dictionaries
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

mystuff = {"one":"Batman","two":300000,"three":"tres","four":"Apples","five":5}

print(mystuff['one'])
#this behaves differently than the way that typical lists do.

print("mystuff['two'] :",mystuff['two'])
#you can edit sections from a dictionary with a

#keys are immutatble, meaning you cannot change them dynamically 

#this is how you delete from a dictionary
del mystuff['four']
print(mystuff)

print(len(mystuff))

dictionary = mystuff.copy()
print(dictionary)
del dictionary['five']
print(dictionary)
print(mystuff)
#Copies are not the same thing as clones, if you change the copy then you change
#just that version, but what if you change the origin?

print(dictionary.keys)

dictionary.update(mystuff)
print(mystuff)


