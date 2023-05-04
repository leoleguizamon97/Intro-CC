import numpy

#main
coordenadas = []

def validarDecimal(val):
	try:
		x = float(val)
	except ValueError: 
		return False
	return True

while True:
    #Obtenemos las cordenadas, solicitamos un formato
	print('Ingrese las cordenadas separadas por un espacio, use puntos para las cifras decimales:\n Ejemplo: [x,y] = 1.5 2.5')
	contador = 1
	while True:
		cadena = input(f'Ingrese la cordenada numero {contador}: \t')
		try:
			#Validamos ingreso
			val1, val2 = cadena.split()
			#Validamos si lo ingresado es un numero
			x = validarDecimal(val1)
			y = validarDecimal(val2)
			#Agregamos a la lista o solicitamos de nuevo
			if x and y:
				contador+=1
				coordenadas.append(cadena)
				#Pregunta si quiere seguir agregando
				if contador > 2:
					agregar = input('¿Desea agregar mas coordenadas? [n: para no agregar mas] [Enter para continuar]: ')
					print(agregar.lower())
					if agregar.lower() == 'n':
						break
			else:
				print('El valor ingresado no es un numero! Intente nuevamente.')
			
		except ValueError:
			print('La cadena no contiene dos valores exactos. Intente nuevamente')