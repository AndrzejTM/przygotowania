lista1 = ["programowanie", "Python", "zadanie", "student", "klasa"]

def odwracanie_słów():
    odwrocona_lista = [x[::-1] for x in lista1]
    return odwrocona_lista

wynik = odwracanie_słów()
print(wynik)


