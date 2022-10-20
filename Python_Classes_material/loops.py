#!/usr/bin/env python
# coding: utf-8

# In[1]:


len(dir(list))


# In[2]:


len(dir(list))


# In[5]:


#  0 1 2
names = ["A", "B", "C"]
# -3 -2 -1 

print(names[0])

print(names[-2]),


# In[6]:


# 0  1 2 3 4 
names = ["Mubashir", "Asim","rauf" ,"ABC", "def"]
# -5 -4 -3 -2 -1
print(names[-1])
print(names[0])


# In[8]:


list = ["1", "2", "3" ,"5"]
print(list[0])
print(list[-3])


# In[10]:


names = ["py1", "py2", "Py3", "py6"]
print(names[2])
print(names[-2])
print(names[1])


# In[12]:


names =[]
names.append("A")
names.append("B")
names.append("c")
names


# In[15]:


names=[]
names.append("A")
names.append("B")
names.append('C')
names.append(3)
names


# In[18]:


names = ['A', 'B', 'C']
print(names)
names.clear()
print(names)


# In[19]:


names = ["a", "b", "C"]
print(names)
names.clear()
print(names)


# In[20]:


names = ["A", "1" ,"2","F"]
print(names)
names.clear()
print(names)


# In[21]:


names = ["A"]
print(names)
names.copy()
print(names)


# In[23]:


names = ["A"]
print(names)
names.copy()
print(names)


# In[24]:


names = ["A"]
print(names)
names.copy()
print(names)


# In[26]:


names = ['A'] #shallow copy
names1 = names
print("names", names)
print("names", names1)
names[0] ="Pakistan"
print("names", names)
print("names", names1)


# In[28]:


names = ["A", "B", 'C']
names1 = names
print("names", names)
print("names", names1)
names[1] = "Mubashir"
names[-3] = "Samole"
print("names", names)
print("names", names1)


# In[30]:


names = ["A", "B", 'C', "D"]
names1 = names
print("names", names)
print("names", names1)
names[1] = "Mubashir"
names[-4] = "any"
names[-1] = "S"
print("names", names)
print("names" ,names1)


# In[34]:


names = ["A", "B", "C"]
names.copy() #deep copy
print("names",names)
print("names",names1)
names[0] = "Pakistan"
print("names", names)
print("names",names1)


# In[38]:


names = ["A","B","V","C ,"A", "D"]
names.count("A")


# In[39]:


names = ["A","B","C","A","A"]
names.count("A")


# In[40]:


names = ["A", "B", "A", "F"]
names.count("A")


# In[41]:


help(list)


# In[46]:


l1 = [1 ,2 , 3]
l2 = [4,5,5]
print(l1 + l2) #inline operation
print(l1.__add__(l2))

print(l1)
print(l2)


# In[47]:


l1 = [1,2,3]
l2 = [4,5,6]
print(l1 + l2)
print(l1.__add__(l2))
print(l1)
print(l2)


# In[48]:


l1 = [1,2,3]
l2 = [4,5,6]

print(l1)
print(l2)

l1.extend(l2)

print(l1)
print(l2)


# In[49]:


l1 = ["A", "S", 'D', "D"]
print(l1.index("A"))


# In[50]:


l1 = ["A", "A", 'A',"B", 'B']
print(l1.index("A"))
print(l1.index("B"))


# In[58]:


l1 = []
l1.insert(0 , "Mubashir")
l1.insert(0, "A")
l1.insert(0,"H")
print(l1)
l1.insert(1, "farooq")
print(l1)


# In[56]:


l1 =[]
l1.insert(1,"mubashie")
print(l1)


# In[59]:


a = print('Pakistan')
print(a)


# In[60]:


dir(list)


# In[62]:


l1 =["A", "B", "C","D", "P"]

print(l1)

l1.sort(reverse=True)
print(l1)


# In[63]:


l1 = ["A", "B", "C", "P", "L"]
print(l1)
l1.sort(reverse=False)
print(l1)


# In[64]:


l1 =["1", "2", "3", "5"]
print(l1)
l1.pop(3)
print(l1)


# In[65]:


l1 = ["a", "b", "c", "D"]
"D" in l1


# In[68]:


l1 = ("A", "B", "C")
l1[2]


# In[83]:


counter = 1 #counter
while counter <=5: # logic
        print("pakistan",counter)
        counter += 1


# In[73]:



counter = 1 # Counter
while counter <=10: #Logic
    print("pakistan",counter)
    counter +=1 # Increment


# In[74]:


counter = 1
while counter <= 10:
    print("Pakistan",counter)
    counter +=1


# In[82]:


counter = 1
while counter <= 12:
    print("pakistan", counter)
    counter +=1


# In[ ]:


counter = 20
while counter >= 10:
    print("mubashir", counter)
    counter 


# In[ ]:


list(range(1,10))


# In[ ]:


list(range(1,10))


# In[ ]:


for i in range(1,11):
    print("Pk"+str(i))


# In[88]:


list(range(1,11))


# In[89]:


for i in range(1,11):
    print("Pk"+str(i))


# In[93]:


for x in range(1,11):
    print("mub"+str(x))


# In[94]:


for y in range(1,12):
    print("mub"+str(y))


# In[95]:


["pk"+str(i) for i in range(1,11)]


# In[96]:


for n in range(1,11)
print(f'2 X {n} = {n*2}')


# In[97]:


for n in range(1,11):
    #print(2,"X",n,"=",n*2)
    #print("2 X "+str(n)+"="+str(n*2))
    print(f'2 X {n} = {n*2}')


# In[98]:


for n in range(1,11):
    print(2, "X",n, "=", n*2)


# In[99]:


for n in range(1,20):
    print(3 ,"X", n, "=", n*3)


# In[100]:


user_input = int(input("Enter Number"))

for t in range(1, user_input + 1):
    for n in range(1,11):
        print(f'{t} X {n} = {t*n}')


# In[102]:


user_input = int(input("Enter Number"))

for t in range(1, user_input +1):
    for n in range(1,11):
        print(f'{t} X {n} ={t*n}')


# In[103]:


user = int(input("Enter Number"))
for r in range(1,11):
    for t in range(1, user+1):
        print(f'{t}X{r}={r*t}', end='\t')
    print()


# In[108]:


user = int(input("Enter number"))
for n in range(1,11):
    for t in rang(1, user+1):
        print(f'{t}X{r}={r*t}', end'\t')
    print()


# In[109]:


user = int(input("Enter Number"))
for r in range(1,11):
    for t in range(1, user+1):
        print(f'{t}X{r}={r*t}', end='\t')
    print()


# In[110]:


user = int(input("Enter Number"))
for r in range(1,11):
    for t in range(1, user+1)
    print(f'{t}X{r}={r*t}',end=\t')
          print()


# In[ ]:




