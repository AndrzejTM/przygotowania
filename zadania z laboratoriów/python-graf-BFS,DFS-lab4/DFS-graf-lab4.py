# Definicja grafu, gdzie klucze to węzły, a wartości to listy sąsiadów
graf = {
    'A': ['B', 'C', 'D', 'F'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'C'],
    'E': ['B', 'F'],
    'F': ['C', 'A', 'E'],
    'G': ['B', 'D']
}


# Funkcja implementująca algorytm przeszukiwania w głąb (DFS)
def przeszukiwanie_w_glab(graf, wezel_startowy, odwiedzone=None):
    # Jeśli zbiór odwiedzonych węzłów jest pusty, inicjalizujemy go jako pusty zbiór
    if odwiedzone is None:
        odwiedzone = set()

    # Dodajemy bieżący węzeł do zbioru odwiedzonych
    odwiedzone.add(wezel_startowy)

    # Drukujemy odwiedzony węzeł
    print(wezel_startowy, end=" ")

    # Dla każdego sąsiada bieżącego węzła w grafie
    for sasiad in graf.get(wezel_startowy, []):
        # Jeśli sąsiad nie został jeszcze odwiedzony
        if sasiad not in odwiedzone:
            # Rekurencyjnie wywołujemy funkcję DFS dla sąsiada
            przeszukiwanie_w_glab(graf, sasiad, odwiedzone)


# Wywołanie funkcji DFS z grafem i węzłem początkowym 'E'
przeszukiwanie_w_glab(graf, 'E')
