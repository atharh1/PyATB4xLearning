class Bank:
    bank_name = "icci"
    _id = 123
    __pass = 1234

    def bank_details(self):
        print(self.bank_name)
        print(self._id)
        print(self.__pass)


b = Bank()
b.bank_details()
print(b.bank_name)

class Branch(Bank):
    def branch_details(self):
        print(self.bank_name)
        print(self.bank_details())

b1=Branch()
print("--------")
b1.branch_details()
print("--------")
b1.bank_details()
