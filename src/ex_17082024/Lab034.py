# Ternary Operator
"""
If Condition then do this
Else do that
"""

# If age > 18 then I can give vote
# else I can't give vote

my_age = int(input("Enter your age Here"))
print("You can vote" if my_age >= 18 else "You can't vote. Stay Home") # One liner

# 2nd way
if my_age >= 18:
    print("You can vote")
else:
    print("You can't vote. Stay Home")

# 3rd way
print("You can vote" if int(input("Enter your age Here")) >= 18 else "You can't vote. Stay Home")

