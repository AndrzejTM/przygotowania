import time  # Importujemy moduł time

lista = ["Adamczyk", "Bąk", "Chmielewski", "Dąbrowski", "Górski", "Kowalski", "Lewandowski", "Nowak", "Piotrowski",
         "Szymański", "Wiśniewski", "Zieliński"]


# Funkcja wyszukiwania liniowego
def wyszukiwanie_liniowe(lista, szukany):
    lista_wyszukanych = list()  # Lista do przechowywania wyników wyszukiwania
    for indeks, element in enumerate(lista):  # Przechodzimy po każdym elemencie listy
        if element == szukany:  # Jeśli element jest równy szukanemu, zapisujemy jego indeks
            lista_wyszukanych.append(indeks)
    return lista_wyszukanych  # Zwracamy listę indeksów, gdzie znaleziono element


# Funkcja wyszukiwania binarnego (zakłada posortowaną listę)
def wyszukiwanie_binarne(lista, szukany):
    lewy, prawy = 0, len(lista) - 1  # Ustalamy początkowe granice przeszukiwania
    while lewy <= prawy:  # Dopóki lewy wskaźnik nie przekroczy prawego
        srodek = (lewy + prawy) // 2  # Obliczamy środek listy
        if lista[srodek] == szukany:  # Jeśli środkowy element to szukany, zwracamy jego indeks
            return srodek
        elif lista[srodek] < szukany:  # Jeśli szukany element jest większy, przesuwamy lewy wskaźnik
            lewy = srodek + 1
        else:  # Jeśli szukany element jest mniejszy, przesuwamy prawy wskaźnik
            prawy = srodek - 1
    return -1  # Jeśli element nie zostanie znaleziony, zwracamy -1


# Funkcja do mierzenia czasu wykonania obu funkcji (z powtórzeniami)
def mierzenie_czasu(lista, szukany, powtorzenia=10000):
    # Mierzymy czas wykonania wyszukiwania binarnego
    start_time = time.perf_counter()  # Używamy perf_counter dla dokładniejszych pomiarów
    for _ in range(powtorzenia):  # Wykonujemy funkcję wiele razy
        wyszukiwanie_binarne(lista, szukany)  # Wywołujemy funkcję wyszukiwania binarnego
    czas_binarny = time.perf_counter() - start_time  # Obliczamy czas wykonania funkcji wyszukiwania binarnego

    # Mierzymy czas wykonania wyszukiwania liniowego
    start_time = time.perf_counter()  # Używamy perf_counter dla dokładniejszych pomiarów
    for _ in range(powtorzenia):  # Wykonujemy funkcję wiele razy
        wyszukiwanie_liniowe(lista, szukany)  # Wywołujemy funkcję wyszukiwania liniowego
    czas_liniowy = time.perf_counter() - start_time  # Obliczamy czas wykonania funkcji wyszukiwania liniowego

    # Zwracamy czasy wykonania obu funkcji
    return czas_binarny, czas_liniowy

wyszukaj_binarnie=wyszukiwanie_binarne(lista, "Lewandowski")
print(wyszukaj_binarnie)
wyszukaj_liniowo=wyszukiwanie_liniowe(lista, "Lewandowski")
print(wyszukaj_liniowo)
# Testujemy funkcje i mierzymy czasy
czas_binarny, czas_liniowy = mierzenie_czasu(lista, "Dąbrowski")

# Wyświetlamy wyniki
print(f"Czas wykonania wyszukiwania binarnego (z {10000} powtórzeniami): {czas_binarny:.6f} sekund")
print(f"Czas wykonania wyszukiwania liniowego (z {10000} powtórzeniami): {czas_liniowy:.6f} sekund")
