import heapq  # Moduł do implementacji kolejki priorytetowej


class Graf:
    def __init__(self):
        # Inicjalizujemy graf jako słownik
        self.graf = {}

    def dodaj_krawedz(self, u, v, waga):
        # Dodajemy krawędzie w obu kierunkach, ponieważ graf jest nieskierowany
        if u not in self.graf:
            self.graf[u] = []
        if v not in self.graf:
            self.graf[v] = []
        self.graf[u].append((v, waga))
        self.graf[v].append((u, waga))

    def znajdz_najkrotsza_sciezke(self, start, cel):
        # Inicjalizujemy odległości jako nieskończone i ustalamy odległość startową na 0
        odleglosci = {wierzcholek: float('inf') for wierzcholek in self.graf}
        odleglosci[start] = 0

        # Kolejka priorytetowa do przetwarzania wierzchołków
        kolejka = [(0, start)]  # (odległość, wierzchołek)

        # Przechowujemy ścieżki, aby móc je odtworzyć
        poprzednicy = {wierzcholek: None for wierzcholek in self.graf}

        while kolejka:
            aktualna_odleglosc, aktualny_wierzcholek = heapq.heappop(kolejka)

            # Jeśli dotarliśmy do celu, możemy przerwać
            if aktualny_wierzcholek == cel:
                break

            # Sprawdzamy sąsiadów aktualnego wierzchołka
            for sasiad, waga in self.graf[aktualny_wierzcholek]:
                nowa_odleglosc = aktualna_odleglosc + waga

                # Jeśli znaleźliśmy krótszą ścieżkę, aktualizujemy odległość
                if nowa_odleglosc < odleglosci[sasiad]:
                    odleglosci[sasiad] = nowa_odleglosc
                    poprzednicy[sasiad] = aktualny_wierzcholek
                    heapq.heappush(kolejka, (nowa_odleglosc, sasiad))

        # Konstruujemy najkrótszą ścieżkę
        sciezka = []
        aktualny = cel
        while aktualny is not None:
            sciezka.append(aktualny)
            aktualny = poprzednicy[aktualny]
        sciezka.reverse()  # Odwracamy, by uzyskać ścieżkę od startu do celu

        return sciezka, odleglosci[cel]


# Przykład użycia
if __name__ == "__main__":
    graf = Graf()
    graf.dodaj_krawedz('A', 'B', 4)
    graf.dodaj_krawedz('A', 'C', 2)
    graf.dodaj_krawedz('B', 'C', 5)
    graf.dodaj_krawedz('B', 'D', 10)
    graf.dodaj_krawedz('C', 'D', 3)
    graf.dodaj_krawedz('D', 'E', 1)

    start = 'A'
    cel = 'E'
    sciezka, dystans = graf.znajdz_najkrotsza_sciezke(start, cel)
    print(f"Najkrótsza ścieżka z {start} do {cel}: {sciezka} o długości {dystans}")
