for n in range (2,10):
    for i in range (2,n):
        if n % i == 0:
            print(f"{n} es un  numero compuesto, divisible por {i}")
            break
    else:
        print(f"{n}es un numero primo")