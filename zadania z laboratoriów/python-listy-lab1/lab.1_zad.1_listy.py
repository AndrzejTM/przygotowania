class Wezel:
    def __init__(self, wartosc=None):
        self.wartosc = wartosc  # Przechowuje wartość
        self.nastepny = None    # Wskaźnik na następny element

class ListaJednokierunkowa:
    def __init__(self):
        self.glowa = None  # Głowa listy, na początku pusta

    # Dodawanie elementu na początek listy
    def dodaj_na_poczatek(self, wartosc):
        nowy_wezel = Wezel(wartosc)  # Tworzymy nowy węzeł
        nowy_wezel.nastepny = self.glowa  # Nowy węzeł wskazuje na aktualną głowę
        self.glowa = nowy_wezel  # Głowa listy wskazuje teraz na nowy węzeł

    # Dodawanie elementu w środku listy (przed danym indeksem)
    def dodaj_w_srodku(self, wartosc, indeks):
        if indeks < 0:
            print("Indeks nie może być ujemny!")
            return

        nowy_wezel = Wezel(wartosc)
        biezacy = self.glowa
        biezacy_indeks = 0

        # Znajdujemy węzeł na odpowiednim indeksie
        while biezacy is not None and biezacy_indeks < indeks - 1:
            biezacy = biezacy.nastepny
            biezacy_indeks += 1

        if biezacy is None:
            print("Indeks poza zakresem!")
        else:
            nowy_wezel.nastepny = biezacy.nastepny  # Nowy węzeł wskazuje na kolejny element
            biezacy.nastepny = nowy_wezel  # Węzeł przed dodanym wskazuje na nowy węzeł

    # Usuwanie elementu z początku listy
    def usun_z_poczatku(self):
        if self.glowa is None:
            print("Lista jest pusta!")
            return
        self.glowa = self.glowa.nastepny  # Przesuwamy głowę na następny element

    # Usuwanie elementu w środku listy (na danym indeksie)
    def usun_z_srodka(self, indeks):
        if indeks < 0:
            print("Indeks nie może być ujemny!")
            return

        biezacy = self.glowa
        biezacy_indeks = 0

        if biezacy is None:
            print("Lista jest pusta!")
            return

        # Szukamy elementu na odpowiednim indeksie
        while biezacy is not None and biezacy_indeks < indeks - 1:
            biezacy = biezacy.nastepny
            biezacy_indeks += 1

        if biezacy is None or biezacy.nastepny is None:
            print("Indeks poza zakresem!")
        else:
            biezacy.nastepny = biezacy.nastepny.nastepny  # Przeskakujemy element do usunięcia

    # Wyświetlanie elementów listy
    def wyswietl(self):
        biezacy = self.glowa
        if biezacy is None:
            print("Lista jest pusta!")
            return
        while biezacy:
            print(biezacy.wartosc, end=" -> ")
            biezacy = biezacy.nastepny
        print("None")  # Koniec listy

# Testowanie implementacji

# Tworzymy listę
lista = ListaJednokierunkowa()

# Dodajemy elementy na początek
lista.dodaj_na_poczatek(10)
lista.dodaj_na_poczatek(20)
lista.dodaj_na_poczatek(30)

# Wyświetlamy listę
print("Lista po dodaniu na początek:")
lista.wyswietl()  # Oczekiwane: 30 -> 20 -> 10 -> None

# Dodajemy element w środku (na indeksie 1)
lista.dodaj_w_srodku(25, 1)

# Wyświetlamy listę
print("Lista po dodaniu w środku:")
lista.wyswietl()  # Oczekiwane: 30 -> 25 -> 20 -> 10 -> None

# Usuwamy element z początku
lista.usun_z_poczatku()

# Wyświetlamy listę
print("Lista po usunięciu z początku:")
lista.wyswietl()  # Oczekiwane: 25 -> 20 -> 10 -> None

# Usuwamy element z indeksu 1
lista.usun_z_srodka(1)

# Wyświetlamy listę
print("Lista po usunięciu z indeksu 1:")
lista.wyswietl()  # Oczekiwane: 25 -> 10 -> None
