# Calculator

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


a = int(input("Enter the value of a\n"))
b = int(input("Enter the value of b\n"))

object_ref = Calc(a, b)

output_sum = object_ref.sum()
output_sub = object_ref.sub()
output_mul = object_ref.mul()
output_div = object_ref.div()

# print(output_sum , output_sub, output_mul, output_div) - In online output

print(f"Sum of {a} & {b} is", output_sum)
print(f"Sub of {a} & {b} is", output_sub)
print(f"Multi of {a} & {b} is", output_mul)
print(f"Div of {a} & {b} is", output_div)
