class Business():

	def __init__(self, name, rut, desc, role):
		self.__name = name
		self.__rut = rut
		self.__desc = desc
		self.__role = role

	def info(self):
		print("Datos de la empresa:\n")
		print(f"Nombre de la empresa: {self.__name}")
		print(f"Descripción: {self.__desc}")
		print(f"Giro: {self.__role}")
		print(f"RUT: {self.__rut}")


