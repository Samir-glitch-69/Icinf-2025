'''
4. Desarrollar un programa de gestión de inventario:
A. Ingresar el nombre de un producto y su precio unitario.
B. Ingresar la cantidad en stock.
C. Calcular el valor total de los productos ingresados y mostrarlo con 2 decimales.
D. Crear una variable booleana llamada umbral, que entregue un True si el valor_total >
100000 y False en caso contrario..
E. Imprimir el nombre del producto, la cantidad, el valor total y el estado umbral en un solo
print() formateado
'''
Nombre = str(input('Ingrese el nombre del producto: \n'))
Pecio_unitario = int(input('Ingrese el precio unitario del producto: \n'))
stock = int(input('Ingrese la cantidad de stock: \n'))

total = stock * Pecio_unitario
print(f'Valor total de el stock: {total:.2f}')
umbral = bool
umbral = True if total > 100000 else umbral = False
print('Su valor escede los 100000' if umbral = True else 