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
# list comprehension 
squared_numbers = [x**2 for x in range(6)]
print(squared_numbers)
cubed_Numbers=[6*x**3+2*x for x in range(8)]
print(cubed_Numbers)
numbers_varaible=[2*x**3 for x in range(67)]
print(numbers_varaible)
##example of how to create, manipulate, and work with list.
project_list=['Operation Quack Build',
'Brickzilla',
'Mortar Kombat',
'Concrete Jungle Boogie',
'The Mighty Duck Build',
'Hard Hat Hilarity',
'Blockbuster Building',
'Trowel and Error',
'The Unlevelers',
'Pylon Pals',
'Mix-Up Mayhem']
print(project_list)
if "Hard Hat Hilarity" in project_list:
    print("Hard Hat Hilarity project is in the list")
project_list.sort() #for sorting list
print(project_list)
project_list.pop(-1) #remove the item at the last index
print(project_list)
project_list.remove("Blockbuster Building")#remove the occurrence
print(project_list)
project_list.insert(0,"Ash")
print(project_list)
project_list.sort() #for sorting list
print(project_list)
