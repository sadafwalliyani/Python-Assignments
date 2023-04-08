a= 7 #global variable 

def abc():
    a=8 #local variable 
    return a 

print(abc()) #call function and return local variable 
print(a)


a= 7 #global variable 
b=1

def abc():
    global a #update function and return variable value
    a=8 #local variable 
    b= 20
    return a, b 

print(abc()) #call function and return local variable 
print(a,b)

a= 7 #global variable 
b=1

def abc():
    a=8 #local variable 
    b= 20
    global c
    c="Pakistan"
    return a, b, c

print(abc()) #call function and return local variable 
print(a,b,c)


a=7

def xyz():
    return a
print(abc())
print(xyz())

#show error
"""a=7 
def abc():
    a=8
    global a
    return a

def xyz():
    return

print(abc())
print(xyz())"""

