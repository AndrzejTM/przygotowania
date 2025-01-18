'''
Napisz program, który dla danego ciągu znaków oblicza tablicę
 numeryczną, gdzie każdy element tej tablicy odpowiada długości
 najdłuższego możliwego fragmentu na początku prefiksu ciągu,
 który jednocześnie kończy ten prefiks
'''
def compute_prefix_array(s):
    n = len(s)
    prefix_array = [0] * n

    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = prefix_array[j - 1]

        if s[i] == s[j]:
            j += 1

        prefix_array[i] = j

    return prefix_array

# Przykład użycia
if __name__ == "__main__":
    ciag = input("Podaj ciąg znaków: ")
    wynik = compute_prefix_array(ciag)
    print("Tablica prefiksów:", wynik)
