import json
import os
import config

directory = config.DIRECTORY
entries = config.entries
directory_path = config.directory_path

for entry in entries:
    myJsonFile = open(directory + "/" + entry, 'r', )
    myJsonData = myJsonFile.read()
    obj = json.loads(myJsonData)
    print(str(obj['abi']))
    json_formated_str = json.dumps(obj['abi'], indent=2)
    myJsonFile = open(directory + "/" + entry, 'w')

    myJsonFile.write(str(json_formated_str))

# myJsonFile = open('jsonfiles/SmartTimelock.json', 'r')
# myJsonFiles = open(myJsonDirectory, 'r')

# myJsonData = myJsonFile.read()
# myJsonDataAll = myJsonFiles.read()

# objs = json.loads(myJsonDataAll)

# obj = json.loads(myJsonData)


# json_formated_str = json.dumps(obj['abi'], indent=2)

# print(str(obj['abi'])) for debugging


# print(json_formated_str)

# myJsonFile = open('jsonfiles/SmartTimelock.json', 'w')

# myJsonFile.write(str(json_formated_str))
