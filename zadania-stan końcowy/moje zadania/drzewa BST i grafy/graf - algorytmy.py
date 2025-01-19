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

graf_wazony = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('E', 3)],
    'D': [('B', 10), ('E', 4), ('F', 11)],
    'E': [('C', 3), ('D', 4), ('F', 8), ('G', 5)],
    'F': [('D', 11), ('E', 8), ('H', 2)],
    'G': [('E', 5), ('H', 3), ('I', 6)],
    'H': [('F', 2), ('G', 3), ('I', 7), ('J', 4)],
    'I': [('G', 6), ('H', 7), ('J', 3)],
    'J': [('H', 4), ('I', 3)]
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


from collections import deque


# 1. Wyznaczanie wszystkich ścieżek między dwoma wierzchołkami
def wszystkie_sciezki(graf, start, cel):
    """
    Znajduje wszystkie ścieżki między dwoma wierzchołkami w grafie.

    :param graf: Słownik reprezentujący graf jako listę sąsiedztwa.
    :param start: Wierzchołek początkowy.
    :param cel: Wierzchołek końcowy.
    :return: Lista wszystkich ścieżek jako listy wierzchołków.
    """

    def dfs(sciezka, wierzcholek):
        if wierzcholek == cel:
            sciezki.append(list(sciezka))
            return
        for sasiad in graf.get(wierzcholek, []):
            if sasiad not in sciezka:
                sciezka.append(sasiad)
                dfs(sciezka, sasiad)
                sciezka.pop()

    sciezki = []
    dfs([start], start)
    return sciezki


# 2. Sortowanie topologiczne
def sortowanie_topologiczne(graf):
    """
    Wykonuje sortowanie topologiczne na grafie skierowanym acyklicznym (DAG).

    :param graf: Słownik reprezentujący graf jako listę sąsiedztwa.
    :return: Lista wierzchołków w kolejności topologicznej.
    """

    def dfs(wierzcholek):
        odwiedzone.add(wierzcholek)
        for sasiad in graf.get(wierzcholek, []):
            if sasiad not in odwiedzone:
                dfs(sasiad)
        stos.append(wierzcholek)

    odwiedzone = set()
    stos = []
    for wierzcholek in graf:
        if wierzcholek not in odwiedzone:
            dfs(wierzcholek)

    return stos[::-1]


# 3. Liczba spójnych składowych
def liczba_spojnych_skladowych(graf):
    """
    Liczy liczbę spójnych składowych w grafie nieskierowanym.

    :param graf: Słownik reprezentujący graf jako listę sąsiedztwa.
    :return: Liczba spójnych składowych.
    """

    def dfs(wierzcholek):
        odwiedzone.add(wierzcholek)
        for sasiad in graf.get(wierzcholek, []):
            if sasiad not in odwiedzone:
                dfs(sasiad)

    odwiedzone = set()
    licznik = 0
    for wierzcholek in graf:
        if wierzcholek not in odwiedzone:
            dfs(wierzcholek)
            licznik += 1
    return licznik


# 4. Minimalne drzewo rozpinające (MST) - Algorytm Kruskala
def mst_kruskal(graf_wazony):
    """
    Znajduje minimalne drzewo rozpinające (MST) dla grafu ważonego.

    :param graf_wazony: Lista krawędzi w postaci (waga, wierzcholek1, wierzcholek2).
    :return: Lista krawędzi wchodzących w skład MST.
    """
    graf_wazony.sort()
    rodzic = {}
    ranga = {}

    def find(wierzcholek):
        if rodzic[wierzcholek] != wierzcholek:
            rodzic[wierzcholek] = find(rodzic[wierzcholek])
        return rodzic[wierzcholek]

    def union(w1, w2):
        korzen1 = find(w1)
        korzen2 = find(w2)
        if korzen1 != korzen2:
            if ranga[korzen1] > ranga[korzen2]:
                rodzic[korzen2] = korzen1
            elif ranga[korzen1] < ranga[korzen2]:
                rodzic[korzen1] = korzen2
            else:
                rodzic[korzen2] = korzen1
                ranga[korzen1] += 1

    mst = []
    for _, w1, w2 in graf_wazony:
        rodzic[w1] = w1
        rodzic[w2] = w2
        ranga[w1] = 0
        ranga[w2] = 0

    for waga, w1, w2 in graf_wazony:
        if find(w1) != find(w2):
            union(w1, w2)
            mst.append((waga, w1, w2))
    return mst


# 5. Najkrótsza ścieżka do wszystkich wierzchołków - Algorytm Dijkstry
def najkrotsza_sciezka_dijkstra(graf_wazony, start):
    """
    Znajduje najkrótsze ścieżki z wierzchołka startowego do wszystkich innych wierzchołków.

    :param graf_wazony: Słownik reprezentujący graf ważony jako listę sąsiedztwa.
    :param start: Wierzchołek początkowy.
    :return: Słownik z najkrótszymi odległościami do każdego wierzchołka.
    """
    import heapq
    odleglosci = {wierzcholek: float('inf') for wierzcholek in graf_wazony}
    odleglosci[start] = 0
    kolejka = [(0, start)]

    while kolejka:
        obecna_odleglosc, obecny_wierzcholek = heapq.heappop(kolejka)
        if obecna_odleglosc > odleglosci[obecny_wierzcholek]:
            continue
        for sasiad, waga in graf_wazony.get(obecny_wierzcholek, []):
            dystans = obecna_odleglosc + waga
            if dystans < odleglosci[sasiad]:
                odleglosci[sasiad] = dystans
                heapq.heappush(kolejka, (dystans, sasiad))
    return odleglosci

# Konwersja grafu na listę krawędzi
def konwertuj_graf_na_liste_krawedzi(graf_wazony):
    krawedzie = []
    for wierzcholek, sasiedzi in graf_wazony.items():
        for sasiad, waga in sasiedzi:
            # Dodajemy tylko jedną wersję każdej krawędzi (unikamy duplikatów w grafie nieskierowanym)
            if (waga, sasiad, wierzcholek) not in krawedzie:
                krawedzie.append((waga, wierzcholek, sasiad))
    return krawedzie

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

krawedzie = konwertuj_graf_na_liste_krawedzi(graf_wazony)

# Znajdź minimalne drzewo rozpinające (MST)
kruskal = mst_kruskal(krawedzie)
print("Minimalne Drzewo Rozpinające (MST):", kruskal)

dijkstra = najkrotsza_sciezka_dijkstra(graf_wazony, "A")
print("Djikstra:", dijkstra)
