class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.next = None

class ListaJednokierunkowa:
    def __init__(self):
        self.glowa = None

    def dodajNaKoncu(self, wartosc):
        nowyWezel = Wezel(wartosc)

        if self.glowa is None:
            self.glowa = nowyWezel
            return

        obecnyWezel = self.glowa
        while obecnyWezel.next:
            obecnyWezel = obecnyWezel.next
        obecnyWezel.next = nowyWezel

    def usunNaKoncu(self):
        if self.glowa is None:
            print("Lista jest pusta")
            return

        if self.glowa.next is None:
            self.glowa = None
            return

        obecnyWezel = self.glowa
        while obecnyWezel.next.next:
            obecnyWezel = obecnyWezel.next

        obecnyWezel.next = None

    def wyswietlanie(self):
        if self.glowa is None:
            print("Lista jest pusta")
            return

        obecnyWezel = self.glowa
        while obecnyWezel:
            print(obecnyWezel.wartosc, end = " -> ")
            obecnyWezel = obecnyWezel.next
        print("None")

if __name__ == "__main__":
    lista = ListaJednokierunkowa()

    lista.dodajNaKoncu(1)
    lista.dodajNaKoncu(2)
    lista.dodajNaKoncu(3)


    lista.wyswietlanie()

    lista.usunNaKoncu()
    lista.wyswietlanie()
    lista.usunNaKoncu()
    lista.wyswietlanie()
    lista.usunNaKoncu()
    lista.wyswietlanie()