cantidadLibros = int(input("Ingrese la cantidad de Libros que desea: "))
libroBase = {"Titulo":"","Autor":"","Año":"","Editorial":"",}
biblioteca = {}
for i in range(cantidadLibros):
    libro = {}
    print(f"Ahora ingresará los elementos del libro {i+1}")
    for clave in libroBase:
        elemento = input(f"Ingrese el/la {clave} del libro {i+1}: ")
        libro[clave] = elemento
    nombrelibro = "libro " + str(i+1)
    biblioteca[nombrelibro] = libro

print(f"Acá todos los libros: \n {biblioteca}")