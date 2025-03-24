# Key : Value 
# 1,2,3,4,45

myDictionary = {
    "name":"Reyansh",
    "age":13,
    "Standard":6
    # "age":30,

}
# lists = [1,2,3,4,5,5]
# print(lists[4])

# Printing the dictionary
print(myDictionary)

# CRUD - Create Update Delete Read 

# Reading 
# Accessing a particular element
print(myDictionary['name'])
print(myDictionary['age'])
print(myDictionary.get('age'))

# Updating the value
myDictionary['Roll Number'] = 123
print(myDictionary)

# Deleting 
# del myDictionary['age'],myDictionary['Standard']
# print(myDictionary)

# myDictionary.clear()
# del myDictionary
print(myDictionary)


# Removing a element

# age = myDictionary.pop('age')
# print(age)


last =  myDictionary.popitem()
# last =  myDictionary.popitem()
print(last)


# Dictionary Methods :
# get all the keys 
print(myDictionary.keys())

print(myDictionary.values())

print(myDictionary.items())

# newDictionary = myDictionary.copy()
# print(newDictionary)

# Mergin two dictionaries 
newDictionary={"greet":"Hello"}
myDictionary.update(newDictionary)
print(myDictionary)
