import random


class LabiryntZeScianami:
    def __init__(self, szerokosc, wysokosc):
        """
        Inicjalizuje labirynt ze ścianami. Tworzy dodatkową ramkę na zewnątrz.
        """
        self.szerokosc = szerokosc * 2 + 1  # Dostosowanie szerokości na ściany
        self.wysokosc = wysokosc * 2 + 1  # Dostosowanie wysokości na ściany
        self.siatka = [['#' for _ in range(self.szerokosc)] for _ in range(self.wysokosc)]
        self.start = (1, 1)  # Start zawsze w wewnętrznym rogu
        self.koniec = (self.wysokosc - 2, self.szerokosc - 2)  # Koniec w przeciwnym rogu

    def generuj_labirynt(self):
        """
        Generuje losowy labirynt przy użyciu algorytmu DFS, uwzględniając ściany.
        """
        odwiedzone = [[False for _ in range(self.szerokosc // 2)] for _ in range(self.wysokosc // 2)]
        self._wykonaj_droge(1, 1, odwiedzone)
        self.siatka[self.start[0]][self.start[1]] = 'S'  # Start
        self.siatka[self.koniec[0]][self.koniec[1]] = 'E'  # Wyjście

    def _wykonaj_droge(self, x, y, odwiedzone):
        """
        Rekurencyjnie tworzy ścieżki w labiryncie z uwzględnieniem ścian.
        """
        odwiedzone[x // 2][y // 2] = True
        kierunki = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(kierunki)

        for dx, dy in kierunki:
            nx, ny = x + dx, y + dy
            if 1 <= nx < self.wysokosc - 1 and 1 <= ny < self.szerokosc - 1 and not odwiedzone[nx // 2][ny // 2]:
                # Otwieramy ścieżkę (usuwamy ścianę pomiędzy)
                self.siatka[x + dx // 2][y + dy // 2] = ' '
                self.siatka[nx][ny] = ' '
                self._wykonaj_droge(nx, ny, odwiedzone)

    def wyswietl_labirynt(self):
        """
        Wyświetla labirynt w konsoli.
        """
        for wiersz in self.siatka:
            print(''.join(wiersz))

    def sterowanie(self):
        """
        Umożliwia graczowi sterowanie w labiryncie.
        """
        pozycja = self.start
        print("\nSterowanie: W - góra, S - dół, A - lewo, D - prawo, Q - wyjście\n")

        while pozycja != self.koniec:
            self.siatka[pozycja[0]][pozycja[1]] = 'P'
            self.wyswietl_labirynt()
            self.siatka[pozycja[0]][pozycja[1]] = ' '

            ruch = input("Wprowadź ruch: ").strip().upper()
            if ruch == 'Q':
                print("Zakończono grę.")
                break

            nx, ny = pozycja
            if ruch == 'W':
                nx -= 1
            elif ruch == 'S':
                nx += 1
            elif ruch == 'A':
                ny -= 1
            elif ruch == 'D':
                ny += 1
            else:
                print("Niepoprawny ruch.")
                continue

            if 0 <= nx < self.wysokosc and 0 <= ny < self.szerokosc and self.siatka[nx][ny] in (' ', 'E'):
                pozycja = (nx, ny)
            else:
                print("Nie możesz tam iść!")

        if pozycja == self.koniec:
            print("Gratulacje! Znalazłeś wyjście!")


# Przykład użycia
if __name__ == "__main__":
    szerokosc = int(input("Podaj szerokość labiryntu (liczba komórek): "))
    wysokosc = int(input("Podaj wysokość labiryntu (liczba komórek): "))

    labirynt = LabiryntZeScianami(szerokosc, wysokosc)
    labirynt.generuj_labirynt()
    labirynt.sterowanie()
