#  type casting -- converting one data type to another data type

#  int() -- converts to integer
#  float() -- converts to float
#  str() -- converts to string
#  bool() -- converts to boolean

x = 100 
y = 500.56
is_valid = True
name = "John"

print("------------------ Before type casting ------------------")
print(x)
print(y)
print(is_valid)
print(name)

print("------------------ After type casting ------------------")
print(int(x))
print(int(y))


print(float(x))
print(float(y))


name1 = name + str(x)
print(name1)
name2 = name + str(y)
print(name2)
name3 = name + str(is_valid)
print(name3)


x = 100 
y = 200
z = 305

# avg_marks = (x + y + z) / 3      # / -- division operator- complete division - float 
avg_marks = int((x + y + z) / 3)   # // -- floor division operator - integer

print(type(avg_marks))
print(avg_marks)

# // -- 2.8 -- first result , 3.2 -- second result  answer - add first and second result -- 2 + 3 = 5
# 2.8 + 3.2 = 6.0






