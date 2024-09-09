# Write a program to find the max between three inputs

# Logic Building

# Step 1:
# User Input ->> Three inputs a, b, c -> Float
# Output: one will be greater

# Step 2: Rough logic
# a & b -> 10 > 8 -> 10 will be greater than 8.

# Step 3: Write the logic
a = input("Enter the first number\n")
a = float(a)
b = input("Enter the second number\n")
b = float(b)
c = input("Enter the third number\n")
c = float(c)

"""
if a > b and b > c:
    print("This is the greater number", a)
elif b > a and a > c:
    print("This is the greater number", b)
else:
    print("This is the greater number", c)
"""
if a > b > c:
    print("This is the greater number", a)
elif b > a > c:
    print("This is the greater number", b)
else:
    print("This is the greater number", c)

    # Second Method

result = max(a, b, c)
print("This is the greater number", result)
