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

    def increase_priority_over_time(self, time_increment):
        """
        Zwiększa priorytet wszystkich elementów w kolejce wraz z upływem czasu.

        :param time_increment: Liczba określająca, o ile należy zmniejszyć wartość priorytetów.
        """
        updated_queue = []
        while self.queue:
            priority, item = heapq.heappop(self.queue)
            # Zmniejsz priorytet (im mniejsza liczba, tym wyższy priorytet)
            new_priority = max(0, priority - time_increment)
            heapq.heappush(updated_queue, (new_priority, item))
        self.queue = updated_queue
        print(f"Zwiększono priorytety wszystkich elementów o {time_increment}.")

# Przykładowe użycie kolejki priorytetowej
if __name__ == "__main__":
    # Inicjalizacja kolejki priorytetowej
    pq = PriorityQueue()

    # Dodawanie elementów do kolejki
    pq.push("Zadanie A", 5)
    pq.push("Zadanie B", 2)
    pq.push("Zadanie C", 7)
    pq.push("Zadanie D", 3)
    #pq.pop()

    # Wyświetlanie zawartości kolejki
    print("Początkowa zawartość kolejki:")
    pq.display()

    # Zwiększenie priorytetu o 2 jednostki
    print("\nZwiększenie priorytetów o 2:")
    pq.increase_priority_over_time(2)
    pq.display()

    # Wyświetlenie elementu o najwyższym priorytecie
    print("\nElement o najwyższym priorytecie:", pq.peek())

    # Usunięcie elementu o najwyższym priorytecie
    print("\nUsuwanie elementu o najwyższym priorytecie:")
    pq.pop()
    pq.display()

    # Kolejne zwiększenie priorytetów
    print("\nZwiększenie priorytetów o 1:")
    pq.increase_priority_over_time(1)
    pq.display()

    # Rozmiar kolejki
    print("\nRozmiar kolejki:", pq.size())

    # Usunięcie wszystkich elementów
    print("\nUsuwanie wszystkich elementów:")
    while not pq.is_empty():
        pq.pop()
    pq.display()
