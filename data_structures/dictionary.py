d = {
    'name':'Linux',
    'course':'Python',
    'fees':20000
}
print(d)
print(d['name'], d['course'], d['fees'])
for i in d:
    print(i, ":", d[i])


#dictionary functions

#keys()
for i in d.keys():
    print(i)

#values()
for v in d.values():
    print(v)

#items()
for k, v in d.items():
    print(k, v)

#get()
print(d['course'])
print(d.get('course'))

#del()
del d['name']
print(d)

#pop()
d.pop('fees')
print(d)

d2 = dict(name='windows', age=28, education='Software Engineering')
print(d2)

#update()
d2.update({'name':'ios'})
d2['age'] = 29
print(d2)

#clear()
d2.clear()
print(d2)


#nested dictionary
students = {
    'John':{'age':30, 'education':'Computer Science', 'RollNo':'2024ABC-1', 'Semester':'1st'},
    'Vick': {'age': 35, 'education': 'Artificial Intelligence', 'RollNo': '2024ABC-2', 'Semester': '1st'},
    'Mark': {'age': 28, 'education': 'Software Engineering', 'RollNo': '2024ABC-3', 'Semester': '1st'},
    'Johson': {'age': 25, 'education': 'Data Security', 'RollNo': '2024ABC-4', 'Semester': '1st'},
}
print(students['John']['age'])
for k, v in students.items():
    print(k, v)

students['John']['age'] = 32
for k, v in students.items():
    print(k, v)
