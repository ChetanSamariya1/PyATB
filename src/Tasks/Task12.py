"""
1) Write a Python program to find the largest number in a list.
2) Write a Python program to find the smallest number in a list.
3) Write a Python program to sum all numbers in a list.
4) Write a Python program to multiply all numbers in a list.
5) Write a Python program to count the number of strings in a list where the string length is 2 or more
and the first and last characters are the same.
6) Write a Python program that takes two lists and returns True if they have at least one common member.
7) Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
8) Write a Python program to get the Fibonacci series between 0- 50.
9) Write a Python program to find the factorial of a number.
10) Write a Python program to check if a number is a prime number.
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1) Write a Python program to find the largest number in a list.
max_num = max(my_list)
print("This is the largest number:", max_num)

# ------------------------------------------------------------------------------------------------------

# 2) Write a Python program to find the smallest number in a list.
small_num = min(my_list)
print("This is the smallest number:", small_num)


# ------------------------------------------------------------------------------------------------------

# 3) Write a Python program to sum all numbers in a list.
def sum_of_numbers(my_list):
    total = 0
    for num in my_list:
        total += num
    return total


total_sum = sum_of_numbers(my_list)
print(f"The sum of all numbers in the list is: {total_sum}")


# ------------------------------------------------------------------------------------------------------

# 4) Write a Python program to multiply all numbers in a list.

def multi_of_number(my_list):
    total = 1
    for num in my_list:
        total *= num
    return total


total_multi = multi_of_number(my_list)
print(f"The multiplication of all number in the list is: {total_multi}")

# ------------------------------------------------------------------------------------------------------

# 5) Write a Python program to count the number of strings in a list where the string length is 2 or more
# and the first and last characters are the same.
my_list2 = ["XYZX"]

