num1 = 10
num2 = 0

try:
    result = num1/num2
except ZeroDivisionError:
    print("Don't divide it by zero, Try Again")
else:
    print(result)
finally:
    print("Execution Completed")

