'''
Desarrollar un algoritmo con operaciones mixtas con números complejos:
A. Ingresar tres valores numéricos diferentes (entero, flotante y complejo)
B. Calcular y mostrar:
● Potencia Compleja (Complejo y Entero)
● Suma Mixta (Complejo y Flotante)
● Producto Mixto (Complejo y Entero)
● Módulo de Potencia Compleja. El módulo se realiza utilizando la función abs()
(Variable Potencia Compleja, con 3 decimales)
'''
#se piden los diferentes numeros
n_complejo = complex(input('Dame un numero complejo, ej 2j\n'))
n_flotante = float(input('Dame un numero decimal o flotante, ej 0.5\n'))
n_entero = int(input('Dame un numero entero, ej 5\n' ))
#se hacen las formulas solicitadas
potencia = n_complejo**n_entero
print(f'potencia compleja: {potencia}')
suma_mixta = n_complejo + n_flotante 
print(f'Suma mixa: {suma_mixta}')
Producto_mixto = n_complejo * n_entero
print(f'Producto mixto: {Producto_mixto}')
#se usa el abs que es el valor absoluto el cual no implica el signo 
abs_potencia = abs(potencia)
#se imprime la variable con abs y con solo 3 decimales ( sin round )
print(f'Variable potencia, con 3 decimales {abs_potencia:.3f}')