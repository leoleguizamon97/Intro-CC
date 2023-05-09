import numpy
#Por practicidad los escarabajos serán referenciados como personas, al igual que en el txt jajaja
def promedio(lista):
    suma = 0
    for p in lista:
        suma += p
    promedio = suma/len(lista)
    return promedio

def desvEstandar(lista,pr=0):
    if pr==0:pr=promedio(lista)
    n = len(lista)
    suma = 0
    for a in lista:
        s=(a-pr)**2
        suma += s
    resultado = suma/n
    return numpy.sqrt(resultado)

medidas		= open('Longitudes.txt','w+')
resultado	= open('Resultados.txt','w+')
i=0
print('Ingrese los datos de los escarabajos. SOLO la longitud!')
while True:
    i+=1
    lon = float(input(f'Escarabajo #{i}: '))
    medidas.write(f'Escarabajo#{i}_{lon}\n')
    if input('Desea agregar mas escarabajos?: [n: no] [Enter: Añadir mas]') == 'n': break
medidas.close()
medidas	= open('Longitudes.txt','r+')

personas	= medidas.readlines()
alturas		= []
#print(personas)

for p in personas:
    p=p.replace('\n','').split('_')
    alturas.append(float(p[1]))
    

pr=promedio(alturas)
de=desvEstandar(alturas,pr)

print(f'Promedio:\t{"{:.4f}".format(pr)}')
print(f'Desv Estandar:\t{"{:.4f}".format(de)}')
print(alturas)

resultado.write(f'El promedio de las longitudes de los escarabajos es: {"{:.4f}".format(pr)} y la desviación estándar es: {"{:.4f}".format(de)}')
    