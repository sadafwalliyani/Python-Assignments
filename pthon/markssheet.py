
username = input("Enter username:")

e=100
m=100
u=100
isl=100
bio=100
total=e+m+u+isl+bio
per=total/500*100
print(username)
print("Sub :  Marks: ",)
print("Eng :  Marks: ",e)
print("Math:  Marks: ",m)
print("Urdu:  Marks: ",u)
print("Isl :  Marks: ",isl)
print("Bio :  Marks: ",bio)
print("Total Marks",total)
print("Percentage",per)
print('Grade',)

if per>=80:print("A+")
elif per>=70:print("B")
elif per>=60:print("C")
else:print("fail")
