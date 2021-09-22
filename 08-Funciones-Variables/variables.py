"""
Variables locales:
Se definen dentro de las funciones y no se pueden usar fuera de ellas
SALVO que hagamos un RETURN

Variables Glovales:
Estan definidas fuera de una funcion y estan disponibles
dentro y fuera de ellas

"""
#Variable global

frase="El vaso esta sobre la mesa"

print(frase)

def holaMundo():
    frase="Hola mundo"
    print (frase)

    year="2021"
    return year

def holaMundo2():
    frase="Hola mundo"
    print (frase)

    year="2021"
    
    global website #DEFINO ESTA VARIABLE COMO GLOBAL
    website="rmi.com.ar"
    print ("DENTRO " , website)

    return "Devuelvo "+ str(year)

    

print (holaMundo())
print(holaMundo2())
print (f"AFUERA {website}")