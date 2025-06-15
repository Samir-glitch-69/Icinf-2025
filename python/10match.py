opcion = input('por farvor, elige una opcion (1-3): ')

match opcion:
    case "1":
        print("haz elegido una hamburfuesa. precio: $5000")
    case "2":
        print("has elegido pizza. precio: $7500")
    case "3":
        print("nose")
    case _:
        print("malo")

#determinar estacion segun mes
mes = 4 #abril 
match mes:
    case 12 | 1 | 2:
        print("verano")
    case 3 | 4 | 5:
        print('otoño')
    case 6 | 7 | 8:
        print('primavera')
    case 9 | 10 | 11:
        print('invierno')
    case _:
        print('mes mal ingresado')

#toda respuesta invalida que esceda o incorrecta es con el guion bajo _ el cual funciona como
#mal ingresado

x = [1, 2, 3]
match x:
    case[a, b, c]:
        print(f'elementos de la lista x: {a}, {b}, {c}')

datos = {'nombre': 'viktor', 'edad': 31}
match datos:
    case {'nombre': n, 'edad': e}:
        print(f'Nombre: {n}, edad: {e}')

#guards 
valor = 6
"""guards subclase de los match case"""
entrada = input('ingrese un valor entero:')#valo ingresado string

try:
    numero = int(entrada)
    print(f'numero ingresado: {numero}')
except ValueError:
    print('error de valor: el valor ingresado no es entero')
except Exception as e:
    print(f'error inesperado: {e}')
else:
    print('¿conversion fue exitosa!')
finally:
    print('finalizacion del bloque')