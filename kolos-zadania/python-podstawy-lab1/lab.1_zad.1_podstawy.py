lista1 = ["Anna", "Krzysztof", "Marek", "Ewa", "Tomasz", "Aleksandra", "Piotr", "Magdalena"]

def najdluzsze_imie(lista1):
        return max(lista1, key=len)

najdłuższy = najdluzsze_imie(lista1)
print(f"Imię o najdłuższej liczbie znaków to: {najdłuższy}")