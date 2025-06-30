import json # manipulacion de archivos json
import os   # metodos para trabajar con el sistema operativo

ruta = os.path.join("Json", "datos.json") # ruta relativa


# lectura de  archivo json
print("=========lectura de json==========")
#utf-8 es el encoding/lenguaje español latinoamerica
with open(ruta, "r", encoding='utf-8') as archivo: # la r es de read es una abreviacion 
    datos = json.load(archivo) # conversion de json a estructura de python 

    # mostrar a el usuario el archivo json 
    for usuarios in datos:
        print(f"ID: {usuarios["id"]}, Nombre: {usuarios["nombre"]}, Edad: {usuarios["edad"]}")
#escritura de archivo json
print("============escritura de json============")

# creando nuevo usuario

nuevo_usuario = {
        "id": 5,
        "nombre": "Fernanda",
        "edad": 30
    }

datos.append(nuevo_usuario)

# Guardar los cambios en el archivo json
with open(ruta, "w", encoding='utf-8') as archivo: # la w es de write es una abreviacion 
    json.dump(
        datos,
        archivo,
        indent=4
    )
