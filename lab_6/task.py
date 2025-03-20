import json
from pathlib import Path
import sys

with open("lab_6/" + str(sys.argv[1])) as data:
    name = "lab_6/" + str(sys.argv[1][:-4:]) + ".csv"
    Path(name).touch()
    with open(name, 'w') as res:
        data = json.loads(data.read())

        first = True
        for emp in data['Employees']:
            if first:
                for index, info in enumerate(emp.items()):
                    res.write(info[0] + (',' * ((index+1) != len(emp))) + ('\n' * ((index+1) == len(emp))))
            
            for index, info in enumerate(emp.items()):
                res.write(info[1] + (',' * ((index+1) != len(emp))) + ('\n' * ((index+1) == len(emp))))
            first = False
                            