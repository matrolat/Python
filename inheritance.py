


class parent:
    def parent_print(self):
        print("parent")

class child(parent):
    def child_print(self):
        print("child")
    

c = child()

c.parent_print()


        