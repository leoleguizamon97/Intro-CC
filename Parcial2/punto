#Presentacion
print("Se imprimira un rombo tan ancho como lo especifique.")
#Variables
ancho = int(input("Ingrese el ancho del rombo: "))
alto = ancho
ancho = (ancho * 2) -1
cuadrado = []
triangulo = []

#Creacion de cuadrado

for j in range(alto):
    cadena = ""
    for i in range(ancho):
        if i % 2 != 1:
            cadena = cadena + "*"
        else:
            cadena = cadena + " "
    cuadrado.append(cadena)

#Creacion del triangulo
for j in range(alto):
    cadena = ""
    contador = 0
    i = 0
    while(contador!=-1):
        i +=1 
        if i % 2 != 1:
            cadena = cadena + "*"
            contador +=1
            if contador == j+1:
                contador = -1
        else:
            cadena = cadena + " "

    cadena = cadena.center(ancho+1," ") 
    triangulo.append(cadena)

#Mostrar resultados

for a in range(alto):
    s  = triangulo[a] +" "+ cuadrado[a]
    print(s)