class Calculator:
    def __init__(self):
        print("Calc")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def __mul__(self, a, b):
        return a * b


c = Calculator()
Sum = c.sum(1, 2)
print(Sum)
print(c.sub(2, 1))
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(c.__mul__(a, b))
