def print_arguments(*args):
# *args = Multiple argument with no limit -> List or Tuple
   #  print(args[0]) - It will return first value

   # For multiple value
   for i in args:
       print(i, end=" ")


print_arguments("Chetan", "Ajay", "Aakash")
print_arguments("Ajay", "Aakash")
print_arguments("Aakash")
print_arguments("Chetan", 123, True)
# Minimum 1 argument is required
