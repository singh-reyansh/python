def count_greater_than_10(numbers):
    count = 0
    for num in numbers:
        if num > 10:
            count += 10
    return count

my_list = [5,7,12,23,34,42]
result = count_greater_than_10(my_list)
print("Number of elements greater than 10:", result)