# Take user inputs and calculate the sum, multiply, substraction & division

# Note: Whenever we try to calculate expected output will not come as it refered as String
# So we need to convert inputs into interger first
# Str ->> Int
# a = input("Enter the first number")
# b = input("Enter the second number") These will not work properly due to string data type
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

print("Sum of the number is ", a+b)
print("Sub of the number is ", a-b)
print("Mul of the number is ", a*b)
print("Div of the number is ", a/b) # Python is very smart language so will display decimal number

print(type(a))
print(type(b))
