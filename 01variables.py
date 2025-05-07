"""Comienzo inicial de python de variables - ULAGOS 2025"""
# los comentarios son con tres comas tmb se puede con los comentarios como este pero es mas extenso 

#definiendo varias variables en una linea ( no es recomendado por los errores que puede haber )
ciudad, region, pais = "castro", "los lagos", "chile"
print(f"hola soy de {ciudad}, {region}, {pais}")

nombre = "Samir"
apellido = "Arana"

# Utilizando variables en un print con comas
#si esta entre medio se tiene que poner comas en los dos extremos
print ("Hola mi nombre es" ,nombre, "y mi apellido es ",apellido)

#tambien se puede con un operador de CONCATENACION que es el signo de suma 
#se tiene que añadir un espacio para que haya uno     |
print ("Hola mi nombre es " +nombre+ "y mi apellido es "+apellido)

#imprimiendo con F-STRING (CADENAS LITERALES)
#se añade la f en el principio y las variables entre llaves {} adentro de todas la comillas 
print (F"Hola mi nombre es {nombre} y mi apellido es {apellido}")

peso = 75
edad = 31 