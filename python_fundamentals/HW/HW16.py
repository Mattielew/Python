#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW16.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: Opening and writing to files 
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
#Takes input from the arguments you pass 

#assigns two variables you intend to pass, script and filename - this means your script expects 2 inputs
script, filename = argv

#print to console status pass filename to be edited 
print("We're going to erase %r" % (filename))
#provide operator opportunity to alter the course of the edit
print("If you don't want that, press CTRL-C (^C).")
print("If you DO want that, hit RETURN")

#where the user proceeds with command to terminate or continue
input("?")

#If script is not torched, then the script will open the listed filepath assigned from argv
print("Opening new file...")
#opening targetfilepath with open method -write command 
target = open(filename, 'w')


#print("truncating the file, goodbye!")
#target.truncate()
#  NOTE -- the open command already truncates files, there's no need for this command it's just Zed throwing some salt
#  in there for his students to catch

print("Now I'm going to ask you for three lines.")
#new variable assignments to write to the file with
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

#accessing the opened file with write command, adding line of the recent variable assignments, with a carriage return
target.write(line1)
target.write("\n")
#once again
target.write(line2)
target.write("\n")
#once again
target.write(line3)

print("And finally, we close it.")
#assigned file passed close method
target.close()
