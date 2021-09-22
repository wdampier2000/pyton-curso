from io import open
import pathlib

"""
para crear un fichero saco la ruta:
archivo=open("fichero_texto.txt","a+")

"""


#abrir archivo
archivo=open(str(pathlib.Path().absolute()) + "/fichero_texto.txt","a+")

#escribir en un archivo
archivo.write("Texto agregado desde Python \n")

#cerrar archivo
archivo.close()

#abrir archivo y leer contenido

archivo_lectura=open(str(pathlib.Path().absolute()) + "/fichero_texto.txt","r")

#contenido= archivo_lectura.read()
#print(contenido)

#leer contenido y guardarlo en lista

lista=archivo_lectura.readlines()
archivo_lectura.close()
print (lista)

for frase in lista:

    if not frase.isnumeric():
        print("** "+frase.upper()) #imprime cada linea en mayuscula
    else:
        print("Es numero")

