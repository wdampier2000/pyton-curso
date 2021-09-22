    
"""
    
    Pedir la nota de 15 alumnos y imprimir cuantos han aprobado y cuantos desaprobaron
"""

contador=0
aprobados=0
desaprobados=0


while contador<15:
    contador+=1
    nota=int(input(f"Nota de alumno {contador} : "))
    if nota<4:
        desaprobados+=1
    else:
        aprobados+=1

print(f"Aprobados: {aprobados}")
print(f"Desprobados: {desaprobados}")
