from io import open
import pathlib
import shutil


ruta_original = "./14-SistemaArchivos/fichero_copiado77.txt"
ruta_nueva = "./14-SistemaArchivos/fichero_copiado77_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva) #le cambio el nombre al archivo

