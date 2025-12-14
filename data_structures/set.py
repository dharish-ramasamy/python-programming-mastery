set1 = {10,30,59,29,390,25}
print(set1)

for i in set1:
    print(i)
print("") 

#set functions

#remove()
set1.remove(10)
print(set1)

#discard()
set1.discard(11)
print(set1)

#pop()
set1.pop()
print(set1)

#clear()
set1.clear()
print(set1)

#add()
set1.add(47)
print(set1)

#update()
list1 = [10, 25, 55, 32]
set1.update(list1)
print(set1)
