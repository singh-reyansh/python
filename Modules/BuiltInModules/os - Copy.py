# 
# MATH MODULE IN PYTHON
# 


import math

# Basic Mathematical Operations
print("\n BASIC MATH OPERATIONS:")
print(f"math.sqrt(25) = {math.sqrt(25)}")  # Square root
print(f"math.pow(2, 3) = {math.pow(2, 3)}")  # Power
print(f"math.fabs(-5.5) = {math.fabs(-5.5)}")  # Absolute value (float)

# Rounding Functions
print("\n ROUNDING FUNCTIONS:")
print(f"math.ceil(4.2) = {math.ceil(4.2)}")  # Round up
print(f"math.floor(4.8) = {math.floor(4.8)}")  # Round down
print(f"math.trunc(7.9) = {math.trunc(7.9)}")  # Truncate decimal

# Exponential and Logarithmic
print("\n EXPONENTIAL & LOGARITHMIC:")
print(f"math.exp(2) = {math.exp(2)}")  # e^x
print(f"math.log(100) = {math.log(100)}")  # Natural log
print(f"math.log10(100) = {math.log10(100)}")  # Base 10 log

# Trigonometric Functions (angles in radians)
print("\n TRIGONOMETRIC FUNCTIONS:")
angle_rad = math.radians(45)  # Convert degrees to radians
print(f"math.sin(45°) = {math.sin(angle_rad):.3f}")
print(f"math.cos(45°) = {math.cos(angle_rad):.3f}")
print(f"math.tan(45°) = {math.tan(angle_rad):.3f}")

# Constants
print("\n MATH CONSTANTS:")
print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")
print(f"math.tau = {math.tau}")

# Factorial and Combinatorics
print("\n FACTORIAL & COMBINATORICS:")
print(f"math.factorial(5) = {math.factorial(5)}")  # 5! = 120
print(f"math.comb(5, 2) = {math.comb(5, 2)}")  # Combinations: C(5,2)
print(f"math.perm(5, 2) = {math.perm(5, 2)}")  # Permutations: P(5,2)


# 
# OS MODULE - Essential Functions
# 
print("=" * 15 ,"OS MODULE FUNCTIONS","=" * 15 )

import os

# Current Working Directory
print("\n DIRECTORY OPERATIONS:")
print(f"Current Working Directory: {os.getcwd()}")

# List directory contents
print("\n LISTING DIRECTORY CONTENTS:")
try:
    items = os.listdir('.')
    print(f"Items in current directory: {items[:5]}...")  # Show first 5
except Exception as e:
    print(f"Error listing directory: {e}")

# File and Directory Operations
print("\n FILE/DIRECTORY OPERATIONS:")

# Check if path exists
test_file = "test_example.txt"
print(f"Does '{test_file}' exist? {os.path.exists(test_file)}")

# Create and remove files (with cleanup)
with open(test_file, 'w') as f:
    f.write("This is a test file for OS module demonstration.")

print(f"Created '{test_file}'")
print(f"File size: {os.path.getsize(test_file)} bytes")

# Remove the test file
os.remove(test_file)
print(f"Removed '{test_file}'")

# Environment Variables
print("\n ENVIRONMENT VARIABLES:")
print(f"OS Platform: {os.name}")
print(f"Home Directory: {os.environ.get('HOME', 'Not found')}")
print(f"PATH variable length: {len(os.environ.get('PATH', ''))} characters")

# Path Operations
print("\n PATH OPERATIONS:")
sample_path = "/home/user/documents/file.txt"
print(f"Sample path: {sample_path}")
print(f"Directory name: {os.path.dirname(sample_path)}")
print(f"File name: {os.path.basename(sample_path)}")
print(f"Split path: {os.path.split(sample_path)}")

# System Information
print("\n SYSTEM INFORMATION:")
print(f"CPU Count: {os.cpu_count()}")
print(f"Process ID: {os.getpid()}")

# Directory Creation and Navigation
print("\n DIRECTORY MANAGEMENT:")
test_dir = "test_directory"

# Create directory
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"Created directory: {test_dir}")

# Change directory and verify
original_cwd = os.getcwd()
os.chdir(test_dir)
print(f"Changed to directory: {os.getcwd()}")

# Return to original directory
os.chdir(original_cwd)
print(f"Returned to: {os.getcwd()}")

# Clean up - remove test directory
os.rmdir(test_dir)
print(f"Removed directory: {test_dir}")

# 
"""

MATH MODULE ESSENTIALS:
• math.sqrt(x)       - Square root
• math.pow(x, y)     - x raised to power y
• math.ceil(x)       - Round up
• math.floor(x)      - Round down
• math.factorial(n)  - n!
• math.sin/cos/tan(x) - Trigonometric functions
• math.pi, math.e    - Mathematical constants

OS MODULE ESSENTIALS:
• os.getcwd()        - Get current directory
• os.listdir(path)   - List directory contents
• os.path.exists()   - Check if path exists
• os.mkdir(path)     - Create directory
• os.remove(path)    - Remove file
• os.path.getsize()  - Get file size
• os.environ         - Environment variables
• os.path.join()     - Join path components
"""