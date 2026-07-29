def fibonacci_after_10():
    a, b = 0, 1
    for _ in range(10):
        a, b = b, a + b
    return a

print(fibonacci_after_10())