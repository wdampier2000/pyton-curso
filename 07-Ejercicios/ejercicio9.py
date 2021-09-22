"""
Pida numeros al usuario hasta meter el numero 111

"""
cont=1

while cont<100:

    num=int(input("Introducir un numero : "))

    if num==111:
        break

    print(f"introdujo el numero {num}")
