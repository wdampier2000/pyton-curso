

def holaMundo(nombre):
    return f"Hola que tal? como estas {nombre}"

def calculadora (num1,num2,basicas=False):
    suma = num1+num2
    resta=num1-num2
    multi=num1*num2
    divi=num1/num2

    if basicas==True:
        cadena= ""
        cadena+="Suma " + str(suma)
        cadena+="\n"
        cadena+="Resta " + str(resta)
        cadena+="\n"
        return cadena

    cadena+="Multiplicacion " + str(multi)
    cadena+="\n"
    cadena+="Division " + str(divi)

    return cadena