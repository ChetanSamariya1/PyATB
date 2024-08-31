# OOPs Concepts

class person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    def talk(self):  # self - this, self will be first argument in every behaviour
        # No Return No Argument
        print("I can talk")

    def sleep(self, name):  # Arg with No return
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with return
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):
        return "I am walking"  # No Arg with Return


# Create an Object of the class
# ObjectRef = ClassName() -> Object

Aakash = person()
Aakash.name = "Aakash"
print(Aakash.name)
Aakash.talk()

Rahul = person()
Rahul.name = "Rahul"
print(Rahul.name)
