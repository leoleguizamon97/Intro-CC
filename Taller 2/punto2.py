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
		cadena = input('Ingrese una lista de coordenadas.\nCada una separada por espacios ( ) y comas (,) para separar los valores\nPor ejemplo: "1,1 1.5,2.65 2,6"\n> ')
		error = False
		if len(cadena.split()) <= 1:
			print('Ingrese mas de una coordenada. Intente nuevamente')
			error = True
		else:
			for a in cadena.split():
				#Valida el formato
				if ',' in a:
					x,y = a.split(',')
					if (not validarDecimal(x)) or (not validarDecimal(y)):
						print(f'Cadena de coordenadas no valida. Intente nuevamente [No es un numero:{a}]')
						error = True
				else:
					print(f'Cadena de coordenadas no valida. Intente nuevamente [No cumple con el formato:{a}]')
					error = True
		if not error:
			listaCoordenadas = cadena.split()
			#print(listaCoordenadas)
			break	
		input()
#Main
ingresoDatos()