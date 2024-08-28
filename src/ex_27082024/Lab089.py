import math

#
# def give_power(num):
#     return math.pow(num,2)
# op = give_power(10)
# print(op)


op = lambda : math.pow(int(input("Enter the number\n")), 2)
print(op())