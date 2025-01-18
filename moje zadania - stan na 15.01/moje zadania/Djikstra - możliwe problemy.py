import sys
import heapq
from collections import defaultdict


# Problem 3: Obsługa wierzchołków odizolowanych i nieosiągalnych
def dijkstra_wierzcholki_odizolowane(graf, start):
    """
    Rozwiązanie problemu wierzchołków odizolowanych i nieosiągalnych.
    Zwraca listę dystansów lub informację "Nieosiągalny" dla wierzchołków, do których nie ma połączenia.
    """
    n = len(graf)
    dystanse = [sys.maxsize] * n  # Inicjalizujemy dystanse jako nieskończoność
    odwiedzone = [False] * n
    dystanse[start] = 0

    for _ in range(n):
        min_dystans = sys.maxsize
        min_index = -1
        for i in range(n):
            if not odwiedzone[i] and dystanse[i] < min_dystans:
                min_dystans = dystanse[i]
                min_index = i

        if min_index == -1:  # Nie ma więcej osiągalnych wierzchołków
            break

        obecny = min_index
        odwiedzone[obecny] = True

        for sasiad in range(n):
            if graf[obecny][sasiad] > 0 and not odwiedzone[sasiad]:
                nowy_dystans = dystanse[obecny] + graf[obecny][sasiad]
                if nowy_dystans < dystanse[sasiad]:
                    dystanse[sasiad] = nowy_dystans

    # Formatowanie wyników z uwzględnieniem nieosiągalnych wierzchołków
    return [
        d if d != sys.maxsize else "Nieosiągalny" for d in dystanse
    ]


# Problem 4: Obsługa wielu najkrótszych ścieżek
def dijkstra_wiele_sciezek(graf, start):
    """
    Rozwiązanie problemu wielu najkrótszych ścieżek.
    Zwraca minimalne dystanse oraz liczbę najkrótszych ścieżek do każdego wierzchołka.
    """
    n = len(graf)
    dystanse = [float('inf')] * n
    liczba_sciezek = [0] * n  # Liczba najkrótszych ścieżek do każdego wierzchołka
    dystanse[start] = 0
    liczba_sciezek[start] = 1
    kolejka = [(0, start)]  # (dystans, wierzchołek)

    while kolejka:
        obecny_dystans, obecny = heapq.heappop(kolejka)

        if obecny_dystans > dystanse[obecny]:
            continue

        for sasiad, waga in graf[obecny].items():
            nowy_dystans = obecny_dystans + waga

            if nowy_dystans < dystanse[sasiad]:
                dystanse[sasiad] = nowy_dystans
                liczba_sciezek[sasiad] = liczba_sciezek[obecny]
                heapq.heappush(kolejka, (nowy_dystans, sasiad))
            elif nowy_dystans == dystanse[sasiad]:
                liczba_sciezek[sasiad] += liczba_sciezek[obecny]

    return dystanse, liczba_sciezek


# Problem 6: Znalezienie pełnej ścieżki
def dijkstra_znajdz_sciezke(graf, start, cel):
    """
    Znalezienie pełnej ścieżki od wierzchołka startowego do docelowego.
    Zwraca listę wierzchołków w ścieżce oraz minimalny dystans.
    """
    n = len(graf)
    dystanse = [sys.maxsize] * n
    poprzednicy = [None] * n
    odwiedzone = [False] * n
    dystanse[start] = 0

    for _ in range(n):
        min_dystans = sys.maxsize
        min_index = -1
        for i in range(n):
            if not odwiedzone[i] and dystanse[i] < min_dystans:
                min_dystans = dystanse[i]
                min_index = i

        obecny = min_index
        odwiedzone[obecny] = True

        for sasiad in range(n):
            if graf[obecny][sasiad] > 0 and not odwiedzone[sasiad]:
                nowy_dystans = dystanse[obecny] + graf[obecny][sasiad]
                if nowy_dystans < dystanse[sasiad]:
                    dystanse[sasiad] = nowy_dystans
                    poprzednicy[sasiad] = obecny

    # Odtwarzanie ścieżki
    sciezka = []
    obecny = cel
    while obecny is not None:
        sciezka.append(obecny)
        obecny = poprzednicy[obecny]
    sciezka.reverse()

    return sciezka, dystanse[cel]


# Problem 7: Unikanie ponownego odwiedzania wierzchołków
def dijkstra_ignoruj_odwiedzone(graf, start):
    """
    Unikanie ponownego odwiedzania wierzchołków.
    Ignoruje wierzchołki, które zostały już przetworzone, aby zoptymalizować algorytm.
    """
    n = len(graf)
    dystanse = [sys.maxsize] * n
    odwiedzone = set()
    dystanse[start] = 0
    kolejka = [(0, start)]

    while kolejka:
        obecny_dystans, obecny = heapq.heappop(kolejka)
        if obecny in odwiedzone:
            continue
        odwiedzone.add(obecny)

        for sasiad, waga in graf[obecny].items():
            nowy_dystans = obecny_dystans + waga
            if nowy_dystans < dystanse[sasiad]:
                dystanse[sasiad] = nowy_dystans
                heapq.heappush(kolejka, (nowy_dystans, sasiad))

    return dystanse


# Przykładowe dane wejściowe
graf_macierz = [
    [0, 1, 0, 0],
    [1, 0, 2, 0],
    [0, 2, 0, 3],
    [0, 0, 3, 0]
]

graf_lista = {
    0: {1: 1, 2: 4},
    1: {2: 2, 3: 6},
    2: {3: 1},
    3: {}
}

# Testowanie
print("Problem 3:", dijkstra_wierzcholki_odizolowane(graf_macierz, 0))
print("Problem 4:", dijkstra_wiele_sciezek(graf_lista, 0))
print("Problem 6:", dijkstra_znajdz_sciezke(graf_macierz, 0, 3))
print("Problem 7:", dijkstra_ignoruj_odwiedzone(graf_lista, 0))
