# 📚 Common Python Methods Cheatsheet

## String Methods

```python
s = "Hello, World!"

s.lower()           # "hello, world!"
s.upper()           # "HELLO, WORLD!"
s.title()           # "Hello, World!"
s.capitalize()      # "Hello, world!"
s.strip()           # Remove whitespace
s.split(",")        # Split into list
s.replace("H", "J") # Replace characters
s.startswith("He")  # True
s.endswith("!")     # True
s.find("World")     # Index of substring
s.count("o")        # Count occurrences
len(s)              # Length
```

## List Methods

```python
lst = [1, 2, 3, 4, 5]

lst.append(6)       # Add to end
lst.insert(0, 0)    # Insert at index
lst.extend([7, 8])  # Add multiple
lst.remove(3)       # Remove first occurrence
lst.pop()           # Remove and return last
lst.pop(0)          # Remove at index
lst.clear()         # Remove all
lst.index(2)        # Find index
lst.count(2)        # Count occurrences
lst.sort()          # Sort in place
lst.reverse()       # Reverse in place
len(lst)            # Length
```

## Dictionary Methods

```python
d = {"name": "Alice", "age": 30}

d.get("name")            # Get value safely
d.keys()                 # Get all keys
d.values()               # Get all values
d.items()                # Get key-value pairs
d.update({"city": "NY"}) # Update/add items
d.pop("age")             # Remove and return
d.clear()                # Remove all
len(d)                   # Number of items
```

## Set Methods

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.add(4)           # Add element
s1.remove(1)        # Remove (error if not exists)
s1.discard(1)       # Remove (no error)
s1.union(s2)        # {1, 2, 3, 4, 5}
s1.intersection(s2) # {3}
s1.difference(s2)   # {1, 2}
```

## File Methods

```python
# Reading
f = open("file.txt", "r")
f.read()            # Read entire file
f.readline()        # Read one line
f.readlines()       # Read all lines as list
f.close()           # Close file

# Writing
f = open("file.txt", "w")
f.write("text")     # Write string
f.writelines(list)  # Write list of strings
f.close()
```

## Useful Built-in Functions

```python
# Type conversion
int(), float(), str(), bool(), list(), tuple(), set(), dict()

# Math
abs(-5)             # Absolute value
round(3.14159, 2)   # Round to 2 decimals
max([1,2,3])        # Maximum
min([1,2,3])        # Minimum
sum([1,2,3])        # Sum

# Iteration
range(10)           # 0 to 9
enumerate(list)     # Index and value
zip(list1, list2)   # Combine lists

# Others
len(obj)            # Length
type(obj)           # Get type
isinstance(obj, type) # Check type
dir(obj)            # List attributes
help(obj)           # Get help
```

---

🚀 **Bookmark this page for quick reference!**
