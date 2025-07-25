#  ADD of 2 no

# C Lang 
"""
include<stdio.h>
int a=10, int b=30, int c
c = a + b;
printf("sum", c)
"""

# Java code
"""
Class Test{
Public static void main(String args[]){
int a=30,b=40,c;
c = a+b
System.out.println("Sum", c)
}
}

"""

# Python Code
# print(10+20)

# Baisic Flow will covere
"""
Basic Python
Jitna code 
# oops 
Problem solving approch 
DSA
Leetcode at least 250+ problems will sovle
"""
# ---------------------------------------------------------------
# Data Types

# ex int ,float, bool, str, complex imp
#  list,tuple, range, set, dict

# 1 int data type  and float

# Q WAP to calculate area of circle 
"""
pi = 3.14
print(type(pi))
r=2
print("radius", type(r))
ans = 0
ans = pi*(r*r)
print("Area of Circle", ans)
"""

"""
We can represent the int values in follng ways
1> Decimal Form (base 10) 0-9  ex a = 10, a=99 a =100
2> Binary Form (Base 2) 0 and 1 [ob or 0b] x = 0B 1111
3> Octal Form (Allow digits 0 to 7) eg x= 0o123
4> Hexa decimal form (Base 16) eg 0x or 0x x=0xFace # 64206 
"""

# 3>  String Data Type
# data1 = "Akash"
# print(data1)
# data2 = "Ankit"
# print(data2)
# data3 = "" # imp to multiple problems
# print(data3)

# Q1 wap to Concatinate the 2 strings
"""
data1 = "Akash"
data2 = "Ankit"
print(data1+data2)

"""

# 4> Bool Data Type (True=1 False=0)
# ex
"""
a=10
b=200
c = a<b
print(type(c))

"""
""" 
a = 50
b = 60
print(a==b)
"""

# 5> complex Data type (a + bj)
"""
a = 10+20j
print(type(a))
"""
# --------------------------------
# Q1 wap to solve area of triangle (1/2* b*h)
"""
base = 20
height=30
half = 1//2
ans = half*base*height
print("type of ans", type(ans))
print("Area of Triangle", ans)
"""


# Q2 Write a program for 
"""
a = 25
b = 15.40
# ans= a*2 + 2ab + b*2 

ans = a*a + 2 * (a*b) + b*b
print("Quadratic equation", ans)

"""

# DAY 2
# Type Casting 
"""
Convert one type to another type.This conversion is called 'Typecasting'
"""
# ex int ,float, bool, str, complex imp

# 1> int

# int(True)  valid
# int(10+20j) invalid
# int('10') valid
# int('123.345') invalid rare case
# int('data') invalid
# int(10.5) valid

# Note: Any type  to int except Complex.

# 2>float
# float(10) valid
# float(10.678) valid
# float(True) valid
#  float(10+20j) invalid
# float('test') invalid
# float('True') invalid IQ

# Note: str value should contain either int type or float type  and should be in 
# Base 10

# 3> complex 
# form 1> Pass the single Value
# complex(10) valid
# complex(False) valid
# complex('10') valid
# complex(10.5) valid
# complex('10.5') valid
# complex('ten') invalid

# form2  complex(x,y)  Pass the two parameters/values:
# complex(10,-2) valid
# complex(10,2) vaid
# complex(True, False) Valid

# 4> Bool (True=1, False=0)

# bool(0) valid False
# bool(1) valid True
# bool(0.123) valid True
# bool(0.000) False
# bool(0+0j) False
# bool(0+1j) True
# bool('') False
# bool('test') True
#  Note  Using bool we can convert all the data types into the bool value.

# 5> str
#  Note  Using str we can convert all the data types into the str value.

# str(10) '10'
# str(10.5) '10.5'
# str('10.5') '10.5'
# str(True) 'True'
# str(False) 'False'
# str(10+20j) '(10+20j)'

#  How to read input values from Key-board

"""
C- Lang
int a;
scanf(a, %f);
"""

"""
Java Lang
int a;
int b;
Scanner sc = new Scanner(System.in);
int a = sc.nextFloat();
b = sc.nextInt();
"""

"""
x = float(input("no1: "))
print(type(x))
y = float(input("no2: "))

print("Sum", x+y)

"""

# Q WAP to calculate area of triangle where input taking from Key-Board i.e B&H

