import numpy
import os

#Variables
listaCoordenadas=[]
listaDistancias=[]
principal = ''

#Funciones
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

def ingresoDatos():
	#Recoge la lista de coordenadas
	while True:
		clear()
		print('\t-----------------------------------------------')
		cadena = input('\tIngrese una lista de coordenadas.\n\tCada una separada por espacios ( ) y comas (,) \n\tpara separar los valores\n\tPor ejemplo: "1,1 1.5,2.65 2,6"\n\t> ')
		error = False
		if len(cadena.split()) <= 1:
			print('\tIngrese mas de una coordenada. Intente nuevamente')
			error = True
		else:
			for a in cadena.split():
				#Valida el formato
				if ',' in a:
					x,y = a.split(',')
					if (not validarDecimal(x)) or (not validarDecimal(y)):
						print(f'\tCadena de coordenadas no valida. Intente nuevamente [No es un numero:{a}]')
						error = True
				else:
					print(f'\tCadena de coordenadas no valida. Intente nuevamente [No cumple con el formato:{a}]')
					error = True
		if not error:
			listaCoordenadas = cadena.split()
			#print(listaCoordenadas)
			break	
		input('\t[Enter para continuar]')
#Main
clear()
print('\t-----------------------------------------------')
print('\tEste programa le permite calcular la minima')
print('\tdistancia entre una lista de puntos y uno dado.\n')
print('\tRetornará la cordenada mas cercana al punto, ')
print('\ttambien le permitira ver la distancia a todos')
input('\tlos demas puntos. :D [Enter para continuar] ')
while True:
	ingresoDatos()
	print('\t-----------------------------------------------')
	if input('Presione enter para salir o [c / C] para usar el\nprograma de nuevo').lower() != 'c':
		break
	listaCoordenadas.clear
	listaDistancias.clear
	principal = ''