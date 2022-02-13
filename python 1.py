#!/usr/bin/env python
# coding: utf-8

# In[16]:


"""You are given a string and two non-negative integers as input.
The two integers specify the start and end indices of a substring in the given string. 
Create a new string by replicating the substring a minimum number of times so that
the resulting string is longer than the input string.
The input parameters are the string, start index of the substring and the end index of substring 
(endpoints inclusive) each on a different line."""
string = input()
start =  int(input())
end = int(input())
substring = string[start:end+1]
a = len(string)
b = len(substring)
repeat = a // b +1
print(substring*repeat)


# In[17]:


"""A class teacher has decided to split her entire class into four groups, namely Sapphire,
Peridot, Ruby, and Emerald for sports competitions.For dividing the students into these 
four groups, she has followed the pattern given below:
Group							
Sapphire	1	5	9	13	17	21	...
Peridot	2	6	10	14	18	22	...
Ruby	3	7	11	15	19	23	...
Emerald	4	8	12	16	20	24	...
All the students are represented by their roll numbers. Based on the above pattern, 
given the roll number as input, print the group the student belongs to as output."""
a = int(input())
if a % 4  == 1:
    print("Sapphire")
if a % 4 == 2:
    print("Peridot")
if a % 4 == 3:
    print("Ruby")
if a % 4 == 0:
    print("Emerald")


# In[18]:


"""A data science company wants to hire data scientists from IIT Madras. The company follows a certain 
criteria for selection: for a student to be selected, the number of backlogs should be at most 55 and 
the CGPA (Cumulative Grade Point Average) should be greater than 66. If the student does not fit the 
above criteria, then the student is not offered the job. If the student is selected, then the salary 
offered is equal to 55 times his/her CGPA (in lakhs).Accept the number of backlogs (integer) and the
CGPA (float) of the student as input. Your task is to determine if the student is selected or not. 
If the student is selected, then print the package. If not, then print the string Not Selected."""
backlogs = int(input())
CGPA = float(input())
if backlogs <= 5 and CGPA > 6.0:
    print(CGPA*5)
    
else:
    print("Not Selected")


# In[ ]:


"""A word is said to be perfect if it satisfies all the following criteria:
(1) All the vowels (a,e,i,o,u) should be present in the word.
(2) Let the vowels be represented as v_1 = a, v_2 = e, v_3 = i, v_4 = o, v_5 = uv 
1​=a,v 2​=e,v 3​=i,v 4​=o,v 5​=u in lexical order.
If i < ji<j, then the first appearance of v_iv i​in the word should come before the first appearance of v_jv j​
If i < ji<j, then the count of v_iv i​should be greater than or equal to the count of v_jv j​
Accept a word as input and do the following:
 (1) If it is a perfect word, print It is a perfect word
 (2) If the word is not a perfect word, print It is not a perfect word"""
word = input()
vowels = "aeiou"
if ('a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word):
    a = word.index("a")
    e = word.index("e")
    i = word.index("i")
    o = word.index("o")
    u = word.index("u")
    if a<e<i<o<u:
        print("It is a perfect word")
    
else: 
    print("It is not a perfect word")


# In[28]:


'''Accept four integers as input and write a program to print these integers in non-decreasing order.
The input will be four integers in four lines. 
The output should be a single line with all the integers separated by a single space in non-decreasing order.
Note: There is no space after the fourth integer.'''
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
a = [n1, n2, n3, n4]
b = sorted(a)
y = int()
for x in b:
    y = x
    
print(y)


# In[29]:


'''Two integers are co-prime if the only common divisor between the two integers is one.
Accept two positive integers as input in two different lines. Print Copriif the two integers are co-prime,
else print Not Coprime. Assume that both the integers are greater than two.'''
n1 = int(input())
n2 = int(input())
flag = True
for x in range(2, n1):
    if n1 % x == 0:
        for y in range(2, n2):
            if n2 % y == 0:
                flag = False
                break
if flag:
    print("Coprime")
else:
    print("Not Coprime")


# In[48]:


"""Accept a string as input, print Integer if the string is an integer, print Float if it a
float, else print None."""
string = str(input())
if string.isdigit():
    print("Integer")
elif string.replace('.' , '' ,1).isdigit():
    print("Float")

else:
    print("None")


# In[51]:


'''Multiple Select Questions (MSQ) could have more than one correct answer. The marks scored by a 
studentin a MSQ will be determined by the following conditions: 
(1) If the question has c correct options, each individual correct option carries = marks 
(2) If a student selects any of the wrong options, the marks awarded for the question will be 0. 
Calculate the marks obtained by the student and print this as float value. 
The input contains four lines. 
(1) First line is the number of marks for the question. 
(2) Second line contains the number of options for the question. 
(3) Third line is a comma-separated sequence of correct options for this question. 
(4) Fourth line is a comma-separated sequence of options given by the student. 
Write a program to print the number of marks scored by a student. 
Note: Options are numbered using positive integers in the range [1, 9], endpoints inclusive. A 
question willhave at most nine 9',options. The number of marks and the correct options will always be 
integers. 
If the question has five options in total, then the options will be numbered as 1,2,3,4,5. '''
marks = int(input())
option = int(input())
correct_options = input().split(',')
answered_options =  input().split(',')
c = 0
for i in answered_options:
    if i in correct_options:
        c += 1
    else:
        c= 0
        break
marks_per_question = marks/len(correct_options)
total_marks = marks_per_question*c
print(total_marks)



# """Consider two non-empty strings a and b of lengths n1 and n2 respectively, which contain only 
# numbers as their characters. Both the strings are in ascending order, that is a[i]≤a[j] for 0≤i<j<n1. The 
# same holds true for b. You need to merge both the strings into one string of length n1+n2 such that all 
# the characters of this combined string are also in ascending order. 
# Accept a and b as input and print this merged string as output."""

# In[56]:


"""Consider two non-empty strings a and b of lengths n1 and n2 respectively, which contain only numbers as their
characters. Both the strings are in ascending order, that is a[i]≤a[j] for 0≤i<j<n1. The same holds true for b.
You need to merge both the strings into one string of length n1+n2 such that all the characters of this combined 
string are also in ascending order. Accept a and b as input and print this merged string as output."""

n = input()
s = input()
t = s+n
w = '0123456789'
m =''
for x in range(len(w)):
    print(x)
    for y in range(len(t)):
        print(y)
        if t[y] == w[x]:
            m += w[x]
print(m)


# In[ ]:




