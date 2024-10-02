# Inheritance

class Father:
    key = "2BHK"

    def car(self):
        print("Father Caer!! Alto", self.key)


class Son(Father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def truck(self):
        print("Truck")


father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.car()
