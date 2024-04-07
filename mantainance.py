class Mantainance():

    def __init__(self, serialnum, name, frecuency, price):
        self.__serialnum = int(serialnum)
        self.__name = name
        self.__frecuency = int(frecuency)
        self.__price = price
        
    def info(self):
        #Información sobre los mantenimientos de las máquinas de juegos
        print("Mantenimiento programado:\n")
        print(f"Máquina n°{self.__serialnum}.")
        print(f"Nombre: {self.__name}.")
        print(f"Frecuencia: Cada {self.__frecuency} días.")
        print(f"Coste: {self.__price}")