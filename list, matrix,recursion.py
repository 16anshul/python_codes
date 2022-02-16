#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(a,b):
    ans = a + b
    return ans
add(1,6)
add(10,72)


# In[3]:


def sub(a,b):
    ans = a-b
    return ans
    
sub(10,8)


# In[5]:


def discount(cost,d):
    ans = cost-(cost*(d/100))
    return ans
discount(100,10)


# In[7]:


def discount(cost,d):
    ans = cost-(cost*(d/100))
    return ans
print("Enter the cost price")
x = int(input())
print("Enter the discount")
y = int(input())
print("The final discount is:" , discount(x,y))


# In[13]:


##List manipulation with function
def list_min(l):
    mini = 0
    for x in range(len(l)):
        if l[x] < mini:
            mini = l[x]
    return mini
l = [1,2,3,4,5,6,10,-10]
print(list_min(l))
    


# In[14]:


def list_maxi(l):
    maxi = l[0]
    for i in range(len(l)):
        if l[i]>maxi:
            maxi = l[i]
    return maxi
l = [1,2,3,4,5,6,78,87,-98]
print(list_maxi(l))


# In[17]:


def append_before(l1 , l2):
    new_l = []
    for i in range(len(z)):
        new_l.append(z[i])  
    for j in range(len(l)):
        new_l.append(l[j])
    return new_l
l = [12,3,4,5,6,4]
z = [12,3,4,5,6,76,7]
print(append_before(l,z))


# In[20]:


def list_appended(l,z):
    new_l = []
    for i in range(len(l)):
        new_l.append(l[i])  
    for j in range(len(z)):
        new_l.append(z[j])
    return new_l
l = [12,3,4,5,6,4]
z = [12,3,4,5,6,76,7]
print(list_appended(l,z))


# In[22]:


def list_average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
    avg = sum / len(l)
    return avg
z = [12,3,4,5,6,76,7,23,4,5,6,6,7,43,32,21,1,3,23,2]
print(list_average(z))


# In[24]:


def obvious_sort(l):
    x = []
    while len(l)>0:
        mini = l[0]
        for i in range(len(l)):
            if mini > l[i]:
                mini = l[i]
        x.append(mini)
        l.remove(mini)
    return x

l = [22,33,44,5,566,777,23,667,323,12]
print(obvious_sort(l))
            
            


# In[27]:


#breaking problem into smaller modules and solving them and make it easy
def mini_list(l):
    mini = l[0]
    for i in range(len(l)):
        if mini > l[i]:
            mini = l[i]
    return mini

def obvious_sort(l):
    x = []
    while len(l)>0:
        mini = mini_list(l)
        x.append(mini)
        l.remove(mini)
        
    return x
l = [22,33,44,5,566,777,23,667,323,12]
print(obvious_sort(l))


# In[33]:


def sum(n):
    ans = 0
    for i in range(n):
        ans = ans + (i+1)
    return ans


# In[ ]:


def initialize_mat(dim):
    C = []
    for i in range(dim):
        C.append([])
        for i in range(dim):
            for j in range(dim):
                C[j].append(0)
    return C

def dot_product(u,v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans = ans + (u[i] * v[i])
    return ans

def row(M,i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l

def column(M,j):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[k][j])
    return l
        
def mat_multi(A,B):
    dim = len(A)
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A,i) , column(B , j))
    return C
A = [[1,2,3] , [4,5,6] , [7,8,9]]
B = [[1,2,1] , [3,1,7] , [6,2,3]]
print(mat_multi(A,B))


# In[36]:


"""RECURSION IN PYTHON"""
#a function calls itself
def sum(n):
    if n == 1:
        return 1
    else:
        for i in range(n):
            return n + sum(n-1)
        
print(sum(10))


# In[39]:


##assuming interest == 10%
def compound_interest(p,n):
    if n ==1:
        return (p*1.1)
    else:
        return (compound_interest(p,n-1))*1.1

print(compound_interest(2000,3))


# In[41]:


def fact(n):
    if n==1:
        return 1
    else:
        return (fact(n-1))*n
print(fact(5))


# In[43]:


def myfunction(x):
    x = x*2
    print("Value of x in funtion 1",x)
x=5
print("Value of x before function call" , x)
myfunction(x)
print("Value of x after function call", x)


# In[46]:


"""Write a Python code using functions which calculates the number of upper case letters, lower case letters, 
total number of characters and number of words"""

def upper_case(s):
    upper = 0
    for c in s:
        if c.isupper():
            upper = upper+1
    return upper

