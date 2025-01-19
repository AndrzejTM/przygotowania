class Figura:
    def __init__(self, nazwa):
        if not nazwa:
            raise ValueError ("Każda figura ma jakąś nazwę")
        self.nazwa = nazwa

    def nazwa_figury(self):
        return f"Jestem {self.nazwa}"

moja_figura = Figura("kwadrat")
print(moja_figura.nazwa_figury())

class Koło(Figura):
    def __init__(self, nazwa, promień):
        super().__init__(nazwa)
        if not promień:
            raise ValueError("Promień musi być podany!")
        self.promień = promień

    @property
    def średnica(self):
            return 2 * self.promień

    @property
    def pole(self):
            return round(3.14 * self.promień * self.promień, 2)
    def nazwa_figury(self):
        return f"Jestem {self.nazwa}, mój promień wynosi: {self.promień}, moja średnica wynosi: {self.średnica}, a pole {self.pole}"

moje_koło = Koło("koło",promień = 5)
print(moje_koło.nazwa_figury())

class Prostokąt(Figura):
    def __init__(self, nazwa, pierwszy_bok, drugi_bok):
        super().__init__(nazwa)
        if not pierwszy_bok:
            raise ValueError("Prosze podać długość pierwszego boku!")
        if not drugi_bok:
            raise ValueError("Prosze podać długość drugiego boku!")
        self.pierwszy_bok = pierwszy_bok
        self.drugi_bok = drugi_bok

    @property
    def pole(self):
        return self.pierwszy_bok * self.drugi_bok

    @property
    def obwód(self):
        return 2 * self.pierwszy_bok + 2 * self.drugi_bok

    def nazwa_figury(self):
        return f"Jestem {self.nazwa}, moje boki to: {self.pierwszy_bok}, {self.drugi_bok}, moje pole wynosi: {self.pole}, a obwód: {self.obwód}"

mój_prostokąt = Prostokąt("Prostokąt", pierwszy_bok=11155, drugi_bok=2225)
print(mój_prostokąt.nazwa_figury())





