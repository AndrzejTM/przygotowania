def quicksort(lista):
    # Jeśli lista ma 1 lub 0 elementów, jest już posortowana
    if len(lista) <= 1:
        return lista
    else:
        # Wybieramy pierwszy element jako pivot
        pivot = lista[0]
        # Podział listy na mniejsze/równe pivotowi oraz większe od pivota
        mniejsze = [x for x in lista[1:] if x <= pivot]
        wieksze = [x for x in lista[1:] if x > pivot]
        # Rekurencyjne sortowanie i łączenie wyników
        return quicksort(mniejsze) + [pivot] + quicksort(wieksze)

# Przykład użycia:
lista = [4, 10, 7, 8, 1, 6, 5]
posortowana_lista = quicksort(lista)
print("Posortowana lista:", posortowana_lista)