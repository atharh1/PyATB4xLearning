class Father:
    fatherhouse = "2bhk"

    def f_display(self):
        print("Father House", self.fatherhouse)


class Son(Father):
    shouse = "3bhk"

    def s_display(self):
        print("Son house", self.shouse)
        print("Father house inherited by son", self.fatherhouse)
        self.f_display()
        print("---------End of SON-------")


class Daugther(Father):
    dhouse = "4bhk"

    def d_display(self):
        print("Daughter house", self.dhouse)
        print("Father house inherited by daughter", self.fatherhouse)
        self.f_display()
        print("---------End of Daughter-----")


s = Son()
s.s_display()
s.f_display()
d = Daugther()
d.d_display()
d.f_display()


class Broker(Son, Daugther):
    def broker_display(self):
        print("--------Broker start----------")
        print("I'm Broker")
        print(" father house borker var",self.fatherhouse)
        self.f_display()
        print("son house ",self.shouse)
        self.s_display()
        print("Daughter house broker var",self.dhouse)
        self.d_display()
        print("----------Borker end----------")

b=Broker()
b.broker_display()
