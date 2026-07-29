def factorial_of_5():
    factorial = 1
    for i in range(1, 6):
        factorial *= i
    return factorial

print(factorial_of_5())