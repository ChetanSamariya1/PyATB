class Parent:
    gold = "2Kg"

    def BHK2(self):
        print("2BHK")


class Child(Parent):
    diamond = "diamond"
    def BHK3(self):
        print("3BHk")


child_obj = Child()
print(child_obj.gold)
child_obj.BHK2()
child_obj.BHK3()
print(child_obj.diamond)

father_obj_ref = Parent()
father_obj_ref.BHK2()
