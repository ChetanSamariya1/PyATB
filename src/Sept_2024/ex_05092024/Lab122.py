# Encapsulation

class Myclass:
    # Public variable
    public_var = "I am Public"
    balance = 0

    # Private variable
    __private_var = "I am private"
    __password = "123456"

    # Protected variable
    _protected_var = "I am protected" # IT can be used in the same package only.


object_ref = Myclass()
print(object_ref.public_var)
print(object_ref.balance)
# print(object_ref.__private_var)  It can not possible.
print(object_ref._protected_var)
