import random
import time

# Sortowanie bąbelkowe
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Sortowanie przez wstawianie
def insertion_sort(lista):
    for i in range(1, len(lista)):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > klucz:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = klucz

# QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    lewa = [x for x in lista if x < pivot]
    rowne = [x for x in lista if x == pivot]
    prawa = [x for x in lista if x > pivot]
    return quicksort(lewa) + rowne + quicksort(prawa)

# Porównanie czasu działania
def compare_algorithms():
    rozmiary = [10, 100, 1000]  # Różne rozmiary list
    for rozmiar in rozmiary:
        lista = [random.randint(1, 1000) for _ in range(rozmiar)]

        # Kopie listy, aby sortować te same dane
        lista_bubble = lista[:]
        lista_insertion = lista[:]
        lista_quick = lista[:]

        print(f"\nRozmiar listy: {rozmiar}")

        # Bubble Sort
        start = time.time()
        bubble_sort(lista_bubble)
        print(f"Bubble Sort: {time.time() - start:.5f} s")

        # Insertion Sort
        start = time.time()
        insertion_sort(lista_insertion)
        print(f"Insertion Sort: {time.time() - start:.5f} s")

        # QuickSort
        start = time.time()
        lista_quick = quicksort(lista_quick)
        print(f"QuickSort: {time.time() - start:.5f} s")

compare_algorithms()
