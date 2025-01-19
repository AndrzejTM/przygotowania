import random

# Generowanie losowej listy
lista = [random.randint(1, 100) for _ in range(20)]
lista.sort()  # Sortowanie listy

# Wyszukiwanie binarne
def wyszukiwanie_binarne(lista, szukana):
    lewy, prawy = 0, len(lista) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == szukana:
            return srodek
        elif lista[srodek] < szukana:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1

# Szukana liczba
szukana = random.randint(1, 100)
wynik = wyszukiwanie_binarne(lista, szukana)

print("Lista (posortowana):", lista)
print(f"Szukana liczba: {szukana}")
if wynik != -1:
    print(f"Liczba {szukana} znaleziona na pozycji {wynik}.")
else:
    print(f"Liczba {szukana} nie została znaleziona.")
