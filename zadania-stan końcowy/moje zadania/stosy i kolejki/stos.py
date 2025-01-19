class Stos:
    def __init__(self):
        self.items = []

    def dodaj(self, item):
        self.items.append(item)

    def usuń_i_zwróć(self):
        if not self.jest_puste():
           return self.items.pop()
        return None

    def jest_puste(self):
        return len(self.items) == 0

    def długość(self):
        return len(self.items)

    def zwróc_bez_usuwania(self):
        if not self.jest_puste():
            return self.items[-1]
        return None

    def usuń_wszystkie(self):
        if not self.jest_puste():
             self.items.clear()
        return None

    def zlicz_wystąpienia(self, item):
        if not self.jest_puste():
            return self.items.count(item)
        return 0

    def wstaw_na_określone_miejsce(self, item, indeks):
        if indeks > len(self.items) or indeks < 0:
            raise IndexError("Indeks poza zakresem!")

        self.items.insert(indeks, item)

    def sortowanie(self):
        if not self.jest_puste():
            return self.items.sort()

    def odwracanie(self):
        if not self.jest_puste():
            return self.items.reverse()

    def indeks_elementu(self, item):
        if not self.jest_puste():
            return self.items.index(item)
        return None

    def wypisz_elementy(self):
        """Wypisuje wszystkie elementy stosu, zaczynając od szczytu."""
        if self.jest_puste():
            print("Stos jest pusty.")
        else:
            print("Elementy stosu (od góry do dołu):")
            for item in reversed(self.items):  # Odwracamy, aby zacząć od szczytu
                print(item)

    def kopiuj(self):
        """
        Tworzy kopię stosu.
        Zwraca nowy obiekt Stos zawierający te same elementy.
        """
        nowy_stos = Stos()
        nowy_stos.items = self.items[:]
        return nowy_stos

    def połącz(self, inny_stos):
        """
        Łączy bieżący stos z innym stos.
        Dodaje elementy z innego stosu na koniec bieżącego stosu.
        """
        self.items.extend(inny_stos.items)

    def sprawdź_zawiera(self, item):
        """
        Sprawdza, czy stos zawiera dany element.
        Zwraca True, jeśli element znajduje się w stosie, w przeciwnym razie False.
        """
        return item in self.items

stos = Stos()
stos.dodaj(5)
stos.dodaj(7)
stos.dodaj(11)
stos.dodaj(12)
print(stos.długość())
print(stos.zwróc_bez_usuwania())
print(stos.usuń_i_zwróć())
print(stos.długość())
print(stos.wypisz_elementy())
stos.dodaj(10)
stos.dodaj(12)
stos.dodaj(3)
print(stos.wypisz_elementy())
stos.dodaj(12)
stos.dodaj(3)
print(stos.wypisz_elementy())
print(stos.zlicz_wystąpienia(12))
print(stos.zlicz_wystąpienia(3))
print(stos.zlicz_wystąpienia(5))
print(stos.indeks_elementu(10))
print(stos.wypisz_elementy())
print(stos.sprawdź_zawiera(6))
