# Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

# Input from the user
num = int(input("Enter the number\n"))

# Initialize the factorial variable
factorial = 1

# Loop to calculate the factorial
for i in range(1, num + 1):
    factorial *= i

# Output the result
print(f"The factorial of {num} is {factorial}.")