def add_positive(numbers, n):
    if n > 0:
        numbers.append(n)

nums = []

user_num = int(input("Enter a number: "))
add_positive(nums, user_num)

print(nums)