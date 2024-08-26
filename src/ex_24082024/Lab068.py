# Create a program to sum of three numbers from user input

num1 = int(input("Enter the 1st number\n"))
num2 = int(input("Enter the 2nd number\n"))
num3 = int(input("Enter the 3rd number\n"))


def sum_of_numbers(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_numbers(num1, num2, num3)
# result = sum_of_numbers(n1=num1, n2=num2, n3=num3)
print(f"Sum of {num1},{num2} & {num3} is", result)
