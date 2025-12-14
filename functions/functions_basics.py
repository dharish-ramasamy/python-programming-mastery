#defining a function
def sum(a, b):
    c = a + b
    print(c)

#calling a function
result = sum(20, 30)
result = sum(10, 20)
print("")

#providing default value for parameter
def showMsg(name = "World", language = "Python"):
    print("Hello", name)
    print("We are learning", language)
    print("Good Luck")
    print("")

showMsg("Max", "C#")
showMsg("John","PHP")


#return statement
def square(num):
    return num**2

result = square(4)
print(result)

