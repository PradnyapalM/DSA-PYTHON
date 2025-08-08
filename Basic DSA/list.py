"""
LIST array in c/c++/java (collections) (Group of elements in a single entity)
If we want to represent a group of individual objects as a single
Entity where insertion order is preserved and duplicates are allowed
then we should go for list.
Note:-1> In List the elements will be placed within square brackets and 
         the comma seprator.
      2> List is Mutable, SO we can change the contents.
      3> Index will play very important role and Python supports
      +ve and and -ve index. Positive means from left to right 
      and Negative means right to left.
      4> We can store any kind of data in the list (Hetrogenous data)
"""
# Topic Creation of List Object

# 1 We can create an empty list object

# list = []
# print(list)

# 2 If we know elements already then we can create list as follows
# list = [10,20,30,40]

# 3> List with Dynamic Input:- 
# list = eval(input("Enter a list"))
# print(list)
# print("Type of ",type(list))

# 4> With list() function

# 1> data = list("Aakash")
# print(data)# ['A', 'a', 'k', 'a', 's', 'h']

# 2>
# data = list(range(5,11))
# print(data) # [5, 6, 7, 8, 9, 10]

# 5 Split function

# data = "Welcome to the Programming World"
# out_data = data.split()
# print("output: ", out_data)

# Topic:  Accessing elements of List
"""
There are Two Ways
1> Index 
2> Slice operator
"""

# 1 By Using Index:--->

# data = [10,20,30,40]
# data[0] # 10
# data[2] #30
# data[-1] # 40

# 2 By using Slice Operator
"""
[begin:stop:step]
or
[start:stop:step]
"""

# data = [0,1,2,3,4,5,6,7,8,9,10]
# print(data[2:7]) # [2, 3, 4, 5, 6]
# print(data[::-1]) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#  Topic : :List vs Mutability
"""
Once we creates a list objects.We can modify its content.
Hence list of objects are Mutable

Note: Mutable object Supports item assignment 
"""

# data = [0,1,2,3,4,5,6,7,8,9,10]
# data[3] = 777
# print(data) # [0, 1, 2, 777, 4, 5, 6, 7, 8, 9, 10]

# data[7] = "Manish"
# print(data)

# Topic : Traversing the elements of List
"""
The sequential access of each element in the list
is called traversal. 
"""

# 1> By Using While Loop

# data = [10,20,30,40,50] 

# i = 0
# while i<len(data):
#     print(data[i])
#     i = i + 1

# 2> By using for Loop

# data = [10,20,30,40,50] 

# for element in data:
#     print(element)

# Q WAP to print only Even No 
# data = [0,1,2,3,4,5,6,7,8,9,10]

# data = [0,1,2,3,4,5,6,7,8,9,10]
# for ele in data:
#     if ele % 2 == 0:
#         print(ele)

# Q To Display an elements by index wise i.e +ve and -ve

# data = ["A","B","C","D"]
# len = len(data)
# i = 0
# for i in range(len):
#     print('{} is available at +ve index:{} and -ve index:{}'.format(data[i], i, i-len))

#  i-len
# 0-4 ---> -4

"""
A is available at +ve index:0 and -ve index:-4
B is available at +ve index:1 and -ve index:-3
C is available at +ve index:2 and -ve index:-2
D is available at +ve index:3 and -ve index:-1
"""

# Topic:-- Important function of LIST

# 1> len():-> Return No of elements present in the list

# data = [10,20,30,40,50] 
# print(len(data))

# 2> count():-> It returns No of occurences of specified item in the list

# data = [1,2,2,2,1,3,4,3,3] 
# print(data.count(4)) #1
# print(data.count(2)) #3

# 3> Index() function :-> It returns the index of first occurence of the specified item
# data = [1,2,2,2,1,3,4,3,3]
# print(data.index(3)) #5

# print(9 in data) # False (if element is not peresent in the list so will get the value error)

# Q WAP to use count or membership operator to check whether the element present in list
# or not
# data = [1,2,2,2,1,3,4,3,3] 
# take_input = int(input("Enter the value to find index"))

# if data.count(take_input):
#     print(take_input, "at availabe in this index", data.index(take_input))
# else:
#     print(take_input, "is not available")


# Day 15
# Topic Manipulating list Element

# 1 Append Function():--> We can use append() function to 
# add item at add the end of the list.

# data = []
# data.append("Akash")
# data.append("Practice")
# data.append("Kiya")
# print(data)

# Q Wap to add all the elements to list upto 100
#  which is divisible by 10

# lst = []

# for i in range(1,101):
#     if i % 10 == 0:
#         lst.append(i)
# print(lst)


# 2>  Inserrt function():-  To insert an item at specified index positon

