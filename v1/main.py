"""
Este es la pagina principal
"""


import funciones
import empleados

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        print("\n\t.::Sistema principal::.\n 1.-Menú de Libros\n 2.-Menú de Empleados\n 3.-Salir")
        try:
            opcion = int(input("\tElige una opción: "))
            match opcion:
                case 1:
                    funciones.menuPrincipal()
                case 2:
                    empleados.menuEmpleados()
                case 3:
                    print("\n\t..::SALIENDO DEL SISTEMA::..")
                    opcion=False
                case _:
                    print(".::Escoje una opción válida::.")
                    funciones.esperarTecla()
        except ValueError:
            print(".::Ingrese un dato numérico::.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()