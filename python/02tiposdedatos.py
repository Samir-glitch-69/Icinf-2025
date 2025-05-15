# Guia de tipos de datos en python 
# 15 de mayo de 2025

# 01 inicializando variables numericas
edad = 31
estatura = 17.1
peso = 75
complejo = 2 + 9j # inicializacion de numero complejo 
complejo2 = complex(1, 4) # inicializacion de numero complejo de otra forma 

print(edad)
print(estatura)
print(peso)
print(complejo)
print(complejo2)

# 02 operacion aritmetica 
imc = peso / (estatura ** 2)
print(f"su imc es: {imc}")
# el ** es una numero elevado y hay una extension de pwn que hace el signo
# la f es parte del print/string para poder tener las variables dentro de llaves
#({[]}) son diferentes con diferentes funciones y nombres
#() parentesis
#{} llaves
#[] corchetes

# operacion de salida del resultado 

# el dos se puede cambiar a la cantidad de decimales que uno quiere

# float es un traspaso a un numero x a decimal mutandolo 
# 03 formato de salida del resultado metodo format 
print("su imc es: {:.2f}".format(imc))
# formato de salida del resultado f-string y :.2f
print(f"su imc es: {imc:.2f}")
#round redondea los decimales a una cantidad entregada 

# 04 datos de tipo string (cadenas de texto) 
universidad = "universidad de los lagos chiloe "
carrera = "ingenieria civil en informatica"
asignatura = "porgramacion"
#ventajas d los comentarios es que cuando se usa ''' o """ se pude mover entre lineas de codigo 
descripcion = ''' esta asignatura es del primer semestre '''

# impresion de caraceres en una cadena de textp

#el corchete cuando se usa en un string es seleccionar la letra o simbolo en especifico para imprimirlo si se 
#sobre pasa el caracter seleccionado da error y si es negativo es de derecha a izquierda ( al reves )
print(carrera[0]) # va de izquierda a derecha para seleccionar
print(carrera[-1]) # va de derecha a izquierda para seleccionar



print ("hola" * 4)
#print ("hola / 4") no se 

#el split() genera un arreglo de string palabra por palabra de una frase "universidad de los lagos"
#4 palabras 
#como ver cuantas palabras tiene un split en especifica
#el split es un arreglo no una palabra clave como print

# utilizando el intervalo de una cadena 
print(asignatura[0:1])
#utilizando el metodo de split 
print(descripcion.split())
# arreglo numerico
v = [1, 2, 3, 4, 5]#un arreglo numerico
print(v[0])# el valor 0 indica la posicion del primer elemento ( indice ) 