"""
✅ Variables and Data Types - Exercise Solutions
=================================================

Compare your solutions with these answers.
Remember: There might be multiple ways to solve these problems!

Author: Tamanna
"""

print("=" * 60)
print("VARIABLES AND DATA TYPES - SOLUTIONS")
print("=" * 60)
print()

# ============================================================================
# SOLUTION 1: Basic Variable Assignment
# ============================================================================

print("Solution 1: Basic Variable Assignment")
print("-" * 40)

name = "Tamanna"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is Student: {is_student}")
print()


# ============================================================================
# SOLUTION 2: Type Identification
# ============================================================================

print("Solution 2: Type Identification")
print("-" * 40)

mystery1 = 42
mystery2 = "42"
mystery3 = 42.0
mystery4 = True

print(f"mystery1 = {mystery1}, Type: {type(mystery1)}")
print(f"mystery2 = {mystery2}, Type: {type(mystery2)}")
print(f"mystery3 = {mystery3}, Type: {type(mystery3)}")
print(f"mystery4 = {mystery4}, Type: {type(mystery4)}")
print()


# ============================================================================
# SOLUTION 3: Type Conversion
# ============================================================================

print("Solution 3: Type Conversion")
print("-" * 40)

# String to integer
str_num = "123"
int_num = int(str_num)
print(f"String '{str_num}' (type: {type(str_num)}) -> Integer {int_num} (type: {type(int_num)})")

# Integer to string
int_val = 456
str_val = str(int_val)
print(f"Integer {int_val} (type: {type(int_val)}) -> String '{str_val}' (type: {type(str_val)})")

# String to float
str_float = "78.9"
float_val = float(str_float)
print(f"String '{str_float}' (type: {type(str_float)}) -> Float {float_val} (type: {type(float_val)})")

# Float to integer
float_num = 10.5
int_from_float = int(float_num)
print(f"Float {float_num} (type: {type(float_num)}) -> Integer {int_from_float} (type: {type(int_from_float)})")
print()


# ============================================================================
# SOLUTION 4: String Concatenation
# ============================================================================

print("Solution 4: String Concatenation")
print("-" * 40)

first_name = "John"
last_name = "Doe"
age = 30

# Method 1: Using f-string (recommended)
message = f"Hello, my name is {first_name} {last_name} and I am {age} years old."
print(message)

# Method 2: Using concatenation
message2 = "Hello, my name is " + first_name + " " + last_name + " and I am " + str(age) + " years old."
print(message2)
print()


# ============================================================================
# SOLUTION 5: Simple Calculator
# ============================================================================

print("Solution 5: Simple Calculator")
print("-" * 40)

num1 = 10
num2 = 3

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
integer_division = num1 // num2
remainder = num1 % num2

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Difference: {num1} - {num2} = {difference}")
print(f"Product: {num1} * {num2} = {product}")
print(f"Quotient: {num1} / {num2} = {quotient:.2f}")
print(f"Integer Division: {num1} // {num2} = {integer_division}")
print(f"Remainder: {num1} % {num2} = {remainder}")
print()


# ============================================================================
# SOLUTION 6: Temperature Converter
# ============================================================================

print("Solution 6: Temperature Converter")
print("-" * 40)

celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
print()


# ============================================================================
# SOLUTION 7: Shopping Cart Total
# ============================================================================

print("Solution 7: Shopping Cart Total")
print("-" * 40)

item1_price = 29.99
item2_price = 15.50
item3_price = 8.75
tax_rate = 0.07  # 7%

subtotal = item1_price + item2_price + item3_price
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

print(f"Item 1: ${item1_price:.2f}")
print(f"Item 2: ${item2_price:.2f}")
print(f"Item 3: ${item3_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")
print()


# ============================================================================
# SOLUTION 8: Variable Swapping
# ============================================================================

print("Solution 8: Variable Swapping")
print("-" * 40)

x = 5
y = 10

print(f"Before swap: x = {x}, y = {y}")

# Python's elegant way to swap
x, y = y, x

print(f"After swap: x = {x}, y = {y}")
print()


