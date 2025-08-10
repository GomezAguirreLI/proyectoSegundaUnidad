
import funciones
import getpass
from usuarios import usuario   
from libros import libro


def main():
    opcion=True
    
    while opcion:
        
        funciones.borrarPantalla()
        opcion=funciones.menu_usuarios()
        
        if opcion=="1" or opcion=="REGISTRO":
        
            funciones.borrarPantalla()
        
            print("\n \t 📝 ..:: Registro en el Sistema ::.. 📝")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            telf=input("\t Ingrese su numero telefonico: ").strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            clave=usuario.codigo_aleatorio()
            
            #Agregar codigo
            resultado=usuario.registrar(nombre,telf,password,clave)
           
            if resultado:
                print(f"\n\t {nombre}, se registro correctamente con el telefono: {telf} y su clave unica es: {clave}")
            else:
                print(f"\n\t Por favor intentelo de nuevo, no fue posible registrar al usuario")
            funciones.esperarTecla()
        elif opcion=="2"or opcion=="LOGIN":
            funciones.borrarPantalla()
            print("\n \t 🔑 ..:: Inicio de Sesión ::.. 🔑")     
            nombre=input("\t Ingrese su nombre: ").upper().strip()

            password=getpass.getpass("\t Ingrese su contraseña: ").strip()
            #aqui empieza el menu de los libros
            registro,admin=usuario.iniciar_sesion(nombre,password)
            if registro:
                if admin:
                    menu_admin(registro[1])
                    funciones.esperarTecla()
                else:
                 menu_libreria(registro[0],registro[1])
                 funciones.esperarTecla()

            else:
                print(f"\n\t Usuario y/o contraseña incorrectas, vuelva a intentarlo")    
                funciones.esperarTecla()
        elif opcion=="3" or opcion=="SALIR":
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla()        





def menu_libreria(usuario_id,nombre):
    bandera=True
    
    while bandera:
         
         funciones.borrarPantalla()
         print(f"\n\t\t Bienvenido {nombre}, ha iniciado sesion con exito")
         
         #AREA DEL TUTORIAL
         tutorial=""
         while tutorial != "S" and tutorial != "N":
            tutorial = input("\n \t \t ¿Desea conocer las cosas que puede realizar? (S/N): ").upper().strip()
            funciones.borrarPantalla()
         if tutorial=="S":
            print("En este sistema usted podra,agregar libros a la gran coleccion de la biblioteca del calvario,rentar libros")
            funciones.esperarTecla()
         
         #area de ps como tal el menu

         opcion=funciones.menu_libreria()
         
         if opcion == "1" or opcion == "AGREGAR LIBRO":
            funciones.borrarPantalla()
            print("\n\t 📚 ..:: Agregar Libro ::.. 📚")
            libro.crearLibro()

         elif opcion == "2" or opcion == "MOSTRAR LIBRO":
                funciones.borrarPantalla()
                libros_disponibles=libro.mostrar_libros()
                if len(libros_disponibles)>0:
                  print("\n\t 📖 ..:: Libros disponibles  ::.. 📖")
                  print(f"{'ID':>15}{'Titulo':>20}{'categoria':>20}{'idioma':>20}{'cant_paginas':>20}{'Estanteria':>20}{'Autor':>20}")
                  for fila in libros_disponibles:
                      print("-"*180)
                      
                      print(f"{fila[0]:>15}{fila[1]:>20}{fila[2]:>20}{fila[3]:>20}{fila[4]:>20}{fila[5]:>20}{fila[6]:>20}")


                funciones.esperarTecla()
         elif opcion == "3" or opcion == "RENTAR LIBRO":
                funciones.borrarPantalla()
                libro.rentar_libro(1,3,5,5)



              
         elif opcion == "4" or opcion == "DEVOLVER LIBRO":
                funciones.borrarPantalla()
                print("\n\t 🔄 ..:: Devolver Libro ::.. 🔄")
                funciones.mostrar_libros_rentados(usuario_id)
                libro_id = input("\t Ingrese el ID del libro a devolver: ").strip()
                resultado = funciones.devolver_libro(usuario_id, libro_id)
                if resultado:
                    print("\n\t Libro devuelto correctamente.")
                else:
                    print("\n\t No se pudo devolver el libro. Intente de nuevo.")
                funciones.esperarTecla()
         if opcion == "5" or opcion =="SALIR":
            print("\n\t Saliendo del menú administrador...")
            bandera = False
            

def menu_admin(nombre):
    bandera = True
    while bandera:
        funciones.borrarPantalla()
        print(f"\n\t\t 👑 Bienvenido Administrador {nombre}, ha iniciado sesión con éxito 👑")
        tutorial = ""
        while tutorial != "S" and tutorial != "N":
            tutorial = input("\n \t \t ¿Desea conocer las cosas que puede realizar como administrador? (S/N): ").upper().strip()
            funciones.borrarPantalla()
        if tutorial == "S":
            print("En este sistema usted podrá gestionar usuarios, gestionar libros, ver los libros rentados y cambiar contraseñas de administrador.")
            funciones.esperarTecla()
        opcion = funciones.menu_administrador()





        if opcion == "5" or opcion == "SALIR":
            print("\n\t👋 Saliendo del menú administrador...")
            funciones.esperarTecla()
            bandera = False
        else:
            print(f"\n\t⚠️ Opción '{opcion}' aún no implementada.")
            funciones.esperarTecla()         

if __name__=="__main__":
    main() 