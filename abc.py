libro = input("escribe el nombre del libro")
paginas = input("escribe la cantidad de paginas")
paginas_leidas = input("escribe la cantidad de paginas leidas")

paginas_restantes = int(paginas) - int(paginas_leidas)
print("Te faltas para terminar de leer" + paginas_restantes + "páginas")

