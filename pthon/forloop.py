student={
    'id':1,
    "name":"sadaf",
    "Father_name":"Mansoor",
    'Education':"MSDS"
}
for i in student:# iterate on keys
    print(i)

    student={
    'id':1,
    "name":"sadaf",
    "Father_name":"Mansoor",
    'Education':"MSDS"
}
for i in student.values():# iterate on values
    print(i)

    student={
    'id':1,
    "name":"sadaf",
    "Father_name":"Mansoor",
    'Education':"MSDS"
}
for i in student.items():# iterate on items
    print(i)

    studetn1 = {
        "id":10001,
         "name":"Sadaf",
           "father_name":"Muhammad Aslam",
           "education":"MSDS"}

for k,v in studetn1.items():# iterate on K V 
    print(k, v)
    k,v=("name",["sadaf","Madiha"])
    print(k)
    print(v)

for i in range (1,11):
        print(i) #body
for i in range (1,11):
        [i*i for i in range(1,11)]
print(i*i) 


print(list((i*i for i in range(1,11))))
print({i:i*i for i in range(1,20)})

print({code:chr(code)for code in range(0,100)})

# list comprehensive style

print([i for i in range(1,20)])
print([i*i for i in range(1,11)])

for row in range(1,11):
    print(row, "*"*row)# pyramid print

for row in range(1,27):
    print(row, end="\t")
    for c in range(65,65+row):
        print(chr(c), end=" ")
    print("")


print([(i,j) for i in range(1,10) for j in range(65,65+i)])
print([(i,chr(j)) for i in range(1,10) for j in range(65,65+i)])

data = [[1,2,3],
       [4,5,7],
       [20,21,25]]
for row in data:
    for c in row:
        print(c)
        print()
for row in data:
    for c in row:
        print(c, end=" ")
        print()


      
        