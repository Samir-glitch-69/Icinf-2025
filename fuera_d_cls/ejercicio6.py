"""crear un programa que recorra una lista de frutas e imprima solo las que empiecen con "a" """
print("Ingrese la cantidad de frutas que quiere identificar con la letra principal: a")
print('Ingrese exactamente la frase "exit" para poder salir e identificar')

# Se crea la lista
lista = []

# Se crea un bucle para tomar las frutas y llevarlas a la lista
while True:
    valor = input("Fruta: ")
    if valor.lower() == "exit":
        break
    lista.append(valor)

# Se imprimen las frutas que empiezan con "a"
print("\nFrutas que empiezan con la letra 'a':")
for fruta in lista:
    if fruta.lower().startswith("a"):
        print(fruta)