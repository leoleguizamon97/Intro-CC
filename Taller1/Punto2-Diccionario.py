#Presentacion
print("Debera ingresar el largo de dos listas, despues listar las claves del diccionario \n seguido de los objetos")
#Variables
tamanoListas=int(input("Ingrese la longitud de las listas: "))
listaClaves = []
listaContenido = []
diccionario = {}

#Ciclo datos de claves
print("***Ahora ingrese las claves***")
for i in range(tamanoListas):
    clave = input(f"Ingrese la clave numero {i+1}: ")
    listaClaves.append(clave)

#Ciclo datos de contenido
print("***Ahora ingrese el contenido***")
for i in range(tamanoListas):
    contenido = input(f"Ingrese el contenido numero {i+1}: ")
    listaContenido.append(contenido)

#Creacion de diccionario
print("Ahora se generará el diccionario")
for i in range(tamanoListas):
    diccionario[listaClaves[i]] = listaContenido[i]

#Mostrar resultado
print(f"Este es el diccionario:\n{diccionario}")