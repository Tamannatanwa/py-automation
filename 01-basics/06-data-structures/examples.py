"""
📊 Data Structures - Comprehensive Examples
============================================

Master lists, tuples, sets, and dictionaries!
Author: Tamanna
"""

print("="*60)
print("DATA STRUCTURES - EXAMPLES")
print("="*60)
print()

# LISTS
print("1. LISTS - Ordered, Mutable")
print("-"*40)

fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")

# Adding elements
fruits.append("orange")
print(f"After append: {fruits}")

# Removing elements
fruits.remove("banana")
print(f"After remove: {fruits}")

# List slicing
numbers = [0, 1, 2, 3, 4, 5]
print(f"\nNumbers: {numbers}")
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print()

# TUPLES
print("2. TUPLES - Ordered, Immutable")
print("-"*40)

coordinates = (10, 20)
print(f"Coordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked - X: {x}, Y: {y}")
print()

# SETS
print("3. SETS - Unordered, Unique Elements")
print("-"*40)

unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print(f"Set (duplicates removed): {unique_numbers}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print()

# DICTIONARIES
print("4. DICTIONARIES - Key-Value Pairs")
print("-"*40)

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding/updating
person["email"] = "alice@example.com"
print(f"After adding email: {person}")

# Looping through dictionary
print("\nAll key-value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")
print()

# LIST COMPREHENSIONS
print("5. LIST COMPREHENSIONS")
print("-"*40)

# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension
squares = [i ** 2 for i in range(5)]
print(f"Squares (comprehension): {squares}")

# With condition
evens = [i for i in range(10) if i % 2 == 0]
print(f"Even numbers: {evens}")
print()

# NESTED STRUCTURES
print("6. NESTED STRUCTURES")
print("-"*40)

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 20, "grade": "A"}
]

print("Students:")
for student in students:
    print(f"  {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
print()

# REAL-WORLD: SHOPPING CART
print("7. REAL-WORLD: SHOPPING CART")
print("-"*40)

cart = {
    "items": [
        {"name": "Laptop", "price": 999.99, "quantity": 1},
        {"name": "Mouse", "price": 29.99, "quantity": 2},
        {"name": "Keyboard", "price": 79.99, "quantity": 1}
    ]
}

print("Shopping Cart:")
total = 0
for item in cart["items"]:
    subtotal = item["price"] * item["quantity"]
    total += subtotal
    print(f"  {item['name']} x{item['quantity']}: ${subtotal:.2f}")
print(f"Total: ${total:.2f}")
print()

print("="*60)
