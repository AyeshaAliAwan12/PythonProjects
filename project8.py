#example of how to create, manipulate, and work with list.
my_list = [1, 2, 3, 4, 5]
print(my_list)
mixed_list = [1, "apple", 3.14, True]
print(mixed_list)
my_list.append(9)#You can add elements to a list using append():
print(my_list)
print(my_list[0])  # First element
print(my_list[-1])  # Last element
print(my_list[1:3])  # Elements from index 1 to 2
my_list.insert(2, "new_item")
print(my_list)
my_list.remove(2)  # Removes first occurrence of 2
print(my_list)
my_list.pop(4)  # Removes the item at index 3
print(my_list)
squared_numbers = [x**2 for x in range(6)]
print(squared_numbers)
if "apple" in mixed_list:
    print("Apple is in the list!")
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)
