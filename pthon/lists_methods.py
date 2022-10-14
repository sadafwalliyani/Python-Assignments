#List and Tuple

#List mutable - changeable []
#tuple imutable- Unchangeable ()

#List
from ast import Num
import numbers
from operator import index
from unicodedata import name

    #       0       1       2       3
names= ['sadaf','rustam', 'Ali','samra']
    #    -4        -3       -2     -1
print(names[2]) #list[index] extract value with positive index 
print(names[-1]) #List[Start:end] extarct value with negative index
print(names) #list[start:end:seq] 

print('before',names)
names[0] = 'Sadaf Mansoor'

print('after',names)

#extract multiple values from list or tuple (start enclude, end exclude one minus)

#esc->m-shift+enter

print(names[1:3]) # start enclude, end exclude index-1
print(names[1:4]) # start enclude, end exclude index-1

#while loop
i=0
while i<len(names):
    print(names[i])
    i+=1

# While Lopp

# s= int(input('start No:'))
# e= int(input('end No:'))
# i=s
# while i<e:
#     print(names[i])
#     i+=1

#list[start:end:seq] 
# Start =enclude
#end = Exclude
#sequence =steps

numbers= list(range(1,21))
print(numbers)

