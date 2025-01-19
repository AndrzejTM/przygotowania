import csv

def wczytaj_dane_z_csv(nazwa_pliku):
    """Wczytuje dane z pliku CSV i zwraca listę słowników."""
    dane = []
    with open(nazwa_pliku, mode='r', encoding='utf-8') as plik:
        czytnik = csv.DictReader(plik)
        for wiersz in czytnik:
            # Konwertuj kolumnę 'Wynagrodzenie' na liczbę
            wiersz['Wynagrodzenie'] = float(wiersz['Wynagrodzenie'])
            dane.append(wiersz)
    return dane

def zapisz_dane_do_csv(nazwa_pliku, dane, naglowki):
    """Zapisuje posortowane dane do pliku CSV."""
    with open(nazwa_pliku, mode='w', encoding='utf-8', newline='') as plik:
        zapis = csv.DictWriter(plik, fieldnames=naglowki)
        zapis.writeheader()
        zapis.writerows(dane)

def posortuj_dane(dane):
    """Sortuje dane według wynagrodzenia, a następnie według nazwiska."""
    return sorted(dane, key=lambda x: (x['Wynagrodzenie'], x['Nazwisko']))

# Główna część programu
if __name__ == "__main__":
    # Nazwa pliku wejściowego i wyjściowego
    nazwa_pliku_wejsciowego = "baza.csv"
    nazwa_pliku_wyjsciowego = "baza_sorted.csv"

    # Wczytanie danych
    dane = wczytaj_dane_z_csv(nazwa_pliku_wejsciowego)

    # Sortowanie danych
    dane_posortowane = posortuj_dane(dane)

    # Zapisanie posortowanych danych
    naglowki = ['Nazwisko', 'Wynagrodzenie']
    zapisz_dane_do_csv(nazwa_pliku_wyjsciowego, dane_posortowane, naglowki)

    print(f"Dane zostały posortowane i zapisane w pliku: {nazwa_pliku_wyjsciowego}")
