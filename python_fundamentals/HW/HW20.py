#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: HW20.py
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
#      VERSION: 1.0.2
#      CREATED: Wed Jul 26 19:51:27 PDT 2017
#     REVISION: Fri Jul 28 16:08:44 PDT 2017
#===============================================================================


from sys import argv

script, input_file = argv
#Ginsberg_I.txt


def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(210)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
#angelheaded hipsters burning for the ancient heavenly connection to the starry dynamo in the machinery of night,

current_line = current_line + 1
print_a_line(current_line, current_file)
#who poverty and tatters and hollow-eyed and high sat up smoking in the supernatural darkness of cold-water flats

current_line = current_line + 1
print_a_line(current_line, current_file)
#floating across the tops of cities contemplating jazz,

