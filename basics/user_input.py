#by default the user input is taken as string

name = input("Enter your name: ")
age = input("Enter your age: ")
profession = input("Enter your profession: ")
print("My name is ", name)
print("My age is ", age)
print("My profession is ", profession)

#without typecaste
val1 = input("Enter first nunmber: ")
val2 = input("Enter second number: ")
print(val1 + val2) #provides wrong output

#with typecaste
val3 = int(input("Enter first nunmber: "))
val4 = float(input("Enter second number: "))
print(val3 + val4)

