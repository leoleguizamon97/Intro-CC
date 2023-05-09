ingreso = open('Conjuntos.txt','w+')

cantidadConjuntos=int(input('Ingrese la cantidad de conjuntos: '))
#ingreso de datos
for i in range(cantidadConjuntos):
	print(f'Ingrese los elementos del conjunto {i} separados por un espacio:')
	l1=input(('> '))
	ingreso.write(f'{l1}\n')
#se cierra el archivo para reiniciar la ubicacion del puntero
ingreso.close()
archivo	= open('Conjuntos.txt','+r')

numeros = archivo.readlines()
lineas = []
conjuntos = []
#Guarda todos los conjuntos en un arreglo
for p in numeros:
	linea=p.replace('\n','').split()
	nuevoConjunto = set()
	for a in linea: nuevoConjunto.add(a)
	conjuntos.append(nuevoConjunto)

union = conjuntos[0]
interseccion = conjuntos[0]

for a in conjuntos:
    union = union | a
    interseccion = interseccion & a

print(f"Union {sorted(union)}, Interseccion {sorted(interseccion)}")
