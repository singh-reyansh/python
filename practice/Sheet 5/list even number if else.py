def has_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
        else:
            continue
    return False

nums = input("Enter numbers sperated by spaces: ")
num_list = nums.split()

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

if has_even(num_list):
    print("True")
else:
    print("False")