#for loop

'''
>> range(5)
Start 0
End <5
Increment 1

>> range(1, 5)
Start 1
End <5
increment 1

>> range(1, 5, 2)
Start 1
End <5
Increment 2
'''
print("for loop")
print("Increment from 0 to 9")
for n in range(0, 10, 1):
    print("no.>> ", n)

print("Decrement from 10 to 1")
for m in range(10, 0, -1):
    print("no.>> ", m)


#while loop
print("while loop")
n = 0
while n<=10:
    print(n)
    n = n + 1
print("")

#break, continue and pass statements

#break statement
for num in range (1, 10):
    if num == 5:
        break
    print(num)

#continue statement
for num in range(1,6):
    if num == 3:
        continue
    print(num)

#pass statement
for num in range(1, 5):
    pass
