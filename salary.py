class Worker():

    def __init__(self, id, name, phsalary, weekdays, hours, tax):
        self.__id = int(id)
        self.__name = name
        self.__phsalary = int(phsalary)
        self.__weekdays = int(weekdays)
        self.__hours = int(hours)
        self.__tax = 0.20

    #accesadores
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_phsalary(self):
        return self.__phsalary
    def get_weekdays(self):
        return self.__weekdays
    def get_hours(self):
        return self.__hours
    def get_tax(self):
        return self.__tax
    
    #mutadores
    def set_id(self, new_id):
        self.__id = new_id
    def set_name(self, new_name):
        self.__name = new_name
    def set_phsalary(self, new_phsalary):
        self.__phsalary = new_phsalary
    def set_weekdays(self, new_weekdays):
        self.__weekdays = new_weekdays
    def set_hours(self, new_hours):
        self.__hours = new_hours

    def info(self):
        #Información sobre el trabajador y su salario
        print("Información del trabajador:\n")
        print(f"Trabajador n°{self.__id}")
        print(f"Señor/a: {self.__name}")
        print(f"Sueldo por hora: {self.__phsalary}")
        print(f"Dias a la semana: {self.__weekdays}")
        print(f"Horas trabajadas al día: {self.__hours}")
        print(f"Sueldo Bruto: {(self.__phsalary * self.__hours * self.__weekdays * 4)}")
        print(f"Descuento por impuestos: {(self.__phsalary * self.__hours * self.__weekdays * 4) * -(self.__tax)}")
        print(f"Sueldo Liquido: {(self.__phsalary * self.__hours * self.__weekdays * 4) - ((self.__phsalary * self.__hours * self.__weekdays * 4) * (self.__tax))}\n")