def lower_case(s):
    lower = 0
    for c in s:
        if c.islower():
            lower = lower + 1
    return lower

def total_char(s):
    total = 0
    for c in s:
        total += 1
    return total

def total_words(s):
    word = 0
    l = sentence.split(' ')
    for i in l:
        word += 1
    return word

sentence = input("Enter the sentence: ")
u = upper_case(sentence)
l = lower_case(sentence)
tc = total_char(sentence)
tw = total_words(sentence)
print(u)
print(l)
print(tc)
print(tw)







# In[47]:


"""Write a Python code using functions to calculate area and perimeter of circle and rectangle"""
import math
PI = math.pi
def cirlce_area(r):
    return PI*r*r

def circle_perimeter(r):
    return 2*PI*r
def rectangle_area(l,b):
    return l*b
def rectangle_perimeter(l,b):
    return (2*(l+b))

polygon =""
while (polygon != exit):
    print("\nPolygons\nCircle\nRectangle\nexit")
    polygon = input("Choose the polygon type or exit")
    property = ""
    if polygon == 'circle':
        r = input("Enter the radius of a circle")
        while property == "":
            print("\nCircle Properties\nArea\nPerimeter")
            property = input("Choose the property and go back")
            if property == "Area":
                cArea = circle_area(r)
                print(f'Area of circle with radius {r} = {cArea} sq.units')
                property = ""
            elif(property == "perimeter"):
                cPerimeter = circle_perimeter(r)
                print(f'Perimeter  of a circle {r} = {cPerimeter} units')
            elif(property == "back"):
                break
            else:
                print("Select the correct property")
                property = ''
                


# In[49]:


'''Type: single argument, single return value 
The factorial of a positive integer n is the product of the first n positive integers. 
 
Write a function named factorial that accepts an integer n as argument. It should return 
the factorial of n if n is a positive integer. It should return -1 if n is a negative integer, and it 
should return 1if n is zero. 
 
1
2
3
4
5
6
7
deffactorial(n): 
'''''''
 Argument:
 n: integer
 Return:
 result: integer
 '''''''
You do not have to accept input from the user or print output to the console. You just have to 
write the function definition. '''
def factorial(n):
    if n<0:
        return -1
    elif n == 0:
        return 1
    else:
        return (factorial(n-1))*n
factorial(4)


# In[53]:


'''In the Gregorian calendar, a leap year has a total of 366 days instead of the usual 365 as a result of 
adding an extra day (February 29) to the year. This calendar was introduced in 1582 to replace the 
flawed Julian Calendar. The criteria given below are used to determine if a year is a leap year or not. 
 If a year is divisible by 100 then it will be a leap year if it is also divisible by 400. 
 If a year is not divisible by 100, then it will be a leap year if it is divisible by 4. 
Write a function named check_leap_year that accepts a year between 1600 and 9999 as 
argument. It should return True if the year is a leap year and False otherwise. '''
def check_leap_year(year):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0)  and year %100 != 0 :
        return True
    else:
        return False
    return check_leap_year(year)
check_leap_year(2020)
    
    


# In[56]:


'''Type: multiple arguments, single return value 
Write a function named maxval that accepts three integers a, b and c as arguments. It should return 
the maximum among the three numbers.'''
def maxval(a, b, c):
    maxv = a
    if b > a:
        maxv = b
    if c > a:
        maxv = c
    return maxv
maxval(34,5,6)


# In[ ]:


'''Write a function named dim_equal that accepts two matrices A and B as arguments. It should 
return True if the the dimensions of both matrices are the same, and False otherwise'''


# In[72]:


'''Type: single argument, multiple return values 
Write a function named first_three that accepts a list L of distinct integers as argument. It 
should return the first maximum, second maximum and third maximum in the list, in this order. You 
can assume that the input list will have a size of at least three. What concept in CT does this remind 
you of? 
'''
def dim_equal(A,B):
    A = []
    B = []

    if len(A) == len(B):
        return True
    else:
        return False

print(dim_equal([[1,2] , [3,4] , [5,6]] , [[7,8] , [9,10]]))
print(len(A))
print(len(B))

    


# In[83]:


'''Write a function named first_three that accepts a list L of distinct integers as argument. It should return the 
first maximum, second maximum and third maximum in the list, in this order. You can assume that the input list 
will have a size of at least three. What concept in CT does this remind you of?'''
def first_three(L):
    maxv = 0
    fmax = 0
    smax = 0
    tmax = 0
    for i in range(len(L)):
        if L[i] > maxv:
            maxv = L[i]
    fmax = maxv
    L.remove(maxv)
    maxv = 0
    for i in range(len(L)):
        if L[i] > maxv:
            maxv = L[i]
    smax = maxv
    L.remove(maxv)
    maxv = 0
    for i in range(len(L)):
        if L[i] > maxv:
            maxv = L[i]
    tmax = maxv
    return fmax, smax, tmax
