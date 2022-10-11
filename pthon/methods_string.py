#1
name= "sadaf mansoor"
print(name.capitalize())
#2
name2= "Sadaf Mansoor"
print(name2.casefold())
#3
name3= "sadaf mansoor"
print("sadaf mansoor"=="saDaF maNsoor")
# name3.casefold() == "saDaF maNsoor".casefold()
print(name3.casefold() == "saDaF maNsoor".casefold())

#4 Bring Name in center
print(name.center(50))
#5 Count
print(name.count("sadaf"))
print(name.count('a'))

#6 Encode
print(name.encode('utf-8'))

#7 End with
print(name.endswith('oor'))

#8 Startswith
print(name.startswith('s'))

#9 ExandTabs
data="""
name:\tSadaf
FatherName:\tMansoor
Batch:\t35=36
Education:\tMaster
"""
print(data)
print(data.expandtabs(20))

