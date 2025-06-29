"""
Sistema que maneje la base de datos de una libreria (la del calvario)

vamos a dividir todo por diccionarios, cada libro debe tener: nombre,genero,cantidad de pagina,autor


libro={
    "Nombre":"",
    "Autor":"",
    "Genero":"":,
    "cantidad de paginas":"",
}
"""

import os
#Platform es para ver que sistema se esta usando
import platform



#Pues aca guardamos el libro en si
libro={}
#Y aqui estamos guardando los libros dentro de una lista
libros=[]

def borrarPantalla():
    #Guardo el nombre del sistema
    sistema=platform.system()
    print(sistema)
    match sistema:

        case "Linux":
            os.system("clear")
        case "Windows":
            os.system("cls")
        case _:
            os.system("clear")
    

def esperarTecla():
    input("\n\t.::Ingrese cualquier tecla para continuar::.")

def menuPrincipal():
    opcion=True
    while opcion:
        try:
            borrarPantalla()

            print("\n\t.::Sistema informatico de una libreria::.\n 1.-Agregar \n 2.-Mostrar \n 3.-Modificar \n 4.Eliminar libro \n 5.Salir")
            opcion=int(input("\tElige una opcion: "))

            match opcion:
                case 1:
                    agregarLibros()
                case 2:
                    mostrarLibros()
                case 3:
                    modificarLibro()
                case 4:
                    print("")
                case 5:
                    print("\n\t..::SALIENDO DEL SW::..")
                    opcion=False
                case _:
                    print(".::Escoje una opción valida")    
        except ValueError:
            print(".::Ingrese un dato numerico::.")

            esperarTecla()
    

def agregarLibros():
    borrarPantalla()
    print("\n\t.:: Alta de Libros ::.\n ")
    nuevo_libro = {}
    nuevo_libro["nombre"] = input("Ingresa el nombre del libro :").upper()
    nuevo_libro["categoria"] = input("Ingresa la categoria del libro: ").upper()
    nuevo_libro["genero"] = input("Ingresa el genero del libro :").upper()
    nuevo_libro["idioma"] = input("Ingresa el idioma :").upper()
    nuevo_libro["Cantidad de paginas"] = input("Ingrese la cantidad de paginas del libro: ").upper()
    nuevo_libro["estanteria"] = input("Ingrese la estanteria donde va a ser guardado :").upper()
    libros.append(nuevo_libro)
    print("..::OPERACION EXITOSA::..")
    esperarTecla()

def mostrarLibros():
    borrarPantalla()
    print("\n\t.::Mostrar libros guardados::.\n")
    if len(libros) > 0:
        for idx, libro in enumerate(libros, 1):
            print(f"\nLibro #{idx}:")
            for clave, valor in libro.items():
                print(f"\t{clave}: {valor}")
        esperarTecla()
    else:
        print("\n\t.::NO HAY LIBROS GUARDADOS::.\n")
        esperarTecla()

def modificarLibro():
    borrarPantalla()
    print("\n\t.::Modificar características del libro::.\n")
    if len(libro) >0:
       continua=True
       while continua:
        print("Características actuales:")
        for idx,libro in enumerate(libros):
                print(f"{idx}.{libro['nombre']}")       


       
         
    else:
        print("\n\t.::NO HAY LIBROS GUARDADOS::.\n")
        esperarTecla()
        return
    
    esperarTecla()