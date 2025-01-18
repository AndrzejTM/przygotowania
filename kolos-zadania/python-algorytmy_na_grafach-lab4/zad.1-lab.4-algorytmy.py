graf = {
'A': ['B', 'C', 'D'],
'B': ['A', 'C', 'F'],
'C': ['A', 'B', 'D', 'G','H'],
'D': ['A', 'C', 'H'],
'E': ['F', 'J'],
'F': ['B', 'E', 'J'],
'G': ['C','D'],
'H': ['D'],
'I': ['J'],
'J': ['F', 'E', 'I']
}

def oblicz_stopien(graf):
    stopnie = {}
    for osoba, sasiedzi in graf.items():
        stopnie[osoba] = len(sasiedzi)  # Stopień węzła to liczba sąsiadów
    return stopnie

def znajdz_osoby_z_max_min_stopniem(stopnie):
    max_osoba = max(stopnie, key=stopnie.get)  # Osoba o najwyższym stopniu
    min_osoba = min(stopnie, key=stopnie.get)  # Osoba o najniższym stopniu
    return max_osoba, stopnie[max_osoba], min_osoba, stopnie[min_osoba]

stopnie = oblicz_stopien(graf)
max_osoba, max_stopien, min_osoba, min_stopien = znajdz_osoby_z_max_min_stopniem(stopnie)

print(f"\nOsoba z najwyższym stopniem: {max_osoba} ({max_stopien} znajomych)")
print(f"Osoba z najniższym stopniem: {min_osoba} ({min_stopien} znajomych)")