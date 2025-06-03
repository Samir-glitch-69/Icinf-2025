'''
A. Ingresar el peso de un paquete en kilogramos (float).
B. Si el peso es menor o igual a 5 kg, el costo es $500.
C. Si es más de 5 kg, el costo es $500 + $100 por cada kilo extra.
D. Mostrar el peso y el costo total del envío en un solo print().
'''
paquete = float(input('Dame el valor en kg de el paquete\n'))
total = paquete * 100
if total <= 500:
    total = 500
print(f'El peso total es: {paquete} y el costo total del envio es: {total}')