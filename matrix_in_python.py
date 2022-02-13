#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Birthday paradox , Search , Sort , Matrix Operations


# In[31]:


"""BIRTHDAY PARADOX"""
import random
l = []
for x in range(30):
    l.append(random.randint(1,100))
l.sort()
print(l)
i = 29
flag = 0
while(i>=0):
    if (l[i] == l[i-1]):
        print("Repeats" , l[i] , l[i-1])
        flag = 1
        
    i = i-1
        
if (flag == 0):
    print("There is no repetition")


# In[36]:


"""Element is present in a list or not"""
l = []
import random
a = 567172
for i in range(100):
    l.append(random.randint(1 , 1000000))
print(l)
flag = 0
for i in range(len(l)):
    if (a == l[i]):
        print("Hip HIp Hurray")
        flag = 1
        break
if (flag == 0):
    print("Element is not found")


# In[ ]:


"""Enter element is present in a list or not"""
import random
l = []
for i in range(30):
    l.append(random.randint(1,10000))
print(l)
print("Enter any number , Enter -1 to exist")
n = 0

while (n != -1):
    print("Enter any number , Enter -1 to exist")
    n = int(input())
    flag = 0
   
    for x in range(len(l)):
        if n == l[x]:
            print("Yup, it is")
            flag = 1
            break
    if (flag == 0):
        print("Element not found")
        
        


# In[58]:


"""Find the least element in the list"""
l = [12,10,7,8,6,42,18,35]
x = []
while (len(l)>0):
    minl = l[0]
    for p in range(len(l)):
        if l[p] < minl :
            minl = l[p]
    x.append(minl)
    l.remove(minl)

print(l)
print(x)
            


# In[65]:



import random
l = random.sample(list(range(10000)) , 1000)

sum1 = 0
for i in range(len(l)):
    sum1 = sum1+l[i]
print(sum1)
    


# In[67]:


"""DOT PRODUCT"""
"""for finding dot  product no of elements should be equal in both list 
we have to apply if condition to check elemensts are equal or not"""
x = [1,7,3,4]
y = [8,6,3,2]
'''dot_product = (1*8) + (7*3) + (3*3) + (4*2)
print(dot_product)'''

sum = 0
for i in range(len(x)):
    sum = sum + x[i]*y[i]
print(sum)


# In[68]:


"""MATRIX ADDITION BY FIRST PRINCIPLES"""
dim = 3
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [2,3,5]
s2 = [4,8,6]
s3 = [55,6,67]

A = []
A.append(r1)
A.append(r2)
A.append(r3)

B = []
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

C = [[0,0,0] , [0,0,0] , [0,0,0]]
#it is not acceptable C = [[] , [] , []]

for i in range(dim):
    for j in range(dim):
        C[i][j] = A[i][j] + B[i][j]
print(C)
        
    
    





# In[69]:


"""MATRIX MULTIPLICATION"""
dim = 3
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [2,3,5]
s2 = [4,8,6]
s3 = [55,6,67]

A = []
A.append(r1)
A.append(r2)
A.append(r3)

B = []
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

C = [[0,0,0] , [0,0,0] , [0,0,0]]
"""C[i][j] is the dot product of the ith row of A and the jth column"""
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]       
        #dot product of A[i][......] and B[j][....]
print(C)
        
        


# In[70]:


import numpy
dim = 3
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [2,3,5]
s2 = [4,8,6]
s3 = [55,6,67]

A = []
A.append(r1)
A.append(r2)
A.append(r3)

B = []
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

M = numpy.mat(A)
N = numpy.mat(B)
print(M*N)


# In[ ]:


"""Let M be a matrix of numbers that has already been defined and populated.
We wish to find the sum of the elements in each row and store all such row-sums in a list called rsum.
For the i^{th}i throw, rsum[i] should be the sum of all elements in that row. 
Select the correct code snippets that achieve this"""
dim = 3
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

