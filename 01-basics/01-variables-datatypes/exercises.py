"""
📝 Variables and Data Types - Practice Exercises
=================================================

Practice what you've learned about variables and data types!
Try to solve these exercises on your own before checking solutions.

Author: Tamanna
Difficulty: Beginner
Time: 30-45 minutes
"""

print("=" * 60)
print("VARIABLES AND DATA TYPES - PRACTICE EXERCISES")
print("=" * 60)
print()

# ============================================================================
# EXERCISE 1: Basic Variable Assignment
# ============================================================================

print("Exercise 1: Basic Variable Assignment")
print("-" * 40)
print("""
Task: Create variables for a person's information
- Create a variable 'name' with your name
- Create a variable 'age' with your age
- Create a variable 'height' with your height in feet (decimal)
- Create a variable 'is_student' with True or False
- Print all variables with descriptive labels
""")

# YOUR CODE HERE
# name = 
# age = 
# height = 
# is_student = 

print("✅ Your output should show all four variables clearly\n")


# ============================================================================
# EXERCISE 2: Type Identification
# ============================================================================

print("Exercise 2: Type Identification")
print("-" * 40)
print("""
Task: Use the type() function
Given these variables, print their types:
""")

mystery1 = 42
mystery2 = "42"
mystery3 = 42.0
mystery4 = True

print(f"mystery1 = {mystery1}")
print(f"mystery2 = {mystery2}")
print(f"mystery3 = {mystery3}")
print(f"mystery4 = {mystery4}")
print()

# YOUR CODE HERE
# Print the type of each variable
# Example: print(f"Type of mystery1: {type(mystery1)}")

print()


# ============================================================================
# EXERCISE 3: Type Conversion
# ============================================================================

print("Exercise 3: Type Conversion")
print("-" * 40)
print("""
Task: Convert between data types
- Convert the string "123" to an integer
- Convert the integer 456 to a string
- Convert the string "78.9" to a float
- Convert the float 10.5 to an integer
- Print the original and converted values with their types
""")

# YOUR CODE HERE

print()


# ============================================================================
# EXERCISE 4: String Concatenation
# ============================================================================

print("Exercise 4: String Concatenation")
print("-" * 40)
print("""
Task: Create a welcome message
- Create variables: first_name, last_name, age
- Use concatenation or f-strings to create a message:
  "Hello, my name is [first_name] [last_name] and I am [age] years old."
- Print the message
""")

# YOUR CODE HERE

print()


# ============================================================================
# EXERCISE 5: Simple Calculator
# ============================================================================

print("Exercise 5: Simple Calculator")
print("-" * 40)
print("""
Task: Perform calculations with variables
- Create two integer variables: num1 = 10, num2 = 3
- Calculate and print:
  * Sum (addition)
  * Difference (subtraction)
  * Product (multiplication)
  * Quotient (division - should be float)
  * Integer division (floor division)
  * Remainder (modulo)
""")

# YOUR CODE HERE

print()


# ============================================================================
# EXERCISE 6: Temperature Converter
# ============================================================================

print("Exercise 6: Temperature Converter")
print("-" * 40)
print("""
Task: Convert Celsius to Fahrenheit
- Create a variable celsius = 25
- Formula: fahrenheit = (celsius * 9/5) + 32
- Print: "25°C is equal to [result]°F"
- Round the result to 2 decimal places
""")

# YOUR CODE HERE

print()


# ============================================================================
# EXERCISE 7: Shopping Cart Total
# ============================================================================

print("Exercise 7: Shopping Cart Total")
print("-" * 40)
print("""
Task: Calculate shopping cart total with tax
- item1_price = 29.99
- item2_price = 15.50
- item3_price = 8.75
- tax_rate = 0.07 (7%)
- Calculate subtotal (sum of all items)
- Calculate tax amount (subtotal * tax_rate)
- Calculate total (subtotal + tax)
- Print all values formatted to 2 decimal places
""")

# YOUR CODE HERE

print()


# ============================================================================
# EXERCISE 8: Variable Swapping
# ============================================================================

print("Exercise 8: Variable Swapping")
print("-" * 40)
print("""
Task: Swap two variables
- Create x = 5, y = 10
- Print values before swap
- Swap the values (use Python's elegant way)
- Print values after swap
""")

# YOUR CODE HERE

print()


# ============================================================================
# EXERCISE 9: Boolean Logic
# ============================================================================

print("Exercise 9: Boolean Logic")
print("-" * 40)
print("""
Task: Work with boolean values
- Create: age = 20, has_ticket = True, has_id = True
- Create boolean: can_enter = age >= 18 and has_ticket and has_id
- Print whether the person can enter (True/False)
- Try changing values and see how it affects the result
""")

# YOUR CODE HERE

print()


# ============================================================================
# EXERCISE 10: User Profile (Challenge)
# ============================================================================

print("Exercise 10: User Profile - Challenge")
print("-" * 40)
print("""
Task: Create a complete user profile
Create variables for:
- username (string)
- user_id (integer)
- email (string)
- age (integer)
- account_balance (float)
- is_premium (boolean)
- member_since (integer year)

Then calculate:
- years_member (2024 - member_since)
- is_adult (age >= 18)

Print a nicely formatted profile showing all information.
Use f-strings and make it look professional!
""")

# YOUR CODE HERE

print()


# ============================================================================
# EXERCISE 11: Data Type Errors (Debugging Practice)
# ============================================================================

print("Exercise 11: Fix the Errors")
print("-" * 40)
print("""
Task: The following code has errors. Fix them!

# Uncomment and fix these lines:
# age = "25"
# next_year_age = age + 1  # This will cause an error!
# message = "I am " + age + " years old"  # This might also have issues
# print(messag)  # Typo in variable name

Fix the code so it runs without errors.
""")

# YOUR CODE HERE (uncomment and fix)

print()


# ============================================================================
# EXERCISE 12: Real-World Application
# ============================================================================

print("Exercise 12: Real-World Application - Salary Calculator")
print("-" * 40)
print("""
Task: Calculate monthly and yearly salary
Given:
- hourly_rate = 25.50
- hours_per_day = 8
- days_per_week = 5
- weeks_per_year = 52

Calculate:
- daily_salary
- weekly_salary
- monthly_salary (assume 4.33 weeks per month)
- yearly_salary

Print all values formatted as currency ($X,XXX.XX)
""")

# YOUR CODE HERE

print()


# ============================================================================
# BONUS CHALLENGE
# ============================================================================

print("BONUS CHALLENGE: BMI Calculator")
print("-" * 40)
print("""
Task: Calculate Body Mass Index (BMI)
- weight_kg = 70
- height_m = 1.75
- Formula: BMI = weight_kg / (height_m ** 2)
- Calculate and print the BMI
- Also create boolean variables:
  * is_underweight = bmi < 18.5
  * is_normal = 18.5 <= bmi < 25
  * is_overweight = 25 <= bmi < 30
  * is_obese = bmi >= 30
- Print BMI and all boolean results
""")

# YOUR CODE HERE

print()
print("=" * 60)
print("Great job! Check solutions.py to compare your answers.")
print("=" * 60)
