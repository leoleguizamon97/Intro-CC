import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Funcion
def recursiva(rep,itr=0,a3=0,a2=0,a1=0):#(repeticiones,iteracion,suma,n-2,n-1)
    if itr == 0:
        print(1)
        recursiva(rep,itr+1)
    elif itr == 1:
        print(1)
        recursiva(rep,itr+1)
    elif itr == 2:
        print(5)
        recursiva(rep,itr+1,1,1,5)
    else:
        suma = a1 + a2 + a3 + 3
        a3 = a2
        a2 = a1
        print(suma)
        if rep>=itr: recursiva(rep,itr+1,a3,a2,suma)
        
    

#Main
clear()
recursiva(10)