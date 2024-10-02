class Grandparent:
    key_gold = "1 Kg"

    def grandparent_method(self):
        return "Grandparent's Method"


class Parent(Grandparent):
    def parent_method(self):
        return "Parent's Method"


class Child(Parent):
    mac_m3_people = "M3 Max"

    def child_method(self):
        return "Child's Method"


child = Child()
print(child.grandparent_method())
