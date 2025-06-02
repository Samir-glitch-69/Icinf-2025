'''
Crear un algoritmo que permita manipular cadenas de texto:
A. Ingresar una frase de máximo 30 caracteres.
B. Generar dos nuevas variables: una en mayúsculas y otra en minúsculas.
C. Utilizar un método propio para determinar cuántas veces aparece la letra «a» (tanto «a»
como «A») en la frase, y muestra el total.
D. Emplear otro método para imprimir la longitud de la frase original.
'''
# se solicita la frase para manipular
frase = str(input('Hola dame una frase entre 0 a 30 caracteres porfavor \n'))[0:30]
# se confirma la frase
print(f'su frase es: {frase}')
#longitud y cantidades 
longitud = len(frase)
A = 'A'
a = 'a'
cantidad_de_A = frase.count(A)
cantidad_de_a = frase.count(a)
#se imprime la longitud con sus respectivas mayusculas
print(f'La longitud del texto es {longitud} y la cantidad de a son {cantidad_de_a} y A son {cantidad_de_A}')