'''Con este concepto de parámetros predeterminados en mente, el objetivo de esta asignación es escribir una sola función, randInt() que tome hasta 2 argumentos.

Si no se proporcionan argumentos, la función debería devolver un entero aleatorio entre 0 y 100.
Si solo se proporciona un número máximo, la función debe devolver un número entero aleatorio entre 0 y el número máximo.
Si solo se proporciona un número mínimo, la función debe devolver un número entero aleatorio entre el número mínimo y 100
Si se proporcionan un número mínimo y máximo, la función debe devolver un número entero aleatorio entre esos 2 valores.
Aquí hay un par de notas importantes sobre el uso de random.random () y round(). (Crea esta función sin usar random.randInt () - ¡estamos tratando de construir ese método nosotros mismos para esta tarea!)

random.random() devuelve un número flotante aleatorio entre 0.00 y 1.00
random.random() * 50 devuelve un número flotante aleatorio entre 0.00 y 50.99
random.random() * 25 + 10 devuelve un número flotante aleatorio entre 10.00 y 35.99
round(num) devuelve el valor entero redondeado de num'''
import random
def randint(min = 0, max = 100):
    if min == 0:
        num = round(max*(random.random()))
        print(num)
        return num
    else:
        num = round((max-min)*(random.random())+min)
        print(num)
        return num

randint(max=3)
randint(min = 97)
randint(3,5)

