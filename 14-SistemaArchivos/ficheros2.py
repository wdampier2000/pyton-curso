from io import open
import pathlib #crear, cargar datos, leer archivo etc
import shutil #copiar, renombrar, eliminar archivo

"""
copiar, renombrar y eliminar un archivo

"""
#copiar
ruta_original=str(pathlib.Path().absolute())+"/fichero_texto.txt"
ruta_nueva=str(pathlib.Path().absolute())+"/fichero_copiado.txt"

shutil.copyfile(ruta_original, ruta_nueva)