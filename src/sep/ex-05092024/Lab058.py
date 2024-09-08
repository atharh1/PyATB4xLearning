class Employ:
    id=None
    age=None
    def __init__(self,id,age):
        self.id=input("Enter the id: ")
        self.age=int(input("Enter the age"))

    def display(self):
        print("Employee id is",self.id ,"Employee age is",self.age)

e=Employ(12,12)
e.display()