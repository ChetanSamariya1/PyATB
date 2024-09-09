def make_pizza(*toppings, base):  # Here 2 * are not allowed.
    print(toppings, base)


make_pizza("Cheese", "Tomoto", "Paneer", base="Thin Crust")
# Here for base, multiple arguments are not allowed.


