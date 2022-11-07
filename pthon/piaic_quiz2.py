class Parent:
    def _init_(self):
        self.x=1
    def change(self):
        self.x=10
class Child(Parent):
    def change(self):
        self.x=self.x+1
        return self.x
def main():
    obj =Child()
    print(obj.change())

main()
            