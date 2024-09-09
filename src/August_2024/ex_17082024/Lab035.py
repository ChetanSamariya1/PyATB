"""
Write a Python program to calculate the
area of a circle given its radius using the formula
area = πr2  ( π = 3.14 )
user input is r
"""
import math

# Logic Building Formula

# Step 1: Figure Out the inputs and output
# input -> r -> data type -> float
# pi = 3.14, math.pi
# power -> pow or ** -> Any of can be used
# Output -> Float, print area

# Step 2:
# Rough Logic -> area = 3.14 * powe(r,2)

# Step 3:
# Write the logic
radius = float(input("Enter the radius of circle\n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius, 2)
print("This is the area of circle", area)
print(f"This is the area of circle {area:.2f}")