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
libro={}



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
    print("\n\t.:: Alta de Peliculas ::.\n ")
    libro.update({"nombre":input("Ingresa el nombre del libro :").upper()})
    libro.update({"categoria":input("Ingresa la categoria:del libro: ").upper()})
    libro.update({"genero":input("Ingresa el genero del libro :").upper()})
    libro.update({"idioma":input("Ingresa el idioma :").upper()})
    libro.update({"Cantidad de paginas":input("Ingrese la cantidad de paginas del libro: ").upper()})
    libro.update({"estanteria":input("Ingrese la estanteria donde va a ser guardado :").upper()})

    print("..::OPERACION EXITOSA::..")

    esperarTecla()

def mostrarLibros():
    borrarPantalla()
    print("\n\t.::Mostrar libros guardados::.\n")
    if len(libro)>0:
        for i in libro:
            print(f"\t {i}:{libro[i]}")
        esperarTecla()

    else:
        print("\n\t.::NO HAY LIBROS GUARDADOS::.")

def modificarLibro():
    borrarPantalla()
    print("\n\t.::Modificar características del libro::.\n")
    if len(libro) >0:
       continua=True
       while continua:
        print("Características actuales:")
        for i, (clave, valor) in enumerate(libro.items(), 1):
            print(f"  {i}. {clave}: {valor}")
        try:
            opcion = int(input("\nElige el número de la característica a modificar (0 para salir): "))
            if opcion == 0:
                continua=False
            claves = list(libro.keys())
            if 1 <= opcion <= len(claves):
                clave = claves[opcion - 1]
                print(f"Valor actual de '{clave}': {libro[clave]}")
                nuevo_valor = input(f"Nuevo valor para '{clave}': ").upper()
                libro[clave] = nuevo_valor
                print("..::MODIFICACIÓN EXITOSA::..\n")
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    else:
        print("\n\t.::NO HAY LIBROS GUARDADOS::.\n")
        esperarTecla()
        return
    
    esperarTecla()