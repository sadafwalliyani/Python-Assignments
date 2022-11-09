"""
OOPS
    object
everything in the world which has name that is called object
    Methods (function, procedure, sub routine)
    performe any action
    must be change some attribute
    or return something
    Attributes (properties, fields, characterstics)
    store some values for perticular time
"""

# Inheritance 
    # Levels of inheritance

"""
# Class
Blue print
    Capitalize each word (ClassName)
    constructor (Method)
    always call when we create new object
    Linear programming

"""

qasim_name = "Muhammad qasim"
qasim_fname= "Muhammad Aslam"
qasim_education = "MSDS"

def qasim_speak():pass
def qasim_eat():pass
def qasim_sleep():pass



asim_name = "Muhammad Asim"
asim_fname= "Muhammad Aslam"
asim_education = "MSDS"

def asim_speak():pass
def asim_eat():pass
def asim_sleep():pass


asif_name = "Muhammad Asif"
asif_fname= "Muhammad Aslam"
asif_education = "MSDS"

def asif_speak():pass
def asif_eat():pass
def asif_sleep():pass

#OOPS
"""
-compress code
-less computing power/ less storage consume
-code management too much simple
"""
#Class
"""
-Blue print/model/structe/template
-Capitalize each word (ClassName) class Class():pass
-constructor (Method)
    -always call when we create new object
    -old programming lanugages
        -same function name as class
Python
    -def __init__(self):
    -first argument:
        >first argument should be any name
        >always keep this during creating time
        >but always ingore during calling
        > always manage each object with individual memory blocks
            -self
            -this
            -abc
            -xyz
> all attribute should be write in constructor body
    -self.attribute_name (within a class)
    -destructor (method)
    -always call when we delete object
> Method
    -def method_name(self,arg1,arg2,..):pass
    -calling time method_name(arg1,arg2)
        -always ignore self
>object action performed
    -always return something or change some attribute value

>Attribute
>class variable
"""

class Student(): # class
    def __init__(self, sid, sname): # constructor method
        #self.attribute_name = constructor_local_variable
        self.id = sid 
        self.name = sname # attribute
        self.education = None # attribute
        self.address = None # attribute
        self.age = None # attribute
        self.user = sname
        self.password = "123"
    
    def login(self,user,pws): # Method
        if self.user == user and self.password == pws:
            return "Valid User"
        else:
            return "Not Valid user"
        
    def display_information(self): # method
        cards = f"""
        PIAIC Student Card
        Registration No: {self.id}
        Name: {self.name}
        Education : {self.education}
        """
        
        return cards

# calling a class
    # ClassName(arg1,arg2,..) 
    # we ignore slef argument calling time

s1 = Student(1,"Muhammad Qasim") # create s1 new object
s2 = Student(2,"Asim")           # create s2 new object
s3 = Student(3,"Asif Khan")      # create s3 new object
s4 = Student(4,"Konain")
s5 = Student(5,"Kamran")

print(s1.name, s1.id) # call attributes values
print(s2.name, s2.id) # object_name.attribute
print(s3.name, s3.id)
print(s5.name, s5.id)