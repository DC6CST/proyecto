class Report():

    def __init__(self, day, income, payment, customers):
        self.__day = int(day)
        self.__income = int(income)
        self.__payment = int(payment)
        self.__customers = int(customers)

    #accesadores
    def get_day(self):
        return self.__day
    def get_income(self):
        return self.__income
    def get_payments(self):
        return self.__payment
    def get_customers(self):
        return self.__customers

    #mutadores
    def set_day(self, new_day):
        self.__day = new_day
    def set_income(self, new_income):
        self.__income = new_income
    def set_payments(self, new_payment):
        self.__payment = new_payment
    def set_customers(self, new_customers):
        self.__customers = new_customers

    def netIncome(self):
        #Información detallada del reporte diario, calculando ganancias y perdidas
        print("Reporte diario:\n")
        print(f"Día {self.__day}")
        print(f"Clientes: {self.__customers} personas.")
        print(f"Ingresos: {self.__income}")
        print(f"Pagos: {self.__payment}")
        print(f"Ingresos netos: {self.__income - self.__payment}\n")