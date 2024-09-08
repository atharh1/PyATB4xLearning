a=10
class Test():
    b=11
    def display(self):
        c=20
        print(a)
        print(self.b)
        print(c)
t=Test()
t.display()
print(a)
print(t.b)
