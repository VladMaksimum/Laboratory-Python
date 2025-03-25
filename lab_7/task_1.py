import jsonschema as check
import json

with open("lab_7/ex_1.json") as file:
    data = json.loads(file.read())
    with open("lab_7/schema_1.json") as schema:
        schema = json.loads(schema.read())
        for item in data['quiz']['sport'].items():
            check.validate(item[1], schema)





