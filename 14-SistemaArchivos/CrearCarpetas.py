import os

#crear carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("La carpeta - mi_carpeta - ya existe")

# Eliminar carpeta

os.rmdir("./mi_carpeta")