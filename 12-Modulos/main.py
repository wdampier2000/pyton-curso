
"""
Modulos son funcionalidades ya hechas para reutilizar

ver en https://docs.python.org/3/py-modindex.html

"""
#IMPORTO TODO
#import mimodulo
#print (mimodulo.holaMundo("Victor"))
#print (mimodulo.calculadora(2,4, True))

#IMPORTO SOLO holaMundo
#from mimodulo import holaMundo # solo importo la funcion holaMundo()
#print(holaMundo("Victor"))

#IMPORTO TODO DE OTRA MANERA

from mimodulo import *

print(holaMundo("Victor"))
print(calculadora(1,2,True))

# Modulo fechas
import datetime
print(datetime.date.today())
fecha= datetime.datetime.now()
print(fecha.year)
print(fecha.hour)
print(fecha.minute)
print(fecha.day)

fechaPersonalizada= fecha.strftime("%d/%m/%Y - %H:%M")
print (fechaPersonalizada)

#Modulo matenmaticas

import math

print(math.sqrt(10))
print(math.pi)
print(math.ceil(math.pi)) #redondeo a la alta

#modulo random

import random


print (random.randint(15,67))










