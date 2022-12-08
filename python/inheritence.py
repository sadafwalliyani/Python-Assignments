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


p1 =Parent()
p1.id=1
p1.name="Sadaf"
p1.fname="Mansoor"

print(p1.name)
print(p1.id)
print(p1.fname)
print(p1.eat("Pizza"))
print(p1.speak("Pakistan Zindabad"))


c1 =Child()
c1.id=1
c1.name="Rayyan"
c1.fname="Rustam"

print(c1.name)
print(c1.id)
print(c1.fname)
print(c1.eat("Pizza"))
print(c1.speak("Pakistan Zindabad"))

"""
Inheritance example2
add some new methods in Child class
"""