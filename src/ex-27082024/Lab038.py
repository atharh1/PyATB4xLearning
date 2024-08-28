def make_pizza(*topping):
    for toppin in topping:
        print(toppin)

print("started")
cus1=make_pizza("olive")
cus2=make_pizza("olive","salt")
cus3=make_pizza(1,2,3)
print("end")