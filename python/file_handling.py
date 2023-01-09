"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""

"""
Syntax
To open a file for reading it is 
enough to specify the name of the file:"""

f=  open("demofile.txt")
f = open("demofile.txt", "rt")

f= open("demofile.txt")
print(f.read())
print(f.read(5))

# Open a file on a different location:

f=open("D:\Python-Assignments\info.csv","r")
print(f.read())

# Return the 5 first characters of the file:
print(f.read(3))

# Read one line of the file:
f= open("demofile.txt", "r")
print(f.readline())

# Read two lines of the file:
print(f.readline())
print(f.readline())
print(f.readline())

# Loop through the file line by line:
f= open("demofile.txt","r")
for x in f:
    print(x)

"""Close Files
It is a good practice to always 
close the file when you are done with it."""

print(f.readline())
f.close()


