"""
LIST(collections) (Group of elements in a single entity)
If we want to represent a group of individual objects as a single
Entity where insertion order is preserved and duplicates are allowed
then we should go for list.
Note:-1> In List the elements will be placed within square brackets and 
         the comma seprator.
      2> List is Mutable, SO we can change the contents
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


 
