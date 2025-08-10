from conexionBD import *
import hashlib
import random

def obtener_claves_usuarios():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT clave FROM usuarios")
        resultados = cursor.fetchall()
        claves = {fila[0] for fila in resultados}
        cursor.close()
        return claves
    except Exception as e:
        print("Error al obtener claves:", e)
        return set()
    
def codigo_aleatorio():

    completo=True
    while completo:
        codigos=obtener_claves_usuarios()
        
        codigo=random.randint(0,10**5)
        
        if codigo not in codigos:
            codigos.add(codigo)
            completo=False


    return codigo       
            

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,telf,contrasena,clave):
    try:
        admin="NO"
        libros_rentados=0
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        sql="INSERT INTO usuarios(nombre, num_telefonico, contrasena, clave, administrador,libros_rentados) VALUES (%s,%s,%s,%s,%s,%s)"
        val=(nombre,telf,contrasena,clave,admin,libros_rentados)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except Exception as e:
        return False

def obtener_claves_usuarios():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT clave FROM usuarios")
        resultados = cursor.fetchall()
        claves = {fila[0] for fila in resultados}
        cursor.close()
        return claves
    except Exception as e:
        print("Error al obtener claves:", e)
        return set()

def obtener_libros_rentados(clave):
    try:
        sql="SELECT * FROM `usuarios` WHERE clave=%s"
        val=(clave)
        cursor.execute(sql,val)
        return cursor.fetchall()
    except Exception as e:
        return []

def iniciar_sesion(nombre,contrasena):
    try:
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()

        sql="select * from usuarios where nombre =%s and contrasena=%s"
        val=(nombre,contrasena)
        cursor.execute(sql,val)
        registros=cursor.fetchone()
        
        if registros:
            if registros[5]=="SI":
                admin=True
                return registros,True
            else:
              return registros,False
        else:
            return None,False
    except Exception as e:
        print(f"[ERROR] No se pudo iniciar sesión: {e}")
        return None,False

