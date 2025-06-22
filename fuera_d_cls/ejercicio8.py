"""crear una lista de productos con sus precios usar un bucle para encontrar el producto mas caro"""

productos = [5, 2, 10, 15]

#inicializa el valor máximo
mas_caro = productos[0]

#recorre la lista
for precio in productos:
    if precio > mas_caro:
        mas_caro = precio

print("el producto más caro cuesta:", mas_caro)