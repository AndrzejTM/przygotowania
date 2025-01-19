def czytaj_długi_tekst(yield_ćwiczenie):
    with open(yield_ćwiczenie, "r") as file:
        for line in file:
            yield line

for line in czytaj_długi_tekst("yield_ćwiczenie"):
    print(line)