L = [1,2,3,4,5,6]
first_three(L)
'''
def first_three(L):
    fmax, smax, tmax = L[0], L[1], L[2]
    for x in L:
        if (x>fmax):
            tmax = smax
            smax = fmax
            fmax = x
            
        elif(x>smax and x <= fmax):
            tmax = smax
            smax = x
        elif (x>tmax and x<= smax):
            tmax = x
        return fmax, smax, tmax'''


# In[ ]:


'''s
A class of English words is called mysterious if it satisfies certain conditions. These conditions are 
hidden from you. Instead, you are given a function named mysterious that accepts a word as 
argument and returns True if the word is mysterious and False otherwise. 
Write a function named type_of_sequence that accepts a list of words as an argument. Its return 
value is a string that depends on the number of mysterious words in the sequence. The exact 
conditions are given in the following table. If k denotes the number of mysterious words in the'''
def type_of_sequence(L):
    count = 0
    for word in L:
        if mysterious(word) == True:
            count +=1
    if count < 2:
        print("mildy mysterious")
    elif 2<=count<5:
        print("moderately mysterious")
    elif count>5
        print("most mysterious")


# In[85]:


'''In a throwback to CT days, write the definition of the following five functions, all of which accept a 
list L as argument. 
(1) is_empty: return True if the list is empty, and False otherwise. 
(2) first: return the first element if the list is non-empty, return None otherwise. 
(3) last: return the last element if the list is non-empty, return None otherwise. 
(4) init: return the first n - 1n−1 elements if the list is non-empty and has size nn, 
return None otherwise. Note that if L has just one element, init(L) should return the empty list. 
(5) rest: return the last n - 1n−1 elements if the list is non-empty and has size nn, 
return None otherwise. Note that if L has just one element, rest(L) should return the empty list.'''
def is_empty(L):
    if len(L) == 0:
        return True
    else:
        return False
        
def first(L):
    if (is_empty(L) == False):
        return L[0]
    else:
        return ("None")
        
def last(L):
    if (is_empty(L) == False):
        return L[-1]
    else:
        return ("None")
def init(L):
    if (is_empty(L) == False):
        if len(L) == 1:
            return []
        else:
            return L[:-1]
    else:
        return ("None")
def rest(L):
    if (is_empty(L) == False):
        if len(L) == 1:
            return []
        else:
            return L[1:]
    else:
        return ("None")
        


# In[ ]:


'''Write a recursive function named fibo that accepts a positive integer n as argument and returns 
the nth Fibonacci number. For this problem,F1=F2=1 are the first two Fibonacci numbers. '''
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# In[87]:


'''Implement the following functions. 
(1) Write a function named get_column that accepts a matrix named mat and a non-negative 
integer named col as arguments. It should return the column that is at index col in the 
matrix mat as a list. Zero-based indexing is used here. 
(2) Write a function named get_row that accepts a matrix named mat and a non-negative integer 
named row as arguments. It should return the row that is at index row in the matrix mat as a list. 
Zero-based indexing is used here. 
'''
def get_column(mat, col):

    colu = []
    for j in range(len(mat)):
        colu.append(mat[j][col])
    return colu

def get_row(mat, row):

    rows = []
    for i in range(len(mat)):
        rows.append(mat[row][i])
    return rows
print(get_column([[1, 2], [3, 4]], 0))
print(get_row([[1, 2], [3, 4]], 1))


# In[ ]:


'''Write a function named insert that accepts a sorted list L of integers and an integer x as input. The 
function should return a sorted list with the element x inserted at the right place in the input list. The 
original list should not be disturbed in the process. You can assume that the input list will be sorted in 
ascending order.'''
'''1) The only built-in methods you are allowed to use are append and remove. You should not use 
any other method provided for lists. 
(2) You do not have to accept input from the user or print output to the console. You just have to write 
the function definition. 
'''
'''def insert(L,x):
    sorted_L = []
    count = 0
    flag = False
    for i in range(len(L)):
        if x<L[i] and flag == False:
            sorted_L.append(x)
            sorted_L.append(L[i])
            flag = True
        else:
            sorted_L.append(L[i])
        if len(sorted_L) == len(L):
            sorted_L.append(x)
        return sorted_L
'''
def insert(L,x):
    L.append(x)
    for i in range(len(L)):
        for j in range(i+1 , len(L)):
            if L[i]>L[j]:
                L[i],L[j] = L[j] , L[i]
    return L


