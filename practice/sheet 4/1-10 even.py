def count_even():
    count = 0
    for i in range(1,21):
        if i % 2 == 0:
            count += 1
    return count
    
print(count_even())