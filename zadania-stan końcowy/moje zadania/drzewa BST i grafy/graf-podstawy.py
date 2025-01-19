class Graf:
    def __init__(self):
        # Inicjalizacja pustego grafu jako słownika.
        # Kluczami są węzły, a wartościami są listy sąsiadów (węzłów połączonych krawędziami).
        self.graf = {}

    def dodaj_wezel(self, wezel):
        """
        Dodaje nowy węzeł do grafu.

        Argumenty:
        - wezel (str): Nazwa węzła, który ma zostać dodany.

        Jeśli węzeł już istnieje, operacja nie ma efektu.
        Zgłasza wyjątek, jeśli węzeł nie jest typu `str`.
        """
        if not isinstance(wezel, str):
            raise ValueError("Węzeł musi być ciągiem znaków (str).")
        # Dodaje węzeł tylko, jeśli jeszcze nie istnieje w grafie.
        if wezel not in self.graf:
            self.graf[wezel] = []

    def dodaj_krawedz(self, od_wezla, do_wezla):
        """
        Dodaje krawędź między dwoma węzłami.

        Argumenty:
        - od_wezla (str): Węzeł początkowy.
        - do_wezla (str): Węzeł końcowy.

        Automatycznie dodaje węzły, jeśli ich jeszcze nie ma w grafie.
        Zgłasza wyjątek, jeśli próbuje dodać pętlę własną (od_wezla == do_wezla)
        lub jeśli argumenty nie są typu `str`.
        """
        if not isinstance(od_wezla, str) or not isinstance(do_wezla, str):
            raise ValueError("Węzły muszą być ciągami znaków (str).")
        if od_wezla == do_wezla:
            raise ValueError("Pętla własna jest niedozwolona.")

        # Jeśli węzły nie istnieją, dodaj je do grafu.
        if od_wezla not in self.graf:
            self.dodaj_wezel(od_wezla)
        if do_wezla not in self.graf:
            self.dodaj_wezel(do_wezla)

        # Dodaj krawędź tylko, jeśli jeszcze nie istnieje.
        if do_wezla not in self.graf[od_wezla]:
            self.graf[od_wezla].append(do_wezla)

    def wyswietl(self):
        """
        Wyświetla graf w formie listy sąsiedztwa.
        Każdy węzeł jest wyświetlany wraz z listą jego sąsiadów.
        """
        for wezel, sasiedzi in self.graf.items():
            # Wyświetla węzeł oraz jego sąsiadów jako ciąg znaków oddzielonych przecinkami.
            print(f"{wezel}: {', '.join(sasiedzi)}")

    def wyswietl_macierz_sasiedztwa(self):
        """
        Wyświetla graf w postaci macierzy sąsiedztwa.
        Macierz sąsiedztwa to tablica 2D, w której:
        - 1 oznacza istnienie krawędzi między węzłami,
        - 0 oznacza brak krawędzi.
        """
        wezly = list(self.graf.keys())  # Pobiera listę wszystkich węzłów w grafie.
        n = len(wezly)  # Liczba węzłów.

        # Inicjalizuje macierz n x n wypełnioną zerami.
        macierz = [[0] * n for _ in range(n)]

        # Tworzy słownik mapujący węzły na ich indeksy w macierzy.
        indeksy = {wezel: i for i, wezel in enumerate(wezly)}

        # Wypełnia macierz na podstawie listy sąsiedztwa.
        for od_wezla, sasiedzi in self.graf.items():
            for do_wezla in sasiedzi:
                # Ustawia wartość 1, jeśli istnieje krawędź od od_wezla do do_wezla.
                macierz[indeksy[od_wezla]][indeksy[do_wezla]] = 1

        # Wyświetla nagłówek macierzy (nazwy węzłów).
        print("   " + " ".join(wezly))
        for i, wezel in enumerate(wezly):
            # Wyświetla każdy wiersz macierzy wraz z odpowiadającym mu węzłem.
            print(f"{wezel}: " + " ".join(map(str, macierz[i])))

graf = Graf()
graf.dodaj_wezel("A")
graf.dodaj_wezel("B")
graf.dodaj_wezel("C")
graf.dodaj_wezel("D")
graf.dodaj_wezel("E")
graf.dodaj_wezel("F")
graf.dodaj_wezel("G")
graf.dodaj_krawedz("A", "B")
graf.dodaj_krawedz("A", "C")
graf.dodaj_krawedz("B", "D")
graf.dodaj_krawedz("C", "E")
graf.dodaj_krawedz("D", "F")
graf.dodaj_krawedz("E", "G")
graf.dodaj_krawedz("F", "A")
graf.dodaj_krawedz("G", "B")
graf.dodaj_krawedz("A", "D")
graf.dodaj_krawedz("C", "F")
graf.dodaj_krawedz("G", "E")
graf.wyswietl()
graf.wyswietl_macierz_sasiedztwa()

