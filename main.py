# -*- coding: utf-8 -*-
__author__ = 'jasg'
import cx_Oracle

from util import util

#importamos las clases
from clase_usuario import Usuario

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
		miUsuario = Usuario(nombre, apellidos, sexo, edad, correo, password)
		miUsuario.muestraTodo()
		#enviando datos a la bd
		QUERY = 'insert into usuario (usuario_id, nombre, apellidos,sexo, edad, correo, password) values (:cliente_id, :nombre, :apellidos, :dni)'
		res = db.query_otro(QUERY, (nombre,apellidos,sexo, edad, correo, password))
		#metodo para guardar los datos del regitro


#metodo para iniciar session

#print("""
#
#\t----------------------------------------------------------------------------
#\t	-Bienvenido                                                              -
#\t	-1) Cambiar Usuario                                                      -
#\t	-2) Cambiar contraseña                                                   -
#\t	-3) Crear nuevo evento evento                                            -
#\t	-4) Ver contactos                                                        -
#\t  -5) Ver Calendario                                                       -
#\t  -6) Ver proximos eventos                                                 -
#\t  -7) Calificar eventos                                                    - 
#\t  -6) Salir                                                                -
#\t----------------------------------------------------------------------------
#	""")

# esto mostrar el menu principal

def menuPrincipal():
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


#aqui es donde aparecera el menu

if __name__ == '__main__':

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

	
