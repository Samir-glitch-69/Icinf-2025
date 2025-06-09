'''Construir un programa que calcule e imprima la sumatoria:
 S =500+456+510+454+520+452+...+800'''
#hay dos patrones el 500 que va sumando 10 cada vez y el 456 que va restando de 2 en 2

s = 0
a = 500
b = 456

while a <= 800:
    s += a 
    print("Sumando:",a)
    a += 10
    
    if b >= 0:
        s += b
        print("Sumando:",b)
        b -= 2
print("La suma total es de:",s)
