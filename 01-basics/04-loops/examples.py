"""
🔄 Loops - Comprehensive Examples
==================================

Master loops in Python!
Author: Tamanna
"""

print("="*60)
print("LOOPS - EXAMPLES")
print("="*60)
print()

# FOR LOOP
print("1. FOR LOOP BASICS")
print("-"*40)

for i in range(5):
    print(f"Count: {i}")
print()

# Real-world: Print shopping list
print("📝 Shopping List:")
items = ["Milk", "Bread", "Eggs", "Butter"]
for item in items:
    print(f"  - {item}")
print()

# WHILE LOOP
print("2. WHILE LOOP")
print("-"*40)

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
print()

# Real-world: Password attempts
print("🔐 Password System:")
attempts = 0
max_attempts = 3
password = "secret"
user_input = ""

while attempts < max_attempts and user_input != password:
    print(f"Attempt {attempts + 1}/{max_attempts}")
    attempts += 1
    if attempts == 2:  # Simulate correct on 2nd try
        user_input = password
        print("✓ Password correct!")
print()

# BREAK and CONTINUE
print("3. BREAK AND CONTINUE")
print("-"*40)

print("Break example (stop at 5):")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("\n")

print("Continue example (skip 5):")
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print("\n")

# Real-world: Finding first even number
numbers = [1, 3, 5, 8, 9, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
print()

# NESTED LOOPS
print("4. NESTED LOOPS")
print("-"*40)

print("Multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()
print()

# LOOP WITH ELSE
print("5. LOOP WITH ELSE")
print("-"*40)

for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed!")
print()

print("="*60)
