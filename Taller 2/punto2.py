import numpy

#Variables
listaCoordenadas=[]
listaDistancias=[]
principal = ''

#Funciones
def validarDecimal(val):
	try:
		x = float(val)
	except ValueError: 
		return False
	return True

def ingresoDatos():
	#Recoge la lista de coordenadas
	error = False
	while True:
		cadena = input('Ingrese una lista de coordenadas.\nCada una separada por espacios ( ) y comas (,) para separar los valores\nPor ejemplo: "1,1 1.5,2.65 2,6"\n> ')
		
		if len(cadena.split()) <= 1:
			print('Ingrese mas de una coordenada. Intente nuevamente')
		else:
			for a in cadena.split():
				#Valida el formato
				if ',' in a:
					x,y = a.split(',')
					if (not validarDecimal(x)) and (not validarDecimal(y)): error=True
				else:
					error = True
			
			if not error:
				listaCoordenadas = cadena.split()
				print(listaCoordenadas)
				break
			else: print(f'Cadena de coordenadas no valida. Intente nuevamente [Error en:{a}]')
#Main
ingresoDatos()