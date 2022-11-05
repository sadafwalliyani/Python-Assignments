a= 7 #global variable
def abc():
    a=8 # local variable 
    return a
print(abc())
print(a)

a=7 
b=1

def abc():
    global a # update global variable using global key
    a=8
    b=20
    return a, b
print(abc()) # call function and return local variable value
print(a,b)


