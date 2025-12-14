tuple1 = (10,30,60,12,10,430,23)
print(tuple1[0])
print(tuple1[-1])

length = len(tuple1)
print(length)

for i in range(0, length-1, 1):
    print(tuple1[i])
print("")

for i in range(length-1, -1, -1):
    print(tuple1[i])
print("")


#tuple functions

#min()
print(min(tuple1))

#max()
print(max(tuple1))

#count()
print(tuple1.count(60))

#index()
print(tuple1.index(10))

print(tuple1.index(10, 1))



