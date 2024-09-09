# * arguments program
def make_pizza(*toppings):
    for item in toppings:
        print(item, end=" ")


a = make_pizza("Olive")
b = make_pizza("Tomoto", "Onion", "Paneer", "Corn")
