# Take input and create a class in Python.

class Person:
    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.mobile = input("Enter the Mobile number\n")
        self.occupation = input("Enter the occupation\n")

    def information(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Mobile Number is {self.mobile}")
        print(f"Occupation is {self.occupation}")


# Create an Object

person1 = Person()

# Call the function

person1.information()
