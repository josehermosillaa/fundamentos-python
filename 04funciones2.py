# # '''1 Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
# # Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

# # 2 Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
# # Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

# # 3 First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
# # Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

# # 4 Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# # Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# # Ejemplo: values_greater_than_second ([3]) debería devolver False

# # 5 Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# # Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# # Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]'''

# # 1 Cuenta regresiva


# def cuentaRegresiva(num):
#     x = []
#     for i in range(num, -1, -1):
#         print('la cuenta regresiva es ', i)
#         x.append(i)
#     print('la lista es ', x)


# print('Cuenta hacia atras')
# print('ingrese un numero')
# num = int(input())
# cuentaRegresiva(num)

# # 2 Imprimir y volver


# def imprimirVolver(list):
#     print('el primer elemento es ', list[0])
#     print('se retornara en esta funcion', list[1])
#     return list[1]

# # print('ingrese una lista con dos elementos')
# # lista = input() consultar


# imprimirVolver([1, 2])

# # 3 Primero + largo


# def primeroLargo(list):
#     a = list[0] + len(list)
#     print('el resultado es', a)


# primeroLargo([1, 5])

# # 4 Valores mayores que el segundo

# def mayorSegundo(list):
#     x = []
#     if len(list) < 2:
#         print(False)
#         return False
#     else:
#         for i in range(0,len(list)):
#             if i == 0:
#                 continue
#             elif list[i]<list[i-1]:
                
#                 x.append(list[i-1])
#                 print(x)
#         print('la lista contiente',len(x),'elementos')
#         return x
        


            

# mayorSegundo([5,2,3,2,1,4])
# # mayorSegundo([1,2])
# mayorSegundo([2])

#5 largo valor
def largo_valor(largo,valor):
    x=[]
    for i in range(0,largo):
        x.append(valor)
    print(f'la lista solicitada es: {x} ')

print('ingrese un numero')
valor = int(input())
print('ingrese el tamaño de la lista')
largo = int(input())

largo_valor(largo,valor)
