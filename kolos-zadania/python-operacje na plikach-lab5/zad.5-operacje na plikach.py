import pickle

# Definicja klasy Pracownik
class Pracownik:
    def __init__(self, imie, wiek, stanowisko):
        self.imie = imie
        self.wiek = wiek
        self.stanowisko = stanowisko

    def __repr__(self):
        return f"Imię: {self.imie}, Wiek: {self.wiek}, Stanowisko: {self.stanowisko}"

# Wczytanie obiektów z pliku pracownicy.pkl
try:
    with open('pracownicy.pkl', 'rb') as file:
        pracownicy = pickle.load(file)
except FileNotFoundError:
    # Jeśli plik nie istnieje, zaczynamy z pustą listą
    pracownicy = []

# Wyświetlenie szczegółów każdego pracownika
for pracownik in pracownicy:
    print(pracownik)

# Dodanie nowego pracownika
imie = input("Podaj imię nowego pracownika: ")
wiek = int(input("Podaj wiek nowego pracownika: "))
stanowisko = input("Podaj stanowisko nowego pracownika: ")

nowy_pracownik = Pracownik(imie, wiek, stanowisko)

# Dodanie nowego pracownika do listy
pracownicy.append(nowy_pracownik)

# Zapisanie zaktualizowanej listy pracowników do pliku pracownicy.pkl
with open('pracownicy.pkl', 'wb') as file:
    pickle.dump(pracownicy, file)

print("Nowy pracownik został dodany i lista pracowników została zapisana.")
