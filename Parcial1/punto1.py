#ciclo recibir conjuntos
numConjuntos = int(input("Ingrese la cantidad de conjuntos: "))

conjuntos = []

for i in range(numConjuntos):
    #Ciclo conjunto 1
    print(f"Ingrese los elementos del conjunto {i+1}")
    conjunto1 = set()
    contador = 0
    while(contador != -1):
        contador += 1
        conjunto1.add(int(input(f"Ingrese el elemento NUMERICO #{contador}: ")))
        #Valida intencion de usuario
        continuar = input("¿Desea ingresar otro elemento? (n): ")
        if continuar == "n" or continuar == "N":
            conjuntos.append(conjunto1)
            contador = -1

#hacemos el ciclo para definir las uniones

union = conjuntos[0]
interseccion = conjuntos[0]

print(union)

for a in conjuntos:
    union = union | a
    interseccion = interseccion & a


#Mostrar resultados
print(f"Union {union}, Interseccion {interseccion}")