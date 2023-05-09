print('++++Evaluacion de polinomio++++')
print('Ingrese SOLO NUMEROS, NO HAY VALIDACION DE ENTRADA')
n=int(input('Ingrese n: '))
x=float(input('Ingrese x: '))

sumatoria = 0
coheficientes=input(f'Ingrese {n} coheficientes separados por espacios:\n').split()
res = 0
def hornet(ant,i):
    global sumatoria
    if i==0: ant = 0
    if i>=n: return
    sumatoria=ant+float(coheficientes[i])
    
    print('Iteracion #: ',i, 'suma:\t',res)
    res = sumatoria * x
    i+=1
    hornet(res,i)
hornet(0,0)
print('Resultado: ',sumatoria)

# for i in range(n):
#     a=float(input(f'Ingrese el valor de a_{i}'))
#     res=a*(x**i)
#     print('Resultado de esta iteracion:',res)
#     sumatoria += res 
# print('El resultado final es:\t',sumatoria)