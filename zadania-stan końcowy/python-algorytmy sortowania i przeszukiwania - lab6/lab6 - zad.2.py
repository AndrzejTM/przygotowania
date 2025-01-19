import time

# Funkcja wyszukiwania binarnego
def wyszukiwanie_binarne(lista, szukany):
    lewy, prawy = 0, len(lista) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == szukany:
            return srodek
        elif lista[srodek] < szukany:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1

# Funkcja do mierzenia czasu wykonania
def zmierz_czas(opis, funkcja, *args):
    start = time.time()  # Czas rozpoczęcia
    wynik = funkcja(*args)  # Wykonanie funkcji
    koniec = time.time()  # Czas zakończenia
    print(f"{opis}: {wynik} (czas: {koniec - start:.6f} s)")  # Wyświetlenie wyniku i czasu
    return wynik

# Listy
lista1 = [1, 2, 3, 5, 7, 9, 11, 12]
lista2 = [5, 2, 7, 4, 11, 8, 14]

# Sortowanie lista2 z pomiarem czasu
zmierz_czas("Sortowanie lista2", lista2.sort)

# Wyszukiwanie liczby 5 w lista1
zmierz_czas("Wyszukiwanie liczby 5 w lista1", wyszukiwanie_binarne, lista1, 5)

# Wyszukiwanie liczby 11 w posortowanej lista2
zmierz_czas("Wyszukiwanie liczby 11 w lista2", wyszukiwanie_binarne, lista2, 11)
