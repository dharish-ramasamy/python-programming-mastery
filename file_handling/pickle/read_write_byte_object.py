# Create and save a data into Byte Object
import pickle
data = {
    "name":"John",
    "age":30,
    "profession":"Software Engineer",
    "salary": "$3000",
    "Experience": "10+ Years"
}
myData = pickle.dumps(data)
print(pickle.loads(myData))
