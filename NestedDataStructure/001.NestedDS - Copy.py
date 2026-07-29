# # DS - Sets , Tuples , Dictionaries , Lists 

# myList = [12,23,45,67,89,0,25,28]

# myInfo= {
#     "Name":"Reyansh",
#     "Class":10,
#     "Country":"USA",
#     "Code":12345
# }

# mySet = {12,14,17,18,10}

# myTuple = (23,25,26,37,29)

# # 

# myList = [12,23,(23,25,26,37,29),45,67,{12,14,17,18,10},89,0,[245,234,567,278],25,{"Name":"Reyansh","Class":10,"Country":"USA","Code":12345
# },28]


# # 45
# print(myList[3])

# # 25 in (23,25,26,37,29)
# print(myList[2][1])

# # Reyansh
# print(myList[10]["Name"])
# print(myList[10].get("Name"))


# #567 in [245,234,567,278]

# print(myList[8][2])

myInfo= {
    "Name":"Reyansh",
    "Class":10,
    "Country":"USA",
    "Code":12345,
    "hobbies":["Cricket","Snooker","Hockey","Badminton"],
    "myScores":(23,25,26,37,29),
    "myMarks":{
        "Maths":90,
        "Science":96,
        "Humanity":86
    }}

# Country
print(myInfo["Country"]) 

# Hockey
print(myInfo["hobbies"][2])

# 37 
print(myInfo["myScores"][3])


# Sciece - 96

print(myInfo["myMarks"]["Science"])



