# User Defined Function Types:

# 1. They can't return -> "None" Return
# 2. No Return Type and with Argument
# 3. No Return Type and with Default Argument
# 4. Argument and with Return Type

# 1. They can't return -> "None" Return
# No return type and No parameter/argument
def greet():
    print("Hello World")


result = greet()
print(result)

# 2. No Return Type and with Argument
def greet_by_name(name):
    print("Hello,", name)

greet_by_name("Chetan")

# 3. No Return Type and with Default Argument
def greet_default_arg(name = "Samariya"):
    print("HEllo,", name)

greet_default_arg("Ajay")
greet_default_arg()
greet_default_arg(name="Aakash")

# Multiple Arguments in single function

def multiple_args(name1= "Chetan", name2= "Ajay", name3= "Aakash"):
    print("Multiple Arguments,", name1, name2, name3)

multiple_args()

# 4. Argument and with Return Type

def sum_of_two_numbers(num1, num2):
    return num1+num2

result = sum_of_two_numbers(10,8)

print(result)

# WIth defualt value
def sum_of_two_numbers_defualt_value(num1 = 30, num2 = 49):
    return num1+num2

result = sum_of_two_numbers_defualt_value()

print(result)

# With input type
num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
def sum_of_two_numbers_with_input(num1, num2):
    return num1+num2


result = sum_of_two_numbers_with_input(num1, num2)

print(result)
