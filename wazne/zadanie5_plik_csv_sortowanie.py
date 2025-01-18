'''
Wczytaj dane z pliku csv. Znajdują się tam kolumny Nazwisko i Wynagrodzenie.
Zaimplementuj odpowiedni algorytm sortowania i posortuj
te dane względem wynagrodzenia. Jeżeli wynagrodzenie powtarza się,
 posortuj określonych pracowników według nazwiska.
'''
import csv

plik_csv = "dane.csv"
try:
    with open(plik_csv, newline='', encoding='utf-8') as plik:
        czytnik = csv.reader(plik)
        naglowki = next(czytnik)

        if "Nazwisko" in naglowki and "Wynagrodzenie" in naglowki:
            indeks_nazwisko = naglowki.index("Nazwisko")
            indeks_wynagrodzenie = naglowki.index("Wynagrodzenie")

            dane = []
            for wiersz in czytnik:
                nazwisko = wiersz[indeks_nazwisko]
                wynagrodzenie = float(wiersz[indeks_wynagrodzenie])
                dane.append((nazwisko, wynagrodzenie))

            posortowane_dane = sorted(dane, key=lambda x: (x[1], x[0]))

            print("Posortowane dane:")
            for nazwisko, wynagrodzenie in posortowane_dane:
                print(f"{nazwisko}: {wynagrodzenie}")
        else:
            print("Plik CSV nie zawiera wymaganych kolumn: 'Nazwisko' i 'Wynagrodzenie'.")
except FileNotFoundError:
    print(f"Plik {plik_csv} nie został znaleziony.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
