# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 04:21:13 2020

@author: a
"""


first = [i for i in (input("Please enter the first string: "))]
second = [i for i in (input("Please enter the second string: "))]

N, M = len(first) + 1, len(second) + 1
A = [[0 for i in range(M)] for j in range(N)]
B = [[0 for i in range(M)] for j in range(N)]
for j in range(1, M):
    for i in range(1, N):
        if first[i-1] == second[j-1]:
            temp = max(A[i-1][j-1]+1, A[i][j-1], A[i-1][j])
            B[i][j] = "side"
        else:
            temp = max(A[i][j-1], A[i-1][j])
            if A[i][j-1] <= A[i-1][j]:
                B[i][j] = "up"
            else:
                B[i][j] = "left"
        A[i][j] = temp

current_X = M - 1
current_Y = N - 1
res = []
while(True):
    if B[current_Y][current_X] == 0:
        break    
    if B[current_Y][current_X] == "side":
        res.append(first[current_Y-1])
        current_X -= 1
        current_Y -= 1
    elif B[current_Y][current_X] == "up":
        current_Y -= 1
    elif B[current_Y][current_X] == "left":
        current_X -= 1
    
result = ""
for i in range(len(res)):
    result += str(res.pop())
    
print("The largest sub string is: ", result, "with the size of: ", len(result))


