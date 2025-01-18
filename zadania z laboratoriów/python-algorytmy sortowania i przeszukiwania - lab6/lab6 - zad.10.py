import random
import time

# Sortowanie przez scalanie
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    srodek = len(lista) // 2
    lewa = merge_sort(lista[:srodek])
    prawa = merge_sort(lista[srodek:])
    return merge(lewa, prawa)

def merge(lewa, prawa):
    wynik = []
    i = j = 0
    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    return wynik

# Przygotowanie list
rozmiary = [100, 1000, 5000]
struktury = ["losowe", "częściowo posortowane", "odwrotnie posortowane"]

for rozmiar in rozmiary:
    for struktura in struktury:
        if struktura == "losowe":
            lista = [random.randint(1, 1000) for _ in range(rozmiar)]
        elif struktura == "częściowo posortowane":
            lista = sorted([random.randint(1, 1000) for _ in range(rozmiar)])
            lista[-10:] = [random.randint(1, 1000) for _ in range(10)]  # Losowe ostatnie 10 elementów
        elif struktura == "odwrotnie posortowane":
            lista = sorted([random.randint(1, 1000) for _ in range(rozmiar)], reverse=True)

        # Pomiar czasu dla MergeSort
        start = time.time()
        merge_sort(lista)
        czas = time.time() - start
        print(f"Rozmiar: {rozmiar}, Struktura: {struktura}, MergeSort: {czas:.5f} s")
