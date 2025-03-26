import json


with open("lab_7/ex_2.json") as tmp:
    data = json.loads(tmp.read())
    tmp.close()

with open("lab_7/ex_2.json",'w') as file:
    file.write(json.dumps(data, indent=4))


data = data["users"]
output = {}
for user in data:
    output[user['name']] = user['phoneNumber']

print(output)