"""
half = 1/2 

# base= 20
# height =30

base = int(input("Enter the base of triangel: "))
height = int(input("Enter the Height of triangel: "))

ans = half*base*height
print("Area of triangle: ", ans)
print(type(ans))
"""

############## Fundamental Data Types VS immutability ##############
"""
mutable = Changable
immutable = Non-Changable

"""
# a1 = 10
# a2 = 10

# Note : Performance and Memory Utilization Improved
# id(a1) 140725996086344
# id(a2) 140725996086344

# immutability: Once we create an object, we cannot perform 
# any change in that object

"""
'is' operator
"""
# ex: 
# a1 = 10
# a2 = 10
# a3 =11
# a1 is a3 False
#  a1 is a2 True

# Day3 Operators
"""
Arithmatic Operator 
Comparision operator
Logic Operator
Bitwise operator
Assignment operator
Special operator
"""

# 1> Arithmatic Operator
"""
+,-,*/,%
/--> Division Operator
//--> Floor Division Operator
**--> Power (Raise to the Power)
"""

"""
a = 7
b = 2

print("Normal Division",a/b)
print("Floor Division", a//b)
"""

# 2>  Bitwise operator (not for Interview)
"""
&,|,^,~,<<,>>

This operator only for int and bool values

"""
# print(4.5 & 5.5) invalid
# print(4&5) Valid
# print(True&True) Valid

# 3> Assignment operator (=)

"""
Assign the value 
ex x=10
x+=10 ----> x = x + 10

[+=, -=, *=, /=, %=, //=, **=,
&=, |=, ^=, >>=, <<=] --> Valid casese
"""

# Note : In python Inc and Dec operator are not allowed
"""
[++x , --x, x++, x--]---> Invalid cases
but ++x and --x --> provides sign symbol only
"""

# 6> Special operator imp code 
# 1> Identity Operator
# 2> Membership Operator

# 1> Identity Operator
"""
It use for the address comparision (is, is not)
"""
"""
a=20
b=30
print(a is not b)---> False
"""

# x=30.5
# y=30.5
# print(x is y)
# print(x==y)---> Comparing Content

"""
# Q What is == operator vs 'is' operator 

Ans:-- a==b Content comparison
       a is b Reference comprarison(address)
""" 

# 2> Membership Operator (in, not in)
"""
To check whether the given object present in given colllection.
(String, List, Set, Tuple, Dict)

in:-> Its Return True when the obj present in the collection

not in :-> Its Return True when the obj present not in the collection
"""

# data = "I am Aakash, learing python is very easy"

# data2 = "10 20 30 50"
# print(type(data2))

# print("Data2", str(20) in data2)

# print('z' in data)
# print('m' in data)
# print('x' not in data)

# data3 = [10,20,30,50,"Ankit"]
# for i in data3:
#     if i==30:
#         print(True)
#     else:
#         print(False)
# print(30 in data3)
# print("Aakash" in data3)

# 7> Ternary Operator code imp
"""
Synatx:-

  x = First Value if Condition else second Value

If condition is True then First Value will be consider else
Second value will be consider
"""

# x = 4 if 10>20 else 5 
# print(x)

# a,b=10,20
# a=10
# b=20
# x= 30 if a<b else 40
# print(x)


#  WAP to print Minimum Value and i/p Taken from Keyboard
"""
n1 = int 40
n2 = int 50
conditon n1<n2
"""

# N1 = int (input (" Enter 1st Number:  " )) 
# N2=  int (input (" Enter 1st Number:  " ))
# X = N1 if N1 < N2 else N2
# print(X)

#  Nesting of Ternanry Operator

# Q find  minimum of 3 nos
"""
first = int (input (" Enter 1st Number:  " ))
second = int (input (" Enter 2nd Number:  " ))
third = int (input (" Enter 3rd Number:  " )) 

    #    30     30<40             30<50            40       40<50               50
min = first if first<second and first<third else second if second<third else third 
print("minimum value", min)
"""

# Day 4
# Logical Operator

"""
In python there are 3 types of logical operators i.e 
and, or, not
"""
# ex
"""
first = True
second = False

print(first and second)
print(first or second)
print(not second)

"""

# Input and Output Statements

# 1> input()
"""
When we want to insert value from the keyboad
then will use this function.
"""
# eg1
"""
data = input("Enter some data")
print(type(data))
print(data)t
"""

