# Day 19

"""
Functions

In python supports 2 types of function
1> Built in Function
2> User Defined Function


1> Built in Function:--> Predefined python functions is nothing 
but the  Built in Function.
eg --> print(), len(), id(), input(), type()..etc

2>User Defined Function:->Devloped by programmer to perform
some tasks are called user defined function.

DRY--> Dont Repeat Yourself

syntax:-- To creare User Defined Function

def functin_name(parameters):
    '''doc string'''
    ----------------
    ----------------
    return Value

Note:-- While creating a functions we can use 2 keywords
1. def (Mandtory)
2. return (optional)
3. We cant use exisiting function name to create user defined function
4.pareters(optional)
5.The function should not define with the numbers or the special characters
except underscore(_).
"""

#  Wap to to wish Good morning

# def wish_me():
#     print("Good Morning")


# wish_me()# calling this function as many time that we want
# wish_me()
# wish_me()

# Topic Parameters 
"""
1.Parameters are inputs to the function.
2.If a function contains parameters, then at the time of calling
compulsary we should provide the values otherwise 
we will get error.
"""

# Q Write a function to take name of the student as an input
# and print with message by name

# def wish_me(name):
#     print("Hello", name, "Good Morning")

# wish_me("Akash")
# wish_me("Atul")
# wish_me("Mia")
# wish_me("John")

"""
Hello Akash Good Morning
Hello Atul Good Morning
Hello Mia Good Morning
Hello John Good Morning
"""

# method2
# name = input("Enter the Name of the student: ")
# def wish_me(name):
#     print("Hello", name, "Good Morning")

# wish_me(name)

# Wap to create function square of no and no is taking from keyboard

# def squareIt(num):
#     print("Square of a number ", num*num)

# num = int(input("Enter a no: "))
# squareIt(num) #Square of a number 49

# Topic Return Statement

"""
1.Function can take input values as a parameter
and execute business logic and returns output to the
caller with return statement.
2.We can return not only the parameters but also we 
can return the defined variables and the datasets.
Note:--> If we are not writing return statement
then default return value is None.

"""

# def squareIt(num):
#     return num*num

# number = int(input("Enter the number: "))
# First way of calling via object
# obj = squareIt(number)
#second way of calling via Print satatement
# print("The square is: " ,obj)
# print("The square of Number: ", squareIt(number))


# wap to create function of additon of 2 no's and no is taking from keyboard

# def addition (num1, num2):
#     return num1 + num2

# num1 = int(input('enter a num1 : '))
# num2 = int(input('enter a num2 : '))

# print("addtion of 2 no", addition(num1,num2))


