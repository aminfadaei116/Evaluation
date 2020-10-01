# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 04:20:25 2020

@author: a
"""


M = int(input("Please enter the M value: "))
N = int(input("Please enter the N value: "))


A = []
first_method = []
## This is the first method
print("now enter every row of the matrix")
for i in range(M):
    temp = [int(i) for i in (input().split())]
    A.append(temp)
    if(i % 2 == 0):
        for j in temp:
            first_method.append(j)
    else:
        for j in temp[::-1]:
            first_method.append(j)
            
result_string = ""
for num in first_method:
    result_string += str(num) + " "
    
print("The first result is: ", result_string)
    