# eg2 Q Read 2 no from keyboard and print their sum
"""
x = (input("Enter some data1 "))
y = (input("Enter some data2 "))
print(type(x))
i = int(x)
print("type of i", type(i))
j = int(y)
print("The Sume", i+j)
"""

# method3
# print("The sum of 2 no", int((input("Enter some daa1 "))) + int((input("Enter some data2 "))) )

# Q  WAP to read employee data i/p taken from keyboard and print that data
"""
eno, ename, esal, eadd, married(True or False)

eno = int(input("Enter Employee Number: "))
ename = input("Enter Employee Name: ")
esal = float(input("Enter Emplyee Salary: "))
eadd = input("Enter Employee Address: ")
# married = bool(input("is married"))
married = eval(input("married?[True|False]:" ))
# to convert into any type
print("Employee Number: ", eno)
print("Employee Name: ", ename)
print("Employee Salary: ", esal)
print("Employee Address: ", eadd)
print("Is married?: ", married)
"""


# eval()
"""
This function takes a string and evaluate the result
"""
# x  = eval("10+20+30")
# print(x) #60

# expr = eval(input("Enter some experession: "))
# print(type(expr))
# print("Ans", expr)

# Note Once we are using eval function then typecasting not required

# Output Statement (print)

# form1
"without any character it will print new line"
# print()

# form2 print(string)
"""
print("Akash")
print("Rahul\nBhai") #new line
print(3*"Vicky") # * and + operator allowed
"""
# Form 3 print() with variable no of arguments
"""
a,b,c = 40,60,80
print("The Values are: ", a,b,c) 
"""

# By default seperator space
"""
print(a,b,c, sep=',') 
print(a,b,c, sep=':') 
print(a,b,c, sep='=') 
"""

# Form 4 print() with end attribute
"""
print("Hello", end=" ")
print("Bhai", end=" ")
print("Kaisa", end=" ")
print("Hai")
"""

# Form 5 print(object) statement
# Pass any object like list(array), tuple, 
"""
list1 = [10,20,49]
tuple1 = (80,80,50)
print("list data", list1)
print("tuple_data", tuple1)
"""

# form 6:- print(Sting, int, list) or any no of arguments
"""
name = "Aaksh"
lan1 = "Java"
lan2 = "Python"
age = 20

print("Hello", name, "your age is", age)
print("you are learing", lan1 , "and", lan2)
"""


# form 7: print(formated string)
"""
syntax:  print("formated string%variable/list)
%d --> int
%f--> float
%s--> string

a=10
b=80.95
c="Akash"
print("Value of a is%d"%a)
print("Value of b is%f"%b)
print("Value of c is%s"%c)
"""


# Form 7 print() with replacement operator {} imp
"""
name = "Mia"
salary = 56565
bf = "Jonny"

print("Hello {} your salary is {} and your friend {} is  waiting".format(name,salary,bf))
print("Hello {} your salary is {} and your friend {} is  waiting".format(bf,salary,name))
"""

# Day 5 Slicing in String
"""
Slice means a piece
[] this opertator is called slice operator.
Which can use to retrive the parts of the string 
"""

# s="ATUL"
# print(s[0])
# print(s[-1])


# Note Left to right +ve
#      Right to left -ve

# print(s[1:])

"""
Syntax: 
s[beign:end:step]--> Return all characters from beign index to end -1 index
"""
  #  01234567
# s = "Learnings Python is very easy"
# print(s[1:7]) #1to6 index of character print kro bol rha hai
     # 1   7-1=6  
# s[beign:end]

# email = "mia@gmail.com"
# print(email[0:3]) #mia
# print(s[1:7])
# print(s[1:7:2])
# s[beign:end:step]
# print(s[1:7:3])

# s[beign:end:step]
# 0123456789101123

# s = "Learnings Python is very easy"
# print(s[1:19:2]) # earnings Python i
# erig yhni
# erig yhni

# s[beign:end:step]  Syntax
# print(s[2:23:3]) # aisyoiv tan
# print(s[2:23:3]) # ais yo i v aksh

# s = "arnings Python is very"
# aisyoiv

# print(s[4:15:4])
# "nings Python" 
#nst
#nst
# ---------
# print(s[:7]) # By default beign is zero(0)
# print(s[1:]) # end index is a last index of the string
# print(s[::]) # default string
# print(s[::0]) # slice step cant be Zero(0)
# print(s[::-1]) # reverse a string

# Day 6 Behaviour of Slice operators (IMP for interview)
"""
s[beign:end:step] syntax step 1,2,555+n
step value can be either +ve or -ve 
1> IF +ve then it should be forword direction(left to right)
and we have to consider "beign to end-1"
2> If -ve then it should be backword direction(right to left)
and we have to consider "beign to end+1"
# ATUL
Note:- 
1>In the forword direction if end value is zero(0)
then the result is always empty 
2>In the backword direction if end value is minus(negative)(-1)
then the result is always empty
"""
s = "abczdefgh"
# print(s[1:0:1]) #empty
# print(s[1:-1:-1]) #empty

"""
In forword direction:--->
Default value beign : 0
default value for end : length of string
default step value is : 1 eg [3:8:1]
"""

"""
In backword direction:--->
Default value beign : -1
default value for end : (length of string +1)
"""


# data = "abcdefghi"
# print(data[-1:-7:-1]) #beign to end+1
      # cdefghi
      # -1 to -7
      # -1 to -7+1  defghi
      # -1 to -6
      # op defghi


# data = "abcdefghijk"
# print(data[-1:5:1]) #beign to end-1 forward direction
#  -1 to 4 in forward direction

# print(data[-2:-8:-5])
# defghijk
# defghij
# -2 to -8 + 1 = > -2 to -7 end+1
# efghij 
# op=> je


# print(data[10:1:-1]) #beign end + 1  bcdefghij
#10 to 2
# out:-   kjihgfedc
# print(data[10]) 

# data = "abcdefghijk"
# print(data[6:1:-1]) #beign to end +1
# 6 to 1
# 6 to 1 +(end+1) = > 6 to 2
# 
# abcdefg
# cdefg
# op gfedc end +1

# data = "abcdefghijk"
# print(data[8:1:-1])
# ihgfedc 
# abcdefghi end+1 8 to 2
# cdefghi

# data = "abcdefghijk"
# print(data[1:6:-1])
# start 1 and need to revers
# print(data[-1:-7:-1])
# -1 to -6
# efghijk
# fghijk
# print(data[1:0:-1]) #beign to end +1

# Day 7 len() in-built Function

# Q  To find the no of characters present in the string
"""
data =  "Atuls"
len_of_the_string = len(data)
print("Length of the String", len_of_the_string)  
"""

# Taking 2 string i/p from  keyboard
# 1> Main string
# 2>Substring
# Substring present in the Main string

# eg 
# "Hi Atul welcome to the Class"
# "welcome to the Class" 
"""
main_string = input("Enter the Main String: ")
sub_string = input("Enter the Sub String: ")
if sub_string in main_string:
    print(sub_string, "is the vailable in the main string")
else:
    print(sub_string, "is not the vailable in the main string")
"""
# eg 
# s = "ATUL"
# print("z" in s)

# Finding Substring
"""
# Forword direction
1> find()
2>index()
for Backword direction
3> rfind()
4> rindex()
"""
# 1> find() : It returns index of first occurences of thre given substring.
# If it is not available then it will get -1

"""
data = "Learning Python is very easy"
print(data.find('Python')) # 
print(data.find("Java"))
print(data.find("r"))
# eg for backword direction
print(data.rfind("r"))

# * find(substring, beign, end)
# It always search python from beign index to end -1
print(data.find('Python',5,20)) #9
print(data.find('Java',5,20)) # -1
"""
"""
index(): This method exactly same as find() method except that if 
the specified substring is not available then we will get value error 
"""
 
# data = "Learning Python is very easy"
# print(data.index("Python", 5,14))

# Q if we don't want to print value error
"""
main_string = input("Enter the Main String: ")
sub_string = input("Enter the Sub String: ")

try:
    main_string.index(sub_string)
except ValueError:
    print("Substring is not found")
else:
    print("Substring is found")
"""
# count()
"""
We can find no of occurences of the substring present in the given string
by using count() method
1> count(substring)
2> count(substring, beign, end) (end-1)

main_string= "abbbsdbfjkdsjksdnsdfnbba"
sub_string = "a"
print("The no of occu: ", main_string.count(sub_string))
"""


# Replacing a string with another string
"""
replace(oldstring, newstring)

s = "Learing Python is very difficult"
s1 = s.replace("difficult", "easy")
print("output", s1)
"""

