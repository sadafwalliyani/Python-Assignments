# Class13 02 Oct 2022
# Inheritance

class Parent():
    def __init__(self):
        self.id =None
        self.name =None
        self.fname =None

    def eat(self, food):
        return f"{self.name} is eating {food}"
    def speak(self,words, language="Urdu"):
        return f"{words}. language={language}"
class Child(Parent):
            pass