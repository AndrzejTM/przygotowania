import csv

with open('students.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)

    suma_ocen = 0
    liczba_osob = 0

    for row in reader:
        suma_ocen += float(row['Srednia_ocen'])
        liczba_osob += 1
        print(row)

    if liczba_osob > 0:
        srednia = suma_ocen / liczba_osob
        print(f"Średnia ocen dla tych osób: {srednia:.2f}")
    else:
        print("Brak danych do obliczenia średniej.")

# Otwieramy plik wejściowy do odczytu
with open('students.csv', mode='r', newline='') as infile:
    reader = csv.DictReader(infile)

    # Przygotowujemy nagłówki do nowego pliku CSV, dodając kolumnę 'Status'
    fieldnames = reader.fieldnames + ['Status']

    # Otwieramy plik wyjściowy do zapisu
    with open('students_summary.csv', mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Zapisujemy nagłówki do nowego pliku
        writer.writeheader()

        # Iterujemy przez wiersze w pliku wejściowym
        for row in reader:
            # Przypisujemy status na podstawie średniej ocen
            srednia_ocen = float(row['Srednia_ocen'])
            if srednia_ocen >= 3.0:
                row['Status'] = 'Zaliczony'
            else:
                row['Status'] = 'Nie zaliczony'

            # Zapisujemy zaktualizowany wiersz do pliku wyjściowego
            writer.writerow(row)

print("Nowy plik students_summary.csv został zapisany.")
