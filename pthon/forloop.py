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