


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usuarios():
   print("\n \t🗒️ .:: Sistema de gestion de libros ::.. \n\t\t1.- 📝 Registro  \n\t\t2.- 🔑 Login \n\t\t3.- 🚪 Salir ")
   opcion=input("\t\t Elige una opción: ").upper().strip() 
   return opcion

def menu_libreria():
   print("\n \t .::  Menu libreria ::. \n\t1.- 🆕 Agregar libro \n\t2.- 📋 Mostrar libros  \n\t3.- ✏️ Rentar libro \n\t4.- 🗑️ Devolver libro \n\t5.- 🚪 Salir """)
   opcion = input("\t\t Elige una opción: ").upper().strip()
   return opcion

def menu_admin():
    print("\n \t🛠️ .:: Menú Administrador ::.\n\t1.- 👤 Gestionar usuarios\n\t2.- 📚 Gestionar libros\n\t3.- 📈 Ver reportes\n\t4.- 🔒 Cambiar contraseña\n\t5.- 🚪 Salir")
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion

 