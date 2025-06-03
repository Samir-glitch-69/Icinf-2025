'''
🔢 Ejercicio 1: Conversor de Moneda
A. Solicitar al usuario un monto en pesos argentinos (float).
B. Ingresar el valor del dólar oficial (float).
C. Calcular cuántos dólares obtendría y redondearlo a 2 decimales.
D. Mostrar ambos valores en un print formateado.
'''
peso_arg = float(input('Dame el monto en pesos argentinos\n'))
#1.180,74 Peso argentino son 1 dolar 
#0,00085 Dólar estadounidense es 1 peso argentino 
total_dolars = peso_arg * 0.00085 
print(f'su total en pesos argentinos es: {round(peso_arg,2)} y su valor en dolares es: {round(total_dolars,2)}')