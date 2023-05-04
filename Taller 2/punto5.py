def corte(m1, b1, m2, b2):
    if (m1 - m2) == 0: return [False,0,0]
    x = (b2 - b1) / (m1 - m2)
    y = m1*x + b1
    return [True,x,y]

rectas		= open('Rectas.txt','+r')
resultado	= open('Resultados.txt','w+')

numeros = rectas.readlines()
lineas = []

for p in numeros:
    p=p.replace('\n','').split()
    recta = [float(p[0]),float(p[1]),float(p[2])]
    lineas.append(recta)
print(lineas)
a=lineas[0][0]
b=lineas[0][1]
c=lineas[0][2]
d=lineas[1][0]
e=lineas[1][1]
f=lineas[1][2]

m1 = a/b
b1 = -(c/b)
m2 = d/e
b2 = -(f/e)

resultado = corte(m1,b1,m2,b2)
print(resultado)

if resultado[0]:
    print(f'Las rectas {a}x+{b}y={c} y {d}x+{e}y={f} se cortan en el punto ({"{:.4f}".format(resultado[1])},{"{:.4f}".format(resultado[2])}).')
else:
    print('Las rectas {a}x+{b}y={c} y {d}x+{e}y={f} no se cortan y por lo tanto son paralelas.')
