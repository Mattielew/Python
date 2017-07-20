#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW10.py
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

tabby_cat = "tabcat\n=======\n\tI'm tabbed in\n"
persian_cat = "Persiancat\n=======\nI'm split\non a line.\n"
backslash_cat = "backslashcat\n=======\n\I'm \\ a \\ cat."

#long string mode means the carriage returns are included, no need to place in the string 
fat_cat = """
fatcat
======= 
I'm a cat who eats:
\t* Cat food
\t* Fishies
\t* Hamburgers
\t* Catnip
\t* Grass
"""

print("Cat's sound off\n======================\n")
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#Extra Credit:
#what other escape sequences are available ?
#\newline	Ignored
#\\	Backslash (\)
#\'	Single quote (')
#\"	Double quote (")
#\a	ASCII Bell (BEL)
#\b	ASCII Backspace (BS)
#\f	ASCII Formfeed (FF)
#\n	ASCII Linefeed (LF)
#\r	ASCII Carriage Return (CR)
#\t	ASCII Horizontal Tab (TAB)
#\v	ASCII Vertical Tab (VT)
#\ooo	ASCII character with octal value ooo
#\xhh...	ASCII character with hex value hh...


