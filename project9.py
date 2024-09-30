# Empty dictionary
my_dict = {}

# Dictionary with integer keys
my_dict = {1: 'Apple', 2: 'Banana'}

# Dictionary with mixed keys
my_dict = {'name': 'Ayesha', 1: [2, 4, 3]}
# Accessing element using key
print(my_dict['name'])  # Output: Ayesha
# Adding new key-value pair
my_dict['age'] = 23

# Modifying existing value
my_dict['name'] = 'Sara'
# Using pop() method to remove an item
my_dict.pop('age')  # Removes key 'age'

# Using del keyword to remove an item
del my_dict['name']

# Removing all elements from the dictionary
my_dict.clear()
# Simple dictionary with string keys and integer values
person = {
    "name": "Ayesha",
    "age": 23,
    "profession": "Intern"
}
# Accessing the value using the key
print(person["name"])  # Output: Ayesha
print(person["age"])   # Output: 23
print(person.get("hobby"))  # Output: None (no error)
# Adding a new key-value pair
person["city"] = "Islamabad"
print(person)  # Now the dictionary has a new key "city"

# Modifying an existing key's value
person["age"] = 24
print(person["age"])  # Output: 24
# Modifying an existing key's value
person["age"] = 24
print(person["age"])  # Output: 24
# Remove and return the value associated with the key
person.pop("city")  # Removes 'city' from the dictionary

# Remove an item using del
del person["profession"]  # Removes 'profession' from the dictionary

# Clear the entire dictionary
person.clear()  # The dictionary is now empty
# Create a new dictionary
my_dict = {"name": "Ayesha", "age": 23, "profession": "Intern"}

# Get all keys
print(my_dict.keys())   # Output: dict_keys(['name', 'age', 'profession'])

# Get all values
print(my_dict.values())  # Output: dict_values(['Ayesha', 23, 'Intern'])
# Loop through keys
for key in person:
    print(key)  # Prints each key

# Loop through values
for value in person.values():
    print(value)  # Prints each value

# Loop through both keys and values
for key, value in person.items():
    print(key, ":", value)
# A dictionary with nested dictionaries
students = {
    "student1": {"name": "Ayesha", "age": 23},
    "student2": {"name": "Sara", "age": 24}
}

# Accessing elements in nested dictionaries
print(students["student1"]["name"])  # Output: Ayesha
# Creating a dictionary
student = {
    "name": "Ayesha",
    "age": 23,
    "university": "Air University"
}

# Accessing values using keys
print(student["name"])      # Output: Ayesha
print(student["age"])       # Output: 23

# Using .get() method to access a key safely
print(student.get("city"))  # Output: None (because "city" doesn't exist)
# Adding a new key-value pair
student["major"] = "Mathematics"
print(student)

# Output: {'name': 'Ayesha', 'age': 23, 'university': 'Air University', 'major': 'Mathematics'}

# Modifying an existing value
student["age"] = 24
print(student["age"])  # Output: 24
# Removing an item using pop()
age = student.pop("age")
print(age)  # Output: 24 (returns the value that was removed)
print(student)  # Output: {'name': 'Ayesha', 'university': 'Air University', 'major': 'Mathematics'}

# Using del to remove an item by key
del student["university"]
print(student)  # Output: {'name': 'Ayesha', 'major': 'Mathematics'}
# Looping through keys
for key in student:
    print(key)  # Output: name, major

# Looping through values
for value in student.values():
    print(value)  # Output: Ayesha, Mathematics

# Looping through both keys and values
for key, value in student.items():
    print(f"{key}: {value}")
    # Output:
    # name: Ayesha
    # major: Mathematics
# Get all keys
print(student.keys())  # Output: dict_keys(['name', 'major'])

# Get all values
print(student.values())  # Output: dict_values(['Ayesha', 'Mathematics'])

# Get all key-value pairs
print(student.items())
# Output: dict_items([('name', 'Ayesha'), ('major', 'Mathematics')])

# Checking if a key exists in the dictionary
if "name" in student:
    print("Key 'name' exists")  # Output: Key 'name' exists
# Two dictionaries
student_info = {"name": "Ayesha", "age": 23}
grades = {"math": 95, "science": 90}

# Using update() to merge them
student_info.update(grades)
print(student_info)
# Output: {'name': 'Ayesha', 'age': 23, 'math': 95, 'science': 90}

# Using | operator (Python 3.9+)
combined = student_info | grades
print(combined)
# Output: {'name': 'Ayesha', 'age': 23, 'math': 95, 'science': 90}
# Nested dictionary
company = {
    "employee1": {"name": "Ayesha", "position": "Analyst"},
    "employee2": {"name": "Sara", "position": "Manager"}
}

# Accessing elements in a nested dictionary
print(company["employee1"]["name"])  # Output: Ayesha
print(company["employee2"]["position"])  # Output: Manager

# Adding a new nested dictionary
company["employee3"] = {"name": "Ali", "position": "Engineer"}
print(company)
# Output:
# {'employee1': {'name': 'Ayesha', 'position': 'Analyst'},
# 'employee2': {'name': 'Sara', 'position': 'Manager'},
# 'employee3': {'name': 'Ali', 'position': 'Engineer'}}

