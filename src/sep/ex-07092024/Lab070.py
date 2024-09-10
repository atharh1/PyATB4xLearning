class A:
    @staticmethod
    def test():
        print("test")
        #A.test(

print("After class A")
A.test()


class B:
    def test1(self):
        print("---Start of Method--")
        print("test1")
        A.test()
        print("---End of Method--")
print("After class B")
A.test()

A.test()
b = B()
b.test1()
print("--After method called--")
A.test()
