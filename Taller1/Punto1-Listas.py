#Presentacion
print("A continuacion ingrese tantas palabras como desee")
print("Despues de cada palabra se le preguntara si desea ingresar mas \n")

#Variables
contador = 0
validador = 0
listaPalabras = []
respuesta = ""

#Ciclo de agregar
while(validador==0):
    #Solicita la palabra
    contador += 1
    palabra = input(f"Ingrese la palabra numero {contador}: ")

    #Agrega a la lista   
    listaPalabras.append(palabra)
    
    #Valida intencion de usuario
    continuar = input("¿Desea ingresar otra palabra? (n): ")
    if continuar == "n" or continuar == "N":
        validador = -1

#Ciclo para validar longitud
for a in listaPalabras:
    #VAlida el tamaño
    if len(a) >= 3:
        respuesta = respuesta + a + " "

#Mostrar resultados
print(respuesta)