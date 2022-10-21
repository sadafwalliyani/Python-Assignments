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


# data4={}
# 'name': ['Sadaf','Sammra','Madiha'],
# 'fname':['Mansoor','Asif','Saeed'],
# 'Course':['AI','ML','DS']

print(4/(3*(2-1)) )
print(4/(3*(2-1)) )