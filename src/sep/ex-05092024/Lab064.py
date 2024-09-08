class Father:
    fbike = "Bullet"
    house = "2bhk"

    def father_display(self):
        print("Father bike", self.fbike)


class Mother:
    mbike = "Activa"

    def mother_display(self):
        print("Mother Bike", self.mbike)


class Son(Father, Mother):
    bike = "Jupiter"

    def son_display(self):
        print("Son bike", self.bike)
        print("Father Inherited bike", self.father_display())
        print("Mothers Inhertied bike", self.mother_display())
        print("Father's house", self.house)
        print("Father bikes var", Father.fbike)
        print("MOther bike var", Mother.mbike)


s = Son()
s.son_display()
