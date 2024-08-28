def outer_func():
    print("This is outer funstion start")

    def inner_func1():
        print("THis is inner func1")
    def inner_func2():
        print("This is innder func2")

    inner_func1()
    inner_func2()
outer_func()
