import os.path

print( "RUTA ACTUAL" , os.path.abspath("./"))
print( "RUTA ANTERIOR" , os.path.abspath("../"))
print("ARCHIVO: " + os.path.abspath("./") + "/14-SistemaArchivos/03-copiar.py")

if os.path.isfile(os.path.abspath("./") + "/14-SistemaArchivos/03-copiar.py"):
    print("El archivo existe")
