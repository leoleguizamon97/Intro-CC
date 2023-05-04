import numpy

#Variables
coordenadas = []

#Funciones
def validarDecimal(val):
	try:
		x = float(val)
	except ValueError: 
		return False
	return True

def ingresoDatos():
	contador = 1
	while True:
		cadena = input(f'Ingrese la cordenada numero {contador}: \t')
		#Validamos ingreso
		try:
			val1, val2 = cadena.split()
			#Validamos si lo ingresado es un numero
			x = validarDecimal(val1)
			y = validarDecimal(val2)
			#Agregamos a la lista o solicitamos de nuevo
			if x and y:
				contador+=1
				coordenadas.append(cadena)
			#Pregunta si quiere seguir agregando (Despues de agregar dos coordenadas)
				if contador > 2:
					agregar = input('¿Desea agregar mas coordenadas? [n: para no agregar mas] [Enter para continuar]: ')
					if agregar.lower() == 'n':
						break
			else:
				print('El valor ingresado no es un numero. Intente nuevamente.')
		except ValueError:
			print('La cadena no contiene dos valores exactos. Intente nuevamente')

def distancia():
	maxDis=0
	#0= distancia 1=id punto1 2=id punto2
	puntos=[maxDis,-1,-1]
	#Funcion lambda solicitada
	dis = lambda a,b,c,d : numpy.sqrt((a-c)**2 + (b-d)**2)
	for i in range(len(coordenadas)-1):
		punto1 = coordenadas[i]
		punto2 = coordenadas[i+1]

		a1,b1 = punto1.split()
		a2,b2 = punto2.split()

		x1 = float(a1)
		y1 = float(b1)
		x2 = float(a2)
		y2 = float(b2)
		
		x = dis(x1,y1,x2,y2)
		if  x > maxDis:
			maxDis = x
			#Los guardamos para enviarlos
			puntos[0]=maxDis
			puntos[1]=i
			puntos[2]=i+1
	
	return puntos

#main
while True:
	#Informamos funcion del programa
	print('█===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O█\n')
	print('Este programa determinará cual es el segmento mas largo de un camino polinomial')
	print('teniendo en cuenta unicamente los puntos contiguos en el trayecto\n')
	print('█===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O===O█\n')
    #Obtenemos las cordenadas, solicitamos un formato
	print('Ingrese las cordenadas separadas por un espacio, use puntos para las cifras decimales:\n Ejemplo: [x,y] = 1.5 2.5\n')
	ingresoDatos()
	#Calcular distancias
	res = distancia()
	print(f'La distancia maxima es: ')
	print(f'{res[0]}\nEntre los puntos #{res[1]+1} [{coordenadas[res[1]]}] y #{res[2]+1} [{coordenadas[res[2]]}]')
	agregar = input('¿Desea Salir? [s: Para salir] [Enter para ingresar mas caminos]: ')
	if agregar.lower() == 's': break
	coordenadas.clear()
	