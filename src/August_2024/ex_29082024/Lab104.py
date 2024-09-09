# Dict
# Key and Value Pair
# Name : Chetan
# Name is Key and Chetan is value
# A dictionary is an unordered collection of data.

student = {
    "name": "Chetan",
    "age": 30,
    "address": "Gujarat"

}
print(student)
print(student["name"])
print(student["age"])
print(student["address"])

student2 = {
    "name": "Chetan",
    "age": 30,
    #  "age": 34, # Key should be unique. Python will take the latest value.
    "address": "Gujarat"

}
print(student2)

# We can change the value in dict
student2["name"] = "Rahul"
print(student2)

# Second method
student3 = dict(name="Amit", age="40", address="Bihar")
print(student3)

# Dictionary in dictionary

student_info = {
    "name": "Chetan",
    "age": 30,
    "address": {
        "Home_Address": "Ahmedabad",
        "Office_Address": "Remote"
    }

}

print(student_info)

student4 = {
    "name": "Chetan",
    "age": 30,
    "address": {
        "Home_Address": "Ahmedabad",
        "Office_Address": "Remote"
    }

}
student5 = {
    "name": "Aakash",
    "age": 20,
    "address": {
        "Home_Address": "Baroda",
        "Office_Address": "Jaipur"
    }

}

student_list = [student4, student5]
print(student_list)
