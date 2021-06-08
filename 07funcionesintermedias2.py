# 1 Actualizar valores en diccionarios y listas
# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# # Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
# x[1][0]=15
# print(x)
# # Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
# students[0]['last_name']='Bryant'
# print(students)
# # En el directorio sports_directory, cambia 'Messi' a 'Andres'
# sports_directory['soccer'][0]='Andres'
# print(sports_directory)
# # Camba el valor 20 en z a 30
# z[0]['y']=30
# print(z)

# # 2 Itera a través de una lista de diccionarios

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# def iterateDictionary(list):
#     for i in range(0,len(students)):
#         a = students[i]['first_name']
#         b = students[i]['last_name']
#         print(f'first_name - {a}, last_name - {b} ')
# iterateDictionary(students)
# # La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# # # Bonus: Hacer que aparezcan exactamente así!
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel

# # 3 Obtén valores de una lista de diccionarios
# # Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

# def iterateDictionary2(key_name, list):
#     for i in range(0, len(list)):
#         print(list[i][key_name])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# 4 Iterar a traves de un diccionario con valores de lista
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# print(dojo['locations'])
# print(dojo)
# def printInfo(some_dict):
#     keys = some_dict.keys()
#     values = some_dict.values()
#     for i in range(0,len(keys)):
#         num = len(values)
#         key = keys[i].upper()
#         print(f'{num} {key} ')

# printInfo(dojo)
for k in dojo:
    print(k.upper())