import random

list1 = [3, 9, 40, 30, 23, 11]

#radiant()
print("Randint", random.randint(1,10))

#randrange()
print("Randrange", random.randrange(1, 10))

#choice()
print("Choice", random.choice(list1))

#random()
print("Random", random.random())

#shuffle()
random.shuffle(list1)
print("Shuffle", list1)

#uniform()
print("Uniform", random.uniform(1, 10))

'''
There are many random module functions 
are there in 'docs.python.org'
'''
