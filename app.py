# user_input = float(input("Enter you weight: "))
# weight_unit = input("Enter k for kilograms and l for lbs: ").lower()
# result = ""
# if weight_unit == 'k':
#     result = str(user_input * 2.20462) + " lbs"
# elif weight_unit == 'l':
#     result = str(user_input * 0.453592) + " kgs"
# else:
#     result = "wrong unit entered"
# print("Your weight is: " + result)

# i = 1
# while i <= 5:
#     print(i * "*")
#     i += 1

# names = ["noman", "daniyal", "awais", "erza"]
# names[1] = "danial"
# print(names[0:4])

# numbers = [1,2,3,4,5]
# for i in numbers:
#     print(i)

### String Formatting ###
# Using format() method:
name = "Danial"
age = 28
formatted_string = "my name is {} and i am {} years old".format(name, age)
# print(formatted_string)

# Using f-strings (Python 3.6+):
formatted_string = f"My name is {name} and i am {age} years old"
# print(formatted_string)

### String Methods ###
str1 = "    hello world !    "
# print(str1.find("world"))

# strip(), lstrip(), and rstrip():
print(str1.strip())
## split and join

### LISTS ###
# Slicing
numbers = [1,2,3,4,5,6]
print(numbers[1:4])  # Output: [2, 3, 4]
print(numbers[:3])   # Output: [1, 2, 3]
print(numbers[3:])   # Output: [4, 5]

# Removing Elements:
numbers = [1, 2, 3, 4]
numbers.remove(3)       # Removes the first occurrence of an element
del numbers[1]          # Removes an element by index
print(numbers)  # Output: [1, 4]

# extend():
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)  # Output: [1, 2, 3, 4, 5]

# insert():
numbers = [1, 2, 3]
numbers.insert(1, 10)
print(numbers)  # Output: [1, 10, 2, 3]

# pop():
numbers = [1, 2, 3]
removed_element = numbers.pop()
print(removed_element)  # Output: 3
print(numbers)  # Output: [1, 2]

# count()
numbers = [1, 2, 2, 3]
count_of_two = numbers.count(2)
print(count_of_two)  # Output: 2

# sort() and reverse():
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]

numbers.reverse()
print(numbers)  # Output: [3, 2, 1]


## DICT ###
person = {
    "name": "Bob",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science"]
}
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30
print(person.get("city", "not found")) # Using get() Method (Avoids KeyError if Key Doesn’t Exist):

# Modifying Dictionaries
# Adding or Updating Key-Value Pairs:
person["email"] = "alice@example.com"  # Adding a new key-value pair
person["age"] = 31                    # Updating an existing value
print(person)

#Removing Key-Value Pairs:
# del person["city"]
print(person)  # 'city' key is removed

age = person.pop("age")
print(age)     # Output: 31
print(person)  # 'age' key is removed

# Using popitem() Method (removes the last inserted key-value pair):
last_item = person.popitem()
print(last_item)  # Output: ('email', 'alice@example.com')

# DIC methods
# keys() and values():
keys = person.keys()
values = person.values()
print(keys)    # Output: dict_keys(['name', 'age', 'city'])
print(values)  # Output: dict_values(['Alice', 30, 'New York'])

# items() (Returns a list of key-value pairs):
items = person.items()
print(items)   # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# update() (Merges another dictionary into the current one):
person.update({"city": "Boston", "phone": "123-456-7890"})
print(person)  # The dictionary is updated with new/modified key-value pairs

# clear() (Removes all elements):
# person.clear()
print(person)  # Output: {}


for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
