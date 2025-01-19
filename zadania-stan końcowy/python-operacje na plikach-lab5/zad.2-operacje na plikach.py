import os
import zipfile

# Ścieżka do pliku ZIP
zip_path = 'archive.zip'

# Katalog docelowy
output_dir = 'rozpakowane'

try:
    # Rozpakowanie pliku ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"Plik {zip_path} został rozpakowany do katalogu '{output_dir}'.")

    # Wyświetlenie rozmiaru każdego pliku w katalogu 'rozpakowane'
    for root, dirs, files in os.walk(output_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            print(f"{file_name} - {file_size} bajtów")

except FileNotFoundError:
    print(f"Błąd: Plik {zip_path} nie został znaleziony.")
except zipfile.BadZipFile:
    print(f"Błąd: Plik {zip_path} jest uszkodzony lub nie jest prawidłowym plikiem ZIP.")
except PermissionError:
    print("Błąd: Brak uprawnień do odczytu lub zapisu plików.")
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")
