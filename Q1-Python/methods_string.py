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

#10 Find
str="Sadaf Walliyani"
    #012345678
print(str.find('Wal'))
print(str.find('S'))
print(str.find('a'))
print(str.find('d'))
print(str.find('l'))
print(str.find("a",4))
print(str.format())

#11 Format_map
records={
    "x": "Sadau",
    "y": "Raju"
}
print("Name: {x}\nFriend: {y}".format_map(records))

#12 Index
print(str.index('d'))

#13 Number in String
str1="sadaf021"
print(str1.isalnum())
print(str.isalnum())

#14 
print("alpha",str1.isalpha())

#15 Scii code
print("Scii",str1.isascii())

#16 Is Number
print(str.isnumeric())
#17 IsDigit
num="2"
print(num.isdigit())

