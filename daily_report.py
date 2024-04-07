class Report():

    def __init__(self, day, income, payments):
        self.__day = int(day)
        self.__income = int(income)
        self.__payments = int(payments)
        
    def netIncome(self):
        print("Reporte diario:\n")
        print(f"Día {self.__day}")
        print(f"Ingresos: {self.__income}")
        print(f"Pagos: {self.__payments}")
        print(f"Ingresos netos: {self.__income - self.__payments}")