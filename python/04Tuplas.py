#creando e instanciando una tupla 
estudiantes = ('samir', 'matias', 'hector', 'pia', 'carkis', True)

#imprimiendo una tupla
print(estudiantes)

#eliminando el ultimo elemento de la tupla 
estudiantes.pop()
print(estudiantes)

'''estudiantes.pop()
print(estudiantes)

estuidantes = ('contanza')
print(estudiantes)'''

# las duplas no se pueden modificar inmutables

#metodo index indica la posicion del elemento 
print(estudiantes.index('carlos'))

#metodo sorted en tuplas ordena elementos en una tupla 
print(sorted(estudiantes))
