lista1 = ['samir', 19, True]
#dentro de los list no pueden haber datos iguales corchetes

#lista vacia 
frutas = []

#lista de solo numeros

n = [1,2,3,4,5,6]

#lista de solo strings - ulitizando la funcion list 
ramos = list(['programacion' , ' quimica', 'poo'])

#imprime la posicion del primer elemento de la lista ( no el caracter )
print(ramos[0])

#cuenta la cantidad de concurrencias de un elemento las concurrencias son cuantas veces se repite un dato o elemento
print(ramos.count('programacion'))

#mutables tuplas que no son mutables osea mas que decir que no pueden cambiar amedida que va el codigo
#no se puee agregar cambiar ni borrar ningun tipo de dato 

#creando e instanciando una tupla 
#esta usa parentesis

estudiantes = ('samir', 'hector', 'matias','carlos')

print(estudiantes)

# index es una funcion que me indica la posicion de un elemento 

print(estudiantes.index('carlos'))

#los set son colleciones no ordenadas de elementos cuando se dice que no se ordena no se puede 
#consultar donde esta ubicado el elemento sin elementos iguales 
#el set es con llaves 

colores = {'azul', 'rojo', 'azul', 'verde'}

#funcion de append va en listas esto añade un elemento a las listas al fina
ramos.append('introducción a la matemáticas')
print(ramos)

#modificar elementos a la lista 
ramos[0] = 'comunicacion' 
print(ramos)

#otra dorma de modificar elementos a la lista aqui se pasan 2 elementos done y el valor
ramos.insert(0,"álgebra")

#elminar el ultimo elemento de la lista
ramos.pop()
print(ramos)

#ordenando elementos de una lista descendente y ascendente 
ramos.sort()
print(ramos)

#ordenando elementos de una lista segun su cantidad de caracteres
ramos.sort(key=len)
print(ramos)

#key es una propiedad de la funcion sort y
#len es la cantidad de caracteres que hay dentro de un stirng

#ocupando el metodo extend
#añade una lista a otra combinandolas pero sin borrarlas solo ufnciona para las listas
ramos.extend(n)
print(ramos)
