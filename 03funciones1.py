#1
def a():
    return 5 #regresa 5
print(a()) #Output = 5

#2
def a():
    return 5 # La funcion retorna 5
print(a()+a()) #Output: 10

#3
def a():
    return 5 #regresa 5 y se acaba la funcion, nunca llega hasta el segundo return
    return 10
print(a()) #Output = 5

#4
def a():
    return 5 #lo mismo que antes, no llega al print por que el return finaliza la función
    print(10)
print(a()) #Output = 5

#5
def a():
    print(5) #imprime 5, la funcion no retorna nada
x = a() #como no retorna nada, deberia salir undefined [None para python]
print(x) #lo mismo que la linea anterior
#output = 5 , None

#6
def a(b,c):
    print(b+c)  #imprime pero no retorna
print(a(1,2) + a(2,3)) 
#Output = 3, 5, None  
# En este caso me dice que los "objetos" del tipo None no pueden usar operadores

#7
def a(b,c):
    return str(b)+str(c) # en este caso la funcion convierte lo que ingresa en string y los concatena
print(a(2,5)) 
#Output = "25"

#8
def a():
    b = 100
    print(b) #imprime 100
    if b < 10: #condicion false
        return 5
    else: #retorna 10
        return 10
    return 7 #se lo salta
print(a()) # imprime 10
#Output = 100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3 #se lo salta por que la funcion termina con el primer return
print(a(2,3)) #imprime 7
print(a(5,3)) #imprime 14
print(a(2,3) + a(5,3)) #imprime 7+14=21

#Output = 7, 14, 21

#10
def a(b,c):
    return b+c
    return 10 #se lo salta
print(a(3,5)) #imprime 8

#Output = 8

#11
b = 500
print(b) #imprime 500
def a():
    b = 300 #este es un nuevo b distinto al anterior
    print(b) #imprime 300
print(b) #imprime 500
a() # llamamos a la funcion 
print(b) #imprime 500

#Output = 500, 500, 300, 500

#12
b = 500
print(b) #imprime 500
def a():
    b = 300
    print(b)
    return b #retorna b
print(b)
a() #retorna b pero no se guardo en una variable para usarlo
print(b)

#Output = 500, 500, 300, 500

#13
b = 500
print(b) #imprime 500
def a():
    b = 300
    print(b)
    return b
print(b) #imprime 500
b=a() #se reasigna el valor de b a 300
print(b) #imprime 300

#Output = 500, 500, 300, 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#por como esta escrita la funcion el output debe ser
#output = 1, 3, 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a() # llama a la funcion y asigna el valor que retorna la funcion a()
print(y) #imprimo ese valor asignado
#Output = 1, 3, 5, 10
