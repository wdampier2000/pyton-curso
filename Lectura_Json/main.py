
import json

def cargar_datos(ruta):
    with open(ruta) as contenido: # ABRIMOS EL ARCHIVO JSON
       cursos = json.load(contenido) # CONVIERTE EL CONTENIDO A UN FORMATO JSON
       for curso in cursos:
            print(curso) # entrega todos los diccionarios
            print(curso.get('nombre')) # entrega el valor de nombre del diccionario
            print(curso.get('duracion', '')) # '' = si no existe entrega cadena vacia

if __name__== '__main__':
    ruta = "./Lectura_Json/datos/cursos.json"
    cargar_datos(ruta)