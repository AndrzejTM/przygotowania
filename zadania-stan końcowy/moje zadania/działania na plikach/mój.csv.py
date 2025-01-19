import csv

# Ścieżki do plików
input_file = "produkty.csv"
output_file = "drogie_produkty.csv"

try:
    # Krok 1: Odczyt pliku CSV i filtrowanie produktów
    drogie_produkty = []  # Definiujemy listę wcześniej, aby była dostępna w całym kodzie

    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # Odczytaj nagłówek
        drogie_produkty.append(header)  # Dodaj nagłówek do listy

        # Filtrowanie produktów droższych niż 4.00 zł
        for row in reader:
            produkt, cena, Dostępność = row[0], float(row[1]), row[2]
            if cena > 4.00 and Dostępność != "Wysoka":
                drogie_produkty.append(row)

    # Krok 2: Zapis filtrowanych produktów do nowego pliku CSV
    with open(output_file, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(drogie_produkty)  # Zapisz nagłówek i filtrowane dane

    print(f"Produkty droższe niż 4.00 zł zostały zapisane w pliku '{output_file}'.")
except FileNotFoundError:
    print(f"Plik {input_file} nie istnieje.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
