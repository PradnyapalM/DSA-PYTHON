# CH1 Analysis of Algorithms
"""
Background

ex Sum of 'n' natural numbers
    input = 3
    output:- 1+2+3 = 6

    or input = 5
    output = 15

solution 1:-- # it will run its own timming
    def fun1(n):
        return n*(n+1)//2 

solution 2:--- it will run its own timming
    def fun2(n):
        sum=0 
        for i in range(1,n+1):
        sum = sum+i
    return sum

solution 3:-- it will run its own timming
    def fun3(n):
        sum=0 
        for i in range(1,n+1):
            for j in range(1, i+1):
                sum = sum + i
    return sum
"""

# Topic Asymptotic Analysis
"""
1. No depenenency on machine programming language etc.
2. We do not have to implement all ideas// algortihms
3. Asymptotic Analysis is about measuring the order
    of growth in terms of input size.

#### Order of Growths   
fun1()--> c1
fun2():-- c2n+c3 # constant of 'n'
fun3():- c4n^2 + c5n + c6  c2n+c3 # constant of 'n'

# compairing fun1() and fun2()

"""
# Q Imagin a scenario that your friend brings faster machine
# the value of c1,c2, and c3 is 1 and give the slower machine to
# you and provide the c1 is 1000.


#  Topic Order of Growth **

"""
A function f(n) is said to growing fanster than g(n) if
    lim  f(n)
        
    n->00
"""

#  Topic Order of Growth **
# Direct way

"""
1. Ignore lower order terms
2. Ignore leading constants.
"""
# Q How do we know which terms are lower ordered??


# Day 26

# Topic Best , Average, wrost cases and Asymptotic Notation

"""
def getSum(l):
    sum = 0
    for x in l: 
        sum = sum +x -> c1n+c2 order of Growth
                        order of growth of 'n' is linear
    return sum 

"""

# Q WAP to find sum of odd in list

def getSumOdd(l):
    if len(l)%2==0:
        return 0
    sum = 0
    for x in l:
        sum = sum + x  #order of growth of 'n' is linear
    return sum

"""
Best Cases = constant

Average case:- Linear constant (under the assumption that even and odd cases are 
                                    euqally likely)
Wrost case = Linear (#order of growth of 'n' is linear)

"""

# Topic Asymptotic Notation (Expression) c1n+c2

"""
Big O: Represents exact or O(n) and for upper bond O(n^2)

Theta:- Represent exact bond 0(n)

Omega:- Represent the exact or lower bond 
        c1n+c2
        __(n), __(1), __(logn)
        
"""


#  Topic Big O Notation (Upper bond on order of growth)
"""
We say f(n) = O Cg(n) if f(n) there exists a constants C and n0 such 
that f(n)<= Cg(n) for n>=n0.

ex: f(n) = 2n+3 can be written as O(n)


"""
# day28

# Topic Important things of Theta notation

"""
# 1 if f(n) = 0 cg(n) then f(n) = Ocg(n) and f(n) = __^__cg(n)
and g(n) = O f(n) and g(n) = __^__f(n)

2. Theta is usefull to represents time complexity when we know 
the exact bond. 
for example, time complexity to find sum, max,min in an array is 0(n)

3. {n^4/2, n^2/,...2n^2, 2n^2+1000n, 4n^2+2nlogn+30.....   } E 0(n^2)
"""

# Day 28

#  Topic subsequent loops (ek ke baad ke loops)

"""
i = 0

while i <n:   # 0(n)
    i = i + 2

i = 1
while i<n:   # 0 log(n)
    i = i * 3

i=1
while i <100: # 0(1)
    i = i + 1

step 1:-- Calculate each oder of growth of loop
step2:- Add them and find or calculate the higher order of growth

0(n)+0 log(n) + 0(1)

ans = 0(n)
"""

# Exmp 7: Nested loop

"""
i = 0
while i < n:
    j = 1
    while j<n:
        j = j*2
    i = i + 1
    #some const value
    # time work
step 1:-- Calculate inner loop of oder of growth.
step 2: then Calculate outer loop
step 3: Multiply both the loop to calculate
final order of growth of nested for loop.
"""
# exp 8 mixed loops

"""
i = 0
while i < n:
    j=1
    while j<n:
        j = j*2
    i = i + 1

i = 0
while i < n:
    j=1
    while j<n:
        j = j+1
    i = i + 1

"""

# exmp 9 Multiple input
"""
i = 0
while i < n:
    j = 1
    while j<n:      # 0(nlogn)
        j = j * 2
    i = i + 2
                        +             =   0(nlogn) + 0(m^2) = 0(nlogn+m^2)
i = 0
while i<m:
    j=1
    whle j<m:      #0(m^2)
        j = j + 1
    i = i + 1


"""
 







