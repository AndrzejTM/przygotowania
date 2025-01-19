# Definiowanie węzła
class Węzeł:
    def __init__(self, wartość=None):
        self.wartość = wartość
        self.następny = None

    #Zwracanie reprezentacji tekstowej wartości przechowywanej w węźle
    def __str__(self):
        return str(self.wartość)

# Definiowanie Listy Jednokierunkowej
class Lista_Jednokierunkowa:
    def __init__(self):
        self.głowa = None

        # Metody listy
    # Dodawanie elementu na początek listy
    def dodaj_na_początek_listy(self, wartość):
        nowy_węzeł = Węzeł(wartość)
        nowy_węzeł.następny = self.głowa
        self.głowa = nowy_węzeł

    # Dodawanie elementu w środku listy (przed danym indeksem)
    def dodaj_wewnątrz(self, wartość, indeks):
        if indeks < 0:
            print("Indeks nie może być ujemny!")
            return

        nowy_węzeł = Węzeł(wartość)
        bieżący = self.głowa  # Poprawiona nazwa zmiennej
        bieżący_indeks = 0

        # Znajdujemy węzeł na odpowiednim indeksie
        while bieżący is not None and bieżący_indeks < indeks - 1:
            bieżący = bieżący.następny  # Poprawiona nazwa zmiennej
            bieżący_indeks += 1

        if bieżący is None:
            print("Indeks poza zakresem!")
        else:
            nowy_węzeł.następny = bieżący.następny  # Nowy węzeł wskazuje na kolejny element
            bieżący.następny = nowy_węzeł  # Węzeł przed dodanym wskazuje na nowy węzeł

    #Dodawanie elementu na koniec listy
    def dodaj_na_koniec(self, wartość):
        nowy_węzeł = Węzeł(wartość)
        if self.głowa is None:  # Jeśli lista jest pusta
            self.głowa = nowy_węzeł
            return

        # Przechodzimy na koniec listy
        bieżący = self.głowa
        while bieżący.następny is not None:
            bieżący = bieżący.następny

        # Dodajemy nowy węzeł na końcu
        bieżący.następny = nowy_węzeł

    # Usuwanie elementu z początku listy
    def usuń_z_początku_listy(self):
        if self.głowa is None:
            print("Lista nie zawiera żadnego elementu!")
            return
        self.głowa = self.głowa.następny

    # Usuwanie elementu w środku listy (na danym indeksie)
    def usuń_ze_srodka(self, indeks):
        if indeks < 0:
            print("Indeks nie może być ujemny!")
            return

        bieżący = self.głowa
        bieżący_indeks = 0

        if bieżący is None:
            print("Lista jest pusta!")
            return

        if indeks == 0:
            self.głowa = self.głowa.następny
            return

        # Szukamy elementu na odpowiednim indeksie
        while bieżący is not None and bieżący_indeks < indeks - 1:
            bieżący = bieżący.następny
            bieżący_indeks += 1

        if bieżący is None or bieżący.następny is None:
            print("Indeks poza zakresem!")
        else:
            bieżący.następny = bieżący.następny.następny  # Przeskakujemy element do usunięcia

    # Usuwanie elementu z końca listy
    def usuń_z_końca(self):
        if self.głowa is None:
            print("Lista nie zawiera żadnego elementu!")
            return

        bieżący = self.głowa
        while bieżący.następny is not None and bieżący.następny.następny is not None:
            bieżący = bieżący.następny

        bieżący.następny = None

    # Wyświetlanie elementów listy
    def wyswietl(self):
        bieżący = self.głowa
        if bieżący is None:
            print("Lista jest pusta!")
            return

        while bieżący:
            if bieżący.następny:  # Poprawiona nazwa zmiennej
                print(bieżący.wartość, end=" -> ")
            else:
                print(bieżący.wartość, end=" -> None")  # Wyświetlamy 'None' tylko na końcu
            bieżący = bieżący.następny
        print()  # Kończymy wypisywanie listy

    # Wyświetlanie poszczególnych elementów listy
    def wyświetl_indeks(self, indeks):
        if indeks < 0:
            print("Indeks nie może być ujemny")
            return

        bieżący = self.głowa
        bieżący_indeks = 0

        # Przechodzimy przez listę, szukając odpowiedniego indeksu
        while bieżący is not None:
            if bieżący_indeks == indeks:
                return bieżący
            bieżący = bieżący.następny
            bieżący_indeks += 1

        # Jeśli indeks jest za duży
        print("Podany indeks jest za duży!")
        return None

    def długość_listy(self):
        if self.głowa is None:
            print("Lista nie zawiera żadnego elementu!")
            return 0

        bieżący = self.głowa
        bieżący_indeks = 0

        while bieżący is not None:
            bieżący_indeks += 1
            bieżący = bieżący.następny

        return bieżący_indeks

    def czy_pusta(self):
        """
        Sprawdza, czy lista jest pusta.
        Zwraca True, jeśli lista jest pusta, w przeciwnym razie False.
        """
        return self.głowa is None

    def usun_wszystko(self):
        """
        Usuwa wszystkie elementy z listy.
        """
        self.głowa = None

    def znajdz(self, wartość):
        """
        Wyszukuje element w liście po wartości.
        Zwraca węzeł, jeśli znajdzie element, w przeciwnym razie None.
        """
        aktualny = self.głowa
        while aktualny:
            if aktualny.wartość == wartość:
                return aktualny
            aktualny = aktualny.następny
        return None

    def zamien(self, wartość1, wartość2):
        """
        Zamienia dwa elementy miejscami na podstawie ich wartości.
        Jeśli któryś z elementów nie istnieje, metoda nic nie robi.
        """
        if wartość1 == wartość2:
            return

        # Znajdź poprzedników i aktualne węzły dla obu wartości
        poprzedni1 = poprzedni2 = None
        węzeł1 = węzeł2 = self.głowa

        while węzeł1 and węzeł1.wartość != wartość1:
            poprzedni1 = węzeł1
            węzeł1 = węzeł1.następny

        while węzeł2 and węzeł2.wartość != wartość2:
            poprzedni2 = węzeł2
            węzeł2 = węzeł2.następny

        # Jeśli któryś z elementów nie został znaleziony, zakończ
        if not węzeł1 or not węzeł2:
            return

        # Jeśli węzeł1 nie jest głową, ustaw jego poprzednika na węzeł2
        if poprzedni1:
            poprzedni1.następny = węzeł2
        else:
            self.głowa = węzeł2

        # Jeśli węzeł2 nie jest głową, ustaw jego poprzednika na węzeł1
        if poprzedni2:
            poprzedni2.następny = węzeł1
        else:
            self.głowa = węzeł1

        # Zamień następne wskaźniki
        węzeł1.następny, węzeł2.następny = węzeł2.następny, węzeł1.następny


lista = Lista_Jednokierunkowa()
lista.dodaj_na_początek_listy(3)
lista.dodaj_na_początek_listy(5)
lista.dodaj_na_początek_listy(4)
lista.dodaj_na_początek_listy(2)
lista.dodaj_wewnątrz(13,2)
lista.dodaj_wewnątrz(12,2)
lista.dodaj_wewnątrz(14,6)
lista.wyswietl()
lista.usuń_ze_srodka(1)
lista.usuń_z_początku_listy()
lista.wyswietl()
print(lista.wyświetl_indeks(0))
print(lista.długość_listy())