# data = [1,2,3,4]
# data.insert(1, 888)
# print(data) [1, 888, 2, 3, 4]

"""
Note:-
If the specified index is greator than max index then element
will be inserted at last  position. if the specified index is 
smaller that min index then the element be will inserted at 
the first postion
"""

# data = [1,2,3,4,5]
# data.insert(50,777)
# print(data) #[1, 2, 3, 4, 5, 777]
# data.insert(-12,222)
# print(data) #[222, 1, 2, 3, 4, 5, 777]

# H.W Diff betwn append() and insert() function (IQ)

# 3 extend() function:--> To add all items of one list to another list

# veg_items = ["Paneer", "Mix-Veg", "Dal-Tadka"]
# nonVeg_items = ["Biryani", "Chicken Tandoori", "Shorma"]

# veg_items.extend(nonVeg_items)
# print(veg_items) # ['Paneer', 'Mix-Veg', 'Dal-Tadka', 'Biryani', 'Chicken Tandoori', 'Shorma']

# 4 remove() function
"""
To remove the specified item form the list.If the item present
multiple times then only first occurrence will be removed.
"""

# data = [10,20,10,30]
# data.remove(10)
# print(data) #[20, 10, 30]

"""
Note:- If the specified element not present in the list
      so will get the value error.
"""

# data = [10,20,10,30]
# data.remove(50)
# print(data) # ValueError: list.remove(x): x not in list

# 5 pop() function:-
"""
It removes and returns the last element of the list.
This is the only function which is manipulates list and 
returns some element.
"""

# data = [10,20,30,40]
# print(data.pop()) # 40
# print(data) #[10, 20, 30]

"""
Note:->
If the list is empty then pop() function raises the index error
"""
# list_data = []
# print(list_data.pop()) #IndexError: pop from empty list

# Q How to remove the specified index element
# data = [10,20,30,40]
# print(data.pop(2)) #30
# print(data) #[10, 20, 40]


# List in Dynamic/Growable:-->
"""
append(), insert(), extend()--->Increasing
remove(), pop() ---> To decrease the size
"""

# Topic:-- Ordering Elements of List

# 1> reverse():- IT use to reverse the order of the element of the list

# data = [10,20,30,40]
# data.reverse()
# print(data) #[40, 30, 20, 10]

# 2> sort()
"""
Default orders
1> for numbers:-- Ascendig order
2> for string :-- Alphabetical Order
"""

# data = [10,5,0,20,15]
# data.sort()
# print(data) #[0, 5, 10, 15, 20]

# data = ["dog", "cat", "tiger", "zebra", "lion"]
# data.sort()
# print(data) #['cat', 'dog', 'lion', 'tiger', 'zebra']

"""
sort accourding to reverse of default natural sorting 
order by using reverse = True argument
"""

# data = [40,10,30,20]
# data.sort()
# print(data) #[10, 20, 30, 40]

# data.sort(reverse=True)
# print(data) #[40, 30, 20, 10]
# data.sort(reverse=False)
# print(data) #[10, 20, 30, 40] 

# data = ["Mukul","Ankit","Jackson", 20, 40]
# data.sort(reverse=True)
# print(data) #['Mukul', 'Jackson', 'Ankit']

"""
Note:- 
IF we use diffrent or mix data type in the list and when we apply 
the sort() function then will get TypeError
"""

# Topic:--->  Aliasing and cloning of List objects (IQ)
# Aliasing --> Shallow Copy
# cloning --> Deep copy

"""
The process of giving another reference variable to the existing 
list is called aliasing (Shallow Copy)
"""

# x = [10,20,30,40]
# y = x
# print(id(x)) #2547395744384
# print(id(y)) #2547395744384

"""
Note:--
The problem in this approach is using one reference variable if we
are changing the content then those changes will reflected to the 
other reference variable
"""

# x = [10,20,30,40]
# y = x
# y[1] = 777
# print(x) #[10, 777, 30, 40]
# print(id(x))
# print(id(y))

"""
Note:- 
To overcome this problem we should go for cloning (Deep copy).
The process of creating exacalty duplicate(replica) independent
object is called Deep copy(cloning)

We can implement Deep copy by using slice operator or
by using "copy()" function
"""

# 1> By using slice operator

# x = [10,20,30,40]
# y = x[:]
# y[1] = 77
# print(x)
# print(id(x)) #1781725221504
# print(id(y)) #1781727393472

# 2> By using copy() function

# x = [10,20,30,40,50,60]
# y = x.copy()
# y[1] = 888
# print(x) #[10, 20, 30, 40, 50, 60]
# print(y) #[10, 888, 30, 40, 50, 60]


