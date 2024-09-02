# Create a program, take 2 inputs from the user like num1, num2 and give them
# 1. max number
# 2. power num1 to num2
# 3. Sub, Mul, Sum and Div
# Format the output with String Format f"{}"

num1 = int(input("This is the first number\n"))
num2 = int(input("This is the second number\n"))

# Format the output with String Format f"{}"
# 1. Max number
max_num = max(num1, num2)
print(f"The Max from {num1} & {num2} is {max_num:.2f}")

# 2. power num1 to num2
power_num = pow(num1,num2)
print(f"{num1} raised to the power of {num2} is {power_num:.2f}")

# 3. Sub, Mul, Sum and Div
sum_num = num1 + num2
sub_num = num1 - num2
mul_num = num1 * num2
div_num = num1 / num2

print(f"The Sum of {num1} & {num2} = {sum_num:.2f}")
print(f"The Sub of {num1} & {num2} = {sub_num:.2f}")
print(f"The Mul of {num1} & {num2} = {mul_num:.2f}")
print(f"The Div of {num1} & {num2} = {div_num:.2f}")
