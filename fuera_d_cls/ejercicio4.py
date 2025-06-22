"""Pedir al usuario su nombre y edad, luego mostrar cuantos años tendra en 10 años"""

#se piede el nonmbre y la edad 
nombre = input("ingrese su nombre\n")
edad = int(input("ingrese su edad\n"))

#se calcula la edad despues de 10 años
edad = edad + 10

#se imprime el nombre y edad
print(f"Hola {nombre}, tu edad en 10 años sera: {edad}")