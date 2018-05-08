def hacerRegistro():
	print("Registrese:")
	nombre = str(input("Ingrese su nombre: "))
	apellidos = str(input("Ingrese sus apellidos:"))
	correo = str(input("Ingrese su correo: "))
	password = str(input("Ingrese su contraseña nueva: "))
	edad = int(input("Ingrese su edad: "))
	sexo = bool(input("Ingrese el sexo que es usted: "))
	telefono = str(input("Ingrese su numero de telefono: "))
	if edad <= 18:
		print("Usuario ", nombre, " usted no puede crear su cuenta por que es menor de 18 años")
	else:
		print("Bienvenido ", nombre)
		#metodo para guardar los datos del regitro

def inciarSesion():
		print("Incie sesion")
	usuario = str(input("Ingrese usuario"))
    contra = str(("Ingrese password"))
    
    if usuario=="usuario" || contra=="password":
    	print("Bienvenido Usuario:" + usuario)
    	print("password:" + contra)
    else:
print("""

\t----------------------------------------------------------------------------
	Red Social de Eventos OpenWorld
	1) Realizar registro
	2) Inciar Sesion
	3) Salir
	""")
print()
print()
confirmacion = int(input("Ingrese su opcion: "))

"""
parte despues de iniaiand

"""	
print("""

\t----------------------------------------------------------------------------
\t	-Bienvenido                                                              -
\t	-1) Cambiar Usuario                                                      -
\t	-2) Cambiar contraseña                                                   -
\t	-3) Crear nuevo evento evento                                            -
\t	-4) Ver contactos                                                        -
\t  -5) Ver Calendario                                                       -
\t  -6) Ver proximos eventos                                                 -
\t  -7) Calificar eventos                                                    - 
\t  -6) Salir                                                                -
\t----------------------------------------------------------------------------
	""")
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

	
