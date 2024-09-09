my_shopping_list = ["Milk", "Butter", "Bread"]

more_item = input("Enter the new item\n")
print(my_shopping_list[0])
print(len(my_shopping_list))


def bring_food(my_shopping_list):
    my_shopping_list.append("Cheese")  # Add value in the list. Only one can at a time
    my_shopping_list.append("Toast")
    my_shopping_list.append(more_item)  # Add value from the input
    my_shopping_list.insert(2, more_item)  # Add value at certain position
    # my_shopping_list.remove("Butter") # To remove value from the list
    return my_shopping_list


more_food = bring_food(my_shopping_list)
print(more_food)
