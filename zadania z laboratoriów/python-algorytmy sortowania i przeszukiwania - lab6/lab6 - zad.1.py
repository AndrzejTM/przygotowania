lista = [7, 8, 2, 11, 5, 1, 4, 9, 11, 8, 5, 2, 11, 1]

def wyszukiwanie_liniowe(lista, szukany):
    lista_wyszukanych = list()
    for indeks, element in enumerate(lista):
        if element == szukany:
            lista_wyszukanych.append(indeks)
    return lista_wyszukanych

lista_szukanych = wyszukiwanie_liniowe(lista, 11)
print(lista_szukanych)


