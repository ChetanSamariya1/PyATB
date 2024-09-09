squares = [1, 4, 9, 16, 25]
print(squares)
# List in Mutable in nature.
# Mutable - change -> We can change the value at any time.
# List use more memory compare to tuple.
# List can be used for dynamic data.

squares[3] = 20
print(squares)

# Tuple - Collection of items.
# Tuple is immutable in nature.
# Values can not be changed.
# Tuple use less memory compare to list.
# Tuple is little faster compare to list.
# Tuple can be used for static data.
my_tuple = (1, 4, 9, 16, 25)
print(my_tuple)
# my_tuple[3] = 18
# print(my_tuple) # tuple' object does not support item assignment
# Duplication is allowed in tuple.

# Convert tuple into list and same list into tuple
the_list = [10,20,30]
print(the_list)
print(tuple(the_list))

the_tuple = (40,50,60)
print(the_tuple)
print(list(the_tuple))