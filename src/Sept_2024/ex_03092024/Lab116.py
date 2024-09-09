a = 10


class Person:
    b = 11

    def print_info(self):
        print(a)
        print(self.b)


# object_ref = Person()
# object_ref.print_info()

Person().print_info()
