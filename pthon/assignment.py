"""
Question 1:
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a
farm. How many rabbits and how many chickens do we have?
Hint:
Use for loop to iterate all possible solutions.
*******************************************************
"""
from itertools import chain


heads=35
legs=94
# print("chikesn",legs/2)
# chickens=47
# print("Rabbits",legs-chickens)
# rabbits=47
# print(chickens/2)
# print(rabbits/4)

print("Rabbits",legs/4)
rabbits=23
print("chickens",legs-rabbits)
chickens=71
print(rabbits/4)
print(chickens/2)
