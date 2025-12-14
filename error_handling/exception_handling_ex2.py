num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

try:
    result = num1/num2
# except (TypeError, ZeroDivisionError) as e:
except Exception as e:
    print(f"An Error Occurred {e}")
else:
    print(result)
finally:
    print("Execution Completed")
