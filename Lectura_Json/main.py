
import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
       cursos = json.load(contenido)
       print(cursos)


if __name__== '__main__':
    ruta = "./Lectura_Json/datos/cursos.json"
    cargar_datos(ruta)