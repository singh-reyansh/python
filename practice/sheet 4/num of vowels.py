def count_vowels():
    text = "Hello, world!"
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
    
print(count_vowels())