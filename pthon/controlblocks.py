# control blocks (control particular fucntion)

# if 
    # else
    # elif
    # finally
# while
    # break
    # continue
    # pass
# for
    # break
    # continue
    # pass
# try:
    # except
    # finally
    # class
# Function 
    # def

# Reserve words
    # https://realpython.com/lessons/reserved-keywords/


# while Loop
    # break
    # continue
    # pass
# while Logic:
    #statement
    #increment/decrement

print(5==10)

if True:
    print('Pakistan')
if False:
    print('Hindustan')


# while
"""* logic
* flag = counter
* increment/decrement
* break
* continue
* pass """

counter = 0

while counter<=10:
    print("Pakistan Zinda bad", counter)
    counter+=1

    counter = 100

"""while counter>=90:
    print("Pakistan Zinda bad", counter)
    counter-=1
"""
a =1
print(a)
a= a+ 1 #old variable value add with new one
print(a)
a+=1 # old variable value add with new one
print(a)

counter = 0 #flage

while counter<=10: #logic
    print("sadaf", counter) #statement 
    counter+=1 #increment/decrement 

#break 
counter =0
while counter<= 1000000:
    print('Your dead',counter)

    if counter==5:
        break
    counter +=1  
# break in last
counter = 0
while counter <= 1000000:
    counter += 1
    print("Pakistan zinda bad!", counter)
    if counter == 5:
        break  

users=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# searc_users= input('Enter use name')

# counter=0
# while counter < len(users):
#     print(users[counter],counter)
#     if searc_users== users[counter]:
#         break
#     counter+=1

# counter = 0
# while counter < len(users):    
#     if searc_users == users[counter]:
#         print(users[counter], counter)
#         break
    
#     counter +=1

code=65
while code<=90:
        print(code,chr(code))
        code+=1

print(chr(122))

# for 
for i in [0,1,2,3,4]:
    print(i)

for i in []:
    print(4)

# for local_variable in iterated_data_type:
#     print(statement)
    
# iterated_data_type = list, tuple, dictionary, sequential type

for c in "Pakistan Zindabad":
    print(c)

sear_u = input('Enter User')
for u in users:
    print(u)
    if u == sear_u:
        break

    names=[]
    while True:
        name = input("Enter name| Enter 'X' for exit")
        if name == "X" or name== "x":
            break
        names.append(name)
        print(names)

names = []

while True:
    name = input("Enter name| enter 'X' for exit")
    if "X" in name or 'x' in name:
        break
    names.append(name)
    
print(names)