a = 10
b = 4

#arithmetic operators(+, -, *, /, %, **, //)
print("Addition: ", a + b) 
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Modulus: ", a % b)
print("Exponents: ", a ** b) # 10 * 10 * 10 * 10
print("Floor Division: ", a // b)

#assignment operators(=, +=, -=, *=, /=)

a+=b
print(a)
a = a + b
print(a)

a -= b
print(a)
a = a-b
print(a)

a *=b
print(a)
a = a*b
print(a)

a /= b
print(a)
a = a/b
print(a)

#comparision operators(==, !=, >, <, >=, <=)
print("a == b", a == b)
print("a != b", a != b)
print("a > b", a > b)
print("a < b",a < b)
print("a >= b", a >= b)
print("a <= b", a <= b)

#logical operators(and, or, not)
print("And Operator: ", a < b and a <= 10)
print("Or Operator: ", a < b or a < 10)
print("Not Operator: ", not a < b)

#membership operator(in, not in)
string1 = "I am learning python programming"
print("Learning" in string1)
print("Learning" not in string1)

#identity operator(is , is not)
print(a is b)
print(a is not b)
