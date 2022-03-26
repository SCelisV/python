"""
@author: Fabrizio Romano
transcript: SCelis

/SCProjects/0_SCProjects_github.com_SCelisV$ python3 python/SC.Code/learn.pp/learnpp/decorate.sort.undecorate.py

# decorate.sort.undecorate.py

"""

# keys: id and credits, credits also a dictionary there are three key/value pairs
students = [
   dict(id=0, credits=dict(math=9, physics=6, history=7)),      # sum((9, 6, 7)
   dict(id=1, credits=dict(math=6, physics=7, latin=10)),
   dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
   dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

print("type (students): ", type (students))
# type (students):  <class 'list'>

# Esta función crea una tupla con la suma de los creditos por cada estudiante
def decorate(student):
# create a 2-tuple (sum of credits, student) from student dict
# returns an object similar to iterable, with only the values dict.values() 
   return (sum(student['credits'].values()), student)

# Esta función deshace la suma de los creditos, devolviendo el objeto origina
def undecorate(decorated_student):
# discard sum of credits, return original student dict
   return decorated_student[1]

print("<-------------------->")

# imprimir students
# for the first student is equivalent to sum((9, 6, 7)) .

for i in students:
    print(i)
    print(sum(i['credits'].values())) 

"""
{'id': 0, 'credits': {'math': 9, 'physics': 6, 'history': 7}}
22
{'id': 1, 'credits': {'math': 6, 'physics': 7, 'latin': 10}}
23
{'id': 2, 'credits': {'history': 8, 'physics': 9, 'chemistry': 10}}
27
{'id': 3, 'credits': {'math': 5, 'physics': 5, 'geography': 7}}
17
"""

print("<-------------------->")
variable = students
print("type (variable): ", type (variable))
# type (variable):  <class 'list'>

print("<-------------------->")
print("decorate(variable[2]): ", decorate(variable[2]))
# decorate(variable[2]):  (27, {'id': 2, 'credits': {'history': 8, 'physics': 9, 'chemistry': 10}})

print("<-------------------->")

print("decorate_students = decorate(students[0]): ", decorate(students[0]))
# {'id': 0, 'credits': {'math': 9, 'physics': 6, 'history': 7}}
# create a 2-tuple (sum of credits, student) from student dict
# decorate_students = decorate(students[0]):  (22, {'id': 0, 'credits': {'math': 9, 'physics': 6, 'history': 7}})

print("<-------------------->")

print("(map(decorate, students)): ", (map(decorate, students)))
# (map(decorate, students)):  <map object at 0x7ff462b97f10>

print("<-------------------->")

_ = list
print("_(map(decorate, students)): ", _(map(decorate, students)))

"""
_(map(decorate, students)):  
[(22, {'id': 0, 'credits': {'math': 9, 'physics': 6, 'history': 7}}), 
 (23, {'id': 1, 'credits': {'math': 6, 'physics': 7, 'latin': 10}}), 
 (27, {'id': 2, 'credits': {'history': 8, 'physics': 9, 'chemistry': 10}}), 
 (17, {'id': 3, 'credits': {'math': 5, 'physics': 5, 'geography': 7}})]

"""
print("<-------------------->")

print("sorted(map(decorate, students), reverse=True): ", sorted(map(decorate, students), reverse=True))
"""
sorted(map(decorate, students), reverse=True):  
[(27, {'id': 2, 'credits': {'history': 8, 'physics': 9, 'chemistry': 10}}), 
 (23, {'id': 1, 'credits': {'math': 6, 'physics': 7, 'latin': 10}}),
 (22, {'id': 0, 'credits': {'math': 9, 'physics': 6, 'history': 7}}),
 (17, {'id': 3, 'credits': {'math': 5, 'physics': 5, 'geography': 7}})]
"""
print("<-------------------->")

print(" undecorate(students): ", undecorate(students))
# discard sum of credits, return original student dict
# {'id': 1, 'credits': {'math': 6, 'physics': 7, 'latin': 10}}

print("<-------------------->")

_ = list

print("--(map(undecorate, )): ", _(map(undecorate, sorted(map(decorate, students), reverse=True))) )
"""
[{'id': 2, 'credits': {'history': 8, 'physics': 9, 'chemistry': 10}}, 
 {'id': 1, 'credits': {'math': 6, 'physics': 7, 'latin': 10}}, 
 {'id': 0, 'credits': {'math': 9, 'physics': 6, 'history': 7}}, 
 {'id': 3, 'credits': {'math': 5, 'physics': 5, 'geography': 7}}]
"""