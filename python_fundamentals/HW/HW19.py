#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW19.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: More functions with variables and some math 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Wed Jul 26 18:54:29 PDT 2017
#     REVISION: ---
#===============================================================================
from time import sleep

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % (cheese_count))
    print("You have %d boxes of crackers!" % (boxes_of_crackers))
    print("Man that's enough for a party")
    print("Get a blanket.\n")

print("We can just give them functions directly")
cheese_and_crackers(20, 30)

print("or we can use variables")
cheese_count = 30
boxes_of_crackers = 20

cheese_and_crackers(cheese_count, boxes_of_crackers)

print("And we can combine the two: Variables and Math")
cheese_and_crackers(cheese_count + 1000, boxes_of_crackers + 1000)


number = input("pick a number between 1 and 30")
def cool_stuff(number):
    print("Your number is: %r" %(number))    
    print("Isn't that SO cool?????")
    sleep(2)
    print("...")
    sleep(1)
    print("Man, some people are hard to please.")


cool_stuff(number)

