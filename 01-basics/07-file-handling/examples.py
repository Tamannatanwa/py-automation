"""
📁 File Handling - Comprehensive Examples
==========================================

Master file operations in Python!
Author: Tamanna
"""

import os

print("="*60)
print("FILE HANDLING - EXAMPLES")
print("="*60)
print()

# Create a temp directory for demos
temp_dir = "/tmp/file_demo"
os.makedirs(temp_dir, exist_ok=True)

# WRITING TO FILES
print("1. WRITING TO FILES")
print("-"*40)

# Write mode (overwrites)
file_path = f"{temp_dir}/sample.txt"
with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
print(f"✓ Created {file_path}")
print()

# READING FROM FILES
print("2. READING FROM FILES")
print("-"*40)

with open(file_path, "r") as file:
    content = file.read()
print("File content:")
print(content)

# Read line by line
print("Reading line by line:")
with open(file_path, "r") as file:
    for line in file:
        print(f"  {line.strip()}")
print()

# APPEND MODE
print("3. APPEND MODE")
print("-"*40)

with open(file_path, "a") as file:
    file.write("Appended line\n")
print("✓ Appended to file")

with open(file_path, "r") as file:
    print("Updated content:")
    print(file.read())
print()

# FILE EXISTENCE CHECK
print("4. CHECK FILE EXISTENCE")
print("-"*40)

if os.path.exists(file_path):
    print(f"✓ {file_path} exists")
else:
    print(f"✗ {file_path} does not exist")
print()

# REAL-WORLD: LOG FILE
print("5. REAL-WORLD: LOG FILE")
print("-"*40)

log_file = f"{temp_dir}/app.log"
from datetime import datetime

def write_log(message):
    """Write to log file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

write_log("Application started")
write_log("User logged in")
write_log("Data processed successfully")

print(f"✓ Log file created: {log_file}")
print("\nLog contents:")
with open(log_file, "r") as f:
    print(f.read())

print("="*60)
