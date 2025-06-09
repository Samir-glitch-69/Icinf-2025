'''Construir un programa que calcule e imprima la sumatoria:
 S =500+456+510+454+520+452+...+800'''
#hay dos patrones el 500 que va sumando 10 cada vez y el 456 que va restando de 2 en 2

s = 0
a = 500
b = 456

suma_a = 0
suma_b = 0



while a <= 800:
    s = s + a
    suma_a = suma_a + a
    print("\nSumandole 10 al:",a)
    a += 10
    
    if b >= 0:
        s = s + b
        suma_b = suma_b + b
        print("\nRestandole 2 al:",b)
        b = b - 2

print("\nLa suma total de los valores de 500 de 10 en 10 es:",suma_a)
print("\nLa resta total de los valores de 456 de 2 en 2 es:",suma_b)
print("\nEstos dos valores sumados son:",s) 
print()