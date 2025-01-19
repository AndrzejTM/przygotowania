def wyszukiwanie_liniowe(lista, szukana_liczba):
    for indeks in range(len(lista)):
        if lista[indeks] == szukana_liczba:
            return indeks
    return -1

# Przykład użycia:
liczby = [5, 3, 7, 1, 9]
print(wyszukiwanie_liniowe(liczby, 7))  # Wynik: 2

def wyszukiwanie_binarne(lista, szukana_liczba):
    poczatek, koniec = 0, len(lista) - 1
    while poczatek <= koniec:
        srodek = (poczatek + koniec) // 2
        if lista[srodek] == szukana_liczba:
            return srodek
        elif lista[srodek] < szukana_liczba:
            poczatek = srodek + 1
        else:
            koniec = srodek - 1
    return -1

# Przykład użycia:
liczby = [1, 3, 5, 7, 9]
print(wyszukiwanie_binarne(liczby, 7))  # Wynik: 3

def wyszukaj_w_liscie(lista, fraza):
    return fraza in lista, lista.index(fraza)

# Przykład użycia:
lista_slow = ["kot", "pies", "ptak", "ryba"]
print(wyszukaj_w_liscie(lista_slow, "pies"))  # Wynik: True

def wyszukaj_w_zbiorze(zbior, element):
    return element in zbior

# Przykład użycia:
zbior = {"jabłko", "banan", "gruszka"}
print(wyszukaj_w_zbiorze(zbior, "banan"))  # Wynik: True

def wyszukaj_w_slowniku(slownik, klucz):
    return slownik.get(klucz)

# Przykład użycia:
slownik = {"kot": "mruczy", "pies": "szczeka", "krowa": "muczy"}
print(wyszukaj_w_slowniku(slownik, "pies"))  # Wynik: "szczeka"

def kmp_preprocess(wzorzec):
    dlugosc = len(wzorzec)
    lps = [0] * dlugosc
    j = 0
    for i in range(1, dlugosc):
        if wzorzec[i] == wzorzec[j]:
            j += 1
            lps[i] = j
        else:
            if j != 0:
                j = lps[j - 1]
                i -= 1
            else:
                lps[i] = 0
    return lps

def wyszukaj_kmp(tekst, wzorzec):
    lps = kmp_preprocess(wzorzec)
    i, j = 0, 0
    wyniki = []
    while i < len(tekst):
        if tekst[i] == wzorzec[j]:
            i += 1
            j += 1
        if j == len(wzorzec):
            wyniki.append(i - j)
            j = lps[j - 1]
        elif i < len(tekst) and tekst[i] != wzorzec[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return wyniki


def wyszukiwanie_interpolacyjne(lista, szukana_liczba):
    """
    Wyszukiwanie interpolacyjne w posortowanej liście.

    :param lista: Posortowana lista, w której wyszukujemy element.
    :param szukana_liczba: Element do znalezienia.
    :return: Indeks elementu, jeśli znaleziony; -1 w przeciwnym razie.
    """
    poczatek = 0
    koniec = len(lista) - 1

    while poczatek <= koniec and szukana_liczba >= lista[poczatek] and szukana_liczba <= lista[koniec]:
        # Szacowanie pozycji elementu
        if poczatek == koniec:
            if lista[poczatek] == szukana_liczba:
                return poczatek
            return -1

        # Obliczenie pozycji przybliżonej
        pozycja = poczatek + (
                    (koniec - poczatek) // (lista[koniec] - lista[poczatek]) * (szukana_liczba - lista[poczatek]))

        # Sprawdzenie, czy znaleźliśmy element
        if lista[pozycja] == szukana_liczba:
            return pozycja

        # Decyzja, w którym zakresie kontynuować wyszukiwanie
        if lista[pozycja] < szukana_liczba:
            poczatek = pozycja + 1
        else:
            koniec = pozycja - 1

    return -1

def wyszukiwanie_z_haszowaniem(lista, szukana_liczba):
    """
    Wyszukiwanie elementu z wykorzystaniem zbioru haszującego.

    :param lista: Lista elementów, które chcemy przeszukać.
    :param szukana_liczba: Element do znalezienia.
    :return: True, jeśli element istnieje; False w przeciwnym razie.
    """
    zbior_haszujacy = set(lista)  # Tworzenie zbioru haszującego
    return szukana_liczba in zbior_haszujacy


# Przykład użycia:
tekst = "abcabcbcad"
wzorzec = "abc"
print(wyszukaj_kmp(tekst, wzorzec))  # Wynik: [0, 3, 6]
