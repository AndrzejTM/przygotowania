def dijkstra_macierz(graf, start):
    n = len(graf)  # Liczba wierzchołków
    dystanse = [float('inf')] * n  # Inicjalizujemy maksymalne odległości jako "nieskończoność"
    odwiedzone = [False] * n  # Informacja, czy wierzchołek został odwiedzony
    dystanse[start] = 0  # Dystans do wierzchołka startowego wynosi 0

    for _ in range(n):
        # Wybór wierzchołka o minimalnym dystansie
        min_dystans = float('inf')
        min_index = -1
        for i in range(n):
            if not odwiedzone[i] and dystanse[i] < min_dystans:
                min_dystans = dystanse[i]
                min_index = i

        # Zaznaczamy wierzchołek jako odwiedzony
        obecny = min_index
        if obecny == -1:  # Jeśli nie ma dostępnego wierzchołka, przerywamy
            break
        odwiedzone[obecny] = True

        # Aktualizacja dystansów do sąsiadów
        for sasiad in range(n):
            if graf[obecny][sasiad] > 0 and not odwiedzone[sasiad]:
                nowy_dystans = dystanse[obecny] + graf[obecny][sasiad]
                if nowy_dystans < dystanse[sasiad]:
                    dystanse[sasiad] = nowy_dystans

    return dystanse

# Przykładowa macierz sąsiedztwa dla grafu z 10 wierzchołkami
graf = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2, 0],
    [0, 0, 7, 0, 9, 14, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6, 0],
    [8, 11, 0, 0, 0, 0, 1, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 6, 7, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 9, 0]
]

# Wierzchołek startowy (indeks)
startowy = 0  # Wierzchołek 0

# Wywołanie algorytmu
dystanse = dijkstra_macierz(graf, startowy)

# Wynik
print("Najkrótsze odległości od wierzchołka startowego:")
for i, d in enumerate(dystanse):
    print(f"Wierzchołek {i}: {d if d != float('inf') else 'Brak połączenia'}")
