# Mach Statement

# It is Switch in Java
# Both are same
# Match the o/p and execute
# It will work only for Python > 3.10

"""
match variable:
    case pattern 1:
        Code Block
    case pattern 2:
        Code Block
"""

# Write a program to ask the user which browser he wants to run automation

browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.capitalize()

match browser_name:
    case "Firefox":
        print("Execute the Firefox Code")
    case "Chrome":
        print("Execute the Chrome Code")
    case "Edge":
        print("Execute the Edge Code")
    case "Safari":
        print("Execute the Safari Code")
    case _:
        print("Browser Not Found!")