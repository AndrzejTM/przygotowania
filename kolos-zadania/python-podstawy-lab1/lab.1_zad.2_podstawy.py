#najkrótszy sposób, ale bez funkcji

#kwadraty = [x*x for x in range(15) if x %2 ==0]
#print(kwadraty)

#prawidłowy sposób
lista1 = list(range(15))

def kwadraty_parzystych():
    kwadraty_liczb = [x*x for x in lista1 if x%2 == 0]
    return kwadraty_liczb

wynik = kwadraty_parzystych()
print(wynik)








