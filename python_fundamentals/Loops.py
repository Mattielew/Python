#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: Loops.py
#
#        USAGE: Examples of loops in Python 
#
#  DESCRIPTION: New information for Loops
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
#     REVISION: ---
#===============================================================================
 
words = ["red","cat","blue","hat","matt"]
print(words)
print ("""okay, so we are going to loop over the list, nothing fancy.""")
print("""
for i in words:\n
    print(i, 'is a fun thing')\n
""")
for i in words:
    print(i, 'is a fun thing')
# loops can be really useful, you can do all sorts of creative things to iterate
# over many tedious tasks 
print("""
for i in words:\n
     print(i, len(i))\n
""")
for i in words:
     print(i, len(i))

print(words)
print("""
for i in words:\n
    if len(i) >= 4:\n
        print("neat, the string", " ",i, " is greater or equal to 4")\n
    else:\n
        print(i, len(i))\n
""")

for i in words:
    if len(i) >= 4:
        print("neat, the string", " '",i, "' is greater or equal to 4")
    else:
        print(i, len(i))

print("you can also slice out a portion of your list with a loop")
for w in words[:2]:
    print(w)

#So this is going to be a different way to do some loops
words = [1,2,3,4,5,6]
print(words[1])
for index in range(len(words)):
    print("current word",words[index])

#This is another example of prime number looping
for num in range(0,200):
    for i in range(2, num):#use to iterate over the factors of the number
        if num %i == 0:#used to determine if the numbers prime
            j=num/1
            print("%d equals %d * %d" % (num,i,j))
            break
    else:
        print(num, "is a prime number")


print("\npretty neat")
for x in range(0,3):
    print("We're on time %d" % x)


#now loops are dangerous too, we are going to create an infinite loop now 
#be careful! 
#x = 1
#while True:
#    print("To infinitty and beyond! We are getting closer now, we are on %d now"
#            % x)
#    x+=1

#The range function has a series of parameters, a start a stop, and incriment 
for i in range(5):
    print(i)


print("\n")

#two params 
for i in range(3, 6):
    print(i)

print("\n")
# three params
for i in range(4, 10, 2):
    print(i)

print("\n")
#going backwards on the range
for i in range(0,-10,-2):
    print(i)

print("\n")

my_list = ["list1","list2","list3","list4","list5"]
my_list_len = len(my_list)
for i in range(0,my_list_len):
    print(my_list[i])

for element in [1,2,3]:
    print(element)
print("\n")
for element in (1,2,3):
    print(element)
print("\n")
for key in {"one":1,"two":2}:
    print(key)

for char in [1,2,3]:
    print(char)

for line in open("README.md"):
    print(line, end='')

