import random

lista1 = [3, 6, 5, 3, 6, 3, 6, 3, 1, 4, 6, 3, 2, 1, 1, 3, 6, 5, 1, 3, 1, 4, 3, 5, 3, 5, 2, 5, 3, 1]

def sortowanie_babelkowe(lista1):
    n = len(lista1)
    licznik = 0
    for i in range(n):
        zamiana = False
        for j in range (n - 1 - i):
            if lista1[j] > lista1[j+1]:
                lista1[j], lista1[j+1] = lista1[j+1], lista1[j]
                licznik +=1
                zamiana = True
        if not zamiana:
            break
    return lista1,licznik


sortuj_bąbelkowo = sortowanie_babelkowe(lista1)
print("Oto posortowana lista:",sortuj_bąbelkowo)

lista2 = [random.randint(1, 1000) for _ in range(1000)]

def sortowanie_przez_zliczanie(lista2):
    if not lista2:
        return []  # Zwróć pustą listę, jeśli dane wejściowe są puste
    # Znajdź maksymalną wartość w tablicy
    maksymalna_wartosc = max(lista2)

    # Utwórz tablicę do zliczania elementów (od 0 do maksymalnej wartości)
    zliczanie = [0] * (maksymalna_wartosc + 1)

    # Zliczanie wystąpień elementów w tablicy
    for liczba in lista2:
        zliczanie[liczba] += 1

    # Odtworzenie posortowanej tablicy
    posortowana_tablica = []
    for i in range(len(zliczanie)):
        posortowana_tablica.extend([i] * zliczanie[i])  # Dodaj wartość `i`, powtórzoną `zliczanie[i]` razy

    return posortowana_tablica

sortuj_przez_zliczanie = sortowanie_przez_zliczanie(lista2)
print(sortuj_przez_zliczanie[:20])

lista3 = [3, 5, 8, 12]
lista4 = [2, 7, 10, 14]

def scalanie(lewa, prawa):
    lista5 = []
    i = j = 0

    # Przechodzimy przez obie części i dodajemy mniejsze elementy do wynikowej listy
    while i < len(lewa) and j < len(prawa):
        if lewa[i] < prawa[j]:
            lista5.append(lewa[i])
            i += 1
        else:
            lista5.append(prawa[j])
            j += 1

    # Dodajemy pozostałe elementy z lewej i prawej części
    lista5.extend(lewa[i:])
    lista5.extend(prawa[j:])

    return lista5

lista5 = scalanie(lista3, lista4)
print(lista5)

lista6 = [89, 45, 68, 90, 29, 34]

def sortowanie_przez_wstawianie(lista6, lewy, prawy):
    # Sortowanie fragmentu za pomocą sortowania przez wstawianie
    for i in range(lewy + 1, prawy + 1):
        klucz = lista6[i]
        j = i - 1
        while j >= lewy and lista6[j] > klucz:
            lista6[j + 1] = lista6[j]
            j -= 1
        lista6[j + 1] = klucz

def scalanie(lista6, lewy, srodek, prawy):
    # Tworzymy kopie fragmentów listy
    lewa_czesc = lista6[lewy:srodek + 1]
    prawa_czesc = lista6[srodek + 1:prawy + 1]

    # Wskaźniki dla scalania
    i = j = 0
    k = lewy

    while i < len(lewa_czesc) and j < len(prawa_czesc):
        if lewa_czesc[i] <= prawa_czesc[j]:
            lista6[k] = lewa_czesc[i]
            i += 1
        else:
            lista6[k] = prawa_czesc[j]
            j += 1
        k += 1

    # Dodanie pozostałych elementów
    while i < len(lewa_czesc):
        lista6[k] = lewa_czesc[i]
        i += 1
        k += 1

    while j < len(prawa_czesc):
        lista6[k] = prawa_czesc[j]
        j += 1
        k += 1

def timsort(lista6):
    # Określenie minimalnego rozmiaru runa
    MIN_RUN = 32
    n = len(lista6)

    # Sortowanie małych fragmentów
    for start in range(0, n, MIN_RUN):
        koniec = min(start + MIN_RUN - 1, n - 1)
        sortowanie_przez_wstawianie(lista6, start, koniec)

    # Scalanie posortowanych fragmentów
    rozmiar = MIN_RUN
    while rozmiar < n:
        for lewy in range(0, n, 2 * rozmiar):
            srodek = min(lewy + rozmiar - 1, n - 1)
            prawy = min(lewy + 2 * rozmiar - 1, n - 1)
            if srodek < prawy:
                scalanie(lista6, lewy, srodek, prawy)
        rozmiar *= 2

sortuj_Tim_Sort = timsort(lista6)
print(sortuj_Tim_Sort)

lista7 = [75, 89, 62, 93, 58, 84, 73, 91, 66, 77, 85, 60, 70, 88, 64]
def quicksort(lista7):
    # Jeśli lista ma 1 lub 0 elementów, jest już posortowana
    if len(lista7) <= 1:
        return lista7
    else:
        # Wybieramy pierwszy element jako pivot
        pivot = lista7[0]
        # Podział listy na mniejsze/równe pivotowi oraz większe od pivota
        mniejsze = [x for x in lista7[1:] if x <= pivot]
        wieksze = [x for x in lista7[1:] if x > pivot]
        # Rekurencyjne sortowanie i łączenie wyników
        return quicksort(mniejsze) + [pivot] + quicksort(wieksze)

sortuj_szybko = quicksort(lista7)
print(sortuj_szybko)

nazwiska = ["Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski",
"Zieliński", "Szymański", "Woźniak", "Dąbrowski", "Zając", "Król", "Wieczorek", "Majewski",
"Olszewski", "Stępień", "Jaworski", "Malinowski", "Adamczyk", "Górski", "Nowicki",
"Pawlak", "Wróbel", "Pawłowski", "Michalski", "Sikora", "Krajewski", "Baran",
"Tomczak", "Markowski", "Borkowski", "Sadowski", "Jankowski", "Przybylski",
"Wesołowski", "Chmielewski", "Czarnecki", "Urbański", "Grabowski", "Błaszczyk",
"Wilk", "Włodarczyk", "Biernacki", "Michalak", "Zych", "Głowacki", "Lis", "Makowski"]

# Sortowanie alfabetyczne
sorted_names = sorted(nazwiska)

# Sortowanie w odwrotnej kolejności
reverse_sorted_names = sorted(nazwiska, reverse=True)
print("Pierwsze 5 nazwisk (alfabetycznie):", sorted_names[:5])
