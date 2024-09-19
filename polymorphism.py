

class parent:
    def display(self):
        print("parent")

class child(parent):
    def display(self):
        print("child")
        

a = parent()
a.display()

b = child()
b.display()
