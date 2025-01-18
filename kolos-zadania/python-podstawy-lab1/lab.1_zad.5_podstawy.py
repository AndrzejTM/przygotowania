#imiona z dużej
lista1 = ["Emilia", "Krzysztof", "ela", "Marek", "Edward", "ewa", "Zbigniew", "Anna", "Eryk", "Ola"]

def imiona_na_e():
    szukane_imiona = [x for x in lista1 if x[0] == "e" or x[0] == "E"]
    return szukane_imiona

wynik = imiona_na_e()
print([x.upper() for x in wynik])

#imiona oryginalnie
lista2 = ["Emilia", "Krzysztof", "ela", "Marek", "Edward", "Ewa", "Zbigniew", "Anna", "Eryk", "Ola"]

def imiona_na_e_2():
    szukane_imiona_2 = [x for x in lista1 if x[0] == "e" or x[0] == "E"]
    return szukane_imiona_2

print(imiona_na_e_2())









