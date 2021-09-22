
"""
Como una lista pero son datos que almacena indices alfanumerico

formato clave > valos

"""

persona= { 

    "nombre": "Victor",       #nompre es el indice, Victor es el valor
    "apellido": "Rigacci",
    "email": "riga@rmi.com.ar",

}
print(type(persona))
print(persona)
print(persona["apellido"])

print("\n")

#lista con diccionarios

contactos=[
    {
        'nombre': 'Antonio',
        'email': 'antonio@gmail.com'
    },

   {
        'nombre': 'Jose',
        'email': 'jose@gmail.com'
    },
   {
        'nombre': 'Raul',
        'email': 'raul@gmail.com'
    },
   {
        'nombre': 'Ricardo',
        'email': 'ricardo@gmail.com'
    }
]

print(contactos)

print(contactos[1]['nombre'])
contactos[1]['nombre']="Josesito"
print(contactos[1]['nombre'])
