def outer_function():
    var1 = 30  # local int variable

    def inner_function():
        print(var1)

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()
    print("This is end of inner function")

print("abc")

outer_function()
print("end of outer function")