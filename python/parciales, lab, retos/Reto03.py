suma = 0
division = 0
for n in range(500,100,-3):
    for i in range(1,n):

        print(n)
        division += i
        suma += n
        break
promedio = suma/division
print(f"\nLa suma total de todos los numeros es: {suma}")
print(f"\nLa cantidad de numeros que se sumaron fue de: {division}")
print(f"\nEl promedio total de toda la sumatoria es: {promedio}\n")