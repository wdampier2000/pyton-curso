

import json
from typing import NoReturn

ruta = "./Lectura_Json/datos/nubemotic.json"

f= open(ruta,'r')
c= f.read()
js=json.loads(c)
sitio=list()
cont=0

while cont<=24:
    
    print(cont, "SITIO: ", js[cont]["name"])
    cont2=0
    while cont2<=5:
        print(cont, cont2, "Parametro: ", js[cont]["ios"][cont2]["name"]," :", js[cont]["ios"][cont2]["value"], " (", js[cont]["ios"][cont2]["updated_at"], ")")
        #print(cont, cont2, "Parametro: ", js[cont]["ios"][cont2]["value"])
        #print(cont, cont2, "Parametro: ", js[cont]["ios"][cont2]["updated_at"])
        sitio.append(cont, cont2, "Parametro: ", js[cont]["ios"][cont2]["name"]," :", js[cont]["ios"][cont2]["value"], " (", js[cont]["ios"][cont2]["updated_at"], ")")

        cont2+=1
    
    cont+=1