'''
1. Contar las repeticiones de una palabra en una tupla:
a) Lea el parrafo. Este debe ser ingresado por teclado. ´
b) Separe sus palabras y debe guardarlas en una lista.
c) Solicite al usuario una palabra a buscar.
d) Imprima cuantas veces aparece dicha palabra (Debe ser sensible a may ´ usculas y ´
minusculas). ´
Requisito especial: Si el parrafo est ´ a vac ´ ´ıo, debe lanzar y capturar una excepcion (Va- ´
lueError) indicando “El texto no puede estar vac´ıo”.
'''
'''Universidad de los lagos es muy wena por que los lagos son los lagos // este es el parrafo que usamos'''

#se ingresa el parrafo a revisar
parrafo = input('\nIngrese su parrafo a revisar: ').lower() 

if parrafo.strip() == "":
    raise ValueError("\nEl texto no puede estar vacio")


#se separa las palabras dentro del parrafo
print("\nPalabras separadas en lista: ",parrafo.split())

palabra_a_buscar = input("\nIngrese una palabra que desee buscar y saber cuantas veces aparece en el parrafo: ").lower()

print("\nLa palabra:",palabra_a_buscar.upper(),"aparece",parrafo.count(palabra_a_buscar),"veces\n")

