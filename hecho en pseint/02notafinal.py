"""
El estudiante debe ingresar su nota final. Si es mayor o igual a 4.0, se muestra “Aprobado”, 
en caso contrario, “Reprobado”. 
"""
notaf = float(input(f"\ningrese su nota final:\n"))
if notaf <= 0 or notaf > 7.0:
    print("nota mal ingresada\n")
elif notaf >= 4.0: print("aprovado\n")

else:
    print("reprobado\n")