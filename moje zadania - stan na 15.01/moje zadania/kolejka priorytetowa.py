import heapq


class PriorityQueue:
    """
    Klasa implementująca kolejkę priorytetową.
    Elementy są usuwane w kolejności ich priorytetów (najmniejszy priorytet jako pierwszy).
    """

    def __init__(self):
        """Inicjalizuje pustą kolejkę priorytetową."""
        self.queue = []  # Lista przechowująca elementy w postaci kopca

    def push(self, item, priority):
        """
        Dodaje element do kolejki priorytetowej.

        :param item: Element do dodania do kolejki.
        :param priority: Priorytet elementu (im mniejsza liczba, tym wyższy priorytet).
        """
        heapq.heappush(self.queue, (priority, item))
        print(f"Element '{item}' z priorytetem {priority} został dodany do kolejki.")

    def pop(self):
        """
        Usuwa i zwraca element o najwyższym priorytecie.

        :return: Element o najwyższym priorytecie.
        :raises IndexError: Jeśli kolejka jest pusta.
        """
        if self.is_empty():
            raise IndexError("Nie można usunąć elementu z pustej kolejki!")
        priority, item = heapq.heappop(self.queue)
        print(f"Element '{item}' z priorytetem {priority} został usunięty z kolejki.")
        return item

    def peek(self):
        """
        Zwraca element o najwyższym priorytecie bez jego usuwania.

        :return: Element o najwyższym priorytecie.
        :raises IndexError: Jeśli kolejka jest pusta.
        """
        if self.is_empty():
            raise IndexError("Kolejka jest pusta, brak elementów do podglądu!")
        priority, item = self.queue[0]
        return item

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
        Wyświetla wszystkie elementy w kolejce wraz z ich priorytetami.
        """
        if self.is_empty():
            print("Kolejka jest pusta.")
        else:
            print("Zawartość kolejki (priorytet, element):", self.queue)


# Przykładowe użycie kolejki priorytetowej
if __name__ == "__main__":
    pq = PriorityQueue()

    # Dodawanie elementów do kolejki
    pq.push("Zadanie A", 2)
    pq.push("Zadanie B", 1)
    pq.push("Zadanie C", 3)

    # Wyświetlanie zawartości kolejki
    pq.display()

    # Podgląd elementu o najwyższym priorytecie
    print("Element o najwyższym priorytecie:", pq.peek())

    # Usuwanie elementów z kolejki
    pq.pop()
    pq.pop()

    # Wyświetlanie zawartości po usunięciach
    pq.display()

    # Sprawdzenie rozmiaru kolejki
    print("Rozmiar kolejki:", pq.size())
