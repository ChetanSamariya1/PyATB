# Functions Scope

global_b = 12 # This is a global variable which can also print outside or within the function.
# This can be used in multiple functions.

def  my_funciton():
    a = 10 # This is a local variable within the function.
    print(a)
    print(global_b) # This is global variable.

my_funciton()
print(global_b)

def my_function2():
    b = 15
    print(global_b)
    print(b)


my_function2()