"""
🔢 Operators in Python - Comprehensive Examples
================================================

Learn all types of operators with practical examples.

Author: Tamanna
"""

print("="*60)
print("PYTHON OPERATORS - EXAMPLES")
print("="*60)
print()

# ============================================================================
# 1. ARITHMETIC OPERATORS
# ============================================================================

print("1. ARITHMETIC OPERATORS")
print("-"*40)

a = 10
b = 3

print(f"a = {a}, b = {b}\n")

# Addition
print(f"Addition: {a} + {b} = {a + b}")

# Subtraction
print(f"Subtraction: {a} - {b} = {a - b}")

# Multiplication
print(f"Multiplication: {a} * {b} = {a * b}")

# Division (always returns float)
print(f"Division: {a} / {b} = {a / b:.2f}")

# Floor Division (integer division)
print(f"Floor Division: {a} // {b} = {a // b}")

# Modulus (remainder)
print(f"Modulus: {a} % {b} = {a % b}")

# Exponentiation (power)
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Real-world example: Calculate discount
print(f"\n💰 Real-world: Shopping Discount")
original_price = 100
discount_percent = 20
discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount
print(f"Original: ${original_price}, Discount: {discount_percent}%")
print(f"You save: ${discount_amount}, Pay: ${final_price}")
print()

# ============================================================================
# 2. COMPARISON OPERATORS
# ============================================================================

print("2. COMPARISON OPERATORS")
print("-"*40)

x = 10
y = 20

print(f"x = {x}, y = {y}\n")

# Equal to
print(f"Equal: {x} == {y} is {x == y}")

# Not equal
print(f"Not Equal: {x} != {y} is {x != y}")

# Greater than
print(f"Greater than: {x} > {y} is {x > y}")

# Less than
print(f"Less than: {x} < {y} is {x < y}")

# Greater than or equal
print(f"Greater or equal: {x} >= {y} is {x >= y}")

# Less than or equal
print(f"Less or equal: {x} <= {y} is {x <= y}")

# Real-world example: Age verification
print(f"\n🔞 Real-world: Age Verification")
age = 18
min_age = 18
can_vote = age >= min_age
print(f"Age: {age}, Minimum: {min_age}")
print(f"Can vote: {can_vote}")
print()

# ============================================================================
# 3. LOGICAL OPERATORS
# ============================================================================

print("3. LOGICAL OPERATORS")
print("-"*40)

# AND operator
print("AND operator (both must be True):")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and False = {False and False}")
print()

# OR operator
print("OR operator (at least one must be True):")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")
print()

# NOT operator
print("NOT operator (inverts boolean):")
print(f"not True = {not True}")
print(f"not False = {not False}")
print()

# Real-world example: Login validation
print(f"🔐 Real-world: Login System")
username_correct = True
password_correct = True
is_logged_in = username_correct and password_correct
print(f"Username OK: {username_correct}, Password OK: {password_correct}")
print(f"Login successful: {is_logged_in}")
print()

# ============================================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================================

print("4. ASSIGNMENT OPERATORS")
print("-"*40)

# Basic assignment
num = 10
print(f"num = {num}")

# Add and assign
num += 5  # same as: num = num + 5
print(f"After num += 5: {num}")

# Subtract and assign
num -= 3  # same as: num = num - 3
print(f"After num -= 3: {num}")

# Multiply and assign
num *= 2  # same as: num = num * 2
print(f"After num *= 2: {num}")

# Divide and assign
num /= 4  # same as: num = num / 4
print(f"After num /= 4: {num}")

# Real-world: Bank account
print(f"\n💳 Real-world: Bank Account")
balance = 1000
print(f"Initial balance: ${balance}")
balance += 500  # deposit
print(f"After deposit of $500: ${balance}")
balance -= 200  # withdrawal
print(f"After withdrawal of $200: ${balance}")
print()

# ============================================================================
# 5. MEMBERSHIP OPERATORS
# ============================================================================

print("5. MEMBERSHIP OPERATORS")
print("-"*40)

fruits = ["apple", "banana", "cherry"]
print(f"Fruits list: {fruits}\n")

# in operator
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")

# not in operator
print(f"'mango' not in fruits: {'mango' not in fruits}")

# Real-world: Checking permissions
print(f"\n🔑 Real-world: Permission Check")
user_roles = ["admin", "editor"]
has_admin = "admin" in user_roles
print(f"User roles: {user_roles}")
print(f"Has admin access: {has_admin}")
print()

# ============================================================================
# 6. IDENTITY OPERATORS
# ============================================================================

print("6. IDENTITY OPERATORS")
print("-"*40)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a\n")

# is operator (checks if same object)
print(f"a is b: {a is b} (different objects)")
print(f"a is c: {a is c} (same object)")

# is not operator
print(f"a is not b: {a is not b}")

print("\nNote: == checks value, is checks identity")
print(f"a == b: {a == b} (same values)")
print()

# ============================================================================
# 7. OPERATOR PRECEDENCE
# ============================================================================

print("7. OPERATOR PRECEDENCE")
print("-"*40)

# Precedence order (high to low):
# 1. ** (exponentiation)
# 2. *, /, //, % (multiplication, division)
# 3. +, - (addition, subtraction)
# 4. Comparisons
# 5. Logical operators

result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print(f"10 + 5 * 2 = {result1} (multiplication first)")
print(f"(10 + 5) * 2 = {result2} (parentheses first)")

# Real-world: Complex calculation
print(f"\n🧮 Real-world: Compound Interest")
principal = 1000
rate = 0.05  # 5%
time = 2
amount = principal * (1 + rate) ** time
interest = amount - principal
print(f"Principal: ${principal}")
print(f"Rate: {rate*100}% per year")
print(f"Time: {time} years")
print(f"Final amount: ${amount:.2f}")
print(f"Interest earned: ${interest:.2f}")
print()

print("="*60)
print("✨ End of Operators Examples")
print("="*60)
