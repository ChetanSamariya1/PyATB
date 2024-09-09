class Person:
    # class variable
    # Instance Variable

    def __init__(self, name):
        self.name = name

    def walk(self, name):
        print(self.name)


a = Person("Aakash")
b = Person("Bharat")
c = Person(input("Enter the name\n"))
d = Person(input("Enter the name\n"))
e = Person(input("Enter the name\n"))

print(a.name, b.name, c.name, d.name, e.name)
# We can print multiple arguments
