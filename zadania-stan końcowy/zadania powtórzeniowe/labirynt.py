import random


class Labirynt:
    def __init__(self, szerokosc, wysokosc):
        """
        Inicjalizuje labirynt o zadanej szerokości i wysokości.
        """
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.siatka = [['#' for _ in range(szerokosc)] for _ in range(wysokosc)]
        self.start = (0, 0)
        self.koniec = (wysokosc - 1, szerokosc - 1)
        self.sciezka = []

    def generuj_labirynt(self):
        """
        Generuje losowy labirynt korzystając z algorytmu DFS.
        """
        odwiedzone = [[False for _ in range(self.szerokosc)] for _ in range(self.wysokosc)]
        self._wykonaj_droge(0, 0, odwiedzone)
        self.siatka[self.start[0]][self.start[1]] = 'S'
        self.siatka[self.koniec[0]][self.koniec[1]] = 'E'

    def _wykonaj_droge(self, x, y, odwiedzone):
        """
        Rekurencyjnie wykonuje ścieżkę w labiryncie.
        """
        odwiedzone[x][y] = True
        kierunki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(kierunki)

        for dx, dy in kierunki:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.wysokosc and 0 <= ny < self.szerokosc and not odwiedzone[nx][ny]:
                # Otwieramy przejście
                self.siatka[x][y] = ' '
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
        Umożliwia sterowanie graczem w labiryncie.
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
    szerokosc = int(input("Podaj szerokość labiryntu: "))
    wysokosc = int(input("Podaj wysokość labiryntu: "))

    labirynt = Labirynt(szerokosc, wysokosc)
    labirynt.generuj_labirynt()
    labirynt.sterowanie()
