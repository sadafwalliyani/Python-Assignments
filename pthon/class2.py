#AI Class-4

from tkinter.font import names


print('Class-5')
# oprand 
# Operators

print(10+5)
print(10-5)
print(10*5)
print(10/5)


#Pre defined functions in Python
# print()
# type()
name= "Sadaf"
print(type(name)) # data type 
# id()
print(id(name)) #memory address
# len() 
print(len(name)) #length (count number of charactors)

# Types of string
# 1
name1= "sadaf"
print(name,type(name))
# 2 Define space Characters (\n \t)
data='Name:\t\tSadaf\nfatherName:\tMansoor\nBatch\t\t36-37'
print(data,)
# 3 Triple Code
data1="""
Triple Code Example
Name:           Sadaf
FatherName:     Mansoor
Batch:          36-37
"""
print(data1)

# Concatination(Combine two or more variables and values)| Text formation
first_name="Sadaf"
father_name="Mansoor"
batch="36-37"
print(first_name,father_name,batch)

#
data2="""
Name:           {}
FatherName:     {}
Batch:          {}
""".format( name,father_name,batch)

print(data2)
data3="""
Name:           {1}
FatherName:     {0}
Batch:          {2}
""".format( father_name,name,batch)
print(data3)

data4= f"""
Name:           {name}
FatherName:     {father_name}
Batch:          {batch}
"""
print(data4)