A = []
A.append(r1)
A.append(r2)
A.append(r3)
b = []
for i in range(dim):
    b.append(0)
    for j in range(dim):
    b[-1] += A[i][j]
print(b)



# In[71]:


"""matrix is a square matrix that is given to you. Select all correct implementations of a program that 
copies the last column of the matrix into a list named last_col."""
n = len(matrix)
last_col = [ ]
for i in range(n):
    for j in range(n):
        if j == n - 1:
        	last_col.append(matrix[i][j])
n = len(matrix)
last_col = [ ]
for i in range(n):
    last_col.append(matrix[i][-1])


# In[72]:


"""Accept a positive integer n as input and print the list of first n positive integers as output."""
n = int(input())
l = []
for i in range(1,n+1):
    l.append(i)
print(l)


# In[74]:


"""Accept a sequence of words as input, append all these words to a list in the order in which they are entered, 
and print this list as output. The first line in the input is a positive integer nn that denotes the number
of words in the sequence.The next nn lines will have one word on each line"""
n = int(input())
l = []
while (len(l)<n):
    p = input()
    l.append(p)
print(l)


# In[20]:


"""Accept a sequence of comma-separated integers as input and print the maximum value in the sequence as output."""
num = input()
L = num.split(',')
maxn = 0
for i in range(len(L)):
    L[i] = int(L[i])
    if L[i] > maxn:
        maxn = L[i]
print(maxn)


# In[79]:


num = "1,2,3,4,5"
L = num.split(",")
M = list(num)
print(L)
print(M)


# In[85]:


'''This question introduces you to the idea of prefix codes. Prefix code is a block of visible code that is already 
provided to you. You have to type your code below the prefix code. Note that the contents of the prefix cannot
be modified.
A list L of words is already given to you as a part of the prefix code. Print the longest word in the list.
If there are multiple words with the same maximum length, print the one which appears at the rightmost end of 
the list.
You do not have to accept input from the console as it has already been provided to you.'''
L = input().split(',')
maxl = 0
long_word = ''
for i in L:
    
    if(len(i)>=maxl):
        maxl = len(i)
        word = i
print(word)


# In[ ]:


'''Accept a space-separated sequence of positive real numbers as input.Convert each element of the sequence into 
the greatest integer less than or equal to it. Print this sequence of integers as output, with a comma between 
consecutive integers.'''
seq = input().split(' ')
new_list = []
for i in seq:
    new_list.append(int(float(i)))
#print(*new_list , sep = '')
for j in new_list:
    print(new_list , end = '')


# In[93]:


'''Accept a sequence of comma-separated words as input. Reverse the sequence and print it as output.'''
seq = input().split(',')
List = []
for i in seq:
    List.append(i)
b = List[::-1]
print(*b , sep = ',')



# In[100]:


'''Accept a square matrix as input and store it in a variable named matrix.
The first line of input will be, nn, the number of rows in the matrix. 
Each of the next nn lines will have a sequence of nn space-separated integers.'''
n = int(input())
matrix = []
for i in range(n):
    row = input().split() #'1 2 3 4'
    #row = ["1" ,"2", "3", "4"]
    for j in range(n):
        row[j] = int(row[j])
    #[1, 2, 3, 4]
    matrix.append(row)
    
print(matrix)


# In[101]:


"""Create Empty Matrix"""
m =  int(input())
n = int(input())
matrix =  []
for i in range():
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)
print(matrix)
        


# In[114]:


'''Accept a positive integer nn as input and print the identity matrix of size n times n×n. Your output should have
n lines, where each line is a sequence of n comma-separated integers that corresponds to one row of the matrix.'''
n = int(input())
Matrix = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    Matrix.append(row)
    #print(*row , sep = ',')
#print(Matrix)
    for k in range(len(row)-1):
        print(row[k] , end = ',')
    print(row[-1])





# In[118]:


