# -*- coding: utf-8 -*-
__author__ = 'dbquebin'
import cx_Oracle

from util import util

#importamos las clases
from clase_usuario import Usuario

db = util()

#fin de importacion


#metodo para el registro en del nuevo usuario
def hacerRegistro():
	print("Registrese: \n")
	nombre = str(input("Ingrese su nombre: "))
	apellidos = str(input("Ingrese sus apellidos:"))
	correo = str(input("Ingrese su correo: "))
	password = str(input("Ingrese su nueva contraseña: "))
	edad = int(input("Ingrese su edad: "))
	sexo = bool(input("Ingrese el sexo que es usted: "))
	if edad <= 18:
		print("Usuario ", nombre, " usted no puede crear su cuenta por que es menor de 18 años")
	else:
		print("Bienvenido ", nombre)
		QUERY = 'insert into cliente (id_cliente, nombre, apellidos, dni) values (:id_cliente, :nombre, :apellidos, :dni)'
		res = db.query_otro(QUERY, ('003', nombre, apellidos, '741852'))

def inciarSesion():#metodo para inciar sesion
	print("\tInicio de Sesion")
	correo = str(input("Correo: "))
	contraseña = str(input("Contraseña: "))
	if  correo == "jasg" and contraseña == "12345":
		print("\nCorrecto")
		#aqui le aparecera la nueva interfaz del usuario
		interfazUsuario()
	else:
		print("\tIncorrecto")

#interfaces para el sistema 
def publicarEvento():
	print("Complete los datos del Evento")
	print("Nombre del evento")
	print("Fecha d")




def interfazUsuario():#interfaz para el inicio de sesion
	print("""
		------------------------------------------------
		|	1) Publicar Evento  
		|   2) Asignar Grupo
		|   3) Ver lista de amigo
		|   4) Cerrar Sesion
		|_______________________________________________

		""")
	op = int(input("Opcion:     "))
	while op > 4:
		if op  == 1:
			print("Publicar Evento")
		elif op == 2:
			print("Asignacion de Grupos")
		elif op == 3:
			print("Lista de Amigos")
		elif op == 4:
			print("Usted Salio")

		op = int(input("Opcion:     "))

def menuPrincipal():#menu para mostrar el menu principal para ambos usuarios
	print("""
	
	\t--------------------------------------------------------
	\t|	 Red Social de Eventos OpenWorld               |
	\t|	 1) Realizar registro                          |
	\t|	 2) Inciar Sesion                              |
	\t|	 3) Salir                                      |
	\t|                                                      |
	\t|                                                      |
	\t--------------------------------------------------------
		""")
	print()


#main principal

if __name__ == '__main__':#con esto ejecuto el main principal

	menuPrincipal()

	confirmacion = int(input("\tIngrese su opcion: "))
	if confirmacion == 1:
		hacerRegistro()
	elif confirmacion == 2:
		inciarSesion()
	elif confirmacion == 3:
		print("Usted salio")
	else:
		menuPrincipal()
# aqui termina el menu principal

	
