# TIPO DE PASO DE ARGUMENTOS EN FUNCIONES

# 01. ARGUMENTOS POSICIONALES
print("========== ARGUMENTOS POSICIONALES ==========")
def suma(a, b):
    return a + b

# Llamada a la función con argumentos posicionales: 2 + 4, 3 + b
resultado = suma(2, 3)  # El orden sí importa: a=2, b=3  
print(resultado)

# 02. ARGUMENTOS CON VALOR POR DEFECTO
print("\n========== ARGUMENTOS CON VALOR POR DEFECTO ==========")

# Definición de la función 'resta' con parámetros por defecto (b = 5)
def resta(a, b=5, c=1):
    return a - b - c

# Caso 1: Usando solo el argumento obligatorio 'a' (b tomará su valor por defecto: 5)
resultado1 = resta(6, 4, 2)  # Equivalente a suma(6, 5)
print("Caso 1 (b por defecto):", resultado1)  # 6 - 5 = 1

# Caso 2: Pasando ambos argumentos (ignora el valor por defecto de 'b')
resultado2 = resta(4, 4)  # a=4, b=4
print("Resultado 2 (b personalizado):", resultado2)  # 4 - 4 = 0

# 03. ARGUMENTOS POR NOMBRE (KEYWORDS)
print("\n========== ARGUMENTOS POR NOMBRE ==========")
def calcular_potencia(base, exponente):
    return base ** exponente

# Llamada con argumentos por nombre (el orden no importa)
resultado = calcular_potencia(exponente=3, base=2)
print(resultado)