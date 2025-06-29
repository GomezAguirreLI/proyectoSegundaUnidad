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
    borrarPantalla()
    opcion=True
    while opcion:
        try:
            print("\n\t.::Sistema informatico de una libreria::.\n 1.-Agregar \n 2.-Mostrar \n 3.-Modificar \n 4.Eliminar libro \n 5.Salir")
            opcion=int(input("\tElige una opcion: "))

            match opcion:
                case 1:
                    print("Agregar") 
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
    

    