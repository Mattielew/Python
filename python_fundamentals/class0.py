#!/usr/bin/python
#-*- coding: utf-8 -*-
#===============================================================================
#
#         FILE: class0.py
#
#        USAGE: ./ 
#
#  DESCRIPTION: This is going to be a file exploring classes 
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


class MyClass:
    """A simple example of a class"""
    def __init__(self):
            self.data = []

    """A method in the class"""
    def f(self):
        return 'hello world'


class Complex:
    def __init__(self, realprt, imgprt):
        self.r = realprt
        self.i = imgprt

x = MyClass
print(x.f(x))

print("\nNow, let's add some inputs to return back to us")

z = Complex(0.3,0.4)
print(z.r, z.i)


#This requires one positional argument(self)
#Is there a way that you can all no arguments?

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name#instance variable uniique to each instance 

d = Dog('Fido')
b = Dog('Bruce')
c = Dog('Spaghetti')

print(d.kind) #kind for all the classes
print(d.name) #unique to just the instance 

class Dog:
    kind = 'canine'

    tricks = []

    def __init__(self, name):
        self.name = name#instance variable uniique to each instance 

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.name)

d.add_trick('play dead')
e.add_trick('roll over')

print(e.tricks)


#let's do something funky now 
#define method outside the class
def fl(self, x, y):
    return max(x, x+y)

#then we will call the method inside with some substitution
class C:
    f = fl

    def g(self):
        return 'hello world'

    h = g

c = C.f('carl',1,2)
print(c)
z = C.h('carl')
print(z)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

x = Bag()
print(x.__class__)
x.add(1)
y = x.addtwice(1)
print(y)


#calling an empty class and then entering information into it
class Employee():
    pass

john = Employee()
# This is going to generate a new employee instance 
#fill in the fields that will list out the records 
john.name = 'John Doe'
john.dept = 'Computer Lab'
john.sal = 100000
print(john.name, "gets an average salary of $",john.sal, ".00 per year")
print("Not bad", john.name)




#Fruits that demonstrate the different instances of a class 
class Fruit:
    #common to all types of fruits
    def __init__(self, name, color):
        self.name = name
        self.color = color

x = Fruit("banana","yellow")

print(x.color)


#This is going to be a file for the examples of classes in python


class MyClass:
    """A simple example of a class"""
    def __init__(self):
            self.data = []

    """A method in the class"""
    def f(self):
        return 'hello world'


class Complex:
    def __init__(self, realprt, imgprt):
        self.r = realprt
        self.i = imgprt

x = MyClass
print(x.f(x))

print("\nNow, let's add some inputs to return back to us")

z = Complex(0.3,0.4)
print(z.r, z.i)


#This requires one positional argument(self)
#Is there a way that you can all no arguments?

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name#instance variable uniique to each instance 

d = Dog('Fido')
b = Dog('Bruce')
c = Dog('Spaghetti')

print(d.kind) #kind for all the classes
print(d.name) #unique to just the instance 

class Dog:
    kind = 'canine'

    tricks = []

    def __init__(self, name):
        self.name = name#instance variable uniique to each instance 

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.name)

d.add_trick('play dead')
e.add_trick('roll over')

print(e.tricks)


#let's do something funky now 
#define method outside the class
def fl(self, x, y):
    return max(x, x+y)

#then we will call the method inside with some substitution
class C:
    f = fl

    def g(self):
        return 'hello world'

    h = g

c = C.f('carl',1,2)
print(c)
z = C.h('carl')
print(z)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

x = Bag()
print(x.__class__)
x.add(1)
y = x.addtwice(1)
print(y)


#calling an empty class and then entering information into it
class Employee():
    pass

john = Employee()
# This is going to generate a new employee instance 
#fill in the fields that will list out the records 
john.name = 'John Doe'
john.dept = 'Computer Lab'
john.sal = 100000
print(john.name, "gets an average salary of $",john.sal, ".00 per year")
print("Not bad", john.name)

#Fruits that demonstrate the different instances of a class 
class Fruit:
    #common to all types of fruits
    def __init__(self, name, color):
        self.name = name
        self.color = color

x = Fruit("banana","yellow")

print(x.color)



print("hey! we are moving faster!")

