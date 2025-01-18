class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __eq__(self, other):
        if isinstance(other, Wezel):
            return self.wartosc == other.wartosc
        return False

    def __hash__(self):
        return hash(self.wartosc)

    def __str__(self):
        return f"{self.wartosc}"

    def __repr__(self):
        return self.__str__()
