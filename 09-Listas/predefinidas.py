
cantantes= list(("Luis Miguel", "Riqui Martin", "Julio Iglesias", "BBKing", "Calamaro", "Nina Ricci", "Pappo", "Juan Manuel Serrat"))
numeros=[1,2,5,7,3,4]

#ordenar

print (numeros)
numeros.sort()
print(numeros)

#AGREGAR ELEMENTOS EN UNA LISTA
print(cantantes)
cantantes.append("Rodrigo") #lo agrega al final
cantantes.insert(2, "La mona Gimenez") #lo inserta en el tercer lugar y corre toda la lista
print(cantantes)

#ELIMINAR ELEMENTOS DE UNA LISTA
cantantes.pop(1)
print("\n")
print(cantantes)

cantantes.remove("Nina Ricci")
print (cantantes)

#Invertir listas

numeros.reverse()
print(numeros)

#busacar si existe dentro de una lista

print('Pappo' in cantantes)
print('Nina Ricci' in cantantes)

#contar elementos

print(len(cantantes))

#cuantas veces aparece un elemento

print(numeros.count(3))

#conseguir un indice

print(cantantes.index("Pappo"))

#Unir listas

cantantes.extend(numeros)

print (cantantes)
