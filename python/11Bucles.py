#01 while 
edad = 15 
num = 0 

#bucle infinito 
# """
# while edad < 18:
#   print("eres menor de edad, no puedes manejar")
# "
#el codigo no tiene limite entonces hace el loop infinito

#bucle infinito 2 
#"""shile true: 
#   print(num)
#    num += 2"

#bucle normal de impresion de numeros de 0 a 100 en 2 en 2
num = 0
while num <= 100: 
    print(num)
    num += 2 
    #num = num +2 
print("Primer bucle terminado!!")

#combinando while y else de 100 al 200 de 2 en 2 con else

while num <= 200:
    print(num)
    num += 2 
else: 
    print("mi condicion es igual o mayor a 200")
    print("segundo blucle terminado")

#siempre una manera de cerrar el bucle para evitar bucles infinitos 
# con break quiebra el bucle o else 
#"""
# while True:
#   parametro = input(">")
#   if parametro == "exit":
#       break 
#   else:
#       print(parametro) 
#"
print()
#imprime una lista del 1 al 10 no imprime el limite del intervalo 
for i in range(1,11): 
    print(i)
print()
# el digito de la derecha es para contar  de dos en dos o en otras cantidades 
for i in range(1,11,2):
    print(i)
print()
for i in range(2,21,4):
    print(i)