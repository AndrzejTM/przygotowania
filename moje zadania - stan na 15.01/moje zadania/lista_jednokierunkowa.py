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

# sprawdzanie czy lista jest pusta, usuwanie wszystkich elemnetów, wyszukiwanie elementu po wartości, zamiana dwóch elementów miejscami