"""
📚 Variables and Data Types - Examples
======================================

This file contains comprehensive examples of variables and data types in Python.
Each example is well-commented and includes real-world use cases.

Author: Tamanna
Purpose: Learn Python basics through practical examples
"""

# ============================================================================
# 1. INTEGER (int) - Whole Numbers
# ============================================================================

print("=" * 60)
print("1. INTEGER EXAMPLES")
print("=" * 60)

# Basic integer assignment
age = 25
print(f"Age: {age}")
print(f"Type: {type(age)}\n")

# Negative integers
temperature = -5
print(f"Temperature: {temperature}°C")
print(f"Type: {type(temperature)}\n")

# Large integers (Python handles big numbers automatically)
world_population = 7900000000
print(f"World Population: {world_population:,}")
print(f"Type: {type(world_population)}\n")

# Real-life example: Calculating total items in inventory
apples = 50
oranges = 30
total_fruits = apples + oranges
print(f"🍎 Real-life Example: Inventory Management")
print(f"Apples: {apples}, Oranges: {oranges}")
print(f"Total Fruits: {total_fruits}\n")


# ============================================================================
# 2. FLOAT (float) - Decimal Numbers
# ============================================================================

print("=" * 60)
print("2. FLOAT EXAMPLES")
print("=" * 60)

# Basic float assignment
height = 5.9
print(f"Height: {height} feet")
print(f"Type: {type(height)}\n")

# Pi value
pi = 3.14159
print(f"Value of Pi: {pi}")
print(f"Type: {type(pi)}\n")

# Scientific notation
distance_to_sun = 1.496e8  # 149.6 million km
print(f"Distance to Sun: {distance_to_sun:,} km")
print(f"Type: {type(distance_to_sun)}\n")

# Real-life example: Calculating bill with tax
bill_amount = 100.50
tax_rate = 0.08  # 8% tax
total_bill = bill_amount * (1 + tax_rate)
print(f"💰 Real-life Example: Restaurant Bill")
print(f"Bill Amount: ${bill_amount}")
print(f"Tax Rate: {tax_rate * 100}%")
print(f"Total Bill: ${total_bill:.2f}\n")


# ============================================================================
# 3. STRING (str) - Text Data
# ============================================================================

print("=" * 60)
print("3. STRING EXAMPLES")
print("=" * 60)

# Basic string assignment
name = "Tamanna"
print(f"Name: {name}")
print(f"Type: {type(name)}\n")

# Single vs double quotes (both work the same)
message1 = "Hello, World!"
message2 = 'Hello, World!'
print(f"Message 1: {message1}")
print(f"Message 2: {message2}\n")

# Multi-line strings using triple quotes
address = """123 Main Street
Apt 4B
New York, NY 10001"""
print(f"Address:\n{address}\n")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}\n")

# String formatting (f-strings - modern Python way)
age = 30
greeting = f"My name is {name} and I am {age} years old"
print(f"Greeting: {greeting}\n")

# Real-life example: Creating email addresses
username = "john.doe"
domain = "company.com"
email = f"{username}@{domain}"
print(f"📧 Real-life Example: Email Generation")
print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Email: {email}\n")


# ============================================================================
# 4. BOOLEAN (bool) - True/False Values
# ============================================================================

print("=" * 60)
print("4. BOOLEAN EXAMPLES")
print("=" * 60)

# Basic boolean assignment
is_student = True
has_license = False
print(f"Is Student: {is_student}")
print(f"Has License: {has_license}")
print(f"Type: {type(is_student)}\n")

# Comparison operations return booleans
age = 18
is_adult = age >= 18
print(f"Age: {age}")
print(f"Is Adult: {is_adult}\n")

# Real-life example: Login validation
username_correct = True
password_correct = True
is_logged_in = username_correct and password_correct
print(f"🔐 Real-life Example: Login System")
print(f"Username Correct: {username_correct}")
print(f"Password Correct: {password_correct}")
print(f"Is Logged In: {is_logged_in}\n")


# ============================================================================
# 5. TYPE CONVERSION (Type Casting)
# ============================================================================

print("=" * 60)
print("5. TYPE CONVERSION EXAMPLES")
print("=" * 60)

# String to Integer
age_str = "25"
age_int = int(age_str)
print(f"String to Integer:")
print(f"  Original: '{age_str}' (type: {type(age_str)})")
print(f"  Converted: {age_int} (type: {type(age_int)})\n")

# Integer to String
score = 95
score_str = str(score)
message = "Your score is: " + score_str
print(f"Integer to String:")
print(f"  Original: {score} (type: {type(score)})")
print(f"  Converted: '{score_str}' (type: {type(score_str)})")
print(f"  Message: {message}\n")

# String to Float
price_str = "19.99"
price_float = float(price_str)
print(f"String to Float:")
print(f"  Original: '{price_str}' (type: {type(price_str)})")
print(f"  Converted: {price_float} (type: {type(price_float)})\n")

# Float to Integer (truncates decimal part)
pi = 3.14159
pi_int = int(pi)
print(f"Float to Integer:")
print(f"  Original: {pi} (type: {type(pi)})")
print(f"  Converted: {pi_int} (type: {type(pi_int)})")
print(f"  Note: Decimal part is removed, not rounded!\n")

# Integer/Float to Boolean
number1 = 0
number2 = 42
bool1 = bool(number1)
bool2 = bool(number2)
print(f"Number to Boolean:")
print(f"  {number1} -> {bool1} (0 is False)")
print(f"  {number2} -> {bool2} (Non-zero is True)\n")

