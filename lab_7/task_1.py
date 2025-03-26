import jsonschema as jsch
import json

with open("lab_7/ex_1.json") as file:
    data = json.loads(file.read())
    with open("lab_7/schema_1.json") as schema:
        schema = json.loads(schema.read())
        jsch.validate(data, schema)





