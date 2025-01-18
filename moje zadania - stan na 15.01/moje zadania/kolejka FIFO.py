class FIFOQueue:
    """
    Klasa implementująca kolejkę FIFO (First In, First Out).
    Pierwszy element, który zostanie dodany, jest również pierwszym, który zostanie usunięty.
    """

    def __init__(self):
        """Inicjalizuje pustą kolejkę."""
        self.queue = []

    def enqueue(self, item):
        """
        Dodaje element na koniec kolejki.

        :param item: Element do dodania do kolejki.
        """
        self.queue.append(item)
        print(f"Element {item} został dodany do kolejki.")

    def dequeue(self):
        """
        Usuwa i zwraca pierwszy element z kolejki.

        :return: Pierwszy element kolejki.
        :raises IndexError: Jeśli kolejka jest pusta.
        """
        if self.is_empty():
            raise IndexError("Nie można usunąć elementu z pustej kolejki!")
        item = self.queue.pop(0)
        print(f"Element {item} został usunięty z kolejki.")
        return item

    def peek(self):
        """
        Zwraca pierwszy element w kolejce bez usuwania go.

        :return: Pierwszy element kolejki.
        :raises IndexError: Jeśli kolejka jest pusta.
        """
        if self.is_empty():
            raise IndexError("Kolejka jest pusta, brak elementów do podglądu!")
        return self.queue[0]

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
            print("Zawartość kolejki:", self.queue)


# Przykładowe użycie kolejki FIFO
if __name__ == "__main__":
    fifo_queue = FIFOQueue()

    # Dodawanie elementów do kolejki
    fifo_queue.enqueue(1)
    fifo_queue.enqueue(2)
    fifo_queue.enqueue(3)

    # Wyświetlanie zawartości kolejki
    fifo_queue.display()

    # Podgląd pierwszego elementu w kolejce
    print("Pierwszy element w kolejce:", fifo_queue.peek())

    # Usuwanie elementów z kolejki
    fifo_queue.dequeue()
    fifo_queue.dequeue()

    # Wyświetlanie zawartości po usunięciach
    fifo_queue.display()

    # Sprawdzenie rozmiaru kolejki
    print("Rozmiar kolejki:", fifo_queue.size())
