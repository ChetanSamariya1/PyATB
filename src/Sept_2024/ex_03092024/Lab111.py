# Calculator

class Calc:
    # def __init__(self):
    #     print("Calculator")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Calc()
a = float(input("Enter the value of a\n"))
b = float(input("Enter the value of b\n"))
output_sum = object_ref.sum(a, b)
output_sub = object_ref.sub(a, b)
output_mul = object_ref.mul(a, b)
output_div = object_ref.div(a, b)

# print(output_sum , output_sub, output_mul, output_div) - In online output

print(f"Sum of {a} & {b} is", output_sum)
print(f"Sub of {a} & {b} is", output_sub)
print(f"Multi of {a} & {b} is", output_mul)
print(f"Div of {a} & {b} is", output_div)
