# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 04:48:38 2020

@author: a
"""


M = int(input("Please enter the M value: "))
N = int(input("Please enter the N value: "))

## getting the matrix
A = []
print("now enter every row of the matrix")
for i in range(M):
    temp = [int(i) for i in (input().split())]
    A.append(temp)
    
# An example here
    
# M = 5
# N = 4  

# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 3, 2, 3], [1, 1, 2, 2]]
    
## new variables
direction = ["right", "down", "left", "up"]
direction_step = 0
current_X = -1
current_Y = 0
result = []
end_X = N
end_Y = M-1
x_step = 0
y_step = 0

# computation

for step in range(M * N):
    if direction[direction_step % 4] == "right":
        current_X += 1
        x_step += 1
    elif direction[direction_step % 4] == "down":
        current_Y += 1
        y_step += 1
    elif direction[direction_step % 4] == "left":
        current_X -= 1
        x_step += 1
    elif direction[direction_step % 4] == "up":
        current_Y -= 1
        y_step += 1

    result.append(A[current_Y][current_X])
    if (x_step == end_X and end_X != 0):
        direction_step += 1
        end_X -= 1
        x_step, y_step = 0, 0
    elif(y_step == end_Y and end_Y != 0):
        direction_step += 1
        end_Y -= 1
        x_step, y_step = 0, 0

        
result_string = ""
for num in result:
    result_string += str(num) + " "
    
print("The first result is: ", result_string)

