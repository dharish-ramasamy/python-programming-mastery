import json
from textwrap import indent

# Define a Json Data
data = {
    "name":"John",
    "age": 25,
    "city": "Bangalore"
}

print(type(data))

# Convert Python Object into Json String
jsonString = json.dumps(data, indent=4)
print(type(jsonString))
print("JSON String: ", jsonString)

# Convert JSON string back into Python Object
pythonObject = json.loads(jsonString)
print(type(pythonObject))
print("Python Object: ", pythonObject)
