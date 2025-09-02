"""
Day 24
Size
-> How many rows you want in the pattern
-> inupt taking from user
n = int(input("Enter the no of ROWS))
or function parameter or n=5
def pattern(n):

Basic Syntax:-->
for row in range():
    for column in range():
        print("*", end="")

"""

# Q 1
"""
******
******
******
******
******
"""

# n = int(input("Enter the no of Rows"))
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# Q 2 Increasing Trangle Pattern
"""
*
**
***
****
*****
"""

# n = int(input("Enter the no of Rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# Q3 Decrising Triangle Pattern

""" 
   j=0
i=0******
*****
****
***
**
*
"""

# n = int(input("Enter the no of Rows: "))

# for i in range(n):
#     for j in range(i,n): # or range(n-i)
#         print("*", end=" ")
#     print()


# Q4 Right Sided Traingle
"""
     *
    **
   ***
  ****
 *****
"""

# n = int(input("Enter the no of Rows: "))

# for i in range(n):
#     for j in range(i,n):
#         print(" ", end="")
#     for k in range(i+1):
#         print("*", end="")
#     print()

# Q5. Right sided downward triangle
"""
******
 *****
  ****
   ***
    **
     *
"""

# n = int(input("Enter no of rows: "))

# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for k in range(i,n):
#         print("*", end="")
#     print()

# Q6 Hill pattern

'''
    *
   ***
  *****
 *******
*********
'''

n = int(input("Enter no of rows: "))
for i in range(n):

    for j in range(i,n):
        print(" ", end="")

    for k in range(i):
        print("*", end="")

    for m in range(i+1):
        print("*", end="")

    print()

# Note:- We need to minimize one column to look Hill pattern (i+1) insetead will use 'i'

# Q7. Reverse Hill Pattern
'''
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
'''
