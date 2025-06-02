#Crear un algoritmo que sirva de Conversor de Temperatura:
#A. Solicitar por consola una temperatura en grados Celsius (números flotantes)
#B. Calcular su equivalente en grados Fahrenheit y Kelvin utilizando las fórmulas
#correspondientes.
#C. Mostrar los tres valores en pantalla, redondeados a 2 decimales.

#se identifica celcius como float y se pide el dato
celcius = float(input('Dame el valor de los grados celcius: '))
#se calcula los fahrenheit y kelvin con sus respectivas formulas
fahrenheit = (celcius * (9/5)) + 32
kelvin = celcius + 273.15
#se imprime en la consola los diferentes resultados 
print(f" Su valor en celcius es: {round(celcius,2)} \n valor transformado en fahrenheit es: {round(fahrenheit,2)}\n Su valor en Kelvin es: {round(kelvin,2)}")
