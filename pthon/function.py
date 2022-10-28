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
