"""
Nested For Loop

Use Cases:- When for each iteration of the loop
we need to repeat some action a given number of times.

syntax:-->
[outer loop]
for <var1> in <iter1>:
    #optional code
    [nested/inner loop]
    for <var2> in <iter2>
        # code
    #optional code
"""

# # eg
# #[outer loop]
# for i in range(4): #it will run 4 times (0 to 3) include
#     #[inner loop]
#     for j in range(2):# it will run 2 times (0 to 1) include
#         print(i,j)

"""
0 0
0 1
1 0
1 1
2 0
2 1
3 0
3 1
"""

"""
#####################Iteration###########################
"""
# eg
# for i in range(2,5): #{2,3,4} Row
#     for j in range(3,5): #{3,4} column
#         print(i,j)

# eg
# for i in range(8,11):
#     for j in range(6,9):
#         print(i,j)

"""
    * # row i = 5
   * *
  * * *
 * * * *
* * * * *
"""

# rows = 5
# for i in range(1, rows+1):
#     # Printing the space
#     for j in range(rows-i):
#         print(" ", end="")
#     #Printing the star
#     for k in range(i):
#         print("*", end=" ")
#     print()

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""







