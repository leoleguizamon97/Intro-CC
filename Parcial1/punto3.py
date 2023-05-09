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

#Ciclo para validar 

for a in listaPalabras:
    contadorVocales = 0 
    contadorConsonantes = 0
    tamaño = 0
    for caracter in a:
        tamaño += 1
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
            contadorVocales += 1
        elif caracter == " ":
            #solo es un espacio
            1+1
        else:
            contadorConsonantes += 1
    if contadorVocales == 3 and tamaño >= 6:
        respuesta = respuesta + a + " "

#Mostrar resultados
print(respuesta)