from collections import deque

graf = {
'A': ['B', 'C', 'D', 'H'],
'B': ['A', 'C', 'F'],
'C': ['A', 'B', 'D', 'G','H', 'J'],
'D': ['A', 'C', 'H', 'J'],
'E': ['F', 'J', 'G'],
'F': ['B', 'E', 'J', 'G'],
'G': ['C','D'],
'H': ['D', 'F', 'C'],
'I': ['J'],
'J': ['F', 'E', 'I']
}

def oblicz_stopien(graf):
    stopnie = {}
    for osoba, sasiedzi in graf.items():
        stopnie[osoba] = len(sasiedzi)  # Stopień węzła to liczba sąsiadów
    return stopnie

def znajdz_osoby_z_max_min_stopniem(stopnie):
    max_osoba = max(stopnie, key=stopnie.get)  # Osoba o najwyższym stopniu
    min_osoba = min(stopnie, key=stopnie.get)  # Osoba o najniższym stopniu
    return max_osoba, stopnie[max_osoba], min_osoba, stopnie[min_osoba]


def czy_polaczone(graf, wierzcholek1, wierzcholek2):
    """
    Sprawdza, czy dwa wierzchołki są bezpośrednio połączone w grafie.
    :param graf: Słownik reprezentujący graf.
    """
    # Sprawdzenie, czy wierzchołek1 istnieje w grafie
    if wierzcholek1 in graf:
        # Sprawdzenie, czy wierzchołek2 jest w sąsiedztwie wierzchołka1
        if wierzcholek2 in graf[wierzcholek1]:
            return True
    return False

def czy_skierowany(graf):
    """
    Sprawdza, czy graf jest skierowany.

    :param graf: Słownik reprezentujący graf jako listę sąsiedztwa.
    :return: True, jeśli graf jest skierowany, False jeśli jest nieskierowany.
    """
    for wierzcholek, sasiedzi in graf.items():
        for sasiad in sasiedzi:
            # Sprawdź, czy istnieje odwrotna krawędź
            if wierzcholek not in graf.get(sasiad, []):
                return True  # Graf jest skierowany
    return False  # Graf jest nieskierowany


def czy_spojny(graf):
    """
    Sprawdza, czy skierowany graf jest silnie spójny.

    :param graf: Słownik reprezentujący graf jako listę sąsiedztwa.
                 Przykład: {1: [2], 2: [3], 3: [1]}
    :return: True, jeśli graf jest silnie spójny, False w przeciwnym razie.
    """

    def dfs(wierzcholek, odwiedzone):
        """
        Funkcja pomocnicza do przeszukiwania w głąb (DFS).
        """
        odwiedzone.add(wierzcholek)
        for sasiad in graf.get(wierzcholek, []):
            if sasiad not in odwiedzone:
                dfs(sasiad, odwiedzone)

    wierzcholki = list(graf.keys())
    if not wierzcholki:
        return True  # Pusty graf jest spójny

    # Sprawdź spójność z pierwszego wierzchołka
    odwiedzone = set()
    dfs(wierzcholki[0], odwiedzone)

    if len(odwiedzone) != len(wierzcholki):
        return False  # Nie wszystkie wierzchołki osiągalne

    # Odwróć graf
    graf_odwrocony = {w: [] for w in graf}
    for w, sasiedzi in graf.items():
        for sasiad in sasiedzi:
            graf_odwrocony[sasiad].append(w)

    # Sprawdź spójność w odwróconym grafie
    odwiedzone.clear()
    dfs(wierzcholki[0], odwiedzone)

    return len(odwiedzone) == len(wierzcholki)


def czy_cykliczny(graf):
    """
    Sprawdza, czy w skierowanym grafie istnieje cykl.

    :param graf: Słownik reprezentujący graf jako listę sąsiedztwa.
    :return: True, jeśli graf zawiera cykl, False w przeciwnym razie.
    """

    def dfs(wierzcholek, odwiedzone, stos_rekurencji):
        odwiedzone.add(wierzcholek)  # Oznacz wierzchołek jako odwiedzony
        stos_rekurencji.add(wierzcholek)  # Dodaj wierzchołek do stosu rekurencji

        for sasiad in graf.get(wierzcholek, []):
            if sasiad not in odwiedzone:  # Jeśli sąsiad nie był odwiedzony, rekurencja
                if dfs(sasiad, odwiedzone, stos_rekurencji):
                    return True
            elif sasiad in stos_rekurencji:  # Jeśli sąsiad jest w stosie rekurencji, mamy cykl
                return True

        stos_rekurencji.remove(wierzcholek)  # Usuń wierzchołek ze stosu po zakończeniu DFS
        return False

    odwiedzone = set()
    stos_rekurencji = set()

    for wierzcholek in graf:
        if wierzcholek not in odwiedzone:
            if dfs(wierzcholek, odwiedzone, stos_rekurencji):
                return True

    return False


def odleglosc_miedzy_wierzcholkami(graf, start, cel):
    """
    Oblicza odległość (najkrótszą ścieżkę) między dwoma wierzchołkami w grafie.

    :param graf: Słownik reprezentujący graf jako listę sąsiedztwa.
    :param start: Wierzchołek początkowy.
    :param cel: Wierzchołek końcowy.
    :return: Liczba całkowita reprezentująca odległość między wierzchołkami
             lub -1, jeśli wierzchołki nie są połączone.
    """
    if start == cel:
        return 0  # Odległość do samego siebie wynosi 0

    odwiedzone = set()
    kolejka = deque([(start, 0)])  # Kolejka przechowująca pary (wierzchołek, odległość)

    while kolejka:
        wierzcholek, odleglosc = kolejka.popleft()

        if wierzcholek == cel:
            return odleglosc  # Znaleźliśmy wierzchołek docelowy

        if wierzcholek not in odwiedzone:
            odwiedzone.add(wierzcholek)
            for sasiad in graf.get(wierzcholek, []):
                if sasiad not in odwiedzone:
                    kolejka.append((sasiad, odleglosc + 1))

    return -1  # Jeśli nie ma połączenia między wierzchołkami

stopnie = oblicz_stopien(graf)
print(stopnie)

max_min_stopień = znajdz_osoby_z_max_min_stopniem(stopnie)
print(max_min_stopień)

połączenie = czy_polaczone(graf, "A", "E")
print(połączenie)

czy_graf_jest_skierowanny = czy_skierowany(graf)
print(czy_graf_jest_skierowanny)

spójność = czy_spojny(graf)
print(spójność)

cykliczność = czy_cykliczny(graf)
print(cykliczność)

odległość = odleglosc_miedzy_wierzcholkami(graf, "A", "E")
print(odległość)
