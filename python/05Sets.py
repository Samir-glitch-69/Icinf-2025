#creando sets
colores = {'azul', 'rijo', 'azul', 'verde'}
colorcitos = {'azul', 'naranjo'}

#imprimiendo
print(colores)

#aplicando el metodo difference
diferencia = colores.difference(colorcitos) 
print(diferencia)

#agregando u nuevo elemento al set (metodo add)
colores.add('blanco')
print(colores)

#eliminando un elemento del set 
colores.discard('blanco')
print(colores)