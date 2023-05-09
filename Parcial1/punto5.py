#menu Entrada, PlatoPrincipal, Bebida y Postre.
cantidadMenus = int(input("Ingrese la cantidad de menus que desea: "))
menuBase = {"Entrada":"","Plato principal":"","Bebida":"","Postre":"",}
restaurante = {}
for i in range(cantidadMenus):
    menu = {}
    print(f"Ahora ingresará los elementos del menu {i+1}")
    for clave in menuBase:
        elemento = input(f"Ingrese el/la {clave} del menu {i+1}: ")
        menu[clave] = elemento
    nombreMenu = "Menu " + str(i+1)
    restaurante[nombreMenu] = menu

print(f"Acá todos los menus: \n {restaurante}")