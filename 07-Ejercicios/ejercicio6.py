"""
mostrar todas las tablas de multiplicar del 1 al 10

"""


for tabla in range (1,11):

    print (f"Tabla de {tabla} ")


    for i in range (1,10):
        valor= tabla*i
        print (f" {tabla} x {i} = {valor}")
        i+=1
