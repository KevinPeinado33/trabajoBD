class Usuario():
	
	"""constructor"""
	def __init__(self, idUsuario, nomUsuario, apellidoUsuario, sexoUsuario, edadUsuario, email, contraseña):
		super(Usuario, self).__init__()	
		#self.idUsuario = idUsuario
		self.idUsuario = idUsuario
		self.nomUsuario = nomUsuario
		self.apellidoUsuario = apellidoUsuario
		self.sexoUsuario = sexoUsuario
		self.edadUsuario = edadUsuario
		self.email = email
		self.contraseña = contraseña
		
	"""metodos get y set"""
	def getIdUsuario(self): #solo podemos mostrar el id no podemos modificar
		return self.idUsuario

	def setIdUsuario(self, idUsuario):
		self.idUsuario = idUsuario

	def getNomUsuario(self):
		return self.nomUsuario

	def setNomUsuario(self, nomUsuario):
		self.nomUsuario = nomUsuario

	def getApellidoUsuario(self):
		return self.apellidoUsuario

	def setApellidoUsuario(self, apellidoUsuario):
		self.apellidoUsuario = apellidoUsuario

	def getSexoUsuario(self):
		return self.sexoUsuario

	def setSexoUsuario(self, sexoUsuario):
		self.sexoUsuario  = sexoUsuario

	def getEdadUsuario(self):
		return self.edadUsuario

	def getEdadUsuario(self, edadUsuario):
		self.edadUsuario = edadUsuario

	def getEmail(self):
		return self.email

	def setEmail(self, email):
		self.email = email

	def getContraseña(self):
		return self.contraseña

	def setContraseña(self, contraseña):
		self.contraseña = contraseña

	def muestraTodo(self):
		print("Nombre: ", self.nomUsuario, 
			" apellido: ", self.apellidoUsuario, " sexo: ", self.sexoUsuario, " edad: " , self.edadUsuario)