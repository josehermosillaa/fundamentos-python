'''Básico : imprime todos los enteros del 0 al 150.
Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
Cuenta regresiva por cuatro : imprime números positivos a partir de 2018, cuenta atrás por cuatro.
Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)'''

# Basico
for i in range(0, 151):
    print(i)

# Múltiplos de cinco
for cinco in range(0, 1001, 5):
    print(cinco)

# Contar, Dojo Way
for i in range(1, 101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)
'''Nota al pie debe ponerse la condición i%10==0 primero para no tener problemas'''

# Uf, eso es bastante grande
x = 0
for i in range(0, 500001):
    if i % 2 != 0:
        x = x+i
        # print(x)
print('La suma es:', x)

# Cuenta regresiva por 4
for i in range(2018, 0, -4):
    print('contando', i)

# Contador Flexible (lowNum,highNum,mult)


def contadorFlex(lowNum, highNum,mult):
    x=mult
    for i in range(lowNum, highNum):
        if i % mult == 0:
            print(i)


print('ingrese el numero inicial (numero mas bajo)')
lowNum = int(input())
print('ingrese el numero final')
highNum = int(input())+1
print('ingrese el multiplo requerido')
mult = int(input())
contadorFlex(lowNum, highNum, mult)
# sin funcion habria que definir directamente en el for

