import csv

# Wczytanie danych z pliku sales.csv
with open('sales.csv', mode='r', newline='') as infile:
    reader = csv.DictReader(infile, delimiter=',')

    # Wypisanie nagłówków, aby sprawdzić, jak wyglądają
    print("Nagłówki w pliku CSV:", reader.fieldnames)

    # Przygotowanie listy do przechowywania wyników sprzedaży
    sales_summary = []

    for row in reader:
        print(row)  # Wypisanie całego wiersza, aby sprawdzić dane

        produkt = row['Produkt']
        ilosc = float(row['Ilosc'])
        cena = float(row['Cena'])

        # Obliczenie łącznej sprzedaży dla danego produktu
        laczna_sprzedaz = ilosc * cena

        # Dodanie wyników do listy
        sales_summary.append({'Produkt': produkt, 'Sprzedaż': laczna_sprzedaz})

        # Wypisanie wyniku dla danego produktu
        print(f"{produkt}: {laczna_sprzedaz:.2f}")

# Zapisanie wyników do pliku sales_summary.csv
with open('sales_summary.csv', mode='w', newline='') as outfile:
    fieldnames = ['Produkt', 'Sprzedaż']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    # Zapisanie nagłówków
    writer.writeheader()

    # Zapisanie wyników sprzedaży
    writer.writerows(sales_summary)

print("Wyniki sprzedaży zostały zapisane w pliku sales_summary.csv.")

