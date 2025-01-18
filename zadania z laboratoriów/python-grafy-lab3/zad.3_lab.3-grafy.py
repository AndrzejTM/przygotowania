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

    def dodaj_krawedz(self, od_wezla, do_wezla):
        """Dodaje krawędź między węzłami."""
        if not isinstance(od_wezla, str) or not isinstance(do_wezla, str):
            raise ValueError("Węzły muszą być ciągami znaków (str).")
        if od_wezla == do_wezla:
            raise ValueError("Pętla własna jest niedozwolona.")
        if od_wezla not in self.graf:
            self.dodaj_wezel(od_wezla)
        if do_wezla not in self.graf:
            self.dodaj_wezel(do_wezla)
        if do_wezla not in self.graf[od_wezla]:
            self.graf[od_wezla].append(do_wezla)

    def wyswietl(self):
        """Wyświetla graf w formie listy sąsiedztwa."""
        for wezel, sasiedzi in self.graf.items():
            print(f"{wezel}: {', '.join(sasiedzi)}")

    def wyswietl_macierz_sasiedztwa(self):
        """Wyświetla graf w postaci macierzy sąsiedztwa."""
        wezly = list(self.graf.keys())
        n = len(wezly)
        macierz = [[0] * n for _ in range(n)]

        indeksy = {wezel: i for i, wezel in enumerate(wezly)}

        for od_wezla, sasiedzi in self.graf.items():
            for do_wezla in sasiedzi:
                macierz[indeksy[od_wezla]][indeksy[do_wezla]] = 1

        # Wyświetlanie macierzy
        print("   " + " ".join(wezly))
        for i, wezel in enumerate(wezly):
            print(f"{wezel}: " + " ".join(map(str, macierz[i])))

# Przykład użycia:
projekt_graf = Graf()

# Dodajemy węzły (pliki/katalogi)
projekt_graf.dodaj_wezel("src/main.py")
projekt_graf.dodaj_wezel("src/utils.py")
projekt_graf.dodaj_wezel("src/components/component1.py")
projekt_graf.dodaj_wezel("src/components/component2.py")
projekt_graf.dodaj_wezel("tests/test_main.py")

# Dodajemy krawędzie (importy)
projekt_graf.dodaj_krawedz("src/main.py", "src/utils.py")
projekt_graf.dodaj_krawedz("src/main.py", "src/components/component1.py")
projekt_graf.dodaj_krawedz("src/utils.py", "src/components/component2.py")
projekt_graf.dodaj_krawedz("tests/test_main.py", "src/main.py")

# Wyświetlamy graf
projekt_graf.wyswietl()

# Wyświetlamy macierz sąsiedztwa
projekt_graf.wyswietl_macierz_sasiedztwa()