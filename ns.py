#se pide un numero entero
n = int(input("Ingresa un número: "))
#se define resultado como 1
resultado = 1

for i in range(1, n + 1):
    resultado *= i

print(f"El factorial de {n} es {resultado}")