# Print() -- Function

#Default behaviour is that print goes to new line after printing a statement

print("Arvinder")
print(1000)
print(True)

print()

# \n -- Newline 
print("Arvinder \n")
print("Arvinder \n")
print("Arvinder \n")


print("Arvinder")
print("Arvinder" , end=" ")
print("Arvinder",end=" ")

print("Arvinder",end=".")
print("Arvinder","Arvin", sep="-" ,end="0000000")
print()

print("100","300","500", sep="+" ,end="=$")
# print()  -- to add an empty line 
print()
# \n - to add a new line

print("100","300","500", sep="+")



# Formatted String 
# x =100
# print(x)

# x = "Reyansh"
# print(x)
x = 20 
y = 300.40
is_valid = True
name = "John"
print("My name is", name, "and my age is", x, "and my marks are", y, "and Am I married?", is_valid)


print(f'My name is {name} and my age is {x} and my marks are {y} and Am I married? {is_valid}')

# print("The title of the book is "The wings of Fire" in 2020.")

print('The title of the book is "The wings of Fire" in 2020.')
print("The title of the book is \"The wings of Fire\" in 2020.")

print('The title of the book is \'The wings of Fire\' in 2020.')