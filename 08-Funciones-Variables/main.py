"""
FUNCION: ES UN CONJUNTO DE INSTRUCCIONES AGRUPADAS BAJO UN NOMBRE CONCRETO QUE PUEDEN
REUTILIZARSE INVOCANDO A LA FUNCION TANTAS VECES COMO SEA NECESARIO   

EJ:

PARA DEFINIRLA:

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

PARA INVOCARLA:

nombreDeMiFuncion(mi_parametro)

"""

"""
#EJEMPLO 1

print ("\n \n -----------Ejemplo 1-------------")

def muestraNombres():
    print("Victor")
    print("Juan")
    print("Jose")
    print("Raul")
    print("Adrian")
    print("\n")

muestraNombres()

# EJEMPLO 2

print ("\n \n -----------Ejemplo 2-------------")

def mostrarTuNombre(nombre):
    print (f"Tu nombre es {nombre}")

mostrarTuNombre("Victor Rigacci")
mostrarTuNombre("Jose Perez")
mostrarTuNombre("Juan Rodriguez")

# EJEMPLO 3

print ("\n \n -----------Ejemplo 3-------------")

def mostrarTuNombre(nombre,edad):
    print (f"Tu nombre es {nombre}")

    if edad>=18:
        print(" y es mayor de edad")
    else:
        print(" y es menor de edad")

nombre= input("Ingresar Nombre: ")
edad = int(input("Ingresar Edad: "))
mostrarTuNombre(nombre, edad)




# EJEMPLO 4


print ("\n \n -----------Ejemplo 4-------------")

def tablaMultiplicar(nro):
    pos=0
    
    while pos<21:
        resultado= pos*nro
        print (f"{nro} X {pos} = {resultado}")
        pos+=1


nro = int(input("Ingresar numero de la tabla a mostrar: "))
tablaMultiplicar(nro)


"""

# EJEMPLO 5 PARAMETROS OPCIONALES


print ("\n \n -----------Ejemplo 5-------------")

def getEmpleado(nombre,dni= "S/D"):
    print ("EMPLEADO")
    print (f"Nombre {nombre}")

    if dni!="S/D":
        print (f"DNI {dni}")

getEmpleado("Vic")