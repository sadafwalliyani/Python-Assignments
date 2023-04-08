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

def solve(heads,legs):
    error_msg = "No solution"
    chicken_count =0
    rabbit_count =0

    if(heads>=legs):
        print(error_msg)
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))
        print(chicken_count,rabbit_count)
        print(error_msg)
