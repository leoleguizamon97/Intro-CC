#Eneagono
import numpy as nu
#Funciones
def area(n,r):
	a=((n*r**2*nu.sin((2*nu.pi)/n))/2)
	return a
def perimetro(n,r):
	angulo=nu.pi*2/n
	print(nu.sqrt( (r**2) + (r**2) - (2*(r*r)*nu.cos(angulo))))
	p=nu.sqrt( (r**2) + (r**2) - (2*(r*r)*nu.cos(angulo)))*n
	return p 
#Ciclo principal
while True:
	lados		= int(input('Ingrese la cantidad de lados:\n> '))
	distancia	= float(input('Ingrese la distacncia del centro a uno de sus vertices (radio):\n> '))
	print(f'N-agono de {lados}:')
	print(f'\tEl area es de: {area(lados,distancia)}')
	print(f'\tEl perimetro es de: {perimetro(lados,distancia)}')
	if input('¿Desea ingresar otro angulo? [Enter: si] [X: Salir]\n> ').lower() == 'x': break