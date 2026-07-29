def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = input("Enter numbers sperated by a space: ")
num_list = [int(x) for x in nums.split()]

print("Maximum Value: ", find_max(num_list))