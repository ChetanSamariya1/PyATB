# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine
# if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal). Use an if-else statement to classify the triangle.

side1 = float(input("Enter the first side\n"))
side2 = float(input("Enter the second side\n"))
side3 = float(input("Enter the third side\n"))

if side1 == side2 and side2 == side3:
    print("This is Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is Isosceles Triangle")
else:
    print("This is Scalene Triangle")