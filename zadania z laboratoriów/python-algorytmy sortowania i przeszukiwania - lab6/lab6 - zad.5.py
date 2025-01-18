import random  # Importujemy moduł random, aby generować losowe liczby
import time  # Importujemy moduł time, aby mierzyć czas wykonania algorytmu


# Implementacja algorytmu sortowania przez wstawianie
def insertion_sort(arr):
    # Iterujemy przez wszystkie elementy w liście, zaczynając od drugiego (i = 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Zmienna 'key' przechowuje aktualnie rozpatrywany element
        j = i - 1  # Zmienna 'j' wskazuje na poprzedni element w liście
        # Dopóki element 'j' jest większy niż 'key', przesuwamy go na prawo
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Przesuwamy element o jedno miejsce w prawo
            j -= 1  # Przechodzimy do poprzedniego elementu
        arr[j + 1] = key  # Wstawiamy 'key' na odpowiednie miejsce


# Funkcja generująca listę częściowo posortowaną
def partially_sorted_list(n, sorted_percentage=0.9):
    # Generujemy posortowaną część listy, składającą się z 90% elementów
    sorted_part = list(range(int(n * sorted_percentage)))
    # Generujemy pozostałą część listy (n - 90%)
    unsorted_part = random.sample(range(int(n * sorted_percentage), n), n - len(sorted_part))
    # Łączymy posortowaną część z losową
    return sorted_part + unsorted_part


# Funkcja generująca listę całkowicie losową
def random_list(n):
    # Tworzymy listę z losowych liczb od 0 do n-1
    return random.sample(range(n), n)


# Funkcja do testowania algorytmu i mierzenia czasu działania
def test_insertion_sort(n):
    # Testowanie na liście częściowo posortowanej
    partially_sorted = partially_sorted_list(n)
    start_time = time.time()  # Zaczynamy pomiar czasu
    insertion_sort(partially_sorted)  # Wywołujemy funkcję sortującą
    partially_sorted_time = time.time() - start_time  # Mierzymy czas wykonania

    # Testowanie na liście losowej
    random_lst = random_list(n)
    start_time = time.time()  # Zaczynamy pomiar czasu
    insertion_sort(random_lst)  # Wywołujemy funkcję sortującą
    random_lst_time = time.time() - start_time  # Mierzymy czas wykonania

    # Zwracamy czasy wykonania dla obu przypadków
    return partially_sorted_time, random_lst_time


# Ustawienie rozmiaru listy na 1000 elementów
n = 1000  # Można zmieniać rozmiar w zależności od potrzeb

# Testujemy algorytm sortowania
partially_sorted_time, random_lst_time = test_insertion_sort(n)

# Wyświetlamy czas działania dla obu przypadków
print(f'Czas sortowania na liście częściowo posortowanej: {partially_sorted_time:.6f} sekund')
print(f'Czas sortowania na liście losowej: {random_lst_time:.6f} sekund')

