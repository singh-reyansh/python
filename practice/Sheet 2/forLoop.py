# Python Loops Tutorial
# This script demonstrates various ways to use for loops in Python
# Reference: W3Schools Python Loops (https://www.w3schools.com/python/python_for_loops.asp)

# --- Basic For Loop ---
# Loops through numbers 0 to 24
# range(start, stop, step) generates a sequence of numbers
print("Basic number sequence (0 to 24):")
for x in range(25):
    print(x, end=" ")  # end=" " keeps output on same line with space separator
print("\n")  # New line for separation

# --- For Loop with Custom Start ---
# Starts at 2, ends at 9 (10 is excluded)
print("Loop starting at 2 (2 to 9):")
for x in range(2, 10):
    print(x, end=" ")
print("\n")

# --- For Loop with Step ---
# Step defines increment between numbers
print("Loop with step of 1 (2 to 9):")
for x in range(2, 10, 1):  # Step of 1 is default, shown for clarity
    print(x, end=" ")
print("\n")

print("Loop with step of 2 (2 to 8):")
for x in range(2, 10, 2):  # Prints every second number
    print(x, end=" ")
print("\n")

print("Odd numbers (1 to 9):")
for x in range(1, 10, 2):  # Prints odd numbers
    print(x, end=" ")
print("\n")

# --- Reverse Loop ---
# Counting down from 20 to 2
print("Reverse loop (20 to 2):")
for x in range(20, 1, -1):  # Negative step for decrement
    print(x, end=" ")
print("\n")

# --- Looping Through a List ---
# Lists are iterable data structures
x = [12, 13, 24, 256, 78, 50]
print("List contents:", x)

# Using index with range() and len()
print("Looping through list indices:")
for item in range(len(x)):
    print(f"Index: {item}, Value: {x[item]}")
print()

# Direct iteration over list elements
print("Direct list iteration:")
for item in x:
    print(item, end=" ")
print("\n")

# --- Looping Through a String ---
# Strings are iterable, one character at a time
greet = "hello"
print("Looping through string characters:")
for char in greet:
    print(char, end=" ")
print("\n")

# Using index with string
print("Looping through string indices:")
for i in range(len(greet)):
    print(f"Index: {i}, Character: {greet[i]}")
print()

# --- Summing List Elements ---
# Calculating sum of list elements
result = 0
print("Calculating sum of list elements:")
for item in range(len(x)):
    result += x[item]
    print(f"Adding {x[item]}, Current sum: {result}")
print(f"Final sum: {result}")
