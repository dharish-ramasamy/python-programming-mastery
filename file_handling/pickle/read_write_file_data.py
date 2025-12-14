# Write Data into File
import pickle
data = {
    "name":"John",
    "age":30,
    "profession":"Software Engineer",
    "salary": "$3000",
    "Experience": "10+ Years",
    "Hobbies": "Learning New Skills",
    "Education":"BSAI"
}
writeData = open("my-data.txt", "wb")
pickle.dump(data, writeData)
writeData.close()


# Read Data from a file
myFile = open("my-data.txt", "rb")
loadData = pickle.load(myFile)
print(loadData)
