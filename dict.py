book = {
    "title": "Lord of the ring",
    "author": "Daniyal",
    "year_published": "2020",
    "genre": "adventure"
}

book.update({"isbn": "1234"})
book.update({"year_published": "2022"})
del book["genre"]
print(book)

for key, value in book.items():
    print(f"{key}: {value}")
print(book.keys())
print(book.values())

def add(*args):
    return sum(args)

result = add(1, 2, 3, 4)
print(result)  # Output: 10

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York

# Modifying Global Variables: To modify a global variable inside a function, use the global keyword.
x = 10

def my_function():
    global x
    x = 20

my_function()
print(x)  # Output: 20

