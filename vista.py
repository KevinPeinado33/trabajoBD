def hacerRegistro(self):
	print("Registrese:")
	nombre = str(input("Ingrese su nombre: "))
	apellidos = str(input("Ingrese sus apellidos:"))
	correo = str(input("Ingrese su correo: "))
	password = str(input("Ingrese su contraseña nueva: "))
	edad = int(input("Ingrese su edad: "))
	telefono = str(input("Ingrese su numero de telefono: "))
	if edad <= 18:
		print("Usuario ", nombre, " usted no puede crear su cuenta por que es menor de 18 años")
	else:
		print("Bienvenido ", nombre, " ")
		#metodo para guardar los datos del regitro


def inciarSesion(self):
	print("Incie sesion")
	usuario = str(input("Ingrese "))

print("""

\t----------------------------------------------------------------------------
	Red Social de Eventos OpenWorld
	1) Realizar registro
	2) Inciar Sesion
	3) Salir
	""")
print()
confirmacion = int(input("Ingrese su opcion: "))

	