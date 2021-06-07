# 1. TAREA: imprimir "Hola mundo"
print("Hola Mundo")
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Jose!"
print("Hola",name )	# con una coma
print( "Hola "+name )	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
name = 25
print( "Hola",name,"!" )	# con una coma
print( "Hola "+ str(name)+"!" )	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
z="Me encanta comer {} y {}." .format(fave_food1, fave_food2)
print( "Me encanta comer {} y {}." .format(fave_food1, fave_food2) ) # con .format()
print( f"Me encanta comer {fave_food1} y {fave_food2}" ) # con una cadena f
print(z.upper())