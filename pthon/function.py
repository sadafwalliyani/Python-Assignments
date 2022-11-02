"""
FUNTIONS
    Function name
    arguments
Function body
    Set of statement
Function Calling
    name()
    pass arguments
"""

"""
PRE-DEFINE 
USER-DEFINE
RETURN:
    if store output in variable ## Non-return
    if not store output in variable ## defualt
    not required any argument when we call ## required arguments
    function will not work without it ## optional arguments
    if we did'nt provide it function will also work with some defualt arguments value ## Generator function
    generate value one by one
    alway remember old generated value ## Lambda function
    one line function
    it has no name
    one time use only
"""

"""
RECURSIVE FUNCTION 
    It call in own body 

"""

# PRE-DEFINE FUNCTION

from cgitb import text
from lib2to3.pgen2.token import RPAR


print("Helloo") 
print(len('Hello'))
print(id('Hello'))

# RETURN/NON-RETURN FUNCTION

a= len("Pakistan Zinda Baf") #None return 
print(a) #unable to store value in variable 


# # USER DEFINE FUNCTION 
# def function_word(arg1, arg2,):
#     statement1
#     statement2

# function_word(arg1, arg2)


def piaic_introduction():
    print("PIAIC") # statement1
    print("Course") # statement2
    print("\t AI") # statement3
    print("\t Blockchain") # statement4
piaic_introduction()
print(piaic_introduction)

def piaic_introduction1():
    txt="""
    PIAIC 
    Course offer 
    AI
    Blockchain
    Cloud Computing 
    Metaverse 
    """
    return txt
print(piaic_introduction1()) #return function


# required arguments
def addition(num1, num2):
    return num1+num2
print(addition(7,20))
print(addition(7,20000))
print(addition(7,3000))
print(addition(7,800))

# OPTIONAL ARGUMENTS

def addition(num1=0, num2=0):
    return num1+num2

print(addition())
print(addition(1))
print(addition(2,3))
print(addition(10,30))

# required and optional arguments

def making_briyani(rice,meat,tomatoes="0.5 KG"):
    txt=f"""
    Boiling {rice} rice...
    making qorma with {meat} meat...
    mixing tomatos {tomatoes}...
    now you enjoy briyani:)
    """
    return txt
a = making_briyani("Sehla",'chiken')
print(a)
print(a)
print(a)

print(print("Pakistan"))
print(making_briyani("Basmati","Beaf","1 KG"))


# optional argument2 unlimited

def my_sum(num1, *num): #*num
    print(num1,num)
    return num1+sum(num)
my_sum(10,2,2,2,2,2,2)


import numpy as np
num=np.array((2,2,2,2,2))
print(2+num)


def my_sum(num1,*num): # unlimited num/parameters can take
    print(num1,num)

    result = num1

    for n in num:
        result +=n

        return result

print(my_sum(7,2,2,3,4,5))

def my_sum(num1,num2,*num): # *num 
    print(num1,num2,num)
    return num1 + num2 +sum(num)

print(my_sum(7,2,2,3,4,5))


def my_sum(*num): # *num during define = tuple
    print(num)
    return sum(num)
print(
my_sum(7,2,2,3,4,5))


a, b=[20,25,] # unzip
print(a)
print(b)

l = [1,20,30,50,100]
print(l[0],l[1],l[2],l[3],l[4])
print(*l) #during call * before iterated datatype = unzip values
print(1,20,30,50,100)
print(l)

print(my_sum(*l))

def my_new_sum(num1,num2,num3,num4):
    return num1 + num2 + num3 + num4

l = [10,20,30,40]

# my_new_sum(*l)
# my_new_sum(l[0],l[1],l[2],l[3])
my_new_sum(50,l[0],*l[-2:])

#calling function with keyword arguments

def student_card(rollnum, name, fname, course):
    card=f"""
    PIAIC STUDENT IDENTITY CARD
    Roll No      : {rollnum}
    Name         : {name}
    Father's Name: {fname}
    Course       : {course} 
    """
    return card

print(student_card(1, "sadaf","Mansoor", "AI"))
print(student_card(1, "sadaf","Mansoor", "CNC"))
print(student_card(1, "sadaf","Mansoor", "BLOCK CHAIN"))
