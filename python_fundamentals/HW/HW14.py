#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW14.py
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

script, username = argv
prompt = '=======>'
prompt2 = '>>'
prompt3 = ':) '
print("Hi %s, I'm the %s Script" % (username, script))
print("I' like to ask you a few questions")

print("Do you like me %s?" % (username))
likes = input(prompt)

print("Where do you live %s?" % (username))
lives = input(prompt2)

print("What kind of computer do you have?")
comp = input(prompt3)

print("""

Allright, here's what you said:
    * %r to liking me,
    * %s is your stomping-grounds,
    * %s is your mean-machine.
""" % (likes, lives, comp))

