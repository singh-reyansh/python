# Data Types - Numeric Type - Integer , Float , Complex 


# Loosely Typed - A variable has no predefined type associated with . it will be change it's behaviour according to the value on the right side.

x = 10
x = "Hello"
print(type(x))
x = True
print(type(x))

# Numeric - Integer - Any number without decimals. 

x = 2000
x = -4000
print(type(x))


# type()- It is a built in function in Python which is used to print the type of any variable.

y = 100.34
print(type(y))
z = 200.0
# x = 200 -- Integer takes - 4 bytes -- 4 slots 
print(type(z))

# Complex Number - A representation of Negative numbers inside the root.
# / -3 = 3i    i= /-1

# cn = 4 + 3j      - Real part + imaginary part = Complex Number


# Every Number has a max limit 

# Type Casting -- Converting one type into another

# Integer to Float 
x = 3000
print("Before Casting (Integer):",type(x))
print(x)
y = float(x)
print("After Casting (Integer):",type(y))
print(y)


# Float to Integer
x = 3000.456
print("Before Casting (Float):",type(x))
print(x)
y = int(x)
print("After Casting (Float):",type(y))
print(y)

# Casting a float into integer is not considered safer because of data loss.
# (30.3)*4 = 121.2

# 30*4 = 120


