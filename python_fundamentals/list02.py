#from pprint import pprint
#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: list02.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: lists 02 
#
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Matthew Lewis 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Wed Jun 21 08:13:33 PDT 2017
#     REVISION: Tue Jul  4 12:56:38 PDT 2017
#===============================================================================


print("Lists continued")
print("==================================================")


x = list(range(0,102,2))
print(x)
#Lists can easily help you condense information into a few lines.
#what previously took a long time to write out,you can program to generate.
y =[["I","blue","green"],[1,3,2],[3,"orange","am"," "],[1.5,9.2,3.4],["more","to","learn"]]
print(y[0][0]+y[2][3]+y[2][2]+y[2][3]+y[4][2]+"ing!")
#of course, the amount of time required to come up with the code could have been
#used to write out the information, be mindful of when elegant solutions are
#just, wastes of time. 

x = [1,2,3,4,5,6]

#Acessing elements continued
#the syntax for accessing elements in the list is the same as the command for
#accessing characters in a string


# this is intesting, any expression that evaluates to an integer can be used as
# an index
#so if you do some math and generate an output that can reference your list

#the difference, -1 generates a reverse reference to the last element in the
#list 
print(x[2-3])

#use some loops in your interations and references to create some interesting
#output
#positive iteration to element 3 on the list 3
print(x[2-0])
horsemen = ["War","Famine","Pestilence","Death"]
for i in [0,1,2,3]:
    print("The horseman of " + horsemen[i])

x = list(range(2,10))
print(x)
#this is going to print out all elements in the list going up to but not
#including element 3 
print(x[:3])
#This is going to be a listing of all elements after Elm#3 
print(x[3:])

#add up all the elements of the list 
print(x)
#you can also use the lists to do some math here we take the sum with the
#<sum>function 

y = sum(x)
print(y)

z = x.append(5)
print(x)

def func(x):
    print(x)

def func_2(x):
    return 2*x

print(func_2(3))

a = [1,2,3,4]
b = [5,6,7,8]
print("The lists we are going to compare are")
print(a,"\n",b)
z = map(func, a)
print(z)

x = [[0,1],[2,3],[4,5]]
print(x)

#Check to see if two lists have at least one common element
d = len(set(a) & set(b))>0
#add some fun logic 
if d == False:
    print("aiyaiyai incorrect")
else:
    print(d)

if 6 in a or b:
    print("yes")
else:
    print("no")

z = a.count(2)
print(z, " is the count of occurrances of '2' in list(a)")

c = [x for x in a if not x in b]
print(c)

#listing the differences between the lists.
d = list(set(a).difference(*[set(a) for i in b]))
print(d)

#Now combining loops with lists
words = ["fig","hat","2000","several","things","to","iterate","over"]

for w in words:
    print(w, len(w))


result = []
for x in range(10):
    for y in range(100):
        result.append((x,y))
#print(result)


squares=[]
for x in range(10):
    squares.append(x**2)
print("These are the squares")
print(squares)

#Same thing but this is with list-comprehension 
squares = [x**2 for x in range(10)]
print(squares)