# ============================================================================
# SOLUTION 9: Boolean Logic
# ============================================================================

print("Solution 9: Boolean Logic")
print("-" * 40)

age = 20
has_ticket = True
has_id = True

can_enter = age >= 18 and has_ticket and has_id

print(f"Age: {age}")
print(f"Has Ticket: {has_ticket}")
print(f"Has ID: {has_id}")
print(f"Can Enter: {can_enter}")

# Test with different values
print("\nTest with different values:")
age2 = 16
can_enter2 = age2 >= 18 and has_ticket and has_id
print(f"Age: {age2}, Can Enter: {can_enter2}")
print()


# ============================================================================
# SOLUTION 10: User Profile (Challenge)
# ============================================================================

print("Solution 10: User Profile - Challenge")
print("-" * 40)

username = "techguru123"
user_id = 54321
email = "techguru@example.com"
age = 28
account_balance = 1500.75
is_premium = True
member_since = 2020

# Calculations
years_member = 2024 - member_since
is_adult = age >= 18

# Display profile
print("=" * 50)
print("           USER PROFILE")
print("=" * 50)
print(f"Username       : {username}")
print(f"User ID        : {user_id}")
print(f"Email          : {email}")
print(f"Age            : {age} years")
print(f"Adult Status   : {'Yes' if is_adult else 'No'}")
print(f"Account Balance: ${account_balance:.2f}")
print(f"Premium Member : {'Yes' if is_premium else 'No'}")
print(f"Member Since   : {member_since} ({years_member} years)")
print("=" * 50)
print()


# ============================================================================
# SOLUTION 11: Data Type Errors (Debugging Practice)
# ============================================================================

print("Solution 11: Fix the Errors")
print("-" * 40)

# Fixed code:
age = "25"
next_year_age = int(age) + 1  # Convert age to integer first
message = f"I am {age} years old"  # Use f-string or convert age to string
print(message)  # Fixed typo
print(f"Next year I'll be {next_year_age}")
print()


# ============================================================================
# SOLUTION 12: Real-World Application
# ============================================================================

print("Solution 12: Real-World Application - Salary Calculator")
print("-" * 40)

hourly_rate = 25.50
hours_per_day = 8
days_per_week = 5
weeks_per_year = 52

daily_salary = hourly_rate * hours_per_day
weekly_salary = daily_salary * days_per_week
monthly_salary = weekly_salary * 4.33  # Average weeks per month
yearly_salary = weekly_salary * weeks_per_year

print(f"Hourly Rate    : ${hourly_rate:.2f}")
print(f"Daily Salary   : ${daily_salary:.2f}")
print(f"Weekly Salary  : ${weekly_salary:.2f}")
print(f"Monthly Salary : ${monthly_salary:,.2f}")
print(f"Yearly Salary  : ${yearly_salary:,.2f}")
print()


# ============================================================================
# BONUS CHALLENGE SOLUTION
# ============================================================================

print("BONUS CHALLENGE: BMI Calculator")
print("-" * 40)

weight_kg = 70
height_m = 1.75

bmi = weight_kg / (height_m ** 2)

# BMI categories
is_underweight = bmi < 18.5
is_normal = 18.5 <= bmi < 25
is_overweight = 25 <= bmi < 30
is_obese = bmi >= 30

print(f"Weight: {weight_kg} kg")
print(f"Height: {height_m} m")
print(f"BMI: {bmi:.2f}")
print()
print("BMI Categories:")
print(f"  Underweight (< 18.5)  : {is_underweight}")
print(f"  Normal (18.5 - 24.9)  : {is_normal}")
print(f"  Overweight (25 - 29.9): {is_overweight}")
print(f"  Obese (>= 30)         : {is_obese}")
print()

# Determine category
if is_underweight:
    category = "Underweight"
elif is_normal:
    category = "Normal"
elif is_overweight:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI category: {category}")
print()

print("=" * 60)
print("🎉 Congratulations on completing the exercises!")
print("Keep practicing to master variables and data types!")
print("=" * 60)
