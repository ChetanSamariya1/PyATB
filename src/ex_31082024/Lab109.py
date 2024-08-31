# Constructor
# Special Function in Class, __init__()
# It will be automatically called when you create an Object

class Dog():
    name = None
    age = None

    def __init__(self, name, age):
        # This is Constructor function. It does not return anything
        print("DC | I will be automatically called when you create an Object")
        print("Called, Object is created")
        self.name = name
        self.age = age

    def sleep(self): # This is the normal function.
        print("Sleeping")


dog1 = Dog("Chow", 10)
print(dog1.name)

dog2 = Dog("Huskey", 8)
print(dog2.name)
