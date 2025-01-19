import pickle  # Importujemy moduł pickle, który służy do serializacji i deserializacji obiektów w Pythonie

# Definiujemy klasę Pracownik, która będzie reprezentować pojedynczego pracownika
class Pracownik:
    def __init__(self, Imię, Wiek, Zawód):
        # Inicjalizacja obiektu z trzema atrybutami: Imię, wiek i zawód
        self.Imię = Imię
        self.Wiek = Wiek
        self.Zawód = Zawód

    def __repr__(self):
        # Reprezentacja obiektu w postaci czytelnej dla użytkownika
        return f"Imię: {self.Imię}, Wiek: {self.Wiek}, Stanowisko: {self.Zawód}"

# Blok try-except pozwala obsłużyć potencjalne błędy podczas otwierania pliku
try:
    # Otwieramy plik 'zawody.pkl' w trybie binarnym do odczytu ('rb')
    with open('zawody.pkl', 'rb') as file:
        # Ładujemy dane z pliku za pomocą pickle
        dane = pickle.load(file)

        # Tworzymy listę obiektów Pracownik na podstawie załadowanych danych
        # Każdy element w danych (słownik) przekazywany jest jako argumenty do konstruktora Pracownik
        zawody = [Pracownik(**pracownik) for pracownik in dane]
except FileNotFoundError:
    # Jeśli plik 'zawody.pkl' nie istnieje, ustawiamy listę zawody jako pustą
    zawody = []

# Iterujemy przez listę zawody i wyświetlamy informacje o każdym pracowniku
for pracownik in zawody:
    print(pracownik)
