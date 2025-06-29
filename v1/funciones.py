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



#Pues en si los libros 
libros={}



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
                    print("f")
                case 3:
                    print("")    
                case 4:
                    print("")
                case 5:
                    print("")
                case _:
                    print(".::Escoje una opción valida")    
        except ValueError:
            print(".::Ingrese un dato numerico::.")

            esperarTecla()
    

def agregarLibros():
    borrarPantalla()
    print("\n\t.:: Alta de Peliculas ::.\n ")
    libros.update({"nombre":input("Ingresa el nombre del libro :").upper()})
    libros.update({"categoria":input("Ingresa la categoria:del libro: ").upper()})
    libros.update({"genero":input("Ingresa el genero del libro :").upper()})
    libros.update({"idioma":input("Ingresa el idioma :").upper()})
    libros.update({"Cantidad de paginas":input("Ingrese la cantidad de paginas del libro: ").upper()})
    print("..::OPERACION EXITOSA::..")

    esperarTecla()