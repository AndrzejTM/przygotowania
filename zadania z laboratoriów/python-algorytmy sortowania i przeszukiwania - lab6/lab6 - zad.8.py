import random

# Lista liczb
lista = [random.randint(1, 10) for _ in range(100)]  # Lista liczb od 1 do 10

# Sortowanie listy
lista.sort()

najczestszy = None
max_wystapien = 0
obecny_element = None
licznik = 0

for liczba in lista:  # Iterujemy przez każdy element w posortowanej liście
    if liczba == obecny_element:  # Sprawdzamy, czy bieżąca liczba jest taka sama jak poprzednia (obecny_element)
        licznik += 1  # Jeśli tak, zwiększamy licznik wystąpień dla tej liczby
    else:  # Jeśli bieżąca liczba jest inna niż obecny_element (zmiana liczby)
        if licznik > max_wystapien:  # Sprawdzamy, czy licznik wystąpień dla poprzedniej liczby jest większy niż max_wystapien
            max_wystapien = licznik  # Jeśli tak, aktualizujemy max_wystapien na wartość licznika
            najczestszy = obecny_element  # Aktualizujemy najczestszy na poprzednią liczbę (obecny_element)
        obecny_element = liczba  # Ustawiamy nową bieżącą liczbę (obecny_element)
        licznik = 1  # Resetujemy licznik dla nowej liczby na 1 (pierwsze wystąpienie)

# Po zakończeniu pętli sprawdzamy ostatnią liczbę, która mogła mieć najwięcej wystąpień
if licznik > max_wystapien:  # Sprawdzamy, czy licznik wystąpień dla ostatniej liczby jest większy niż max_wystapien
    max_wystapien = licznik  # Jeśli tak, aktualizujemy max_wystapien na wartość licznika
    najczestszy = obecny_element  # Aktualizujemy najczestszy na ostatnią liczbę


print(lista)
print("Najczęstsza liczba to:", najczestszy, "i ma", max_wystapien, "wystąpień")