# Real-life example: User input conversion
print(f"💡 Real-life Example: Processing User Input")
user_input = "100"  # Simulating input from user
quantity = int(user_input)  # Convert to integer for calculation
price_per_item = 5.99
total_cost = quantity * price_per_item
print(f"User Input: '{user_input}' (string)")
print(f"Quantity: {quantity} (integer)")
print(f"Price per Item: ${price_per_item}")
print(f"Total Cost: ${total_cost:.2f}\n")


# ============================================================================
# 6. VARIABLE NAMING CONVENTIONS
# ============================================================================

print("=" * 60)
print("6. VARIABLE NAMING BEST PRACTICES")
print("=" * 60)

# Good variable names (descriptive and follow conventions)
student_name = "Alice"          # lowercase with underscores (snake_case)
total_price = 99.99             # descriptive
is_valid = True                 # boolean starts with 'is_' or 'has_'
MAX_ATTEMPTS = 3                # constants in UPPERCASE
user_age_in_years = 25          # very descriptive

# Print the good examples
print("✅ Good Variable Names:")
print(f"  student_name = '{student_name}'")
print(f"  total_price = {total_price}")
print(f"  is_valid = {is_valid}")
print(f"  MAX_ATTEMPTS = {MAX_ATTEMPTS}")
print(f"  user_age_in_years = {user_age_in_years}\n")

# Bad variable names (avoid these!)
print("❌ Bad Variable Names to Avoid:")
print("  x = 'Alice'              # Not descriptive")
print("  p = 99.99                # Single letter, unclear")
print("  StudentName = 'Bob'      # Should be snake_case, not PascalCase")
print("  total-price = 50         # Hyphens not allowed (causes error)")
print("  2nd_value = 10           # Can't start with number\n")


# ============================================================================
# 7. MULTIPLE ASSIGNMENT
# ============================================================================

print("=" * 60)
print("7. MULTIPLE ASSIGNMENT EXAMPLES")
print("=" * 60)

# Assign same value to multiple variables
x = y = z = 0
print(f"Same value to multiple variables:")
print(f"  x = {x}, y = {y}, z = {z}\n")

# Assign different values to multiple variables in one line
name, age, city = "Alice", 28, "New York"
print(f"Different values in one line:")
print(f"  name = '{name}'")
print(f"  age = {age}")
print(f"  city = '{city}'\n")

# Swapping variables (Python way - elegant!)
a = 5
b = 10
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a  # Swap values
print(f"After swap: a = {a}, b = {b}\n")


# ============================================================================
# 8. CHECKING TYPES WITH type() FUNCTION
# ============================================================================

print("=" * 60)
print("8. CHECKING DATA TYPES")
print("=" * 60)

# Using type() function to check data types
sample_int = 42
sample_float = 3.14
sample_string = "Hello"
sample_bool = True

print(f"Value: {sample_int}, Type: {type(sample_int)}")
print(f"Value: {sample_float}, Type: {type(sample_float)}")
print(f"Value: '{sample_string}', Type: {type(sample_string)}")
print(f"Value: {sample_bool}, Type: {type(sample_bool)}\n")


# ============================================================================
# 9. REAL-WORLD EXAMPLE: User Profile
# ============================================================================

print("=" * 60)
print("9. COMPLETE REAL-WORLD EXAMPLE: User Profile")
print("=" * 60)

# Creating a user profile with different data types
user_id = 12345                           # int
username = "tech_enthusiast"              # str
email = "user@example.com"                # str
age = 28                                  # int
account_balance = 1250.75                 # float
is_premium_member = True                  # bool
signup_year = 2020                        # int
years_active = 2024 - signup_year         # calculated int

# Display user profile
print(f"👤 User Profile:")
print(f"{'='*40}")
print(f"User ID        : {user_id}")
print(f"Username       : {username}")
print(f"Email          : {email}")
print(f"Age            : {age} years")
print(f"Balance        : ${account_balance:.2f}")
print(f"Premium Member : {is_premium_member}")
print(f"Years Active   : {years_active} years")
print(f"{'='*40}\n")

# Use case: Eligibility check
min_age_for_premium = 18
can_upgrade = age >= min_age_for_premium and account_balance > 0
print(f"🎯 Eligibility Check:")
print(f"Can upgrade to premium: {can_upgrade}")
print(f"Reason: Age >= {min_age_for_premium} and Balance > $0\n")


# ============================================================================
# 10. COMMON MISTAKES AND HOW TO AVOID THEM
# ============================================================================

print("=" * 60)
print("10. COMMON MISTAKES TO AVOID")
print("=" * 60)

print("""
❌ Mistake 1: Trying to concatenate string and number
   Wrong: "Age: " + 25
   Right: "Age: " + str(25) or f"Age: {25}"

❌ Mistake 2: Using reserved keywords as variable names
   Wrong: class = "Python" (class is a keyword)
   Right: class_name = "Python"

❌ Mistake 3: Forgetting data type conversion
   Wrong: age = "25"; age + 5 (will cause error)
   Right: age = int("25"); age + 5

❌ Mistake 4: Using spaces in variable names
   Wrong: user name = "Alice" (causes syntax error)
   Right: user_name = "Alice"

✅ Always use descriptive variable names
✅ Follow Python naming conventions (snake_case)
✅ Convert data types when necessary
✅ Use type() to check data types when debugging
""")

print("=" * 60)
print("✨ End of Variables and Data Types Examples")
print("=" * 60)