'''Accept a square matrix A and an integer s as input and print the matrix A as output. Multiplying a matrix by an 
integer ss is equivalent to multiplying each element of the matrix by s.The first line of input is a positive 
integer,n, that denotes the dimension of the matrix A. Each of the next nn lines contains a sequence of 
space-separated integers. The last line of the input contains the integer s.Print the matrix ⋅A as output. 
Each row of the matrix must be printed as a sequence of space separated integers, one row on each line.
There should not be any space after the last number on each line. If the expected output looks exactly like the 
actual output and still you are getting a wrong answer, it is because of the space at the end.'''
n = int(input())
matrix = []
for i in range(n):
    row = input().split()
    for j in range(n):
        row[j] =int(row[j])
    matrix.append(row)
s = int(input())
for i in range(n):
    for j in range(n-1):
        print(matrix[i][j]*s , end = ' ')
    print(matrix[i][-1]*s)
    


# In[ ]:


"""Accept two square matrices AA and BB of dimensions n \times nn×n as input and compute their sum A + BA+B.
The first line will contain the integer nn. This is followed by 2n2n lines. Each of the first nn lines is a 
sequence of comma-separated integers that denotes one row of the matrix AA. Each of the last nn lines is a 
sequence of comma-separated integers that denotes one row of the matrix BB.
Your output should again be a sequence of nn lines, where each line is a sequence of comma-separated integer 
that denotes a row of the matrix A + BA+B"""
n = int(input())
N1 = []
N2 = []
M = []
for i in range(n):
    row1 = input().split(',')
    for j in range(n):
        row1[j] = int(row1[j])
    N1.append(row1)
    
for l in range(n):
    row2 = input().split(',')
    for m in range(n):
        row2[m] = int(row2[m])
    N2.append(row2)
    
for p in range(n):
    row3 = []
    for q in range(n):
        row3.append(0)
        M.append(row3)
for i in range(len(N1)):
    for j in range(len(N2)):
        M[i][j] = N1[i][j] + N2[i][j]
        if(j != len(N1) - 1):
            print( M[i][j] , end = ',')
        else:
            print(M[i][j])


# In[2]:


'''L is a list of real numbers that is already given to you. You have to sort this list in descending 
order and store the sorted list in a variable called sorted_L. 
 You do not have to accept input from the console as it has already been provided to you. You do 
not have to print the output to the console. Input-Output is the responsibility of the invisible 
code for this problem. '''
L = [1.1 , 2.2 , 3.3]
sorted_L = []
while len(L) > 0:
    t = 0
    for i in L:
        if i > t:
            t = i
    sorted_L.append(t)
    L.remove(t)
    t = 0
    
print(sorted_L)
            
            


# In[5]:


'''In the first line of input, accept a sequence of space-separated words. In the second line of input, 
accept a single word. If this word is not present in the sequence, print NO. If this word is present in the 
sequence, then print YES and in the next line of the output, print the number of times the word appears 
in the sequence'''
words = input().split(" ")
test = input()
if test not in words:
    print("NO")
else:
    print("yes")
    count = 0
    for word in words:
        if test == word:
            count += 1
    print(count)
        


# In[23]:


