# Klasa reprezentująca pojedynczy węzeł drzewa BST.
class Wezel:
    def __init__(self, klucz):
        self.klucz = klucz  # Wartość węzła
        self.lewy = None  # Lewy potomek
        self.prawy = None  # Prawy potomek


# Klasa reprezentująca drzewo binarne wyszukiwania (BST).
class BSTree:
    def __init__(self):
        self.korzen = None  # Korzeń drzewa, początkowo pusty

    # Prywatna metoda do rekurencyjnego wstawiania nowego klucza.
    def _wstawianie_rekurencyjne(self, wezel, klucz):
        # Jeśli klucz jest mniejszy, dodaj go do lewego poddrzewa.
        if klucz < wezel.klucz:
            if wezel.lewy is None:  # Jeśli lewy potomek nie istnieje, utwórz nowy węzeł.
                wezel.lewy = Wezel(klucz)
            else:  # W przeciwnym razie rekurencyjnie wstaw klucz.
                self._wstawianie_rekurencyjne(wezel.lewy, klucz)
        # Jeśli klucz jest większy, dodaj go do prawego poddrzewa.
        elif klucz > wezel.klucz:
            if wezel.prawy is None:  # Jeśli prawy potomek nie istnieje, utwórz nowy węzeł.
                wezel.prawy = Wezel(klucz)
            else:  # W przeciwnym razie rekurencyjnie wstaw klucz.
                self._wstawianie_rekurencyjne(wezel.prawy, klucz)

    # Prywatna metoda do iteracyjnego wstawiania nowego klucza.
    def _wstawanie_iteracyjne(self, klucz):
        obecny_wezel = self.korzen

        # Iteracyjnie przechodź po drzewie, aż znajdziesz miejsce do wstawienia.
        while obecny_wezel is not None and obecny_wezel.klucz != klucz:
            if klucz < obecny_wezel.klucz:
                if obecny_wezel.lewy is None:  # Jeśli lewy potomek nie istnieje, utwórz nowy węzeł.
                    obecny_wezel.lewy = Wezel(klucz)
                    return
                obecny_wezel = obecny_wezel.lewy  # Przejdź do lewego potomka.
            else:
                if obecny_wezel.prawy is None:  # Jeśli prawy potomek nie istnieje, utwórz nowy węzeł.
                    obecny_wezel.prawy = Wezel(klucz)
                    return
                obecny_wezel = obecny_wezel.prawy  # Przejdź do prawego potomka.

    # Publiczna metoda do wstawiania klucza do drzewa.
    def wstawianie_klucza(self, klucz):
        if self.korzen is None:
            self.korzen = Wezel(klucz)  # Jeśli korzeń jest pusty, utwórz go.
        else:
            self._wstawianie_rekurencyjne(self.korzen, klucz)
            # self._wstawanie_iteracyjne(klucz)  # Alternatywne podejście: iteracyjne.

    # Prywatna metoda do znajdowania węzła o minimalnym kluczu w poddrzewie.
    def _min_klucz(self, obecny_wezel=None):
        if obecny_wezel is None:
            obecny_wezel = self.korzen  # Zaczynamy od korzenia, jeśli nie podano węzła.
        while obecny_wezel.lewy is not None:  # Przechodź w lewo, aż znajdziesz minimalny klucz.
            obecny_wezel = obecny_wezel.lewy
        return obecny_wezel

    # Publiczna metoda do usuwania klucza z drzewa.
    def usuwanie_klucza(self, klucz):
        self.korzen = self._usun_wezel(self.korzen, klucz)

    # Prywatna metoda do rekurencyjnego usuwania węzła.
    def _usun_wezel(self, wezel, klucz):
        if wezel is None:  # Jeśli drzewo jest puste, zwróć None.
            return None

        if klucz < wezel.klucz:  # Jeśli klucz jest mniejszy, przejdź do lewego poddrzewa.
            wezel.lewy = self._usun_wezel(wezel.lewy, klucz)
        elif klucz > wezel.klucz:  # Jeśli klucz jest większy, przejdź do prawego poddrzewa.
            wezel.prawy = self._usun_wezel(wezel.prawy, klucz)
        else:
            # Przypadek 1: Węzeł nie ma dzieci.
            if wezel.lewy is None and wezel.prawy is None:
                return None
            # Przypadek 2: Węzeł ma jedno dziecko (tylko prawe lub lewe).
            if wezel.lewy is None:  # Tylko prawe dziecko.
                return wezel.prawy
            elif wezel.prawy is None:  # Tylko lewe dziecko.
                return wezel.lewy
            # Przypadek 3: Węzeł ma dwoje dzieci.
            # Znajdź następnika (najmniejszy klucz w prawym poddrzewie).
            nastepnik = self._min_klucz(wezel.prawy)
            wezel.klucz = nastepnik.klucz  # Skopiuj wartość następnika do bieżącego węzła.
            # Usuń następnika z prawego poddrzewa.
            wezel.prawy = self._usun_wezel(wezel.prawy, nastepnik.klucz)

        return wezel

    # Prywatna metoda do przechodzenia drzewa w porządku LVR (in-order traversal).
    def _LVR(self, wierzcholek):
        if wierzcholek.lewy is not None:  # Odwiedź lewe poddrzewo.
            self._LVR(wierzcholek.lewy)
        print(wierzcholek.klucz, end=" ")  # Wyświetl bieżący klucz.
        if wierzcholek.prawy is not None:  # Odwiedź prawe poddrzewo.
            self._LVR(wierzcholek.prawy)

    # Publiczna metoda do wyświetlania drzewa w porządku LVR.
    def wyswietlanie_drzewa(self):
        if self.korzen is None:  # Jeśli drzewo jest puste.
            print("Drzewo jest puste")
            return
        self._LVR(self.korzen)  # Rozpocznij od korzenia.
        print()

    def szukanie_klucza(self, klucz):
        aktualny_wezel = self.korzen

        while aktualny_wezel is not None:
            # Jeśli klucz znaleziony, zwróć węzeł
            if aktualny_wezel.klucz == klucz:
                return aktualny_wezel
            # Przeszukiwanie w lewo lub prawo
            elif klucz < aktualny_wezel.klucz:
                aktualny_wezel = aktualny_wezel.lewy
            else:
                aktualny_wezel = aktualny_wezel.prawy

        # Jeśli nie znaleziono węzła
        return "Nie znaleziono klucza"

    def liczba_wezlow(self):
        return self._liczba_wezlow(self.korzen)

    def _liczba_wezlow(self, wezel):
        # Jeśli węzeł jest pusty, zwróć 0
        if wezel is None:
            return 0
        # Rekurencyjnie licz węzły w lewym i prawym poddrzewie
        lewy = self._liczba_wezlow(wezel.lewy)
        prawy = self._liczba_wezlow(wezel.prawy)
        # Zwróć sumę węzłów lewego i prawego poddrzewa oraz bieżącego węzła
        return 1 + lewy + prawy

    def pre_order(self):
        self._pre_order(self.korzen)

    def _pre_order(self, wezel):
        # Jeśli węzeł nie jest pusty, wykonaj operację
        if wezel is not None:
            # Odwiedź korzeń (wypisz klucz)
            print(wezel.klucz, end=" ")
            # Rekurencyjnie przejdź do lewego poddrzewa
            self._pre_order(wezel.lewy)
            # Rekurencyjnie przejdź do prawego poddrzewa
            self._pre_order(wezel.prawy)

    def wysokosc_drzewa(self):
        return self._wysokosc_drzewa(self.korzen)

    def _wysokosc_drzewa(self, wezel):
        # Jeśli węzeł jest pusty, zwróć -1
        if wezel is None:
            return -1
        # Rekurencyjnie oblicz wysokość lewego i prawego poddrzewa
        lewa_wysokosc = self._wysokosc_drzewa(wezel.lewy)
        prawa_wysokosc = self._wysokosc_drzewa(wezel.prawy)
        # Zwróć maksymalną wysokość z obu poddrzew plus 1 (dla bieżącego węzła)
        return 1 + max(lewa_wysokosc, prawa_wysokosc)\


    def usun_w_przedziale(self, min_klucz, max_klucz):
        self.korzen = self._usun_w_przedziale(self.korzen, min_klucz, max_klucz)

        # Rekurencyjna metoda usuwająca węzły w przedziale

    def _usun_w_przedziale(self, wezel, min_klucz, max_klucz):
        # Jeśli węzeł jest pusty, nic nie robimy
        if wezel is None:
            return None

        # Jeśli klucz węzła jest mniejszy niż min_klucz, to usuwamy węzły z prawego poddrzewa
        if wezel.klucz < min_klucz:
            wezel.prawy = self._usun_w_przedziale(wezel.prawy, min_klucz, max_klucz)

        # Jeśli klucz węzła jest większy niż max_klucz, to usuwamy węzły z lewego poddrzewa
        elif wezel.klucz > max_klucz:
            wezel.lewy = self._usun_w_przedziale(wezel.lewy, min_klucz, max_klucz)

        # Jeśli klucz węzła mieści się w przedziale [min_klucz, max_klucz], to go usuwamy
        else:
            # Jeśli węzeł ma jedno lub zero dzieci
            if wezel.lewy is None:
                return wezel.prawy
            elif wezel.prawy is None:
                return wezel.lewy

            # Jeśli węzeł ma dwoje dzieci, znajdź następnika (najmniejszy element w prawym poddrzewie)
            wezel.klucz = self._min_w_prawym_poddrzewie(wezel.prawy)
            wezel.prawy = self._usun_w_przedziale(wezel.prawy, wezel.klucz, wezel.klucz)

        return wezel

        # Pomocnicza metoda do znalezienia najmniejszego węzła w prawym poddrzewie

    def _min_w_prawym_poddrzewie(self, wezel):
        while wezel.lewy is not None:
            wezel = wezel.lewy
        return wezel.klucz

        # Metoda do wyświetlania drzewa (opcjonalnie, pomocnicza)

    def pre_order(self):
        self._pre_order(self.korzen)
        print()

    def _pre_order(self, wezel):
        if wezel is not None:
            print(wezel.klucz, end=" ")
            self._pre_order(wezel.lewy)
            self._pre_order(wezel.prawy)

# Testowanie drzewa BST.
if __name__ == "__main__":
    bstree = BSTree()

    # Wstawianie kluczy do drzewa.
    bstree.wstawianie_klucza(8)
    bstree.wstawianie_klucza(3)
    bstree.wstawianie_klucza(1)
    bstree.wstawianie_klucza(6)
    bstree.wstawianie_klucza(4)
    bstree.wstawianie_klucza(7)
    bstree.wstawianie_klucza(10)
    bstree.wstawianie_klucza(14)
    bstree.wstawianie_klucza(13)
    bstree.wyswietlanie_drzewa()





