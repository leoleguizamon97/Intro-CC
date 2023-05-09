import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Funcion
def recursiva(rep,itr=0,a4=0,a3=0,a2=0,a1=0):#(repeticiones,iteracion,suma,n-2,n-1)
    if itr == 0:
        print(1)
        recursiva(rep,itr+1)
    elif itr == 1:
        print(-1)
        recursiva(rep,itr+1)
    elif itr == 2:
        print(-3)
        recursiva(rep,itr+1)
    elif itr == 3:
        print(7)
        recursiva(rep,itr+1,1,-1,-3,7)
    else:
        suma = a1 + a2 + a3 + a4 + 2
        a4 = a3
        a3 = a2
        a2 = a1
        print(suma)
        if rep>=itr: recursiva(rep,itr+1,a4,a3,a2,suma)
#Main
clear()
#Este primer argumento define la cantidad de repeticiones
recursiva(10)