"""
Write to an Existing File
To write to an existing file, you must add a 
parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""


# Open the file "demofile2.txt" and append content to the file:?
f = open("demofile.txt", "a")
f.write("now the file has more content!")
f.close()

#open and read the file after the appending:
f=open("demofile.txt", "r")
print(f.read())

# Create a file called "myfile.txt":
# f = open("myfile.txt", "x")

# Result: a new empty file is created!
# Create a new file if it does not exist:

f=open("myfile.txt", "w")

"""Delete a File
To delete a file, you must import 
the OS module, and run its os.remove() function:"""

# Remove the file "demofile.txt":
# import os
# os.remove("myfile.txt")

# Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

os.rmdir("myfolder")