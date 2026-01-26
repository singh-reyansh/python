# JSON is a data format that follows a strict syntax built around key value pair like strings , lists , numbers , booleans and null. 

# machine readable and independent of language 

# structured data 

# JSON is ideal when it comes to sharing over the internet.

# 123 -- text , "pass":"123" , "num":123

# Readable and easy to access , easy to parse , can be duirectly converted into built in data types -- dictionary to Json and vice versa.

# 

# import json 

# data = {
#     "name":"Reyansh",
#     "COuntry":"USA",
#     "Code":1234
# }

# json_result = json.dumps(data)
# print(json_result)


# import json 
# json_text = '{"name": "Reyansh", "COuntry": "USA", "Code": 1234}'
# data = json.loads(json_text)
# print(data)

# 

# import json 
# with open("simple.json","r") as f:
#     data = json.load(f)

# print(data)
# print(data["Code"])


import json 
data = {
    "id":12,
    "name":"Reyansh",
    "Country":"USA"
}

with open("reyansh.json","w") as f:
    json.dump(data,f, indent=4, sort_keys=True)


