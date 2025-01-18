class Wezel:
    def __init__(self, klucz):
        self.klucz = klucz
        self.lewy = None
        self.prawy = None

class BSTree:
    def __init__(self):
        self.korzen = None

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

    def wstawianie_klucza(self, klucz):
        if self.korzen is None:
            self.korzen = Wezel(klucz)  # Jeśli korzeń jest pusty, utwórz go.
        else:
            self._wstawianie_rekurencyjne(self.korzen, klucz)

    # Prywatna metoda do znajdowania węzła o minimalnym kluczu w poddrzewie.
    def _min_klucz(self, obecny_wezel=None):
        if obecny_wezel is None:
            obecny_wezel = self.korzen  # Zaczynamy od korzenia, jeśli nie podano węzła.

        while obecny_wezel.lewy is not None:  # Przechodź w lewo, aż znajdziesz minimalny klucz.
            obecny_wezel = obecny_wezel.lewy
        return obecny_wezel

    # Prywatna metoda do znajdowania węzła o minimalnym kluczu w poddrzewie.
    def max_klucz(self, obecny_wezel=None):
        if obecny_wezel is None:
            obecny_wezel = self.korzen

        if obecny_wezel is None:
            return None

        while obecny_wezel.prawy is not None:
            obecny_wezel = obecny_wezel.prawy

        return obecny_wezel

    def _LVR(self, wierzcholek):
        if wierzcholek is None:
            return

        if wierzcholek.lewy is not None:  # Odwiedź lewe poddrzewo.
            self._LVR(wierzcholek.lewy)

        print(wierzcholek.klucz, end=" ")  # Wyświetl bieżący klucz.

        if wierzcholek.prawy is not None:  # Odwiedź prawe poddrzewo.
            self._LVR(wierzcholek.prawy)

    def _VLR(self, wierzcholek):
        """
        Przechodzi przez drzewo w porządku pre-order (VLR) i wyświetla klucze.

        :param wierzcholek: Węzeł, od którego rozpoczyna się przechodzenie.
        """
        # Jeśli wierzchołek jest pusty, zakończ działanie
        if wierzcholek is None:
            return

        # Wyświetl bieżący klucz (visit)
        print(wierzcholek.klucz, end=" ")

        # Odwiedź lewe poddrzewo (left)
        self._VLR(wierzcholek.lewy)

        # Odwiedź prawe poddrzewo (right)
        self._VLR(wierzcholek.prawy)

    def _LRV(self, wierzcholek):
        """
        Przechodzi przez drzewo w porządku post-order (LRV) i wyświetla klucze.

        :param wierzcholek: Węzeł, od którego rozpoczyna się przechodzenie.
        """
        # Jeśli wierzchołek jest pusty, zakończ działanie
        if wierzcholek is None:
            return

        # Odwiedź lewe poddrzewo (Left)
        self._LRV(wierzcholek.lewy)

        # Odwiedź prawe poddrzewo (Right)
        self._LRV(wierzcholek.prawy)

        # Wyświetl bieżący klucz (Visit)
        print(wierzcholek.klucz, end=" ")

    def suma_wezlow_LVR(self, wierzcholek):
        if wierzcholek is None:
            return 0

        return (
            self.suma_wezlow_LVR(wierzcholek.lewy) +
            wierzcholek.klucz +
            self.suma_wezlow_LVR(wierzcholek.prawy)
        )

    def suma_wezlow(self):
        return self.suma_wezlow_LVR(self.korzen)


    def najwiekszy_LRV(self, wierzcholek):
        if wierzcholek is None:
            return 0

        najwiekszy_lewy = self.najwiekszy_LRV(wierzcholek.lewy)
        najwiekszy_prawy = self.najwiekszy_LRV(wierzcholek.prawy)

        # Zwróć największą wartość spośród lewego poddrzewa, prawego poddrzewa i bieżącego węzła
        return max(najwiekszy_lewy, najwiekszy_prawy, wierzcholek.klucz)

    def liczba_lisci_VLR(self, wierzcholek):
        if wierzcholek is None:
            return 0

        if wierzcholek.lewy is None and wierzcholek.prawy is None:
            return 1

            # Rekurencyjnie zlicz liście w lewym i prawym poddrzewie
        liczba_lisci_lewy = self.liczba_lisci_VLR(wierzcholek.lewy)
        liczba_lisci_prawy = self.liczba_lisci_VLR(wierzcholek.prawy)

        # Zwróć sumę liści w lewym i prawym poddrzewie
        return liczba_lisci_lewy + liczba_lisci_prawy

    def _min_w_prawym_poddrzewie(self, wezel):
        """
        Znajduje najmniejszy klucz w prawym poddrzewie danego węzła.
        """
        if wezel.prawy is None:
            raise ValueError("Prawe poddrzewo nie istnieje.")

        wezel = wezel.prawy  # Przejście do prawego dziecka
        while wezel.lewy is not None:  # Przemieszczanie się w lewo
            wezel = wezel.lewy
        return wezel.klucz  # Zwracamy klucz najmniejszego węzła

    def _min_w_lewym_poddrzewie(self, wezel):
        # Funkcja znajduje najmniejszy klucz w lewym poddrzewie danego węzła.
        while wezel.lewy is not None:  # Dopóki istnieje lewy węzeł:
            wezel = wezel.lewy  # Przechodzimy do lewego węzła.
        return wezel.klucz  # Zwracamy klucz najmniejszego węzła.

    def _max_w_prawym_poddrzewie(self, wezel):
            # Funkcja znajduje największy klucz w prawym poddrzewie danego węzła.
            # Aby znaleźć największy klucz, przechodzimy jak najdalej w prawo,
            # ponieważ w drzewie binarnym wyszukiwania największe wartości są po prawej stronie.
            while wezel.prawy is not None:  # Dopóki istnieje prawy węzeł:
                wezel = wezel.prawy  # Przechodzimy do prawego węzła.
            return wezel.klucz  # Zwracamy klucz największego węzła.

    def _max_w_lewym_poddrzewie(self, wezel):
        """
        Znajduje największy klucz w lewym poddrzewie danego węzła.
        """
        if wezel.lewy is None:
            raise ValueError("Lewy poddrzewo nie istnieje.")

        wezel = wezel.lewy  # Rozpocznij od lewego dziecka
        while wezel.prawy is not None:  # Przechodź w prawo, aż do końca
            wezel = wezel.prawy
        return wezel.klucz  # Zwracamy klucz największego węzła

    def pre_order(self):
        self._pre_order(self.korzen)
        print()

    def _pre_order(self, wezel):
        if wezel is not None:
            print(wezel.klucz, end=" ")
            self._pre_order(wezel.lewy)
            self._pre_order(wezel.prawy)

    def wysokosc_drzewa_iteracyjnie(self):
        """
        Oblicza wysokość drzewa BST w sposób iteracyjny.

        :return: Wysokość drzewa (int)
        """
        if self.korzen is None:
            return 0  # Drzewo puste ma wysokość 0

        max_wysokosc = 0
        stos = [(self.korzen, 1)]  # Stos przechowuje węzły wraz z ich poziomami

        while stos:
            wezel, poziom = stos.pop()
            if wezel:
                max_wysokosc = max(max_wysokosc, poziom)  # Aktualizacja maksymalnej wysokości
                # Dodajemy prawego i lewego potomka wraz z ich poziomami do stosu
                stos.append((wezel.lewy, poziom + 1))
                stos.append((wezel.prawy, poziom + 1))

        return max_wysokosc


if __name__ == "__main__":
    drzewo = BSTree()
    drzewo.wstawianie_klucza(5)
    drzewo.wstawianie_klucza(7)
    drzewo.wstawianie_klucza(6)
    drzewo.wstawianie_klucza(4)
    drzewo.wstawianie_klucza(2)
    drzewo.wstawianie_klucza(11)
    drzewo.wstawianie_klucza(9)
    drzewo.wstawianie_klucza(13)
    drzewo.wstawianie_klucza(12)
    drzewo.wstawianie_klucza(15)
    drzewo.wstawianie_klucza(17)
    drzewo.wstawianie_klucza(3)
    drzewo.wstawianie_klucza(1)
    drzewo.pre_order()

    print("Post-order (LRV):")
    drzewo._LRV(drzewo.korzen.lewy)

    print("\nPre-order (VLR):")
    drzewo._VLR(drzewo.korzen.prawy)

    print("\nIn-order (LVR):")
    drzewo._LVR(drzewo.korzen.prawy)

    if drzewo.korzen:
        print("\n")
        print(drzewo._min_w_prawym_poddrzewie(drzewo.korzen))
    else:
        print("Prawe poddrzewo korzenia nie istnieje.")

    print(drzewo.wysokosc_drzewa_iteracyjnie())