"""
motrar todos los numeros entre dos numeros ingresados por el usuario

"""

num1=int(input("Ingresar el primer numero: "))
num2=int(input("Ingresar el segundo numero: "))

if num1<num2:
    for i in range (num1+1, num2):
        print(i)
else:
    print("No hay numeros")