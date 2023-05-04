import numpy

#main
cordenadas = []

while True:
    #Obtenemos las cordenadas, solicitamos un formato
	print('Ingrese las cordenadas separadas por un espacio, use puntos para las cifras decimales:\n Ejemplo: 1.5 2.5')
	contador = 0
	while True:
		cadena = input(f'ingrese la cordenada numero {contador}: \t')
		contador+=1
		try:
			val1, val2 = cadena.split()
		except ValueError: print()