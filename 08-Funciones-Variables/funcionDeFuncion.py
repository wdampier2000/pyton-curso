
def getNombre(nombre):
    texto=f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto=F"Los apellidos son: {apellidos}"
    return texto

def getTodo(nombre, apellidos):
    texto= getNombre(nombre)+ " , " + getApellidos(apellidos)
    return texto

print(getNombre("Victor"), getApellidos("Rigacci"))

print(getTodo("Victor","Rigacci"))
