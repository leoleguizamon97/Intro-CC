import numpy
import os

#Variables
listaCoordenadas=[]
listaDistancias=[]
listaDistancias2=[]
principal = []

#Funciones
dis = lambda a,b,c,d : numpy.sqrt((a-c)**2 + (b-d)**2)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def validarDecimal(val):
	try:
		x = float(val)
	except ValueError: 
		return False
	return True

def validarCoordenadas(val):
	error = False
	for a in val.split():
		#Valida el formato
		if ',' in a:
			x,y = a.split(',')
			if (not validarDecimal(x)) or (not validarDecimal(y)):
				print(f'\tCoordenada no valida. Intente nuevamente [No es un numero:{a}]')
				error = True
		else:
			print(f'\tCoordenada no valida. Intente nuevamente [No cumple con el formato:{a}]')
			error = True
	return error

def ingresoDatos():
	#Recoge la lista de coordenadas
	global listaCoordenadas
	global principal
	while True:
		clear()
		print('\t-----------------------------------------------')
		cadena = input('\tIngrese una lista de coordenadas.\n\tCada una separada por espacios ( ) y comas (,) \n\tpara separar los valores\n\tPor ejemplo: "1,1 1.5,2.65 2,6"\n\t> ')
		error = False

		if len(cadena.split()) <= 1:
			print('\tIngrese mas de una coordenada. Intente nuevamente')
			error = True
		else:
			error = validarCoordenadas(cadena)

		if not error:
			listaCoordenadas = cadena.split()
			#print(listaCoordenadas)
			break
		input('\n\t[Enter para continuar]')
	while True:
		clear()
		print('\t-----------------------------------------------')
		cadena = input('\tAhora ingrese las dos coordenadas principales:\n\t> ')
		if len(cadena.split()) != 2:
			print('\tIngrese DOS coordenadas. Intente nuevamente')
			error = True
		else:
			error = validarCoordenadas(cadena)
			if not error:
				principal = cadena.split()
				break
		input('\n\t[Enter para continuar]')

def distancia():
	global principal
	global listaCoordenadas
	global listaDistancias
	global listaDistancias2

	#0= distancia 1=id punto 2= distancia2 3=id punto2
	resultado=[0,-1,0,-1]
	#Inicializa el punto principal
	a,b = principal[0].split(',')
	x1 = float(a)
	y1 = float(b)
	#Hace una comparacion con un punto para obtener un valor estandar real
	a1,b1 = listaCoordenadas[0].split(',')
	x2 = float(a1)
	y2 = float(b1)		
	minDis = dis(x1,y1,x2,y2)
	#Compara con todos los demas puntos
	for punto in listaCoordenadas:
		a1,b1 = punto.split(',')
		x2 = float(a1)
		y2 = float(b1)		
		x = dis(x1,y1,x2,y2)
		listaDistancias.append(x)
		if  x <= minDis:
			minDis = x
			#Los guardamos para enviarlos
			resultado[0]=minDis
			resultado[1]=listaCoordenadas.index(punto)
	#Ahora lo mismo con el punto2
	#Inicializa el punto principal
	a,b = principal[1].split(',') #Solo cambia esta linea. Por tiempo no hago una funcion
	x1 = float(a)
	y1 = float(b)
	#Hace una comparacion con un punto para obtener un valor estandar real
	a1,b1 = listaCoordenadas[0].split(',')
	x2 = float(a1)
	y2 = float(b1)		
	minDis2 = dis(x1,y1,x2,y2)
	#Compara con todos los demas puntos
	for punto in listaCoordenadas:
		a1,b1 = punto.split(',')
		x2 = float(a1)
		y2 = float(b1)		
		x = dis(x1,y1,x2,y2)
		listaDistancias2.append(x)
		if  x <= minDis2:
			minDis2 = x
			#Los guardamos para enviarlos
			resultado[2]=minDis2
			resultado[3]=listaCoordenadas.index(punto)
	return resultado
#Main
clear()
print('\t-----------------------------------------------')
print('\tEste programa le permite calcular la minima')
print('\tdistancia entre una lista de puntos y uno dado.\n')
print('\tRetornará la cordenada mas cercana al punto, ')
print('\ttambien le permitira ver la distancia a todos')
input('\tlos demas puntos. :D [Enter para continuar]\n\t> ')
while True:
	ingresoDatos()
	print('\t-----------------------------------------------')
	res = distancia()
	clear()
	print(f'\tP1: La menor distancia es:\t{"{:.3f}".format(res[0])}\n\tLa coordenada correspondiente es la numero: {res[1]+1} [{listaCoordenadas[res[1]]}]')
	print(f'\tP2: La menor distancia es:\t{"{:.3f}".format(res[2])}\n\tLa coordenada correspondiente es la numero: {res[3]+1} [{listaCoordenadas[res[3]]}]')
	print(f'\tLista de distancias y sus puntos.\n\t Puntos:[{principal[0]} | {principal[1]}]')
	puntos		= ''
	distancias	= ''
	distancias2 = ''
	for p in listaCoordenadas:	puntos		+= '\t'+ str(p)
	for d in listaDistancias:	distancias	+= '\t'+ str("{:.3f}".format(d))
	for d2 in listaDistancias2:	distancias2	+= '\t'+ str("{:.3f}".format(d2))
	print(f'Puntos: {puntos}')
	print(f'DistanciaP1: {distancias}')
	print(f'DistanciaP2: {distancias2}')
	if input('\tPresione enter para salir o [c / C] para usar el\n\tprograma de nuevo\n\t> ').lower() != 'c':
		break
	listaCoordenadas.clear
	listaDistancias.clear
	principal = ''