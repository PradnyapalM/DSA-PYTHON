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

    





