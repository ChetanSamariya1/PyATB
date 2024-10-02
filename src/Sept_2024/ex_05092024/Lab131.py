# Hierarchical Inheritance

class Father:
    def BHK1(self):
        print("1 BHK")


class Son1(Father):
    def BHK2(self):
        print("2 BHK")


class Son2(Father):
    def BHK3(self):
        print("3 BHK")


class Son3(Father):
    def no_house(self):
        print("No House")


son1 = Son1()
son1.BHK1()
son1.BHK2()

son2 = Son2()
son2.BHK1()
son2.BHK3()

son3 = Son3()
son3.BHK1()
son3.no_house()