#  Splitting of string
"""
We can split the given string accourding to specified seprator
by using split() 
split(seprator) 
default seprator is space

data = "Vicky is my friend"
out = data.split() 
print(type(out))
print(out)

for x in out:
    print(x)

data = "25-05-2085"
sp_data = data.split("-")
print("date of data", sp_data)
for x in sp_data:
    print(x)

data = "25:05:2085"
sp_data = data.split(":")
print("date of data", sp_data)
for x in sp_data:
    print(x)

"""
#  Join() Method

"""
We can join group of Strings (list or tuple) the given seprator

syntax : 'seprator'.join(group of string)

data = ["Akash", "Atul", "Ankit"]
out = '-'.join(data)
print(type(out))
print(out)
"""

# Q WAP to remove spaces of the string using(list and join() method)
"""
data = "Atul is my friend"
list = data.split() # value into the list
out = "".join(list)
print(out)
"""

# Day 8  Changing Case of String imp for interview
# We have 4 methods to change the case of of String

# 1> upper():- To convert all Charaters to UpperCase
# 2 lower():- To convert all Charaters to lowercase
# 3>swapcase():-  Lower to upper and upper to lower case
# 4> title():- To convert all Charaters to TitleCase i.e first Capital
# 5> capialized():- Only first character will be converted to upppercase and all
# remaining characters can be converted to lower case

"""
Power-bi 
numpy
pandas
sikit learn
"""

"""
data = "Learning python is very easy"
print(data.upper())
print(data.lower())
print(data.capitalize())
print(data.swapcase())
print(data.title())
"""

# Topic: Checking starting and ending part of the string
"""
1> startswith(substring)
2> endswith(substring)
"""

# test@gmail.com
# best@hotmail.com

# data = "Learning python is very easy"
# print(data.startswith('Learning')) #True
# print(data.startswith('learning')) # False
# print(data.endswith('easy')) # True

#  Topic:- To check type of characters present in the string ### for IMP interview
# 1> isalnum(): => (a to z, A to Z, 0 to 9)
# 2 isaplha(): => (a to z, A to Z)
# 3 isdigit(): => (0 to 9)
# 4 islower(): => lowercase letters
# 5 isupper(): => uppercase letters
# 6 isspace(): => only spaces

# data = "Test123456and789"
# print(data.isdigit())
# print(data.isalpha())
# print(data.isalnum())
# print(data.islower())
# print(data.isupper())
# print(data.istitle())
# print(data.isspace())

# for x in data:
#     if x.isdigit():
#         print(x, end="")
        
# Flow Control
"""
Describe the order in which statements will be executed at runtime
"""
# Conditional Statements
# 1>  if                                                      
# 2> if-elif
# 3  if-elif-else

# #Iterative Statements
# 1> For  
# 2> while

# Transfer Statement
# 1 break
# 2> continue
# 3> pass

# Conditional Statements
# 1> if statement

"""
syntax [if condition: statement]

name = input("Enter Name: ")
if name == "Aakash":
    print("Hello Akash Good Morning")
print("Good Night")
"""
# 2> if - else statement
"""
syntax: 
if cond:
    statement 1
else:
    statemen 2

name = input("Enter Name: ")
if name == "Aakash":
    print("Hello Akash Good Morning")
else:
    print("Good Night")
"""
# 2> if-elif-else statement
"""
syntax: 
if condition 1:
    statement 1
elif condition 2 :
    statemen 2
else:
    Defalut statement

Brand = input("Enter your Brand: ")
if Brand == "Lamborghini":
    print("Its a Child brand")
elif Brand == "Audi":
    print("Its a Girl Brand")
elif Brand == "Tata":
    print("Its a Legend Brand")
else:
    print("Other brands are not recommended")

"""

# Q WAP to print biggest no taking i/p from keyboard 2 no's

# a= int(input("Enter your First Number:"))
# b= int(input("Enter your Second Number:"))

# if a>b:
#   print("A is Bigger")
# else:
#   print("B is Bigger")

# Q WAP to print biggest no taking i/p from keyboard 3 no's

a= int(input("Enter your First Number:"))
b= int(input("Enter your Second Number:"))
c= int(input("Enter your third Number:"))

if a>b and a>c:
    print ("First Number is Bigger :",a)
elif b>c:
    print("Second  Number is Bigger :",b)
   
else:
    print("Third Number is Bigger : ",c)























