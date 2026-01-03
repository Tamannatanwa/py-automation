"""
🎯 Functions - Comprehensive Examples
======================================

Master functions in Python!
Author: Tamanna
"""

print("="*60)
print("FUNCTIONS - EXAMPLES")
print("="*60)
print()

# BASIC FUNCTION
print("1. BASIC FUNCTIONS")
print("-"*40)

def greet():
    """Simple greeting function"""
    print("Hello, World!")

greet()
print()

# FUNCTION WITH PARAMETERS
print("2. FUNCTIONS WITH PARAMETERS")
print("-"*40)

def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

greet_person("Tamanna")
greet_person("Alice")
print()

# FUNCTION WITH RETURN VALUE
print("3. RETURN VALUES")
print("-"*40)

def add_numbers(a, b):
    """Add two numbers and return result"""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
print()

# FUNCTION WITH DEFAULT PARAMETERS
print("4. DEFAULT PARAMETERS")
print("-"*40)

def greet_with_title(name, title="Mr."):
    """Greet with optional title"""
    print(f"Hello, {title} {name}")

greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")
print()

# *ARGS - VARIABLE ARGUMENTS
print("5. *ARGS - VARIABLE ARGUMENTS")
print("-"*40)

def sum_all(*numbers):
    """Sum any number of arguments"""
    total = sum(numbers)
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
print()

# **KWARGS - KEYWORD ARGUMENTS
print("6. **KWARGS - KEYWORD ARGUMENTS")
print("-"*40)

def print_info(**info):
    """Print user information"""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
print()

# LAMBDA FUNCTIONS
print("7. LAMBDA FUNCTIONS")
print("-"*40)

square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add = lambda a, b: a + b
print(f"3 + 4 = {add(3, 4)}")
print()

# REAL-WORLD: CALCULATOR
print("8. REAL-WORLD: CALCULATOR")
print("-"*40)

def calculator(num1, num2, operation):
    """Simple calculator function"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print()

# REAL-WORLD: TEMPERATURE CONVERTER
print("9. REAL-WORLD: TEMPERATURE CONVERTER")
print("-"*40)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.1f}°F")

temp_f2 = 77
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f2}°F = {temp_c2:.1f}°C")
print()

print("="*60)
