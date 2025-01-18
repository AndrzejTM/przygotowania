lista1 = list(range(12))

def suma_liczb():
    suma = sum(lista1[x] for x in range(0, 12, 2))
    print(suma)

suma_liczb()




