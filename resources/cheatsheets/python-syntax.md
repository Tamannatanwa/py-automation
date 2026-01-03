# 🐍 Python Syntax Cheatsheet

## Variables and Data Types

```python
# Variables
name = "Alice"
age = 25
height = 5.9
is_student = True

# Type conversion
int("10")    # String to integer
str(42)      # Integer to string
float("3.14") # String to float
```

## Operators

```python
# Arithmetic
+ - * / // % **

# Comparison
== != < > <= >=

# Logical
and or not

# Assignment
= += -= *= /=
```

## Control Flow

```python
# If-else
if condition:
    # code
elif other_condition:
    # code
else:
    # code

# Ternary operator
result = "yes" if condition else "no"
```

## Loops

```python
# For loop
for item in iterable:
    print(item)

# While loop
while condition:
    # code

# Break and continue
for i in range(10):
    if i == 5:
        break
    if i == 3:
        continue
```

## Functions

```python
# Basic function
def greet(name):
    return f"Hello, {name}"

# Default parameters
def greet(name, title="Mr."):
    return f"Hello, {title} {name}"

# Variable arguments
def sum_all(*numbers):
    return sum(numbers)

# Keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
square = lambda x: x ** 2
```

## Data Structures

```python
# List
my_list = [1, 2, 3]
my_list.append(4)
my_list[0]  # Access

# Tuple
my_tuple = (1, 2, 3)

# Set
my_set = {1, 2, 3}
my_set.add(4)

# Dictionary
my_dict = {"name": "Alice", "age": 30}
my_dict["name"]  # Access
```

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
```

## File Operations

```python
# Read
with open("file.txt", "r") as f:
    content = f.read()

# Write
with open("file.txt", "w") as f:
    f.write("Hello, World!")

# Append
with open("file.txt", "a") as f:
    f.write("New line\n")
```

## Exception Handling

```python
try:
    # code that might raise exception
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Always executes")
```

## Common Methods

```python
# String methods
s = "hello"
s.upper()          # "HELLO"
s.capitalize()     # "Hello"
s.replace("h", "j") # "jello"
s.split(",")       # Split into list

# List methods
lst = [1, 2, 3]
lst.append(4)      # Add to end
lst.pop()          # Remove last
lst.extend([5, 6]) # Add multiple
len(lst)           # Length

# Dictionary methods
d = {"a": 1, "b": 2}
d.keys()           # Get keys
d.values()         # Get values
d.items()          # Get key-value pairs
```

---

💡 **Pro Tip**: Practice daily to master Python syntax!
