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

#se piden las diferentes variables para su uso posterior 
nombre = input('Nombre del producto: ')
precio = float(input('Precio unitario: '))
cantidad = int(input('Cantidad en stock: '))
#formula para saber el total
total = precio * cantidad
#se imprimen los diferentes resultados y si es mayo o menor a 100000 con un if else ( la condicion va al medio )
print(f'{nombre} - Cantidad: {cantidad}, Total: ${total:.2f}, Estado: {"Mayor a 100000" if total > 100000 else "Menor o igual a 100000"}')