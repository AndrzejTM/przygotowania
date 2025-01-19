def oblicz_tablice_prefiksow(ciag):
    """
    Oblicza tablicę prefiksów dla danego ciągu znaków.

    :param ciag: Ciąg znaków (string)
    :return: Lista długości najdłuższego możliwego fragmentu będącego prefiksem i sufiksem
    """
    dlugosc_ciagu = len(ciag)
    tablica_prefiksow = [0] * dlugosc_ciagu  # Inicjalizacja tablicy wynikowej
    dlugosc_prefiksu = 0  # Długość bieżącego prefiksu będącego sufiksem

    # Iterujemy po ciągu od drugiego znaku
    for i in range(1, dlugosc_ciagu):
        # Dopóki długość prefiksu nie pasuje do bieżącego znaku, cofamy się
        while dlugosc_prefiksu > 0 and ciag[dlugosc_prefiksu] != ciag[i]:
            dlugosc_prefiksu = tablica_prefiksow[dlugosc_prefiksu - 1]

        # Jeśli bieżący znak pasuje, zwiększamy długość prefiksu
        if ciag[dlugosc_prefiksu] == ciag[i]:
            dlugosc_prefiksu += 1

        # Zapisujemy długość prefiksu w tablicy
        tablica_prefiksow[i] = dlugosc_prefiksu

    return tablica_prefiksow


# Przykład użycia
if __name__ == "__main__":
    ciag = input("Podaj ciąg znaków: ")
    wynik = oblicz_tablice_prefiksow(ciag)
    print(f"Tablica prefiksów dla ciągu '{ciag}': {wynik}")
