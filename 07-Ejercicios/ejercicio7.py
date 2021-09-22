"""
    Numeros impares entre dos numeros ingresados por el usuario

"""

num1= int(input("Ingresar primer numero :"))
num2= int(input("Ingresar segundo numero :"))

if num1<num2:
    for i in range (num1,num2):
        resto= i % 2
        if resto!=0:
                print(f"Impar =  {i}")
else:
    print("El segundo numero debe ser mayor que el primero")
