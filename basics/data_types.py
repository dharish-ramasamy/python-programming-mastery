# Numeric
    # Integers
    # Float
    # Complex Numbers

# Sequence Type
    # String
    # List[val, val, val]
    # Tuple(val, val, val)
    # Dictionary {key:value}
    # Set {value}

# Integer
num1 = 10
print(num1, type(num1))

# Float
num2 = 10.5
print(num2, type(num2))

# Complex
num3 = 10j
print(num3, type(num3))

# String
Str = "Hello World"
print(Str, type(Str))

# List
students = ["std1", "std2", "std3", "std4"]
print(students, type(students))
print(students[1])

# Tuple
studentDetails = ("std1", "std2", "std3", "std4")
print(studentDetails, type(studentDetails))
print(studentDetails[0])

# Dictionary
employee = {
    "name": "emp_name",
    "age": 25,
    "salary": 80000,
    "scale": 17
}
print(employee, type(employee))
print(employee['age'])

# Set
employeeData = {
    "emp_name", 25, 80000, 17
}
print(employeeData, type(employeeData))
