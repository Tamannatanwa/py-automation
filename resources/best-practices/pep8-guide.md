# 📏 PEP 8 Style Guide Summary

PEP 8 is the official Python style guide. Following these conventions makes your code more readable and professional.

## Indentation

```python
# ✅ Use 4 spaces per indentation level
def my_function():
    if True:
        print("Properly indented")

# ❌ Don't mix tabs and spaces
```

## Line Length

```python
# ✅ Maximum line length: 79 characters
# ✅ For docstrings/comments: 72 characters

# ❌ Avoid very long lines
result = some_function(argument1, argument2, argument3, argument4, argument5, argument6)

# ✅ Break long lines
result = some_function(
    argument1, argument2,
    argument3, argument4
)
```

## Naming Conventions

```python
# ✅ Variables and functions: lowercase_with_underscores
my_variable = 10
def my_function():
    pass

# ✅ Constants: UPPERCASE_WITH_UNDERSCORES
MAX_SIZE = 100
PI = 3.14159

# ✅ Classes: CapitalizedWords (PascalCase)
class MyClass:
    pass

# ✅ Private: _leading_underscore
_private_variable = 10

# ❌ Don't use single character names (except in loops)
l = 10  # Bad
count = 10  # Good
```

## Imports

```python
# ✅ Imports at top of file
import os
import sys
from typing import List, Dict

# ✅ Group imports
# 1. Standard library
# 2. Third-party
# 3. Local application

# ❌ Don't use wildcard imports
from module import *  # Bad

# ✅ Use specific imports
from module import function1, function2  # Good
```

## Whitespace

```python
# ✅ One space around operators
x = 1 + 2

# ✅ No spaces around = in function arguments
def func(a=1, b=2):
    pass

# ✅ Spaces after commas
my_list = [1, 2, 3, 4]
my_dict = {"a": 1, "b": 2}

# ❌ No trailing whitespace
```

## Comments

```python
# ✅ Use complete sentences
# This function calculates the average of a list of numbers.

# ✅ Inline comments: two spaces before #
x = x + 1  # Increment x

# ✅ Block comments
# This is a longer explanation
# that spans multiple lines
# to explain complex logic
```

## Docstrings

```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        float: The average value
        
    Raises:
        ValueError: If list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```

## Quick Checklist

- [ ] 4 spaces for indentation
- [ ] Lines ≤ 79 characters
- [ ] Proper blank lines
- [ ] Imports organized correctly
- [ ] Descriptive variable names
- [ ] snake_case for functions/variables
- [ ] PascalCase for classes
- [ ] UPPERCASE for constants
- [ ] Proper spacing
- [ ] Meaningful comments
- [ ] Comprehensive docstrings

---

🔗 **Full PEP 8**: https://pep8.org/
