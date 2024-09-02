# Write a Python program to calculate the area of a circle
# given its radius using the formula  area=π×r^2 ( Take pie as 3.14)

# input will be r
r = float(input("Enter the value of radius of a circle\n"))

area = 3.14 * r * r

print("Area of a circle:", area)
print(f"Aread of circle for given {r} is, {area:.2f}")
