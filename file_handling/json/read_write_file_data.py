# Write and Read Json Data from a File

import json
from textwrap import indent

# Define a Json Data
data = {
    "name":"John",
    "age": 25,
    "city": "Bangalore"
}

# Write JSON data to a file

# file = open("json-data.json", "w")
with open("json-data.json", "w") as file:
    json.dump(data, file, indent=4)
print("JSON data has been written to json-data.json file")


# Read data from a file

# myData = open("json-data.json", "r")
with open("json-data.json", "r") as file:
    loadedData = json.load(file)
print(loadedData)

