# A program with sorting and user input list

# Predefined list of names
my_list_input = ["ashok", "vinod", "mahesh", "anjali"]

# Capitalize each value in the list
capitalized_list = [name.capitalize() for name in my_list_input]

# Loop to get 3 names from the user
for _ in range(3):
    # Prompt the user to enter a name
    name = input("Enter a name:\n")
    # Capitalize the entered name
    capitalized_name = name.capitalize()
    # Append the entered name to the list
    capitalized_list.append(capitalized_name)

# Sort the list in alphabetical order
capitalized_list.sort()

# Print the sorted list
print("Sorted List:", capitalized_list)

# Print the length of the list
print("Length of List:", len(capitalized_list))
