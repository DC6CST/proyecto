class Business():

	def __init__(self, name, rut, desc, role):
		self.__name = name
		self.__rut = rut
		self.__desc = desc
		self.__role = role
	
	#accesadores
	def get_name(self):
		return self.__name
	def get_rut(self):
		return self.__rut
	def get_desc(self):
		return self.__desc
	def get_role(self):
		return self.__role

	#mutadores
	def set_name(self, new_name):
		self.__name = new_name
	def set_rut(self, new_rut):
		self.__rut
	def set_desc(self, new_desc):
		self.__desc
	def set_role(self, new_role):
		self.__role

	def info(self):
		#Información detallada de la empresa
		print("Datos de la empresa:\n")
		print(f"Nombre de la empresa: {self.__name}.")
		print(f"Descripción: {self.__desc}.")
		print(f"Giro: {self.__role}.")
		print(f"RUT: {self.__rut}\n")


