# variables can hold values of different data types .

# 1. Integer - whole numbers  -- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 2. Float - decimal numbers -- 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1
# 3. String - text -- "John", "Jane", "Doe", "Smith"
# 4. Boolean - True or False -- True, False

x = 200    # integer
y = 400.50 # float
name = "John" # string
is_valid = True # boolean


print(x)
print(y)
print(name)
print(is_valid)

# 
x = 3000
x = 400.50

# type() function -- it returns the type of the variable
print(type(x)) # <class 'float'>
y = 500
print(type(y)) # <class 'int'>
print(type(name)) # <class 'str'>
print(type(is_valid)) # <class 'bool'>

# is_valid = 100       # True or False

x = y +100
# Traceback (most recent call last):
#   File "c:\Users\Admin\Desktop\python\Day3\002.variables.py", line 33, in <module>
#     name = name + 100
# TypeError: can only concatenate str (not "int") to str
# name = name + 100
# print(name)

























