
current_year = 2013
current_month = 9  # Example where birthday has passed
current_day = 30   

birth_year = 2013
birth_month = 9
birth_day = 30

age = current_year - birth_year

if (current_month, current_day) <= (birth_month, birth_day):
    age -= 1
    print(age)
else:
    print("Your birthday has passed, HAPPY BELATED BIRTHDAY!")
    
# Ensure age is always printed
print("Exact age:", age)
