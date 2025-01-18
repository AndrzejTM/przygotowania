from collections import deque

# Definiujemy graf, gdzie każdy węzeł jest kluczem, a jego sąsiedzi to lista wartości
graf = {
    'A': ['B', 'C', 'D', 'F'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'C'],
    'E': ['B', 'F'],
    'F': ['C', 'A', 'E'],
    'G': ['B', 'D']
}


# Funkcja implementująca algorytm przeszukiwania wszerz (BFS)
def przeszukiwanie_wszerz(graf, wezel_startowy):
    # Tworzymy zbiór odwiedzonych węzłów, żeby uniknąć cykli i powtórzeń
    odwiedzone = set()

    # Tworzymy kolejkę do przetwarzania węzłów (FIFO - First In, First Out)
    kolejka = deque([wezel_startowy])

    # Dodajemy węzeł początkowy do zbioru odwiedzonych
    odwiedzone.add(wezel_startowy)

    # Rozpoczynamy przeszukiwanie wszerz
    while kolejka:
        # Zdejmujemy węzeł z przodu kolejki
        wezel = kolejka.popleft()

        # Drukujemy odwiedzony węzeł
        print(wezel, end=" ")

        # Przechodzimy przez wszystkich sąsiadów aktualnego węzła
        for sasiad in graf.get(wezel, []):
            # Jeśli sąsiad nie został jeszcze odwiedzony, dodajemy go do kolejki
            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)  # Oznaczamy sąsiada jako odwiedzonego
                kolejka.append(sasiad)  # Dodajemy sąsiada do kolejki


# Wywołujemy funkcję z grafem i węzłem początkowym 'F'
przeszukiwanie_wszerz(graf, 'F')
