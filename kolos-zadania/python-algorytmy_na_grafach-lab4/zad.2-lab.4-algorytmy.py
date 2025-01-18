import heapq

class Graf:
    def __init__(self):
        # Inicjalizacja pustego grafu
        self.graf = {}

    def dodaj_wezel(self, wezel):
        """Dodaje nowy węzeł do grafu."""
        if not isinstance(wezel, str):
            raise ValueError("Węzeł musi być ciągiem znaków (str).")
        if wezel not in self.graf:
            self.graf[wezel] = []

    def dodaj_krawedz(self, od_wezla, do_wezla, waga):
        """Dodaje krawędź między węzłami z wagą."""
        if not isinstance(od_wezla, str) or not isinstance(do_wezla, str):
            raise ValueError("Węzły muszą być ciągami znaków (str).")
        if od_wezla == do_wezla:
            raise ValueError("Pętla własna jest niedozwolona.")
        if not isinstance(waga, (int, float)) or waga <= 0:
            raise ValueError("Waga musi być liczbą dodatnią.")
        if od_wezla not in self.graf:
            self.dodaj_wezel(od_wezla)
        if do_wezla not in self.graf:
            self.dodaj_wezel(do_wezla)
        self.graf[od_wezla].append((do_wezla, waga))
        self.graf[do_wezla].append((od_wezla, waga))  # Dla grafu nieskierowanego

    def wyswietl(self):
        """Wyświetla graf w formie listy sąsiedztwa."""
        for wezel, sasiedzi in self.graf.items():
            sasiedzi_str = ", ".join([f"{sasiad} (waga: {waga})" for sasiad, waga in sasiedzi])
            print(f"{wezel}: {sasiedzi_str}")

    def wyswietl_macierz_sasiedztwa(self):
        """Wyświetla graf w postaci macierzy sąsiedztwa."""
        wezly = list(self.graf.keys())
        n = len(wezly)
        macierz = [[0] * n for _ in range(n)]

        indeksy = {wezel: i for i, wezel in enumerate(wezly)}

        for od_wezla, sasiedzi in self.graf.items():
            for do_wezla, waga in sasiedzi:
                macierz[indeksy[od_wezla]][indeksy[do_wezla]] = waga

        # Wyświetlanie macierzy
        print("   " + " ".join(wezly))
        for i, wezel in enumerate(wezly):
            print(f"{wezel}: " + " ".join(map(str, macierz[i])))

    def najkrotsza_sciezka(self, start, cel):
        """Znajduje najkrótszą ścieżkę pomiędzy dwoma węzłami za pomocą algorytmu Dijkstry."""
        if start not in self.graf or cel not in self.graf:
            raise ValueError("Podane węzły muszą istnieć w grafie.")

        odleglosci = {wezel: float('inf') for wezel in self.graf}
        odleglosci[start] = 0
        kolejka = [(0, start)]
        poprzednicy = {wezel: None for wezel in self.graf}

        while kolejka:
            obecna_odleglosc, obecny_wezel = heapq.heappop(kolejka)

            if obecny_wezel == cel:
                break

            for sasiad, waga in self.graf[obecny_wezel]:
                nowa_odleglosc = obecna_odleglosc + waga
                if nowa_odleglosc < odleglosci[sasiad]:
                    odleglosci[sasiad] = nowa_odleglosc
                    poprzednicy[sasiad] = obecny_wezel
                    heapq.heappush(kolejka, (nowa_odleglosc, sasiad))

        # Odtwarzanie ścieżki
        sciezka = []
        obecny = cel
        while obecny is not None:
            sciezka.append(obecny)
            obecny = poprzednicy[obecny]

        return sciezka[::-1], odleglosci[cel]

# Przykład użycia:
miasta_graf = Graf()

# Dodajemy węzły i krawędzie z wagami
miasta_graf.dodaj_krawedz("Warszawa", "Kraków", 293)
miasta_graf.dodaj_krawedz("Warszawa", "Gdańsk", 342)
miasta_graf.dodaj_krawedz("Kraków", "Wrocław", 268)
miasta_graf.dodaj_krawedz("Wrocław", "Poznań", 175)
miasta_graf.dodaj_krawedz("Poznań", "Gdańsk", 300)
miasta_graf.dodaj_krawedz("Gdańsk", "Olsztyn", 136)
miasta_graf.dodaj_krawedz("Olsztyn", "Warszawa", 211)
miasta_graf.dodaj_krawedz("Kraków", "Rzeszów", 167)
miasta_graf.dodaj_krawedz("Rzeszów", "Lublin", 150)
miasta_graf.dodaj_krawedz("Lublin", "Warszawa", 170)

# Wyświetlamy graf
miasta_graf.wyswietl()

# Wyświetlamy macierz sąsiedztwa
miasta_graf.wyswietl_macierz_sasiedztwa()

# Znajdujemy najkrótszą ścieżkę między dwoma miastami
sciezka, dystans = miasta_graf.najkrotsza_sciezka("Kraków", "Lublin")
print(f"Najkrótsza ścieżka: {' -> '.join(sciezka)} z dystansem {dystans} km")
