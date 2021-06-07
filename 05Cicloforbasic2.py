'''
1 Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

2 Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve

3 Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
Ejemplo: sum_total ([6,3, -2]) debería devolver 7

4 Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

5 Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
Ejemplo: longitud ([]) debería devolver 0

6 Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
Ejemplo: mínimo ([]) debería devolver False

7 Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
Ejemplo: máximo ([]) debería devolver False

8 Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 'longitud': 4}

9 Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37] '''

# # 1 Tamaño Grande
# def tamañoGrande(list):
#     for i in range(0,len(list)):
#         if list[i] > 0:
#             list[i] = 'big'

#     print(f'la lista de tamaño grande es {list}')
#     return list


# tamañoGrande([- 1, 3, 5, -5])

# # 2 contar positivos
# def contar_positivos(list):
#     sum = 0
#     for i in range(0, len(list)):
#         if list[i]>0:
#             sum +=1
#     print(f'la cuenta es {sum}')
#     list[-1]=sum
#     print(f'su lista es ',list)
#     return list


# contar_positivos([1,6, -4, -2, -7, -2])

# #3 Suma total
# def sum_total(list):
#     a = 0
#     for i in range(0,len(list)):
#         a += list[i]
#     print(f'la suma total de la lista es: {a}')
#     return a

# sum_total ([1,2,3,4])
# sum_total ([6,3, -2])

# #4 promedio de la lista
# def promedio(list):
#     c = 0
#     b = len(list)
#     for i in range(0,len(list)):
#         c += list[i]
#     print(f'el promedio de la lista es: {c/b}')
#     return c/b

# promedio([1,2,3,4])

# #5 longitud
# def longitud(list):
#     x=len(list)
#     print(f'el largo de la lista es {x}')

# longitud([])
# longitud([1,2,3,4])

# #6 Minimo
# def minimo(list):
#     menor = 0
#     if len(list) == 0:
#         print('no existen elementos en la lista',False)
#         return
#     elif len(list) == 1:
#         menor = list[0]

#     else:
#         for i in range(0, len(list)):
#             if i == 0:
#                 menor = list[0]
#             elif list[i] < menor:
#                 menor = list[i]
#     print(f'el minimo de la lista es {menor}')
#     return menor

# minimo([1,-5,3,4])


# # 7 Maximo de una lista
# def maximo(list):
#     mayor = 0
#     if len(list) == 0:
#         print('no existen elementos en la lista',False)
#         return
#     elif len(list) == 1:
#         mayor = list[0]

#     else:
#         for i in range(0, len(list)):
#             if i == 0:
#                 mayor = list[0]
#             elif mayor <list[i]:
#                 mayor = list[i]
#     print(f'el maximo de la lista es {mayor}')
#     return mayor

# maximo([30000000000000000000000000,4,5,6,2,100,10000,100000000,-1])
# maximo([])
# maximo([155])

# # 8 analisis final
# '''suma total promedio, minimo maximo y longitud de la lista'''

# def analisis_final(list):
#     x = {}
#     suma = 0
#     mayor = 0
#     menor = 0
#     b = len(list)

#     for i in range(0, len(list)):
#         suma += list[i]
#     promedio = suma/b
#     for i in range(0, len(list)):
#         if i == 0:
#             menor = list[0]
#         elif list[i]<menor:
#             menor = list[i]
#             # print(menor)

#     if len(list) == 0:
#         print('no existen elementos en la lista',False)
#         return
#     elif len(list) == 1:
#         mayor = list[0]

#     else:
#         for i in range(0, len(list)):
#             if i == 0:
#                 mayor = list[0]
#             elif mayor <list[i]:
#                 mayor = list[i]

            
#     x['suma total'] = suma
#     x['promedio'] = promedio
#     x['minimo'] = menor
#     x['maximo'] = mayor
#     x['longitud de la lista'] = len(list)

#     print(x)

# analisis_final([1,2,3,4,5,6,7,8,9,10])

# 9 lista inversa

def listainversa(list):
    for i in range(0,int(len(list)/2)):
        a = list[len(list)-1-i]
        b = list[i]
        list[i] = a
        list[len(list)-1-i] = b
        print(list)
    # print(list)
    return list
listainversa([37,2,1, -9,5,-7,-8])

        
