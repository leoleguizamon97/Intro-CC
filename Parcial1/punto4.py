#Presentacion
print("Ingrese un texto a continuacion, se contaran vocales y consonantes")

#Variables
cadena =  input()
contadorVocales = 0 
contadorConsonantes = 0
#Ciclos
for caracter in cadena:
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        contadorVocales     += 1
    elif caracter == " ":
      #solo es un espacio
      1+1
    else:
        contadorConsonantes += 1
#Mostrar resultados
print(f"El número de vocales en la oración es {contadorVocales} y el de consonantes es {contadorConsonantes}.")