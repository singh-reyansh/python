
# [expression for item in itetable if condition]

myList = [1,4,2,6,3,7,9,4]

# Create a list containing the square of each number 

# myList2 = [n**2 for n in myList]
# print(myList2)

# Double each and every number present in the list 
# myList2 = [n*2 for n in myList]
# print(myList2)


# Get the list of even numbers 
# even_numbers = [n for n in myList if n%2==0]
# print(even_numbers)

# Filter out the numbers which are divisible by 2 and 3 bo
# myList2 = [n for n in myList if n%2==0 if n%3==0]
# print(myList2)


# Create a list of numbers which are odd and greater than 5 
# myList2 = [n for n in myList if n%2!=0 if n > 5]
# print(myList2)


# Flatten an 2d Array 

matrix = [[1,2,3,4,5],[4,6,7,8,9],[12,23,45,67,89]]
# [
#     [1,2,3,4,5]
#     [4,6,7,8,9]
#     [12,23,45,67,89]
# ]

# flatten_list = [num for row in matrix for num in row ]
# print(flatten_list)
# myList4 = []
# for row in matrix:
#     for num in row:
#         myList4.append(num)

# print(matrix)
# print(myList4)


# Dictionary Comprehension 

# key : Value 

# dictionary_comp = {x : expression for loop if condition}

# Create a dictionary where every value is double of its key

# myDictionary = {x : x*2 for x in myList}
# print(myDictionary)

# Map every word with its length 

# myList5 = ["Hello", "Python", "Online","Course","Remote","Development"]

# # Hello - 5
# result = { x : len(x) for x in myList5}
# print(result)

myList = [x*y for x in range(5) for y in range(5)]
print(myList)

# 
# for x in range(5):
#     for y in range(5):
#         print(x*y, end=" ")

#     print()

# x = 0  Y  = 0 ,1 2, 3, 4  - x*y = 0 0 0 0 0 
# x = 1  Y  = 0 ,1 2, 3, 4    x*y = 0 1 2 3 4 


# 
myDictionary = {1:"One",2:"Two",3:"Three",4:"Four"}

# Invert the dictionary 
# Output : myDictionary = {"One":1,"Two":2,"Three":3,"Four":4}

inverted = { value : key for key , value in myDictionary.items()}
print(inverted)