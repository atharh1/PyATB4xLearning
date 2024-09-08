class Employee:
    name=None
    age=None
    id=None
    dob=None
    def __init__(self,name,age,id,dob):
        self.name=name
        self.age=age
        self.id=id
        self.dob=dob

    def display(self):
        print("Name of employee: ",self.name )
        print("Age of employee: ", self.age)
        print("id of employee: ", self.id)
        print("dob of employee: ", self.dob)

e=Employee("athar",20,123,88)
e.display()