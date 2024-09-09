class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + str(self.model))


lambo = Car("lambo", "V22", 2024)
lambo.start_engine()

xuv = Car("XUV", "V6", 2023)
xuv.start_engine()
