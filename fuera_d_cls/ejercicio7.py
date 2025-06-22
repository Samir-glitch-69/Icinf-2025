"""solicitar 3 notas y calcular el promedio, mostar si esta aprobado"""

# Se crea una i para poder salir del bucle
i = 0

# Se crea una lista
notas = []

while True:
    i += 1
    notas.append(float(input("ingrese su nota: ")))
    if i == 3:
        break

# Se calcula las notas y si aprueba o no

total = sum(notas)

promedio = total/3

if promedio >= 4.0:
    print("aprovado")
else:
    print("desaporvado")
