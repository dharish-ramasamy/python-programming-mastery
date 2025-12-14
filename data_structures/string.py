'''
string is considered a linear data structure in Python. While often introduced as a basic data type, it is also a fundamental data structure because it organizes and stores data (characters) in a specific sequence
'''

#string indexing
str1 = "Hello World"
print("Normal:",str1[0::1])
print("Reverse:",str1[-1:-12:-1])


#string iteration
str1 = "Welcome to python programming language"

print("Normal:")
for n in str1:
    print(n)
print("")

l = len(str1)
print("Reverse:")
for n in range(l-1, -1, -1):
    print(str1[n])


#string functions
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.capitalize())

str1 = "hello world"
print(str1.find('w'))
print(str1.index('d'))
print(str1.isalpha())
print(str1.isdigit())
print(str1.isalnum())

#chr and ord (based on ASCII)

num = 70
print(chr(num))

characters = 'a'
print(ord(characters))


#string formating
str1 = "Hello my name is {lastname} {firstname}".format(firstname = "world", lastname = "hello")
print(str1)
str1 = "Hello my name is {1} {0}".format("hello", "world")
print(str1)
str1 = "Hello my name is {} {}".format("hello", "world")
print(str1)

