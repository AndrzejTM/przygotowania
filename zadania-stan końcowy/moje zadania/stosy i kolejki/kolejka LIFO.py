class LIFOQueue:
    """
    Klasa implementująca kolejkę LIFO (Last In, First Out).
    Ostatni element, który zostanie dodany, jest pierwszym, który zostanie usunięty.
    """

    def __init__(self):
        """Inicjalizuje pustą kolejkę."""
        self.queue = []

    def push(self, item):
        """
        Dodaje element na górę stosu (kolejki LIFO).

        :param item: Element do dodania do kolejki.
        """
        self.queue.append(item)
        print(f"Element {item} został dodany na górę stosu.")

    def pop(self):
        """
        Usuwa i zwraca ostatni element z kolejki.

        :return: Ostatni element kolejki.
        :raises IndexError: Jeśli kolejka jest pusta.
        """
        if self.is_empty():
            raise IndexError("Nie można usunąć elementu z pustej kolejki!")
        item = self.queue.pop()
        print(f"Element {item} został usunięty ze stosu.")
        return item

    def peek(self):
        """
        Zwraca ostatni element w kolejce bez usuwania go.

        :return: Ostatni element kolejki.
        :raises IndexError: Jeśli kolejka jest pusta.
        """
        if self.is_empty():
            raise IndexError("Kolejka jest pusta, brak elementów do podglądu!")
        return self.queue[-1]

    def is_empty(self):
        """
        Sprawdza, czy kolejka jest pusta.

        :return: True, jeśli kolejka jest pusta; False w przeciwnym razie.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Zwraca liczbę elementów w kolejce.

        :return: Liczba elementów w kolejce.
        """
        return len(self.queue)

    def display(self):
        """
        Wyświetla wszystkie elementy w kolejce.
        """
        if self.is_empty():
            print("Kolejka jest pusta.")
        else:
            print("Zawartość stosu (LIFO):", self.queue)

    def reverse(self):
        """
        Odwraca kolejność elementów na stosie.
        """
        self.queue.reverse()
        print("Stos został odwrócony.")

    def find_index(self, item):
        """
        Znajduje indeks elementu na stosie, licząc od góry.

        :param item: Element, którego indeks jest wyszukiwany.
        :return: Indeks elementu (liczony od góry stosu).
        :raises ValueError: Jeśli element nie znajduje się na stosie.
        """
        try:
            return len(self.queue) - 1 - self.queue[::-1].index(item)
        except ValueError:
            raise ValueError(f"Element {item} nie znajduje się na stosie.")


# Przykładowe użycie kolejki LIFO
if __name__ == "__main__":
    lifo_queue = LIFOQueue()

    # Dodawanie elementów do kolejki
    lifo_queue.push(1)
    lifo_queue.push(2)
    lifo_queue.push(3)
    lifo_queue.push(6)
    lifo_queue.push(8)
    lifo_queue.push(4)

    # Wyświetlanie zawartości kolejki
    lifo_queue.display()

    # Podgląd ostatniego elementu w kolejce
    print("Ostatni element na stosie:", lifo_queue.peek())

    # Usuwanie elementów z kolejki
    lifo_queue.pop()
    lifo_queue.pop()

    # Wyświetlanie zawartości po usunięciach
    lifo_queue.display()

    # Sprawdzenie rozmiaru kolejki
    print("Rozmiar stosu:", lifo_queue.size())

    print(lifo_queue.find_index(2))
