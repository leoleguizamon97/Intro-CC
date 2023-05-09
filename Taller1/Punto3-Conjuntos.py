#Presentacion
print("Primero ingrese los dos conjuntos numericos, despues se mostrara \nlas diferentes operaciones entre los conjuntos dados")
#Variables
conjunto1 = set()
conjunto2 = set()
contador = 0

#Ciclo conjunto 1
print("Ingrese los elementos del conjunto 1")
while(contador != -1):
    contador += 1
    conjunto1.add(int(input(f"Ingrese el elemento NUMERICO #{contador}: ")))
    #Valida intencion de usuario
    continuar = input("¿Desea ingresar otra palabra? (n): ")
    if continuar == "n" or continuar == "N":
        contador = -1

#Ciclo conjunto 2
print("Ingrese los elementos del conjunto 2")
contador = 0
while(contador != -1):
    contador += 1
    conjunto2.add(int(input(f"Ingrese el elemento NUMERICO #{contador}: ")))
    #Valida intencion de usuario
    continuar = input("¿Desea ingresar otra palabra? (n): ")
    if continuar == "n" or continuar == "N":
        contador = -1
print(conjunto1)
print(conjunto2)

#Calculo operaciones
z=conjunto1 | conjunto2     #Union
w=conjunto1&conjunto2       #Interseccion
v=conjunto1-conjunto2       #Diferencia
t=conjunto1^conjunto2       #Diferencia simetrica

#Mostrar resultados
print(f"Union {z}, Interseccion {w}, Dif. Simetrica {t} ")