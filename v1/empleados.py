import os
import platform

empleado={}
empleados=[]
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


def agregar_empleado():
    borrarPantalla()
    print("\n\t.:: Alta de Libros ::.\n ")
    empleado["nombre"] = input("Ingresa el nombre del empleado :").upper()
    empleado["edad"] = input("Ingresa la edad del empleado: ").upper()
    empleado["cargo"] = input("Ingresa el cargo del empleado :").upper()
    empleados.append(empleado)
    print("..::OPERACION EXITOSA::..")
    esperarTecla()

def mostrar_empleados():
    borrarPantalla()
    print("\n\t.::Mostrar empleados guardados::.\n")
    if len(empleados) > 0:
        for idx, empleado in enumerate(empleados, 1):
            print(f"\nEmpleado #{idx}:")
            for clave, valor in empleado.items():
                print(f"\t{clave}: {valor}")
        esperarTecla()
    else:
        print("\n\t.::NO HAY EMPLEADOS GUARDADOS::.\n")
        esperarTecla()

def actualizar_empleados():
    borrarPantalla()
    print("\n\t.::Modificar características del empleado::.\n")
    if len(empleado) >0:
       continua=True
       while continua:
            print("Características actuales:")
            for i, (clave, valor) in enumerate(empleado.items(), 1):
                print(f"  {i}. {clave}: {valor}")
            try:
                opcion = int(input("\nElige el número de la característica a modificar (0 para salir): "))
                if opcion == 0:
                    continua=False
                claves = list(empleado.keys())
                if 1 <= opcion <= len(claves):
                    clave = claves[opcion - 1]
                    print(f"Valor actual de '{clave}': {empleado[clave]}")
                    nuevo_valor = input(f"Nuevo valor para '{clave}': ").upper()
                    empleado[clave] = nuevo_valor
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

def menuEmpleados():
    opcion = True
    while opcion:
        try:
            borrarPantalla()
            print("\n\t.::Sistema de empleados::.\n 1.-Agregar empleado\n 2.-Mostrar empleados\n 3.-Modificar empleado\n 4.-Eliminar empleado\n 5.-Salir")
            opcion = int(input("\tElige una opcion: "))
            match opcion:
                case 1:
                    agregar_empleado()
                case 2:
                    mostrar_empleados()
                case 3:
                    actualizar_empleados()
                case 4:
                    eliminar_empleado()
                case 5:
                    print("\n\t..::SALIENDO DEL SISTEMA DE EMPLEADOS::..")
                    opcion = False
                case _:
                    print(".::Escoje una opción valida::.")
                    esperarTecla()
        except ValueError:
            print(".::Ingrese un dato numerico::.")
            esperarTecla()

def eliminar_empleado():
    pass
