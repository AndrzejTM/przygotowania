from collections import deque  # Importujemy deque z modułu collections, który pozwala efektywnie zarządzać kolejką.

# Definiujemy klasę Queue, która implementuje podstawowe operacje na kolejce.
class Queue:
    def __init__(self):
        # Inicjalizujemy pustą kolejkę przy użyciu deque.
        self.items = deque()

    def enqueue(self, item):
        # Metoda dodaje element na koniec kolejki.
        self.items.append(item)

    def dequeue(self):
        # Metoda usuwa i zwraca element z początku kolejki.
        # Jeśli kolejka jest pusta, zwraca None.
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        # Metoda sprawdza, czy kolejka jest pusta.
        return len(self.items) == 0

    def size(self):
        # Metoda zwraca liczbę elementów w kolejce.
        return len(self.items)

# Funkcja symulująca kolejkę w sklepie.
def simulate_shop_queue():
    queue = Queue()  # Tworzymy obiekt kolejki.

    while True:
        # Wyświetlamy menu użytkownikowi.
        print("\nMenu:")
        print("1. Dodaj klienta do kolejki")
        print("2. Obsłuż klienta")
        print("3. Pokaż liczbę klientów w kolejce")
        print("4. Wyjdź")

        # Pobieramy wybór użytkownika.
        choice = input("Wybierz opcję: ")

        if choice == "1":
            # Jeśli użytkownik wybierze 1, dodajemy klienta do kolejki.
            client_name = input("Podaj imię klienta: ")
            queue.enqueue(client_name)
            print(f"Dodano klienta {client_name} do kolejki.")
        elif choice == "2":
            # Jeśli użytkownik wybierze 2, obsługujemy pierwszego klienta w kolejce.
            served_client = queue.dequeue()
            if served_client:
                print(f"Obsłużono klienta: {served_client}")
            else:
                print("Kolejka jest pusta. Brak klientów do obsłużenia.")
        elif choice == "3":
            # Jeśli użytkownik wybierze 3, pokazujemy liczbę klientów w kolejce.
            print(f"Liczba klientów w kolejce: {queue.size()}")
        elif choice == "4":
            # Jeśli użytkownik wybierze 4, kończymy symulację.
            print("Koniec symulacji.")
            break
        else:
            # Obsługa nieprawidłowego wyboru.
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

# Uruchamiamy symulację tylko wtedy, gdy plik jest uruchamiany bezpośrednio.
if __name__ == "__main__":
    simulate_shop_queue()

