"""
🔀 Control Flow - Comprehensive Examples
=========================================

Learn if-else statements and conditional logic.

Author: Tamanna
"""

print("="*60)
print("CONTROL FLOW - EXAMPLES")
print("="*60)
print()

# ============================================================================
# 1. BASIC IF STATEMENT
# ============================================================================

print("1. BASIC IF STATEMENT")
print("-"*40)

age = 18
if age >= 18:
    print(f"Age {age}: You are an adult!")

# Real-world: Temperature check
temperature = 25
if temperature > 30:
    print("It's hot outside!")
if temperature <= 30:
    print(f"Temperature is {temperature}°C - Pleasant weather!")
print()

# ============================================================================
# 2. IF-ELSE STATEMENT
# ============================================================================

print("2. IF-ELSE STATEMENT")
print("-"*40)

score = 75
if score >= 60:
    print(f"Score: {score} - PASS ✓")
else:
    print(f"Score: {score} - FAIL ✗")

# Real-world: Login check
password = "correct123"
if password == "correct123":
    print("🔐 Login successful!")
else:
    print("❌ Incorrect password")
print()

# ============================================================================
# 3. IF-ELIF-ELSE STATEMENT
# ============================================================================

print("3. IF-ELIF-ELSE STATEMENT")
print("-"*40)

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Marks: {marks}, Grade: {grade}")

# Real-world: Shipping cost calculator
weight = 5  # kg
if weight <= 1:
    shipping = 5
elif weight <= 5:
    shipping = 10
elif weight <= 10:
    shipping = 15
else:
    shipping = 20
print(f"📦 Weight: {weight}kg, Shipping: ${shipping}")
print()

# ============================================================================
# 4. NESTED IF STATEMENTS
# ============================================================================

print("4. NESTED IF STATEMENTS")
print("-"*40)

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("✓ You can drive!")
    else:
        print("✗ You need a license")
else:
    print("✗ Too young to drive")

# Real-world: Loan eligibility
income = 50000
credit_score = 750
if income >= 30000:
    if credit_score >= 700:
        print("✓ Loan approved!")
    else:
        print("✗ Credit score too low")
else:
    print("✗ Income too low")
print()

# ============================================================================
# 5. LOGICAL OPERATORS IN CONDITIONS
# ============================================================================

print("5. LOGICAL OPERATORS IN CONDITIONS")
print("-"*40)

# AND operator
username = "admin"
password = "pass123"
if username == "admin" and password == "pass123":
    print("✓ Login successful (AND)")

# OR operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print(f"✓ {day} is a weekend!")

# NOT operator
is_raining = False
if not is_raining:
    print("✓ No rain - Good day for a picnic!")
print()

# ============================================================================
# 6. TERNARY OPERATOR (ONE-LINE IF-ELSE)
# ============================================================================

print("6. TERNARY OPERATOR")
print("-"*40)

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

# More examples
num = 15
result = "Even" if num % 2 == 0 else "Odd"
print(f"Number {num} is {result}")

score = 75
message = "Pass" if score >= 60 else "Fail"
print(f"Score {score}: {message}")
print()

# ============================================================================
# 7. REAL-WORLD EXAMPLE: E-COMMERCE DISCOUNT
# ============================================================================

print("7. REAL-WORLD: E-COMMERCE DISCOUNT CALCULATOR")
print("-"*40)

cart_total = 150
is_member = True
coupon_code = "SAVE20"

discount = 0

# Member discount
if is_member:
    discount += 10  # 10% member discount
    print("✓ Member discount: 10%")

# Bulk purchase discount
if cart_total > 100:
    discount += 5  # Additional 5%
    print("✓ Bulk purchase bonus: 5%")

# Coupon code
if coupon_code == "SAVE20":
    discount += 20  # 20% coupon
    print("✓ Coupon applied: 20%")

# Calculate final price
discount_amount = cart_total * (discount / 100)
final_price = cart_total - discount_amount

print(f"\nCart Total: ${cart_total}")
print(f"Total Discount: {discount}%")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")
print()

# ============================================================================
# 8. REAL-WORLD EXAMPLE: BMI CALCULATOR
# ============================================================================

print("8. REAL-WORLD: BMI CALCULATOR WITH CATEGORIES")
print("-"*40)

weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)

print(f"Weight: {weight}kg, Height: {height}m")
print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    category = "Underweight"
    advice = "Consider eating more nutritious food"
elif bmi < 25:
    category = "Normal weight"
    advice = "Great! Maintain your healthy lifestyle"
elif bmi < 30:
    category = "Overweight"
    advice = "Consider regular exercise"
else:
    category = "Obese"
    advice = "Consult a healthcare professional"

print(f"Category: {category}")
print(f"Advice: {advice}")
print()

print("="*60)
print("✨ End of Control Flow Examples")
print("="*60)
