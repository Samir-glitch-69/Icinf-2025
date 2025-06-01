#creando diccionatio 

paciente = { 
    'nombre':'ignacio', 
    'apellido':'alvaarez',
    'edad': 88,
    'ciudad': 'melipilla',
    'consultas':[14, 20, 40]
}
#se pueden añadir funciones, listas, diccionarios dentro de los diccionarios ya hechos
#esto entra en el parcial 

#otra forma de declarar diccionario 

medico = dict(
    nombre = 'samir',
    apellido = 'arana',
    edad = 20,
    especialidad = 'neurologo'
)

#impresion de diccionarios 
print(paciente)
print(medico)

#consultando un elemento a traves de la clave del diccionario
print(medico['nombre'])

#eliminando una clave del diccionario (metodo del)
del(paciente['nombre'])
print(paciente)
