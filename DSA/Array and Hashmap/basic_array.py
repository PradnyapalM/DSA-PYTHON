"""
Some basic Array questions
"""
# data_list = [10,40,20,50]
# print(max(data_list)) #50
# print(min(data_list)) #10
# # data_list.reverse()
# # print(data_list)
# data_list.sort()
# print(data_list)

#  How does Dynamic size works

# data_list = []
# for i in range(1,1001):
#     data_list.append(i)

# print(data_list)

# , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    # [1,2----]
    # [1,2,3----]

# Amotized Time Complexity
"""
Initialize size = n
We have double size when becomes full

Average time to append             = 0(1)+0(2)+.....0(n)/n+1(time)
in the list                        = 0(n)+0(n)/0(n)
                                   = 0(1)
"""

#  Average or mean of list

# Solution 1
# def average(l):
#     sum = 0
#     n = len(l)
#     for x in l:    0(n)
#         sum = sum + x   
#     return sum/n

# data_list = [10,20,30,40]
# print("The Average: ", average(data_list))

# # Solution2
# def average(l):   #0(1)
#     return sum(l)/len(l)

# data_list = [10,20,30,40]
# print("The Average: ", average(data_list))

# Q Seperate even and odd
# ip [10,41,30,15,80]
#  op even = [], odd = []

# def evenOdd(l):
#     even = []
#     odd = []

#     for x in l:
#         if x%2==0:
#             even.append(x)
#         else:
#             odd.append(x)
#     return even, odd

# l =[10,41,30,15,80]
# print(evenOdd(l))
# eve, odd = evenOdd(l)
# print(f"the Even list {eve}")
# print(f"the Odd list {odd}")

# Q Find the Larget element in the array/list
# l =[10,41,30,15,80]


# def largeElement(l):
#     max_no = 0
#     for x in l:
#         if x>max_no:
#             max_no = x
#     return max_no

# l =[10,41,30,15,80]
# print(largeElement(l))

# Efficient solution

# Approach
"""
################(res)
l0, l1,l2....li-1......li...ln-1
            li>res              Time complexity 0(n)
            or li<=res
"""
#  Time Complexity 0(n)
# def getMax(l):
#     if not l:
#         return None
#     else:
#         res = l[0]
#         for i in range(1, len(l)):
#             if l[i]>res:
#                 res = l[i]
#         return res

# l =[10,41,90,30,15,80]

# print(getMax(l))

# Hashmap (Hashmap is nothing but the dictionary) Hashing

"""
Search 
insert    # average time is complxity is O(1)
delete

# No useful for
1. Finding closest value -- AVL Tree
2. Sorted data----AVL Tree
3. Prefix Searching -- Tries

# Application of Hashing
1.Dictionaries
2.Database Indexing
3.Crytography
4.Cashes
5.Symbol Table
6.Compiler interpreter
7.Routers
8.Getting data from databases
"""
# Topic Hashing Function
# Topic How  Hashing Function Works
"""
1. Should always map large key to small key
2. Should Generate Values from 0 to m-1
3.Should be fast O(1) for integer and O(n) for string and length "len n"
4.Should uniformly distributed large keys into hash table slots.

Example of Hash Function:-->
1.h(large - key) = lagrge-key%m
2. for strings, weighted sum
str[] = "abcd"
(str[0]*x^0 + str[1] * x^1+str[2] * x^2 + str[3] * x^3) % m
3. Uniersal Hashing
""" 
#  Topic Collision Hashing
"""
If we know keys in advance, then it can perfect Hashing.
If we do not know keys then we use one of the following chaining
1.Chaining
2.Open Addressing
    *-> Linear probing
    *-> Quadractic Probing
    *-> Double Hashing
"""

# Topic Chaining (Collision Handling)

"""
Performance:--
m = no.of slots in Hash Table 
n = no.of keys to be inserted

"""

class MyHash:
    def __init__(self,b):
        self.BUCKET = b
        self.table = [[] for x in range(b)]

    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)

    def remove(self, x):
        i = x % self.BUCKET
        if x in self.table[i]:
            self.table[i].remove(x)
    
    def search(self,x):
        i = x % self.BUCKET
        return x in self.table[i]
    
    def PrintTable(self):
        print(self.table)

b = int(input("Enter the size of hashmap Table: "))
obj = MyHash(b)
x = int(input("Enter the value that you want to insert: "))
y= int(input("Enter the value that you want to insert: "))
z = int(input("Enter the value that you want to insert: "))
obj.insert(x)
obj.insert(y)
obj.insert(z)
obj.PrintTable()
# Lets serch the insert data
s = int(input("Enter the value that you want to search: "))
print(obj.search(s))
r = int(input("Enter the value that you want to remove: "))
print(obj.remove(r))
obj.PrintTable()









