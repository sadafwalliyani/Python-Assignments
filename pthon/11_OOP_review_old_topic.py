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

