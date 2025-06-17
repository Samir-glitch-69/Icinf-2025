# 1. Definir Inventario
inventario = {
    "Manzana": (1200, 1150, 1250),
    "Platano": (900, 850, 900),  # Dos precios repetidos y uno diferente
    "Cereza": (3500, 3600, 3450)
}

# 2. Precios Únicos para una fruta concreta (Platano)
# Convertimos la tupla a un set para eliminar duplicados, y luego a una lista
precios_platano_unicos = list(set(inventario["Platano"]))

# 3. Generar una lista con todos los tipos de fruta
tipos_frutas = list(inventario.keys())

# 4. Calcular el precio promedio de los valores únicos de esa fruta (Platano)
promedio_platano = sum(precios_platano_unicos) / len(precios_platano_unicos)

# Mostrar Resultados
print("Diccionario completo de inventario:")
print(inventario)
print("\nValores únicos del precio del plátano:")
print(precios_platano_unicos)
print("\nLista de tipos de frutas:")
print(tipos_frutas)
print("\nPromedio de los valores únicos del precio del plátano:")
print(f"{promedio_platano:.3f}")