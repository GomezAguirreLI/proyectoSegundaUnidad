
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
    libro={}
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

         opcion=funciones.menu_usuarios()
         
         if opcion == "1" or opcion == "AGREGAR LIBRO":
            funciones.borrarPantalla()
            print("\n\t 📚 ..:: Agregar Libro ::.. 📚")

           

         elif opcion == "2" or opcion == "RENTAR LIBRO":
                funciones.borrarPantalla()
                print("\n\t 📖 ..:: Rentar Libro ::.. 📖")
                funciones.mostrar_libros_disponibles()
                libro_id = input("\t Ingrese el ID del libro a rentar: ").strip()
                resultado = funciones.rentar_libro(usuario_id, libro_id)
                if resultado:
                    print("\n\t Libro rentado correctamente.")
                else:
                    print("\n\t No se pudo rentar el libro. Intente de nuevo.")
                funciones.esperarTecla()
         elif opcion == "3" or opcion == "MIS LIBROS":
                funciones.borrarPantalla()
                print("\n\t 📚 ..:: Mis Libros Rentados ::.. 📚")
                funciones.mostrar_libros_rentados(usuario_id)
                funciones.esperarTecla()
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