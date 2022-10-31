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

"""
Dynamic Error Handling with custome message
"""
print("Start")

a=7
b=0
l=[1,2,3]

try:
    open("abc.text")
except Exception as e:
    print("Something Wrong",e)
    print("End")

print("Start")

a=7
b=0
l=[1,2,3]

try:
   print(a/b)
except Exception as e:
    print("Something Wrong",e)
    print("End")

print("Start")

a=7
b=0
l=[1,2,3]

try:
    print(a/b)
    print("abc.txt")
except Exception as e:
    print("Something Wrong",e)
    print("End")

print("Start")

a = 7
b = 0
l = [1,2,3]

try:
    print(a / b)
except Exception as e:
    print("something wrong!",e)
else:
    print("Run if error not occured in above statement")
print("End")

print("Start")

a = 7
b = 2
l = [1,2,3]

try:
    print(a / b)
except Exception as e:
    print("something wrong!",e)
else:
    print("Run if error not occured in above statement")
print("End")

print("Start")
a = 7
b = 0
l = [1,2,3]

try:
    print(a / b)
except Exception as e:
    print("something wrong!",e)
else:
    print("Run if error not occured in above statement")
finally:
    print("always run!")
print("End")

"""
Create our own excption class
"""

class StudentCard():
    def __init__(self,roll,name,age):
        if age < 18 or age > 60:
            raise Exception("not allowed less 18 or greater than 60 years old student")
        self.roll= roll
        self.name= name
        self.age= age

s1 = StudentCard(1,"Sadaf Mansoor",30)
print(s1.age)
print(s1.name)
print(s1.roll)

s2 = StudentCard(2,"Rustam",34)
print(s2.age)
print(s2.name)
print(s2.roll)

try:
  print(s2=StudentCard(20,"ALI",78))
except Exception as er:
    print("Something Wrong",er)