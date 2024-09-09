# def sum_three_num(a,b,c):
#     return a,b,c

# a = int(input("Enter the first number\n"))
# b = int(input("Enter the second number\n"))
# c = int(input("Enter the third number\n"))
#
# sum_of_three = lambda a, b, c: a + b + c
#
# print(sum_of_three(a, b, c))

input_number = int(input("Enter the number\n"))
# def find_odd_even(num):
#     if num%2 ==0:
#         print("even")
#     else:
#         print("odd")
# find_odd_even(input_number)

check_number = lambda num: "Even" if num%2==0 else "Odd"
print(check_number(input_number))