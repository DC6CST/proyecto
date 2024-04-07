class Mantainance():

    def __init__(self, serialnum, name, frecuency, price):
        self.__serialnum = int(serialnum)
        self.__name = name
        self.__frecuency = int(frecuency)
        self.__price = price
        
    #accesadores
    def get_serialnum(self):
        return self.__serialnum
    def get_name(self):
        return self.__name
    def get_frecuency(self):
        return self.__frecuency
    def get_price(self):
        return self.__price

    #mutadores
    def set_serialnum(self, new_serialnum):
        self.__serialnum = new_serialnum
    def set_name(self, new_name):
        self.__name = new_name
    def set_frecuency(self, new_frecuency):
        self.__frecuency = new_frecuency
    def set_price(self, new_price):
        self.__price = new_price

    def info(self):
        #Información sobre los mantenimientos de las máquinas de juegos
        print("Mantenimiento programado:\n")
        print(f"Máquina n°{self.__serialnum}")
        print(f"Nombre: {self.__name}")
        print(f"Frecuencia: Cada {self.__frecuency} días")
        print(f"Coste: {self.__price}\n")