from .wezel import Wezel
from .krawedz import Krawedz


class Graf:
    def __init__(self):
        self.graf = {}

    def __str__(self):
        wynik = "Graf:\n"
        for wezel, krawedzie in self.graf.items():
            if not krawedzie:
                wynik += f"{wezel}: brak krawędzi\n"
            else:
                wynik += (f"{wezel}: " +
                          ", ".join(str(krawedz) for krawedz in krawedzie) +
                          "\n")
        return wynik

    def dodaj_wezel(self, wartosc, cele=None, kierunek="S", waga=None):
        nowy_wezel = Wezel(wartosc)

        if nowy_wezel not in self.graf:
            self.graf[nowy_wezel] = []

        if cele is not None:
            if all(Wezel(cel) in self.graf.keys() for cel in cele):
                for cel in cele:
                    self.dodaj_krawedz(wartosc, cel, kierunek, waga)
            else:
                print("Nieprawidłowe cele - dodano sam wezel")

    def dodaj_krawedz(self, zrodlo, cele, kierunek="S", waga=None):
        wezel_zrodlo = Wezel(zrodlo)

        if wezel_zrodlo not in self.graf:
            print(f"Węzeł źródłowy '{zrodlo}' nie istnieje w grafie.")
            return

        if not isinstance(cele, list):
            cele = [cele]

        for cel in cele:
            wezel_cel = Wezel(cel)

            if wezel_cel in self.graf:
                krawedz = Krawedz((wezel_zrodlo, wezel_cel),
                                  kierunek,
                                  waga)
                self.graf[wezel_zrodlo].append(krawedz)

                if kierunek == "N":
                    krawedz_do_zrodla = Krawedz((wezel_cel, wezel_zrodlo),
                                                kierunek,
                                                waga)
                    self.graf[wezel_cel].append(krawedz_do_zrodla)

                print(f"Dodano krawędź: {krawedz}")
            else:
                print(f"Węzeł docelowy '{cel}' nie istnieje w grafie.")

    def usun_wezel(self, wartosc):
        wezel_do_usuniecia = Wezel(wartosc)

        if wezel_do_usuniecia not in self.graf:
            print(f"Węzeł '{wartosc}' nie istnieje w grafie.")
            return

        del self.graf[wezel_do_usuniecia]

        for wezel, krawedzie in self.graf.items():
            self.graf[wezel] = [
                krawedz for krawedz in krawedzie
                if krawedz.cel != wezel_do_usuniecia
            ]

        print(f"Węzeł '{wartosc}' i jego krawędzie zostały usunięte.")

    def usun_krawedz(self, zrodlo, cel):
        wezel_zrodlo = Wezel(zrodlo)
        wezel_cel = Wezel(cel)

        if wezel_zrodlo not in self.graf:
            print(f"Węzeł źródłowy '{zrodlo}' nie istnieje w grafie.")
            return

        przed_usunieciem = len(self.graf[wezel_zrodlo])
        self.graf[wezel_zrodlo] = [
            krawedz for krawedz in self.graf[wezel_zrodlo]
            if krawedz.cel != wezel_cel
        ]
        po_usunieciu = len(self.graf[wezel_zrodlo])

        if przed_usunieciem != po_usunieciu:
            print(f"Krawędź z '{zrodlo}' do '{cel}' została usunięta.")
            if wezel_cel in self.graf:
                self.graf[wezel_cel] = [
                    krawedz for krawedz in self.graf[wezel_cel]
                    if krawedz.cel != wezel_zrodlo
                ]
        else:
            print(f"Krawędź z '{zrodlo}' do '{cel}' nie istnieje.")
