class Node:
    """Klasa reprezentująca węzeł drzewa BST."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """Klasa reprezentująca drzewo BST."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Wstawia nowy element do drzewa."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Rekurencyjne wstawianie do drzewa."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self, node=None, result=None):
        """Przeszukiwanie IN-ORDER."""
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.left:
            self.in_order_traversal(node.left, result)
        result.append(node.value)
        if node.right:
            self.in_order_traversal(node.right, result)
        return result

    def search(self, value):
        """Wyszukuje wartość w drzewie."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Rekurencyjne wyszukiwanie wartości."""
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


# Funkcje pomocnicze
def read_from_file(baza_do_3):
    """Wczytuje dane z pliku i zwraca listę wartości."""
    with open("baza_do_3", "r") as file:
        return [int(line.strip()) for line in file.readlines()]

def write_to_file(wynik_3, data):
    """Zapisuje dane do pliku."""
    with open("wynik_3", "w") as file:
        file.write("\n".join(map(str, data)))

# Główna część programu
if __name__ == "__main__":
    # Utworzenie obiektu drzewa BST
    bst = BST()

    # Wczytanie danych z pliku
    input_file = "baza_do_3"
    output_file = "wynik_3"
    data = read_from_file(input_file)

    # Wstawianie danych do drzewa
    for value in data:
        bst.insert(value)

    # Przeszukiwanie IN-ORDER i zapis wyniku do pliku
    in_order_result = bst.in_order_traversal()
    write_to_file(output_file, in_order_result)
    print(f"Wynik przeszukiwania IN-ORDER zapisano do pliku: {output_file}")

    # Wyszukiwanie wartości w drzewie
    search_value = int(input("Podaj wartość do wyszukania: "))
    if bst.search(search_value):
        print(f"Wartość {search_value} znajduje się w drzewie.")
    else:
        print(f"Wartość {search_value} NIE znajduje się w drzewie.")
