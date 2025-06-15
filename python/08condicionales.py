# guia de condicionales

from colorama import init, Fore
init()
#condicional if 
print(Fore.CYAN + '############### 01 - utilizando if y else ##############')

licencia = False 
edad = 19 
automovil = False

#¿Estará correcto este codigo?
#incorrecto

print(Fore.YELLOW + '\n>>> testeando los comparadores y el if')
if licencia:
    print(Fore.WHITE + 'puedo conducir porque tengo licencia')
else:
    print(Fore.WHITE + 'No tengo licencia no puedo conducir\n')
print('este print esta fuera del else') # print fuera del bloque else por el tabular 

print(Fore.GREEN + '################ 02 - UTILIZANDO IF, ELIF Y ELSE #################')
if licencia and edad <= 18:
    print(Fore.WHITE + 'puedo conducir por que soy mayor de edad y tengo licencia')
elif automovil:
    print(Fore.WHITE + 'tengo automovil, pero no tengo licencia ni la edad necesaria')
else:
    print(Fore.WHITE + 'no puedo conducir ni tengo la edad, ni licencia ni automovil')