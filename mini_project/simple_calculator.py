#simple calculator program

val1 = eval(input("Enter a first number: "))
val2 = eval(input("Enter a second number: "))
operator = input("Enter operator: ")

if operator == "+":
    print(val1 + val2)
elif operator == "-":
    print(val1 - val2)
elif operator == "*":
    print(val1 * val2)
elif operator == "/":
    print(val1 / val2)
else:
    print("Operator is invalid!")
