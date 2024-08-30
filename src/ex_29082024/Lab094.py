# List

# List is collection of items. Duplication is allowed in the list.
# There is no arrays in Python.

my_list = [1, 2, 3]  # Same type of data. Here are int
# my_list_2 = [1, "Chetan", 3.14, True] # Different data types are allowed together in the list.

print(my_list)
print(len(my_list))  # Length always start from 1.

print(my_list[0])  # Index always start from 0.
print(my_list[1])
print(my_list[2])
# print(my_list[12]) # list index out of range - exception

my_list[0] = "Chetan"
my_list[2] = 3.14123
my_list[1] = True

print("Value of index 0 ->", my_list[0])
print("Value of index 1 ->", my_list[1])
print("Value of index 2 ->", my_list[2])
print(my_list)

# With for loop
for element in my_list:
    print(element)

# Append
my_list = [1, 2, 3]
my_list.append(4) # Append object to the end of the list.
my_list.append(5) # Append object to the end of the list.
print(my_list)

# Append with For loop

value_to_add = [6,7,8,9]

for element in value_to_add:
    my_list.append(element)
print(my_list)

# Extend function
my_list.extend([10,11,12,True, "Chetan"])
print(my_list)
print(len(my_list))

# Insert function

my_list.insert(1, "Aakash")
print(my_list)
print(len(my_list))
my_list.insert(-2, "Ajay") # In Python minus indexing start from right to left.
print(my_list)
print(len(my_list))

# Remove()
my_list.remove("Ajay")
print(len(my_list))

# Copy list

my_copy_list = my_list.copy()
print(my_list, my_copy_list)

# Clear()
my_list.clear()
print(my_list, my_copy_list)

# Sorting
my_list_num = [30,40,10,20]
print(my_list_num)
my_list_num.sort()
print(my_list_num)
my_list_num.sort(reverse=True)
print(my_list_num)


my_list_name = ["Chetan", "Ajay", "Sanjay", "Aakash"]
print(my_list_name)
my_list_name.sort()
print(my_list_name)

# reverse()
my_list_name.reverse()
print(my_list_name)
my_list_num.reverse()
print(my_list_num)
