# What is class?
"""
1.In python Everything is an object
To create objects we required some model or plan
or Blueprint, which is nothing but the class.
2.We can write a class to represents the properties
(attributes) and actions.
3.Proreties can be represented by Variables.
4.Action can be represented by method
5.Hence, class contains both Varibles and methods.
"""

# Topic How to Define class in python
"""
We can define class by using class keyword
synatx:-->

class className:
    '''doc string'''
    varibles:--instance variables , static , local variables
    method:--> instance methods, class method, static methods

"""
# eg
# class student:
#     """ This is student class"""
#     print("This is student class")


# Constructor concept

# class student:
#     def __init__('self'):
#         print("This is a constructor")

# s = student()
# print(s)

"""
Note:- The main purpose of  the constrctor is to declare
and initialize instance variables.
"""
# class student:
#     def __init__('self', name , rollno):
#         'self'.name = name #Instance Variable
#         'self'.rollno = rollno #Instance Variable
#         # one way of declaration
#         # print(f"Name of the student--{'self'.name}")
#         # print(f"Roll no of the student--{'self'.rollno}")
#         print(id('self'))

# s = student("Atul", 77)
# print(s)
# print(id(s))
# # second way of declaration or calling
# print(f"Name of the student--{s.name}")
# print(f"Roll no of the student--{s.rollno}")

"""
Name of the student--Atul
Roll no of the student--77
"""
#  Topic 'self'

"""
1. Within the class to refer current objects python provides on 
implict variable action is nothing but the 'self'.
2.'self' variable always point to current object.
3.'self' variable is the argrument for the constructor and instance methods
4.By using 'self' we can declare instance varibles.
5.We can use 'self' within the class only and 
from outside of class cannot use.
6.Instead of ''self'' we can use any name but recommended to use 'self'.
7.At the time of calling constructor and instance methods we are not
required to provide values for ''self'' varibles.PVM it'self' responsible
to provide value.
"""

# Q Eg 

# class student:
#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks

#     def info(self):#instance method
#         print(f"Stundent Name: {self.name}")
#         print(f"Stundent Roll No: {self.rollno}")
#         print(f"Stundent Marks: {self.marks}")

# s1_object = student("Akash", 21, 91)
# s1_object.info() #print data
# """
# Stundent Name: Akash
# Stundent Roll No: 21
# Stundent Marks: 91
# """
# s2_object = student("Ankit", 22, 92)
# s2_object.info() #print data
# """
# Stundent Name: Ankit
# Stundent Roll No: 22
# Stundent Marks: 92
# """

#  WAP to perform addition , subtraction, division of 2 nos 
# using class , function and object.

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1= num1
#         self.num2= num2
#     def addition(self):
#         print("Addition:", self.num1+self.num2)
#     def subtraction(self):
#         print("Subtraction:", self.num1-self.num2)
#     def division(self):
#         print("Division:", self.num1//self.num2)

# obj = Calculator(28, 12)
# obj.addition()
# obj.subtraction()
# obj.division()

# """
# Addition: 40
# Subtraction: 16
# Division: 2
# """

class calulator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 

    def add(self):
        return f"Addition of to num: {self.num1 + self.num2}"
    
    def sub(self):
        return f"Sub of to num: {self.num1 - self.num2}"
    
    def mul(self):
        return f"Mul of to num: {self.num1 * self.num2}"
    
    def div(self):
        return f"Divisiom of to num: {self.num1 / self.num2}"


a = calulator(20,30)
print(a.add())













