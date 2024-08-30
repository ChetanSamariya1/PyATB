set1 = {10, 20, 30, 40}
set2 = {40, 50, 60, 60}

my_set = set1.union(set2)
print(sorted(my_set))
my_set2 = set1.intersection(set2)
print(sorted(my_set2))
my_set3 = set1.difference(set2)
print(sorted(my_set3))
my_set4 = set2.difference(set1)
print(my_set4)

set3 = {1,2,3,4,5}
set4 ={4,5,8}

my_set5 = set4.issubset(set3)
print(my_set5)
my_set6 = set3.issubset(set4)
print(my_set6)