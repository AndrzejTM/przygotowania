class Zwierze:
    def __init__(self, imie):
        self._imie = imie
    @property
    def imie(self):
        return self._imie
    @imie.setter
    def imie(self, wartosc):
        if not wartosc:
            raise ValueError("Imię nie może być puste")
        self._imie = wartosc
    def przedstaw_sie(self):
        return f"Jestem {self._imie}"

class Pies(Zwierze):
    def __init__(self, imie, rasa, czy_szczeka_czesto, wiek, kolor_siersci):
        super().__init__(imie)
        self._rasa = rasa
        self._czy_szczeka_czesto = czy_szczeka_czesto
        self._wiek = wiek
        self._kolor_siersci = kolor_siersci
    @property
    def rasa(self):
        return self._rasa
    @rasa.setter
    def rasa(self, wartosc):
        if not wartosc:
            raise ValueError("Rasa nie może być pusta")
        self._rasa = wartosc
    @property
    def czy_szczeka_czesto(self):
        return self._czy_szczeka_czesto
    @czy_szczeka_czesto.setter
    def czy_szczeka_czesto(self, wartosc):
        if not isinstance(wartosc, bool):
            raise ValueError("Wartość dla 'czy szczeka często' musi być typu boolean (True/False)")
        self._czy_szczeka_czesto = wartosc

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, wartosc):
        if wartosc < 0 or not isinstance(wartosc, int):
            raise ValueError("Wiek musi być liczbą całkowitą dodatnią")
        self._wiek = wartosc

    @property
    def kolor_siersci(self):
        return self._kolor_siersci

    @kolor_siersci.setter
    def kolor_siersci(self, wartosc):
        if not wartosc:
            raise ValueError("Kolor sierści nie może być pusty")
        self._kolor_siersci = wartosc

    def przedstaw_sie(self):
        szczeka_info = "szczekam często" if self.czy_szczeka_czesto else "nie szczekam często"
        return f"Jestem {self.imie}, a moja rasa to {self.rasa}, {szczeka_info}, mam {self._wiek} lat i kolor sierści {self.kolor_siersci}"

mój_pies = Pies("Burek", "Labrador", 0, 12, "Biały")
print(mój_pies.przedstaw_sie())