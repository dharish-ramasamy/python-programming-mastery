# Defining a List

list1 = [10, 20, 30, 11, 40, 50, 60, 70, "Hello World", 10.5]
print(type(list1))
print(list1)
print(list1[1::2])
print(list1[8][1])
print(list1[-1::-1])

#list iteration
length = len(list1)
print(length)
for i in range(length):
    print(i, list1[i])

for i in range(length-1, -1, -1):
    print(i, list1[i])

for i in list1:
    print(i)


#list compensation
'''
Syntax of List Comprehension:
     [expression for item in list]
''' 

list1 = []
for i in range(1, 51):
    list1.append(i)
print(list1)

list2 = [ind for ind in range(1, 51) if ind % 2 == 1]
print(list2)


#list functions

list1 = [10,20,30,40,50,60,70,80,90,100]

#insert()
list1.insert(2, 22)
print(list1)

#append()
list2 = [20,30]
list1.append(list2)

#extend()
list3 = [40,50]
list1.extend(list3)
print(list1)

#del() 
del list1[2]
print(list1)

#pop()
print(list1.pop(2))

#remove()
list1.remove(10)
print(list1)

#clear()
list1.clear()
print(list1)


list1 = [40,50,60,10, 10,20,30, 80,70,90,100, 101,2, 10]
#count()
c = list1.count(10)
print(c)

#max() 
maxNumber = max(list1)
print(maxNumber)

#min() 
minNumber = min(list1)
print(minNumber)

#sort()
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#reverse() 
list1.reverse()
print(list1)


#zip function
list1 = [50,20,11,50,11,10]
list2 = [10,3,8,100,32, 4]
list3 = [3,2,78,49,23,45]

length = len(list1)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)

for i in range(length):
    print(list1[i], list2[i])

#string conversion
userInput = input("Enter the string:")
print(userInput)
list1 = userInput.split();
print(list1)

list1 = []
for i in range(1, 5):
    userInput = input("Enter a string-"+str(i)+": ")
    list1.append(userInput)
    print(userInput)
print(list1)
