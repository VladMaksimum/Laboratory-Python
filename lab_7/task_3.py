import json


with open("lab_7/ex_3.json") as file:
    global inv
    inv = json.loads(file.read())['invoices']
    
    inv.append({"id":3, "total":300.00, "items":[{"name":"item 4", "quantity":3, "price":100.00}]})
    file.close()

with open("lab_7/ex_3.json",'w') as file1:
    file1.write(json.dumps({"invoices":inv}, indent=4))
