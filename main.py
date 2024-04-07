""" Información del proyecto (colapsable)
La empresa es FSociety, un negocio dedicado a las atracciones electrónicas en ferias locales
Esta empresa está pasando por momentos delicados debido a que siguen utilizando papel
y lapiz para llevar un conteo de la cantidad de gente que sube a sus atracciones
Junto a eso acarrean problemas de sobrecostos debido a las mantenciones de las
máquinas las cuales no están llevando un detalle.
La empresa también cuenta con algunos problemas en las liquidaciones entregadas a los
trabajadores, siendo estas poco detalladas en cuanto a los descuentos que se le realizan
de forma obligatoria siguiendo la ley vigente.

Debe solucionar los siguientes problemas:
° Llevar una cuenta de los clientes, ganancias y gastos diarios
° Detallar las mantenciones de cada máquina y su frecuencia de las mismas
° Informar correctamente los pagos a los trabajadores, incluyendo los impuestos
"""
#importación de clases
from mantainance import Mantainance
from business import Business
from salary import Worker
from daily_report import Report

#test print
print("Cargando información de la empresa...\n")

#Datos de la empresa:
fsociety = Business("FSociety", "77.123.456-7",
                    "Fun Society SPA, Compañía dedicada a atracciones en ferias libres",
                    "Fun electronic services")


#Mantenimientos
m_rollercoaster = Mantainance(10001, "Montaña rusa", 7, 100000)


#Trabajadores
aSmith = Worker(71, "Adam Smith", 3000, 6, 8, any)


#Reportes
day_1 = Report(1, 750000, 150000, 130)


#Información general de todas las clases para uso futuro

fsociety.info()

day_1.netIncome()

m_rollercoaster.info()

aSmith.info()