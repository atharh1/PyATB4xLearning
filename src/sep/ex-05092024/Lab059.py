class Person:
    name=None
    age=None
    def __init__(self):
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
    def display(self):
        print("Perons name is:",self.name,"Persone age is:",self.age)

    def worker(self):
        print("I'm worker ", self.name)
    def father(self):
        print("Im father",self.name)
p=Person()
p.display()
p.worker()
p.father()