
nombre="Victor"

print(type(nombre))

#Detectar el typado

comprobar = isinstance(nombre, str)

if comprobar:
    print (f"Nombre {nombre} es una cadena str")

if not isinstance(nombre,float):
    print(f"No es un float")

#Limpiar espacios
frase="       aca       muchos    espacios      sacar"

print(frase)
print(frase.strip())

#Eliminar variables
year=2021
print (year)
del year
#print(year)

#Comprobar variable vacia
texto="  3 4  7 89 11"
if len(texto) <=0:
    print("variable vacia")
else:
    print("La variable tiene contenido")
    print (len(texto))

#Encontrar caracteres

frase="La vida es bella"
print (frase.find("vida"))

#Reemplazar palabras en un string

print(frase)
frase=frase.replace("vida","moto")
print(frase)

#todo en mayuscula o minuscula

print(frase.lower())
print(frase.upper())
