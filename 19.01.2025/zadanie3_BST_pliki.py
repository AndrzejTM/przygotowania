'''
Napisz program, który odczyta dane z pliku i wstawi je do drzewa BST.
Wykona przeszukanie IN-ORDER zapisując wynik do pliku.
Umożliwi wyszukiwanie konkretnych danych w drzewie zwracając
informację czy się one znajdują w tej strukturze.
'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def in_order_traversal(self, node, result):
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.key)
            self.in_order_traversal(node.right, result)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None:
            return False
        if current.key == key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)


def read_data_from_file(filename):
    try:
        with open(filename, "r") as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except ValueError:
        print("File contains non-integer values.")
        return []


def write_data_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            for item in data:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Error writing to file {filename}: {e}")


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    data = read_data_from_file(input_file)
    if not data:
        return

    bst = BST()
    for item in data:
        bst.insert(item)

    result = []
    bst.in_order_traversal(bst.root, result)
    write_data_to_file(output_file, result)
    print(f"In-order traversal written to {output_file}.")

    while True:
        search_value = input("Enter a value to search in BST (or type 'exit' to quit): ")
        if search_value.lower() == "exit":
            break
        try:
            search_value = int(search_value)
            found = bst.search(search_value)
            if found:
                print(f"Value {search_value} is present in the BST.")
            else:
                print(f"Value {search_value} is not found in the BST.")
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
