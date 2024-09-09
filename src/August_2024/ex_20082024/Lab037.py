# Conditions & Loops

# Write a program to take a user age and let him know if he can go the club.

# Logic Building

# Step 1: User Input -> Data Type -> Int
# Output -> String -> User if he can go or not.

# Step 2: Rough Logic

# age >= 21 -> You can go to Club.
# age < 21 -> You can't go with this age.

# Step 3: Write the logic

age = input("Enter your age here\n")
age = int(age)

# if else condition here
if age >= 21:
    print(f"You can go to Club.\t{age}")
else:
    print(f"You can't go with this age.\t{age}")
