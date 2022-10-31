# ERRORS HANDLING 
"""
Error Types
=Compile time error
=during coding
=Logical Error
=bussiness logic write wrong
=Run Time Error
=live production applications errors
"""

"""
1=[1,2]
print(1[7]) # try to access index 7 value
"""
l = [1,2]
print(l[0])

def my_sum(x,y):
    return x + x # write wrong logic
print(my_sum(7,9)) # We can resolve this error through testing


def my_sum(x,y):
    return x + y # write wrong logic
print(my_sum(7,9)) # We can resolve this error through testing

print(1000*60*40)

"""
How to deal run time errors
try:
    statement 
    # write statement where error chances
except (ErrorClassName,e2,e3,...):
    run if error occured in above statement
else:
    run if not error occured in above statement
finally:
    always run
    """

"""
print("Start Line")
a=7
b=0
print(a/b)
print("End Lines")
"""
print("Start Line")
a=7
b=0

try:
    print(a/b)
except(ZeroDivisionError):
    print("Ap kesi bhi value ko zero divide nhi kr sakty!")
print("End Lines")

print("Start Line")
a=7
b=2

try:
    print(a / b)
except(ZeroDivisionError):
    print("Ap kesi bhi value ko zero divide nhi kr sakty!")
print("End Lines")

print("Start")

a = 7
b = 0
l = [1,2,3]

try:
#     print(a / b)
    print(l[5])
    open("abc.txt")
except (ZeroDivisionError,IndexError,FileNotFoundError):
    print("You write something wrong!")

print("End")

print("Start")

a=7
b=0
l=[1,2,3]

try:
    print(a/b)
except(ZeroDivisionError):
    print("Can't divide any number with zero")
    
try:
    print(l[5])
except(IndexError):
    print("Index not available")

try:
    open("anc.txt")
except (FileNotFoundError):
    print("end")