'''You are given a list marks that has the marks scored by a class of students in a Mathematics test. 
Find the median marks and store it in a float variable named median. You can assume that marks is 
a list of float values. 
Procedure to find the median
(1) Sort the marks in ascending order. Do not try to use built-in methods. Look at the lecture 4.5 of 
week-4 to get a better idea. 
(2) If the number of students is odd, then the median is the middle value in the sorted sequence. If the 
number of students is even, then the median is the arithmetic mean of the two middle values in the 
sorted sequence. 
You do not have to accept input from the console as it has already been provided to you. You do not 
have to print the output to the console. Input-Output is the responsibility of the autograder for this 
problem. Refer PPA-11 if you are not sure how this works. 
'''
marks = [30, 20, 40, 10, 50]
def solution(marks):
    sorted_marks = []
    while marks != []:
        min_mark = 100
        for i in marks:
            if min_mark > i:
                min_mark = i
        sorted_marks.append(min_mark)
        marks.remove(min_mark)
    n = len(sorted_marks)
    if n % 2 != 0:
        median = float(sorted_marks[n // 2])
        
    else:
        mid1 = marks[n//2]
        mid2 = marks[(n//2)-1]
        median = float((mid1 + mid2) / 2)
    return median
solution(marks)
        


# In[7]:


'''Accept two square matrices A and B of dimensions n×n as input and compute their product AB. 
The first line of the input will contain the integer n. This is followed by 2n lines. Out of these, each of 
the first n lines is a sequence of comma-separated integers that denotes one row of the matrix A. Each 
of the last n lines is a sequence of comma-separated integers that denotes one row of the matrix B. 
Your output should again be a sequence of n lines, where each line is a sequence of comma-separated 
integers that denotes a row of the matrix AB. '''
n = int(input())
A = []
B = []
M = []
for i in range(n):
    row1 = input().split(',')
    for j in range(n):
        row1[j] = int(row1[j])
        A.append(row1)
for i in range(n):
    row2 = input().split(',')
    for j in range(n):
        row2[j] = int(row2[j])
        B.append(row2)
for i in range(n):
    row3 = []
    for j in range(n):
        row3.append(0)
        M.append(row3)
        
for i in range(n):
    for j in range(n):
        for k in range(n):
            M[i][j]  =  M[i][j]+(A[i][k] * B[k][j])
            
for i in range(n):
    for j in range(n):
        if j != n-1:
            print(M[i][j] , end = ",")
        else:
            print(M[i][j])

        
    
        


# In[12]:


'''You are given the names and dates of birth of a group of people. Find all pairs of members who share 
a common date of birth. Note that this date need not be common across all pairs. It is sufficient if both 
members in a pair have the same date of birth. 
The first line of input is a sequence of comma-separated names. The second line of input is a sequence 
of comma-separated positive integers. Each integer in the sequence will be in the range [1, 365], 
endpoints inclusive, and stands for some day in the year. 
Find all pairs of names that share a common date of birth and store them in a list called common. 
Each element of this list is itself a list, and should be of the form [name1, name2], such 
that name1 comes before name2 in alphabetical order.'''
name = input().split(',')
bdays = input().split(',')
n = len(name)
for i in range(n):
   bdays[i] = int(bdays[i])
   
common = []
for i in range(n):
   for j in range(n):
       if i != j and bdays[i] == bdays[j] and name[i]<name[j]:
           pair = [name[i],name[j]]
           common.append(pair)
print(common)


# In[19]:


'''You are given a sequence of n points, (xi,yi), 1≤i≤n, in the 2-D plane as input. Also, you are given a 
point P with coordinates (x,y). Print all points in the sequence that are nearest to P. If multiple points 
have the same least distance from P, print the points in the order of their appearance in the sequence. 
The first line of the input is an integer n, representing the number of points in the sequence. Each of 
the next n lines contains the co-ordinates of a point separated by comma. The last line contains 
the x and y co-ordinates of the point P. Assume that all the x and y co-ordinates are integers. 
The distance between two points (x1,y1) and (x2,y2) is ඥ(𝑥ଵ − 𝑥ଶ)
ଶ + (𝑦ଵ − 𝑦ଶ)
ଶ. You can assume 
that the maximum distance from P to any point will not exceed 1000.'''
n = int(input())
l = []
for i in range(n):
    l.append(input())
point = input().split(',')
x = int(point[0])
y = int(point[1])

min_dist = 1000
min_list = []
for i in range(n):
    temp = l[i].split(',')
    temp_x = int(temp[0])
    temp_y = int(temp[1])
    dist = ((x - temp_x)**2 + (y - temp_y)**2)**0.5
    
    if dist < min_dist:
        min_dist = dist
        min_list = [l[i]]
    elif dist == min_dist:
        min_list.append(l[i])

for points in min_list:
    print(points)
        
    
    


# In[ ]:




