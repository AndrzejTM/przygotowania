import json

# Krok 1: Wczytanie danych z pliku JSON
try:
    with open("pracownicy.json", "r", encoding="utf-8") as file:
        pracownicy = json.load(file)
except FileNotFoundError:
    print("Plik pracownicy.json nie został znaleziony.")
    pracownicy = []

if pracownicy:
    # Krok 2: Wyświetlenie liczby pracowników
    print(f"Liczba pracowników: {len(pracownicy)}")

    # Krok 3: Wyświetlenie pracowników w dziale "IT"
    dzial = "IT"
    pracownicy_it = [p for p in pracownicy if p["Dział"] == dzial]
    print(f"Pracownicy w dziale {dzial}:")
    for p in pracownicy_it:
        print(f"  - {p['Imię']}, wiek: {p['Wiek']}")

    # Krok 4: Obliczenie średniego wieku
    sredni_wiek = sum(p["Wiek"] for p in pracownicy) / len(pracownicy)
    print(f"Średni wiek pracowników: {sredni_wiek:.2f} lat")

    # Krok 5: Zapisanie pracowników w wieku powyżej 40 lat do nowego pliku JSON
    pracownicy_40_plus = [p for p in pracownicy if p["Wiek"] > 40]
    with open("pracownicy_40_plus.json", "w", encoding="utf-8") as file:
        json.dump(pracownicy_40_plus, file, ensure_ascii=False, indent=4)
    print("Dane o pracownikach w wieku powyżej 40 lat zapisano do pliku 'pracownicy_40_plus.json'.")
