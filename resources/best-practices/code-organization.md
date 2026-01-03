# 🗂️ Code Organization Tips

## Project Structure

```
project_name/
├── README.md
├── requirements.txt
├── setup.py
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── modules/
│       ├── __init__.py
│       └── module1.py
├── tests/
│   ├── __init__.py
│   └── test_module1.py
└── docs/
    └── documentation.md
```

## File Organization

```python
# 1. Docstring
"""
Module description here.
"""

# 2. Imports (grouped and sorted)
import os
import sys

import requests
import pandas as pd

from .local_module import function

# 3. Constants
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30

# 4. Classes and Functions
class MyClass:
    pass

def my_function():
    pass

# 5. Main execution
if __name__ == "__main__":
    main()
```

## Function Organization

```python
# ✅ Group related functions together
# ✅ Put helper functions after main functions
# ✅ Use clear function names

def process_data(data):
    """Main processing function."""
    cleaned_data = _clean_data(data)
    validated_data = _validate_data(cleaned_data)
    return validated_data

def _clean_data(data):
    """Helper: Clean the data."""
    # Implementation
    pass

def _validate_data(data):
    """Helper: Validate the data."""
    # Implementation
    pass
```

## Documentation

```python
def calculate_discount(price, discount_percent, is_member=False):
    """
    Calculate final price after discount.
    
    This function applies a discount to a price and adds an
    additional member discount if applicable.
    
    Args:
        price (float): Original price
        discount_percent (float): Discount percentage (0-100)
        is_member (bool): Whether customer is a member
        
    Returns:
        float: Final price after discounts
        
    Raises:
        ValueError: If price is negative or discount > 100
        
    Examples:
        >>> calculate_discount(100, 10)
        90.0
        >>> calculate_discount(100, 10, is_member=True)
        85.5
    """
    if price < 0:
        raise ValueError("Price cannot be negative")
    if discount_percent > 100:
        raise ValueError("Discount cannot exceed 100%")
    
    discounted = price * (1 - discount_percent/100)
    if is_member:
        discounted *= 0.95  # Additional 5% member discount
    return discounted
```

---

✨ **Remember**: Well-organized code is easier to understand, maintain, and debug!
