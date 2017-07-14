#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE:  split.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: split a long string into a list using the whitespace, then have some fun with it.
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
#Place it into a list of words
#ignore the whitespaces 
#reference from the list 

words = """Tropical Storm Leslie was a weak, short-lived tropical cyclone that was never well-organized; however, its precursor was
costlier than any other tropical cyclone in the 2000 Atlantic hurricane season. The twelfth named storm of the season,
Leslie formed on October 4 over eastern Florida as a subtropical cyclone, out of a trough of low pressure. Strengthening
over open waters, it attained enough tropical characteristics to be reclassified as Tropical Storm Leslie on October 5.
The storm reached peak winds of 45 mph (75 km/h) before wind shear weakened it, and on October 7 transitioned into an
extratropical cyclone over the open Atlantic Ocean. Leslie lasted three more days before losing its identity.
The precursor to Leslie produced torrential rainfall across Florida, peaking at 17.5 in (440 mm). The flooding damaged
thousands of houses and caused three indirect deaths. Damage in southern Florida totaled $950 million (2000 USD),[nb 1]
around half of which was from agricultural damage. After the flooding, portions of south Florida were declared a
disaster area. Because of the limited impact as a tropical cyclone, the name Leslie was not retired in the Spring of
2001."""

#list = [words.strip() for x in words.split(' ')]

L = words.split(' ')
print(L[2]) #only selects char not word, chop out by spaces #bingo. 

print(L)




