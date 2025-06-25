#SAMIR Y CAMILO


#Se pide el string del resumen de papers cientificos 
resumen = str(input('Ingrese su resumen para escanear con un maximo de 50 caracteres:\n'))
#se crea la longitud del len
longitud = len(resumen)
#se crea una indicacion para saber si escede 50 caracteres 
Limite = bool
print(f'es menor o igual a 50 caracteres, True') if longitud >= 50 else print(f'excede los 50 caracteres, False')
#se imprime la longitud del len
print(longitud)
#el resumen en mayuscula
mayus = resumen.upper()
#resumen en minuscula
minus = resumen.lower()

#imprimir en mayuscula
print ("este es el resumen en mayuscula:")
print (mayus)

#imprimir en minuscula
print ("este es el resumen en minuscula:")
print (minus)

#se crea una variable (e)
e = str
#numero de veces que aparece la vocal e
print ("esta es la cantidad de veces que se repite la vocal e:") 
rep_e = (resumen.count ("e"))
print (rep_e)


#primeros 15
primerosC =(resumen.ljust(15))
#ultimos 15
ultimosC =(resumen.rjust(15))

print("primeros 15 caracteres:", primerosC)
print ('ultimos 15 caracteres:', ultimosC)
