class Osoba:
    def __init__(self, imie, wiek):
        self.__imie = imie  # Prywatny atrybut
        self.__wiek = wiek  # Prywatny atrybut

    # Getter dla imienia
    @property
    def imie(self):
        return self.__imie

    # Setter dla imienia
    @imie.setter
    def imie(self, imie):
        self.__imie = imie

    # Getter dla wieku
    @property
    def wiek(self):
        return self.__wiek

    # Setter dla wieku
    @wiek.setter
    def wiek(self, wiek):
        if wiek > 0:
            self.__wiek = wiek
        else:
            print("Wiek musi być większy niż 0!")

class Pracownik(Osoba):
    def __init__(self, imie, wiek, stanowisko):
        super().__init__(imie, wiek)  # Wywołanie konstruktora klasy bazowej
        self.__stanowisko = stanowisko  # Prywatny atrybut

    # Getter dla stanowiska
    @property
    def stanowisko(self):
        return self.__stanowisko

    # Setter dla stanowiska
    @stanowisko.setter
    def stanowisko(self, stanowisko):
        self.__stanowisko = stanowisko

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, mój wiek to {self.wiek}, a stanowisko to {self.stanowisko}")

Dane_Pracownika = Pracownik("Kuba", "23", "szef")
print(Dane_Pracownika.przedstaw_sie())




