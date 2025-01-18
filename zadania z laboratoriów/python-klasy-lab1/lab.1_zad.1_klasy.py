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
    def __init__(self, imie, rasa, czy_szczeka_czesto):
        super().__init__(imie)
        self._rasa = rasa
        self._czy_szczeka_czesto = czy_szczeka_czesto
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

    def przedstaw_sie(self):
        szczeka_info = "szczekam często" if self.czy_szczeka_czesto else "nie szczekam często"
        return f"Jestem {self.imie}, a moja rasa to {self.rasa} i {szczeka_info}"

class Kot(Zwierze):
    def __init__ (self, imie, ulubione_jedzenie):
        super().__init__(imie)
        self._ulubione_jedzenie = ulubione_jedzenie
    @property
    def ulubione_jedzenie(self):
        return self._ulubione_jedzenie
    @ulubione_jedzenie.setter
    def ulubione_jedzenie(self, wartosc):
        if not wartosc:
            raise ValueError("Ulubione jedzenie nie może być puste")
        self._ulubione_jedzenie = wartosc

    def przedstaw_sie(self):
        return f"Jestem {self.imie}, a moje ulubione jedzenie to {self.ulubione_jedzenie}"


mój_pies = Pies("Burek", "Labrador", 1)
print(mój_pies.przedstaw_sie())
mój_kot = Kot("Mruczek", "sucha karma")
print(mój_kot.przedstaw_sie())
moje_zwierzę = Zwierze("Tom")
print(moje_zwierzę.przedstaw_sie())