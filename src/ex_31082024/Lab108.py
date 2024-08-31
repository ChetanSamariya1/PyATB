class Dog: # class name will always start from the Capital letter
    name = None
    breed = None
    color = None

    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("Bark")
    def eat(self,food):
        print(food)


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)

dog2 = Dog()
dog2.name = "Huskey"
print(dog2.name)

dog3 = dog1
print(dog3.name)
