# Multilevel Interference

class GrandFather:
    gold = "2Kg"

    def BHk1(self):
        print("1BHK")

class Father(GrandFather):
    diamond = "22 karat"

    def BHK2(self):
        print("2BHK")


class Son(Father):
    btc = "1 BTC"

    def BHK3(self):
        print("3BHK")

son_obj = Son()

print(son_obj.gold, son_obj.diamond, son_obj.btc)

son_obj.BHk1()
son_obj.BHK2()
son_obj.BHK3()

father_obj = Father()
father_obj.BHK2()
father_obj.BHk1()
print(father_obj.gold, father_obj.diamond)