class Zwierze:
    def __init__(self, imie):
        if not imie:
            raise ValueError("Imię nie może być puste")
        self.imie = imie

    def przedstaw_sie(self):
        return f"Jestem {self.imie}"
class Rybka(Zwierze):
    def __init__(self, imie, kolor, czy_akwariowa, gatunek=None):
        super().__init__(imie)
        if not kolor:
            raise ValueError("Każda ryba musi mieć jakiś kolor!")
        if not gatunek:
            gatunek = "brak danych"
        if not isinstance(czy_akwariowa, bool):
            raise ValueError("Wartość dla 'czy_akwariowa' musi byćtypu bool")
        self.kolor = kolor
        self.czy_akwariowa = czy_akwariowa
        self.gatunek = gatunek

    def przedstaw_sie(self):
        akwariowa_info = 'akwariowa' if self.czy_akwariowa else 'nie akwariowa'
        return f"Jestem {self.imie}, mój kolor to: {self.kolor}, mój gatunek: {self.gatunek} i jestem {akwariowa_info}"

class Bydło(Zwierze):
    def __init__(self, imie, płeć, rozmiar, kraj_pochodzenia=None):
        super().__init__(imie)
        if płeć not in ["byk", "krowa"]:
            raise ValueError("Nazleży wybrać jedną z dwóch płci!")
        if not rozmiar:
            raise ValueError("Każde zwierzę ma jakiś rozmiar")
        if not kraj_pochodzenia:
            kraj_pochodzenia = "brak danych"
        self.płeć = płeć
        self.rozmiar = rozmiar
        self.kraj_pochodzenia = kraj_pochodzenia

    def przedstaw_sie(self):
        return f"Jestem {self.imie}, płci: {self.płeć}, rozmiaru: {self.rozmiar}, a mój kraj pochodzenia to: {self.kraj_pochodzenia}"

class Małpa(Zwierze):
    def __init__(self, imie, płeć, kolor, czy_niebezpieczny, gatunek = None):
        super().__init__(imie)
        if płeć not in ["samiec", "samica"]:
            raise ValueError("Należy podać płeć")
        if not kolor:
            raise ValueError("Należy podać kolor")
        if not gatunek:
            gatunek = "brak danych"
        if not isinstance(czy_niebezpieczny, bool):
            raise ValueError("Wartość dla 'czy_niebezpieczny' musi byćtypu bool")
        self.płeć = płeć
        self.kolor = kolor
        self.gatunek = gatunek
        self.czy_niebezpieczny = czy_niebezpieczny

    def przedstaw_sie(self):
        niebezpieczny_info = "niebezpieczny" if self.czy_niebezpieczny else "bezpieczny"
        return f"Jestem {self.imie}, płci: {self.płeć}, koloru: {self.kolor}, jestem {niebezpieczny_info} a mój gatunek to: {self.gatunek}"



moje_bydło = Bydło("Jack", "byk", "duży")
print(moje_bydło.przedstaw_sie())
moja_rybka = Rybka("Pasiak", "żółto-czarna", True, "Bocja" )
print(moja_rybka.przedstaw_sie())
moje_bydło = Bydło("Mućka", "krowa", "średni", "USA")
print(moje_bydło.przedstaw_sie())
moja_rybka = Rybka("Ufoludek", "zielony", False)
print(moja_rybka.przedstaw_sie())
moja_małpa = Małpa("King-Kong", "samiec", "biało-czarny",  True)
print(moja_małpa.przedstaw_sie())







