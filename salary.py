class Worker():

    def __init__(self, id, name, ph_salary, weekdays, hours, tax):
        self.__id = int(id)
        self.__name = name
        self.__ph_salary = int(ph_salary)
        self.__weekdays = int(weekdays)
        self.__hours = int(hours)
        self.__tax = 0.20
        
    def info(self):
        #Información sobre el trabajador y su salario
        print("Información del trabajador:\n")
        print(f"Trabajador n°{self.__id}")
        print(f"Señor/a: {self.__name}")
        print(f"Sueldo por hora: {self.__ph_salary}")
        print(f"Dias a la semana: {self.__weekdays}")
        print(f"Horas trabajadas al día: {self.__hours}")
        print(f"Sueldo Bruto: {(self.__ph_salary * self.__hours * self.__weekdays * 4)}")
        print(f"Descuento por impuestos: {(self.__ph_salary * self.__hours * self.__weekdays * 4) * -(self.__tax)}")
        print(f"Sueldo Liquido: {(self.__ph_salary * self.__hours * self.__weekdays * 4) - ((self.__ph_salary * self.__hours * self.__weekdays * 4) * (self.__tax))}")