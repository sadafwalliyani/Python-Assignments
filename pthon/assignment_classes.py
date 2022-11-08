# Task1
# 1. import mother and father attribute

# class Father():
#     def __init__(self, name, age,):
#         self.name=name
#         self.age=age
#         self.color="light brown"
#     def display(self):
#        return f" My Name is {self.name}, I am {self.age} years old"
#     def showAge(self):
#         return self.age *365
# f1= Father




# class Mother():
#     def __init__(self):
#         self.cook = "Food"
#         self.haircolor="black"
#     def showCook(this):
#         return f"I can cook {this.cook}"

#     def showHaircolor(this):
#         return f"My hair Colors are {this.haircolor}"
# m1 = Mother

# class Child(Father, Mother):
#    def __init__(self, name, age, color):
#        super().__init__(name, age, color)
#        self.grade=1
#        self.school="Aga Khan"

# def childclass(this):
#         return f"My Name is {this.name} I am {this.age} years old. I study in class {this.grade}."

# c = Child




class Father():
    def __init__(self,name):
        self.name = name
        self.fname = None
        self.color = 'whitish'
        self.hair_color = 'dark brown'
        
    def speak(self):
        return "Hahahah!"
    
    
class Mother():
    def __init__(self):
        self.height = '5.8 feet'
        self.color = 'white'
        
    def slient(self):
        return "..."
    
class Child(Father,Mother):
    pass

print()