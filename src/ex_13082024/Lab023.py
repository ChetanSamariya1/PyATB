# Formatting concepts of string
numbers = 3.14159265359
# f is used for formatting
formatted_number = f"{numbers:.4f}"
print(formatted_number)

# Format string
num = 90

print("This is the number you are working with "f"{num}")

# Table
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 10 = 20

table = 2
print(f"{table}*1 = {table*1}")
print(f"{table}*2 = {table*2}")
print(f"{table}*3 = {table*3}")