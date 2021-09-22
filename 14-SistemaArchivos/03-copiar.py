from io import open
import pathlib
import shutil

#ruta absoluta:
# si uso /../ subo al directorio anterior

print ("La rutra absoluta es: " , str(pathlib.Path().absolute()))

#Copiar

ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

ruta_alternativa = "./14-SistemaArchivos/fichero_copiado77.txt"
shutil.copyfile(ruta_original, ruta_alternativa)