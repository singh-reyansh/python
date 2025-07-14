# Star Pattern

# *
# print("*")

# * * * * * * * 
# print("* * * * * * * * ")
# print("* "*5)

# * * * * * * * *
# for i in range(20):
#     print("*", end = " ")


# * * * * *
# * * * * *
# * * * * * 
# * * * * *
# * * * * *
# for x in range(5):
#     for i in range(5):
#         print("*", end=" ")
#     print()


# 1 2 3 4 5   
# *           1
# * *         2
# * * *       3
# * * * *     4
# * * * * *   5
"""
for x in range(5):
    for i in range(x+1):
        print("*", end=" ")
    print()
"""

# 1 2 3 4 5
# * * * * *   1
# * * * *     2 
# * * *       3 
# * *         4 
# *           5

# for x in range(5,0,-1):
#     for i in range(x):
#         print("*", end=" ")
#     print()

# 1
# 1 2 
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5
"""
for x in range(5):
    for i in range(x+1):
        print(i+1, end=" ")
    print()
"""
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5

"""

for i in range(5):
    for j in range(i+1):
        print(i+1, end=" ")
    print()
"""


# 1 
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

"""
counter = 1
for i in range(5):
    for j in range(i+1):
        print(counter, end=" ")
        counter+=1
    print()
"""

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
"""
character = 65
for i in range(5):
    for j in range(i+1):
        print(chr(character), end=" ")
    character+=1
    print()
"""

# A 
# B C 
# D E F 
# G H I J 

"""
character = 65
for i in range(5):
    for j in range(i+1):
        print(chr(character), end=" ")
        character+=1
    print()

"""
