'''
1. Graf reprezentujący strukturę projektu

Stwórz graf reprezentujący strukturę dowolnego projektu programistycznego,
na przykład projektu, nad którym obecnie pracujesz, lub struktury tego repozytorium.
    - węzły - plik i katalog w projekcie
    - krawędzie - połączenia między węzłami reprezentują importy

'''

'''
2. Stwórz własną strukturę grafu jako słownik list sąsiedztwa:
   Napisz funkcje, które pozwolą na dodawanie węzłów i krawędzi
   oraz wyświetlanie grafu. Strukturę grafu zbuduj jako słownik, gdzie:
    - Każdy węzeł jest kluczem słownika.
    - Lista sąsiedztwa zawiera węzły, z którymi jest połączony
    
   * Wymagana walidacja
'''

'''
3. Do klasy Graf dodaj funckjonalność reprezentacji grafu za pomocą macierzy sąsiedztwa.
   Dodaj nową metodę wyswietl_macierz_sasiedztwa do istniejącej klasy Graf, która wyświetli
   graf w postaci macierzy sąsiedztwa.

Przykład:
    Dodano krawędź: [A <-> B, w=2]
    Dodano krawędź: [A <-> C, w=2]
    Dodano krawędź: [B -> C, w=3]
    Dodano krawędź: [C <-> D, w=4]
    Dodano krawędź: [D <-> A, w=4]
    Dodano krawędź: [D <-> B, w=4]

    Macierz sąsiedztwa:
       A B C D
    A: 0 2 2 4
    B: 2 0 3 4
    C: 2 0 0 4
    D: 4 4 4 0

 *Nie zmieniaj pozostałych funkcjonalności klasy — dodaj tylko nową metodę.
'''