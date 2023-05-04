import numpy

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

medidas		= open('./Alturas.txt','+r')
resultado	= open('./Resultados.txt','w+')
personas	= medidas.readlines()
alturas		= []

for p in personas:
    p=p.replace('\n','').split('_')
    alturas.append(float(p[1]))

pr=promedio(alturas)
de=desvEstandar(alturas,pr)

print(f'Promedio:\t{"{:.4f}".format(pr)}')
print(f'Desv Estandar:\t{"{:.4f}".format(de)}')
print(alturas)

resultado.write(f'El promedio de las altura de las personas es: {"{:.4f}".format(pr)} y la desviación estándar es: {"{:.4f}".format(de)}')
    