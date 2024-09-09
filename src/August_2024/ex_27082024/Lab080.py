# Decorators in Python

# Concept of Decorators is not in Java.

def my_decorator(func):
    # Two parts
    # Wrapper & Call
    def wrapper():
        print("1. Before function is called")
        print("2. Add Helmet , Knee Guard, Gloves")
        func()
        print("3. After the function is called")
        print("4. Secure Driving")
    return wrapper()

@my_decorator
def drive_bike():
    print("I am driving bike")

@my_decorator
def drive_scooty():
    print("I am driving scooty")