# Definiowanie klasy Węzeł
class Węzeł:
    def __init__(self, wartość=None):
        self.wartość = wartość
        self.poprzedni = None
        self.następny = None

# Definiowanie klasy dwukierunkowej
class ListaDwukierunkowa:
    def __init__(self):
        self.głowa = None
        self.ogon = None

    # Definiowanie metod listy dwukierunkowej
    # Dodawanie elementu na początek listy
    def dodaj_na_poczatek(self, wartość):
        nowy_węzeł = Węzeł(wartość)  # Tworzymy nowy węzeł
        if self.głowa is None:
            self.głowa = self.ogon = nowy_węzeł  # Lista była pusta, ustawiamy oba wskaźniki
        else:
            nowy_węzeł.następny = self.głowa  # Nowy węzeł wskazuje na aktualną głowę
            self.głowa.poprzedni = nowy_węzeł  # Stary pierwszy element wskazuje na nowy
            self.głowa = nowy_węzeł  # Głowa listy teraz wskazuje na nowy węzeł

    # Dodawanie elementu na koniec listy
    def dodaj_na_koniec(self, wartość):
        nowy_węzeł = Węzeł(wartość)  # Tworzymy nowy węzeł
        if self.głowa is None:
            self.głowa = self.ogon = nowy_węzeł  # Lista była pusta, ustawiamy oba wskaźniki
        else:
            nowy_węzeł.poprzedni = self.ogon  # Nowy węzeł wskazuje na poprzedni element (ogon)
            self.ogon.następny = nowy_węzeł  # Poprzedni ogon wskazuje na nowy element
            self.ogon = nowy_węzeł  # Ogon listy teraz wskazuje na nowy węzeł

    # Usuwanie elementu z początku listy
    def usuń_z_poczatku(self):
        if self.głowa is None:
            print("Lista jest pusta!")
            return

        if self.głowa == self.ogon:  # Jeśli lista ma tylko jeden element
            self.głowa = self.ogon = None
        else:
            self.głowa = self.głowa.następny  # Przesuwamy głowę na następny element
            self.głowa.poprzedni = None  # Ustawiamy poprzedni wskaźnik na None

    # Usuwanie elementu z końca listy
    def usuń_z_konca(self):
        if self.ogon is None:
            print("Lista jest pusta!")
            return

        if self.głowa == self.ogon:  # Jeśli lista ma tylko jeden element
            self.głowa = self.ogon = None
        else:
            self.ogon = self.ogon.poprzedni  # Przesuwamy ogon na poprzedni element
            self.ogon.następny = None  # Ustawiamy następny wskaźnik na None

    # Wyświetlanie elementów listy od początku do końca
    def wyświetl_od_poczatku(self):
        bieżący = self.głowa
        if bieżący is None:
            print("Lista jest pusta!")
            return

        while bieżący:
            print(bieżący.wartość, end=" <-> ")
            bieżący = bieżący.następny
        print("None")  # Koniec listy

    # Wyświetlanie elementów listy od końca do początku
    def wyświetl_od_konca(self):
        bieżący = self.ogon
        if bieżący is None:
            print("Lista jest pusta!")
            return

        while bieżący:
            print(bieżący.wartość, end=" <-> ")
            bieżący = bieżący.poprzedni
        print("None")  # Koniec listy

    #sprawdzanie czy lista jest pusta
    def czy_pusta(self):
        if self.głowa is None and self.ogon is None:
            print("Lista jest pusta!")
            return True
        else:
            print("Lista nie jest pusta!")
            return False

    #usuwanie węzła o podanej wartości
    def usuń_konkretny_węzęł(self, indeks):
        if self.głowa is None:
            print("Lista jest pusta!")
            return

        if indeks == 0:
            if self.głowa == self.ogon:  # Lista ma tylko jeden element
                self.głowa = self.ogon = None
            else:
                self.głowa = self.głowa.następny
                self.głowa.poprzedni = None
            return

        bieżący = self.głowa
        bieżący_indeks = 0
        while bieżący is not None and bieżący_indeks < indeks:
            bieżący = bieżący.następny
            bieżący_indeks += 1

        if bieżący is None:  # Indeks poza zakresem
            print("Indeks poza zakresem!")
            return

            # Usuwamy węzeł znajdujący się na środku lub końcu
        if bieżący == self.ogon:  # Usuwamy ogon
            self.ogon = bieżący.poprzedni
            self.ogon.następny = None
        else:  # Usuwamy węzeł z środka
            bieżący.poprzedni.następny = bieżący.następny
            bieżący.następny.poprzedni = bieżący.poprzedni

    def długość_listy(self):
        if self.głowa is None:
            print("Lista nie zawiera żadnego elementu!")
            return 0

        bieżący = self.głowa
        bieżący_indeks = 0
        while bieżący is not None:
            bieżący_indeks +=1
            bieżący = bieżący.następny

        return bieżący_indeks

    def czy_pusta(self):
        if self.głowa is None:
            return "Lista jest pusta!"
        else:
            return "Lista nie jest pusta"

    def zamiana_miejsc(self, wartość_1, wartość_2):
        if self.głowa is None:
            print("Lista jest pusta!")
            return

        if wartość_1 == wartość_2:
            print("Podano te same wartości. Zamiana nie jest konieczna!")
            return

        # Znalezienie węzłów o wartościach wartość_1 i wartość_2
        węzeł_1 = None
        węzeł_2 = None
        bieżący = self.głowa

        while bieżący:
            if bieżący.wartość == wartość_1:
                węzeł_1 = bieżący
            elif bieżący.wartość == wartość_2:
                węzeł_2 = bieżący
            bieżący = bieżący.następny

        # Sprawdzenie, czy oba węzły zostały znalezione
        if not węzeł_1 or not węzeł_2:
            print("Jedna lub obie wartości nie istnieją w liście!")
            return

        # Zamiana wskaźników
        # Zamiana poprzedników
        if węzeł_1.poprzedni:
            węzeł_1.poprzedni.następny = węzeł_2
        else:
            self.głowa = węzeł_2

        if węzeł_2.poprzedni:
            węzeł_2.poprzedni.następny = węzeł_1
        else:
            self.głowa = węzeł_1

        # Zamiana następców
        if węzeł_1.następny:
            węzeł_1.następny.poprzedni = węzeł_2
        if węzeł_2.następny:
            węzeł_2.następny.poprzedni = węzeł_1

        # Zamiana wskaźników węzłów
        węzeł_1.następny, węzeł_2.następny = węzeł_2.następny, węzeł_1.następny
        węzeł_1.poprzedni, węzeł_2.poprzedni = węzeł_2.poprzedni, węzeł_1.poprzedni

lista = ListaDwukierunkowa()
lista.dodaj_na_poczatek(5)
lista.dodaj_na_poczatek(8)
lista.dodaj_na_poczatek(7)
lista.dodaj_na_poczatek(5)
lista.dodaj_na_koniec(4)
lista.dodaj_na_koniec(9)
lista.wyświetl_od_poczatku()
print(lista.czy_pusta())
lista.zamiana_miejsc(5, 9)
lista.wyświetl_od_poczatku()
lista.zamiana_miejsc(7, 4)
lista.wyświetl_od_poczatku()
print(lista.długość_listy())
lista.dodaj_na_koniec(5)
lista.dodaj_na_koniec(7)
lista.wyświetl_od_poczatku()
lista.wyświetl_od_konca()

