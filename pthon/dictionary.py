#dictionary
# {
#     key:value1
#     key:value2,
#     key:value3
#     ...
# }

# always start end with { }
# keys and values
# : seprators between key and values
# , seprators between key : values pair

["qasim","aslam","sadaf",30,]
# we will replace indexes with keys 
# position doesnt matter in dictionary 

data={
    'name': 'Sadaf',
    'fname':'Mansoor',
    'age': 30,
    'qualification': 'MED',
    'skills': ['AI','Graphics','Cloud']
}
# access key value from dictionary 
print(data['name'])
print(data['fname'])

# panda 

import pandas as pd
data2={
'name': ['Sadaf','Sammra','Madiha'],
'fname':['Mansoor','Asif','Saeed'],
'Course':['AI','ML','DS']
}
df=pd.DataFrame(data2)
print(df)


data4={}
data4['name']= 'Sadaf Mansoor' #add key value 1
data4['fname']= 'Mansoor' #add key value 2
data4['Course']= 'AI' #
data4['name']= 'Hamza'
data4['name']= data4['name']+"AI student"

print(data4['fname'])
print(dir(data4))


print(4/(3*(2-1)) ) #same result 
print(4/(3*(2-1)) )
print(4 + 3 % 5)
print(4.00/(2.0+2.0))
x=1
print(x<<2) #The binary form of 1 is 0001. The expression x<<2 implies we are performing bitwise left shift on x. This shift yields the value: 0100, which is the binary form of the number 4.
