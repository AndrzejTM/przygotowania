class Krawedz:
    def __init__(self, laczenie, kierunek="S", waga=None):
        (self.zrodlo, self.cel) = laczenie
        if kierunek == "S" or kierunek == "N":
            self.kierunek = kierunek
        else:
            self.kierunek = "S"

        self.waga = waga

    def __str__(self):
        if self.kierunek == "S":
            return f"[{str(self.zrodlo)} -> {str(self.cel)}, w={self.waga}]\t"
        else:
            return f"[{str(self.zrodlo)} <-> {str(self.cel)}, w={self.waga}]\t"

    def odwroc_kierunek(self):
        if self.kierunek == "S":
            temp_zrodlo = self.zrodlo
            self.zrodlo = self.cel
            self.cel = temp_zrodlo

        else:
            print("Typ kierunku jest nieskierowany")

    def zmien_typ_kierunku(self):
        if self.kierunek == "S":
            self.kierunek = "T"
        else:
            self.kierunek = "S"
