def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

nums = input("Enter numbers seperated by spaces: ")
num_list = nums.split()

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

print(sum_list(num_list))