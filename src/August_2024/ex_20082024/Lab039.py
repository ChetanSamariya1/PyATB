# Write a program to find the max between two inputs

# Logic Building

# Step 1:
# User Input ->> Two inputs a & b -> Float
# Output: one will be greater

# Step 2: Rough logic
# a & b -> 10 > 8 -> 10 will be greater than 8.

# Step 3: Write the logic
a = float(input("Enter the first number\n"))
b = float(input("Enter the second number\n"))

if a > b:
    print("This is the greater number", a)
else:
    print("This is greater number", b)
