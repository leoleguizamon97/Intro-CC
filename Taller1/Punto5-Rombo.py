#Presentacion
print("Se imprimira un rombo tan ancho como lo especifique.")
#Variables
ancho = int(input("Ingrese el ancho del rombo: "))
ancho = (ancho * 2) -1
matriz = []

#Creacion de matriz base
for i in range(ancho):
    fila = []
    for j in range(ancho):
        fila.append("0")
    matriz.append(fila)

#Creacion de rombo
for i in range(ancho):
    for j in range(i):
        matriz[j][int(ancho/2)] = ' '

#Mostrar resultados
for a in matriz:
    print(a)