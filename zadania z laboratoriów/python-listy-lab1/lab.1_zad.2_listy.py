class Wezel:
    def __init__(self, wartosc=None):
        self.wartosc = wartosc  # Przechowuje wartość
        self.poprzedni = None   # Wskaźnik na poprzedni element
        self.nastepny = None    # Wskaźnik na następny element

class ListaDwukierunkowa:
    def __init__(self):
        self.glowa = None  # Głowa listy
        self.ogon = None   # Ogon listy

    # Dodawanie elementu na początek listy
    def dodaj_na_poczatek(self, wartosc):
        nowy_wezel = Wezel(wartosc)  # Tworzymy nowy węzeł
        if self.glowa is None:
            self.glowa = self.ogon = nowy_wezel  # Lista była pusta, ustawiamy oba wskaźniki
        else:
            nowy_wezel.nastepny = self.glowa  # Nowy węzeł wskazuje na aktualną głowę
            self.glowa.poprzedni = nowy_wezel  # Stary pierwszy element wskazuje na nowy
            self.glowa = nowy_wezel  # Głowa listy teraz wskazuje na nowy węzeł

    # Dodawanie elementu na koniec listy
    def dodaj_na_koniec(self, wartosc):
        nowy_wezel = Wezel(wartosc)  # Tworzymy nowy węzeł
        if self.ogon is None:
            self.glowa = self.ogon = nowy_wezel  # Lista była pusta, ustawiamy oba wskaźniki
        else:
            nowy_wezel.poprzedni = self.ogon  # Nowy węzeł wskazuje na poprzedni element (ogon)
            self.ogon.nastepny = nowy_wezel  # Poprzedni ogon wskazuje na nowy element
            self.ogon = nowy_wezel  # Ogon listy teraz wskazuje na nowy węzeł

    # Usuwanie elementu z początku listy
    def usun_z_poczatku(self):
        if self.glowa is None:
            print("Lista jest pusta!")
            return
        if self.glowa == self.ogon:  # Jeśli lista ma tylko jeden element
            self.glowa = self.ogon = None
        else:
            self.glowa = self.glowa.nastepny  # Przesuwamy głowę na następny element
            self.glowa.poprzedni = None  # Ustawiamy poprzedni wskaźnik na None

    # Usuwanie elementu z końca listy
    def usun_z_konca(self):
        if self.ogon is None:
            print("Lista jest pusta!")
            return
        if self.glowa == self.ogon:  # Jeśli lista ma tylko jeden element
            self.glowa = self.ogon = None
        else:
            self.ogon = self.ogon.poprzedni  # Przesuwamy ogon na poprzedni element
            self.ogon.nastepny = None  # Ustawiamy następny wskaźnik na None

    # Wyświetlanie elementów listy od początku do końca
    def wyswietl_od_poczatku(self):
        biezacy = self.glowa
        if biezacy is None:
            print("Lista jest pusta!")
            return
        while biezacy:
            print(biezacy.wartosc, end=" <-> ")
            biezacy = biezacy.nastepny
        print("None")  # Koniec listy

    # Wyświetlanie elementów listy od końca do początku
    def wyswietl_od_konca(self):
        biezacy = self.ogon
        if biezacy is None:
            print("Lista jest pusta!")
            return
        while biezacy:
            print(biezacy.wartosc, end=" <-> ")
            biezacy = biezacy.poprzedni
        print("None")  # Koniec listy

# Testowanie implementacji

# Tworzymy listę
lista = ListaDwukierunkowa()

# Dodajemy elementy na początek i koniec
lista.dodaj_na_poczatek(10)
lista.dodaj_na_poczatek(20)
lista.dodaj_na_koniec(30)
lista.dodaj_na_koniec(40)

# Wyświetlamy listę od początku do końca
print("Lista od początku do końca:")
lista.wyswietl_od_poczatku()  # Oczekiwane: 20 <-> 10 <-> 30 <-> 40 <-> None

# Wyświetlamy listę od końca do początku
print("Lista od końca do początku:")
lista.wyswietl_od_konca()  # Oczekiwane: 40 <-> 30 <-> 10 <-> 20 <-> None

# Usuwamy elementy z początku i końca
lista.usun_z_poczatku()
lista.usun_z_konca()

# Wyświetlamy listę po usunięciu
print("Lista po usunięciu z początku i końca:")
lista.wyswietl_od_poczatku()  # Oczekiwane: 10 <-> 30 <-> None
