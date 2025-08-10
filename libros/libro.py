from conexionBD import *
from mysql.connector import Error
from usuarios import usuario


def crearLibro():


    book={}

    book["nombre"] = input("Ingresa el nombre del libro: ").upper().strip()
    book["categoria"] = input("Ingresa la categoria del libro: ").upper().strip()
    book["idioma"] = input("Ingresa el idioma del libro: ").upper().strip()
    book["cant_paginas"] = input("Ingresa la cantidad de paginas del libro: ").strip()
    book["estanteria"] = input("Ingresa la estanteria en la que ira el libro: ").strip()
    book["autor"] = input("Ingresa el autor del libro: ").upper().strip()

    try:
        cursor = conexion.cursor()
        rentado="NO"
        sql = """
             INSERT INTO libros (nombre, categoria, idioma, cant_paginas, estanteria, autor,rentado)
             VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
        val = (book["nombre"], book["categoria"], book["idioma"], book["cant_paginas"], book["estanteria"], book["autor"],rentado)
        cursor.execute(sql,val)
        conexion.commit()
        input("\n\t\t :::✅ LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅:::")
    except Error as e:
        print(f"\n\t\t ::: Error al insertar el registro  {e}:::")
        input("  ")


def mostrar_libros():
    try:
        sql="SELECT * FROM libros"
        cursor.execute(sql)
        conexion.commit()
        return cursor.fetchall()

    except Error as e:
        print(f"No hay libros disponibles por el momento ")    
        return []
    
def rentar_libro(id_libro,clave_usuario,telf,tiempo):
    try:
        print(f"\n\t ..::LIBROS DISPONIBLES::..")
        
        libros_disponibles=mostrar_libros()
        flag=False
        puede_rentar=False
        if len(libros_disponibles)>0:
            print("\n\t 📖 ..:: Libros disponibles  ::.. 📖")
            print(f"{'ID':>15}{'Titulo':>20}{'categoria':>20}{'idioma':>20}{'cant_paginas':>20}{'Estanteria':>20}{'Autor':>20}")
        
            for fila in libros_disponibles:
                print("-"*180)
                if fila[7]=="NO":
                 flag=True
                 print(f"{fila[0]:>15}{fila[1]:>20}{fila[2]:>20}{fila[3]:>20}{fila[4]:>20}{fila[5]:>20}{fila[6]:>20}")

            #Avisa si ya todos los libros estan rentados
            if flag!=True:
                print(f"Lo sentimos, todos los libros ya fueron rentados")    
            else:
                print(f"Para rentar un libro usted debe no tener mas de dos libros rentados")
                usuario_rentando=usuario.obtener_claves_usuarios
                for filas in usuario_rentando:
                    if fila[6]>2:
                        
                        print(f"\n\t Lamentamos el infortunio pero usted debe regresar al menos un libro para poder rentar otro libro ")
                    else:
                        print(f"\n\t ..::Excelente usted podra rentar el libro que usted quiera.")
                        
                        










    except Error as e:
        print(f"Por el momento no se pueden rentar libros ")    