# In[88]:


'''The range of a list of numbers is the difference between the maximum and minimum values in the list. 
Write a function named get_range that accepts a non-empty list of real numbers as argument. It 
should return the range of the list. 
Note 
(1) Avoid using built-in function such as max and min. 
(2) You do not have to accept input from the user or print output to the console. You just have to write 
the function definition. 
'''
def get_range(L):
    maxv = 0
    minv = 1000
    for x in L:
        if x > maxv:
            maxv = x
    for x in L:
        if x < minv:
            minv = x
    ran_ge = maxv - minv
    return ran_ge
L = [43.26,25.07,19.06,48.65,21.08,32.57,2.82]
get_range(L)


# In[92]:


'''A perfect number is a positive integer that is equal to the sum of all its divisors excluding itself. For 
example, 6is a perfect number as 6 = 1 + 2 + 3. 
Write a function named is_perfect that accepts a positive integer n as argument and 
returns True if it is a perfect number, and False otherwise.'''
def is_perfect(n):
    sumi = 0
    for i in range(1 ,n):
        if n % i == 0:
            sumi += i
    if sumi == n:
        return True
    else:
        return False
is_perfect(8)
            


# In[101]:


'''The distance between two different letters in the English alphabet is defined as one more than the 
number of letters between them. Alternatively, it can be defined as the number of steps needed to 
move from the alphabetically smaller letter to the larger letter. This is always a non-negative integer. 
The distance between any letter and itself is always zero. For example: 

The distance between two words is defined as follows: 
 It is -1, if the words are of unequal lengths. 
 If the word-lengths are equal, it is the sum of the distances between letters at corresponding 
positions in the words. For example: 
dword(dog,cat)=dletter(d,c)+dletter(o,a)+dletter(g,t)=1+14+13=28 
Write a function named distance that accepts two words as arguments and returns the distance 
between them. 
'''
def distance(word_1 , word_2):
    dist = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if len(word_1) != len(word_2):
        return -1
    else:
        for i in range(len(word_1)):
            if word_1[i] == word_2[i]:
                continue
            else:
                dist += abs(alpha.index(word_1[i])- alpha.index(word_2[i]))
    return dist
distance("great" , "greet")


# In[106]:


'''A n×n square matrix of positive integers is called a magic square if the following sums are equal: 
 row-sum: sum of numbers in every row; there are n such values, one for each row 
 column-sum: sum of numbers in every column; there are n such values, one for each column 
 diagonal-sum: sum of numbers in both the main diagonals; there are two values 
There are n + n + 2 = 2n + 2 values involved. All these values must be the same for the matrix to be a 
magic-square. 
Write a function named is_magic that accepts a square matrix as argument and returns YES if it is 
a magic-square and NO if it isn't one. 
Notes 
(1) The cells of a magic square need not be distinct. Some or even all the cells could be identical. 
(2) You do not have to accept input from the user or print output to the console. You just have to write 
the function definition. 
A sample-image for a 3X3 matrix that details the various sums needed. Note that the input need not be 
restricted to 3X3matrices: '''
def is_magic(mat):
    d1 = 0
    d2 = 0
    n = len(mat)
    
    for i in range(n):
        r_sum = 0
        c_sum = 0
        for j in range(n):
            r_sum += mat[i][j]
            c_sum += mat[j][i]
            if i == j:
                d1 += mat[i][j]
            elif i+j == n-1:
                d2 += mat[i][j]
    if not (r_sum == d1 == d2 == c_sum):
        return ("No")
    else:
        return ("Yes")
mat = [[1 ,2, 3] , [4,5,6] , [6,7,8]]
is_magic(mat)


# In[114]:


'''The transpose of a matrix is obtained by swapping its rows and columns: 
൤
𝑎 𝑏 𝑐
𝑑 𝑒 𝑓൨ → ൥
𝑎 𝑑
𝑏 𝑒
𝑐 𝑓൩
Write a function named transpose that accepts a matrix mat as input and returns its transpose. '''
def transpose(mat , col):
    n = len(mat)
    m = len(mat[0])
    mat_transpose =  []
    for i in range(m):
        t = []
        for j in range(n):
            t.append(mat[i][j])
        mat.append(t)
    return mat_transpose
            
col = [3,3]
mat = [[1,2,3] , [4,5,6] , [7,8,9]]
v = transpose(mat , col)
print(v)


# In[ ]:




