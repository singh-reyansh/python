# ========================================
# 1. Basic Function Calling
# ========================================
def greet_first():
    """Print 'Hello' and call the second function."""
    print("Hello")
    greet_second()


def greet_second():
    """Print 'Hi'."""
    print("Hi")


# ========================================
# 2. Print Numbers 1 to 10
# ========================================
def print_numbers_iterative():
    """Print 1 to 10 using a loop."""
    print("\nIterative (Loop):")
    for i in range(1, 11):
        print(i, end=" ")
    print()


def print_numbers_recursive_ascending(n=1):
    """Print numbers from n to 10 (ascending, pre-order)."""
    if n > 10:
        return
    print(n, end=" ")
    print_numbers_recursive_ascending(n + 1)


def print_numbers_recursive_descending(n=10):
    """Print numbers from n down to 1 (descending)."""
    if n < 1:
        return
    print(n, end=" ")
    print_numbers_recursive_descending(n - 1)


def print_numbers_recursive_post_order(n=1):
    """Print 1 to 10 using post-order (ascending after recursion)."""
    if n > 10:
        return
    print_numbers_recursive_post_order(n + 1)
    print(n, end=" ")


# ========================================
# 3. Sum of First 10 Natural Numbers
# ========================================
def sum_numbers_iterative():
    """Calculate sum 1 to 10 using a loop."""
    total = 0
    for i in range(1, 11):
        total += i
    return total


def sum_numbers_recursive(n=1):
    """Recursively sum from n to 10."""
    if n > 10:
        return 0
    return n + sum_numbers_recursive(n + 1)


# ========================================
# Run All Examples
# ========================================
print("=" * 50)
print("RECURSION EXAMPLES - CLEAN & PROFESSIONAL")
print("=" * 50)

# 1. Basic function calls
print("\n1. Basic Function Calls:")
greet_first()

# 2. Print numbers
print("\n2. Printing Numbers 1 to 10:")
print_numbers_iterative()

print("Recursive (Ascending - Pre-order):")
print_numbers_recursive_ascending()
print()

print("Recursive (Descending):")
print_numbers_recursive_descending()
print()

print("Recursive (Ascending - Post-order):")
print_numbers_recursive_post_order()
print()

# 3. Sum examples
print("\n3. Sum of Numbers 1 to 10:")
iterative_sum = sum_numbers_iterative()
recursive_sum = sum_numbers_recursive()

print(f"Iterative Sum : {iterative_sum}")
print(f"Recursive Sum : {recursive_sum}")

# ========================================
# Key Recursion Concepts
# ========================================
print("\n" + "=" * 50)
print("KEY RECURSION CONCEPTS")
print("=" * 50)
print("""
• Base Case       : Stops recursion (e.g., n > 10)
• Recursive Call  : Function calls itself
• Call Stack      : Each call uses memory
• Python Limit    : ~1000 recursive calls max
• Use Loops       : For large inputs to avoid stack overflow
""")
