# Lambda Expression

# A lambda is an anonymous function that returns some form of data.

add_num = int(input("Enter the number\n"))

# def triple(num):
#     return num * 3
#
#
# output = triple(add_num)
# print(output)

output_2 = lambda num: num * 3
print(output_2(add_num))
