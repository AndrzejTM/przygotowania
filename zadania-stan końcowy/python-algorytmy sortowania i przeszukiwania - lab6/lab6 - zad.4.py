import random
import time

# Funkcja sortująca bąbelkowo
def sortowanie_babelkowe(lista):
    n = len(lista)
    for i in range(n):
        zamiana = False
        # Przechodzimy przez listę od 0 do n-i-1
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                # Zamiana miejscami
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamiana = True
        # Jeśli w danym przebiegu nie było zamiany, kończymy działanie
        if not zamiana:
            break

# Testowanie sortowania na małej liście (10 elementów)
lista_mala = random.sample(range(1, 101), 10)
print("Przed sortowaniem lista_mala:", lista_mala)

start_time = time.time()
sortowanie_babelkowe(lista_mala)
end_time = time.time()

print("Po sortowaniu lista_mala:", lista_mala)
print(f"Czas sortowania małej listy: {end_time - start_time:.6f} sekund")

# Testowanie sortowania na dużej liście (1000 elementów)
lista_duza = random.sample(range(1, 10001), 1000)
print("\nPrzed sortowaniem lista_duza, pierwsze 10 elementów:", lista_duza[:10])

start_time = time.time()
sortowanie_babelkowe(lista_duza)
end_time = time.time()

print("Po sortowaniu lista_duza, pierwsze 10 elementów:", lista_duza[:10])
print(f"Czas sortowania dużej listy: {end_time - start_time:.6f} sekund")
