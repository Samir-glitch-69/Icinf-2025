#SAMIR Y CAMILO



#pedir por consola los datos de las 4 herramientas
print("gestion de stock de ferreteria\n")

print ("ingresa los precios base de cada herramienta\n")
P_martillo = float(input("precio de martillo:"))
P_clavo = float(input("precio de clavo:"))
P_serrucho = float(input("precio de serrucho:"))
P_tornillo = float(input("precio de tornillo:"))
    
print ("listo ,ahora ingrese la cantidad de herramientas\n ")
U_martillo = float(input("Cantidad de unidades de martillos:"))
U_clavo = float(input("Cantidad de unidades de clavo:"))
U_serrucho = float(input("Cantidad de unidades de serrucho:"))
U_tornillo = float(input("Cantidad de unidades de tornillo:"))

#Calculo e impresion de subtotales
subM = P_martillo * U_martillo
subC = P_clavo * U_clavo
subS = P_serrucho * U_serrucho
subT = P_tornillo * U_tornillo

#impresion de los subtotales de las herramientas
print ("Precio total de los martillos", round(subM,2))
print ("Precio total de los clavos", round(subC,2))
print ("Precio total de los serruchos", round(subS,2))
print ("Precio total de los tornillos", round(subT,2))

#calcular e imprimir el total entre todas las herramientas
subTOTAL = subM + subC + subS + subT

# no dice especificamente redondead el total 
print ("la suma de todo es de:", subTOTAL)

#se dice el precio mayor de los subtotales
print('el costo mayor es de: ')
print(max(subM,subC,subS,subT))

#se dice el precio menor de los subtotales
print('el costo menor es de: ')
print(min(subM,subC,subS,subT))


#formulas para saber el promedio de los precios unitarios de las herramientas redondeados a 2 decimales 
promedio_M = subM/U_martillo
promedio_C = subC/U_clavo
promedio_S = subS/U_serrucho
promedio_T = subT/U_tornillo

#se redondea a 2 decimales

print(f'estos son los promedio de los valores de unidad de las diferentes herramientas:')
print(f'Martillo: {round(promedio_M,2)}')
print(f'Clavo: {round(promedio_C,2)}')
print(f'Serrucho: {round(promedio_S,2)}')
print(f'Tornillo: {round(promedio_T,2)}')

#el % en iva del total de las herramientas 
iva = subTOTAL * 0.19
print(f'El iva es de: {iva}')