class Calc:
    def __init__(self):
        self.a = int(input("Enter number: "))
        self.b = int(input("Enter number: "))

    def sum(self):
        return self.a + self.b
    def mult(self):
        return self.a * self.b


c = Calc()
print("Sum is ",c.sum())
print("Mul is ",c.mult())
