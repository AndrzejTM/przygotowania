import zipfile
import os

# Pełna ścieżka do pliku ZIP
zip_path = r"C:\Users\user\PycharmProjects\test\Programowanie - kolos\moje zadania\działania na plikach\przykladowe_pliki.zip"
extract_dir = "rozpakowane_pliki"

# Krok 1: Rozpakowanie pliku ZIP
try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Plik ZIP został rozpakowany do folderu: {extract_dir}")
except FileNotFoundError:
    print(f"Plik {zip_path} nie istnieje. Upewnij się, że plik ZIP jest dostępny.")
    exit()

# Krok 2: Sprawdzanie rozmiarów plików
print("\nRozmiary plików:")
try:
    for file_name in os.listdir(extract_dir):
        file_path = os.path.join(extract_dir, file_name)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            print(f"Plik: {file_name}, Rozmiar: {file_size} bajtów")
except Exception as e:
    print(f"Wystąpił błąd podczas sprawdzania plików: {e}")
