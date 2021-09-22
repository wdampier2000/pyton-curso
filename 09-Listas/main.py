"""
Colecciones o conjuntos de datos/valores bajo un unico nombre

Para acceder a esos datos usamos indice numerico

"""

Lista1=["Victor", "Jose", "Raul"]
print (Lista1)

#otra forma
cantantes= list(("Luis Miguel", "Riqui Martin", "Julio Iglesias"))
print (cantantes)

#otra
year = list(range(2020,2025))
print (year)

#otra
variada=["Casa", 2019, 23.8, True, "Victor"]
print (variada)
print("\n")
#Indices

print(cantantes[2])
print("\n")
print(cantantes[0:3])
print("\n")
print(cantantes[1:])

cantantes[2]="Sabrina"
print("\n")
print(cantantes[2])
print("\n")
print(cantantes[0:])

#Agregar elementos

cantantes.append("BBKING")
print(cantantes[0:])

#mostrar listado de cantantes y ubicacion en la lista
print("\n")
for cantante in cantantes:
    print (f"{cantantes.index(cantante)} {cantante}")

"""
#Agregar cantantes a la lista
nuevoCantante=""
while nuevoCantante != "fin":
    nuevoCantante=input(f"Nuevo cantante: ")
    cantantes.append(nuevoCantante)

print(cantantes[0:])
"""
#listas multidimensionales

contactos=[
    [
        'Victor',
        'rmi.com.ar'
    ],
    [
        'Jose',
        'Nubemotic.com.ar'
    ],
    [
        'Roberto',
        'google.com.ar'
    ]
]

print("\n")
print(contactos)

print(contactos[1][1])
print(contactos[1][0])
print(contactos[0][1])

print("\n")

