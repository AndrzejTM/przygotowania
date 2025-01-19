import heapq  # Moduł heapq pozwala na użycie kolejki priorytetowej.
import time  # Moduł time używany do obsługi czasu (np. pomiar czasu życia zadania).

# Klasa zarządzająca kolejką priorytetową zadań.
class PriorityTaskQueue:
    def __init__(self):
        # Kolejka priorytetowa przechowuje zadania w postaci krotek: (-priorytet, czas_utworzenia, max_time, nazwa).
        self.heap = []
        # Słownik mapujący nazwy zadań na ich właściwości, aby można je było łatwo modyfikować.
        self.task_map = {}

    def add_task(self, name, priority, max_time):
        """
        Dodaje nowe zadanie do kolejki priorytetowej.
        :param name: Nazwa zadania.
        :param priority: Priorytet zadania (im wyższy, tym szybciej będzie przetwarzane).
        :param max_time: Maksymalny czas życia zadania w sekundach.
        """
        current_time = time.time()  # Aktualny czas.
        # Dodajemy zadanie do kolejki z negatywnym priorytetem (max-heap) i do słownika.
        heapq.heappush(self.heap, (-priority, current_time, max_time, name))
        self.task_map[name] = (-priority, current_time, max_time)
        print(f"Dodano zadanie: {name}, Priorytet: {priority}, Maksymalny czas życia: {max_time}s.")

    def modify_priority(self, name, new_priority):
        """
        Modyfikuje priorytet istniejącego zadania.
        :param name: Nazwa zadania.
        :param new_priority: Nowy priorytet zadania.
        """
        if name in self.task_map:
            # Jeśli zadanie istnieje, usuwamy je z kolejki i dodajemy z nowym priorytetem.
            _, created_time, max_time = self.task_map[name]
            self.remove_task(name)
            self.add_task(name, new_priority, max_time)
            print(f"Zmieniono priorytet zadania {name} na {new_priority}.")
        else:
            print(f"Zadanie {name} nie istnieje.")

    def remove_task(self, name):
        """
        Usuwa zadanie z kolejki priorytetowej.
        :param name: Nazwa zadania.
        """
        if name in self.task_map:
            del self.task_map[name]  # Usuwamy zadanie ze słownika.
        # Tworzymy nową kolejkę bez usuwanego zadania.
        self.heap = [(p, t, m, n) for p, t, m, n in self.heap if n != name]
        heapq.heapify(self.heap)  # Odbudowujemy kolejkę.

    def process_task(self):
        """
        Przetwarza zadanie o najwyższym priorytecie.
        """
        current_time = time.time()
        while self.heap:
            # Pobieramy zadanie o najwyższym priorytecie.
            priority, created_time, max_time, name = heapq.heappop(self.heap)
            # Sprawdzamy, czy zadanie przekroczyło maksymalny czas życia.
            if current_time - created_time > max_time:
                print(f"Zadanie {name} zostało usunięte z powodu przekroczenia czasu.")
                if name in self.task_map:
                    del self.task_map[name]
                continue  # Przechodzimy do kolejnego zadania.
            # Przetwarzamy zadanie.
            print(f"Przetwarzanie zadania: {name}, Priorytet: {-priority}.")
            if name in self.task_map:
                del self.task_map[name]
            return
        print("Brak zadań do przetworzenia.")

    def increase_priority_over_time(self):
        """
        Podnosi priorytet zadań w miarę upływu czasu.
        """
        current_time = time.time()
        updated_tasks = []
        for priority, created_time, max_time, name in self.heap:
            elapsed_time = current_time - created_time
            # Zwiększamy priorytet o 1 co 10 sekund, jeśli zadanie wciąż istnieje.
            new_priority = -priority + int(elapsed_time // 10)
            updated_tasks.append((-new_priority, created_time, max_time, name))
            self.task_map[name] = (-new_priority, created_time, max_time)
        # Aktualizujemy kolejkę priorytetową.
        self.heap = updated_tasks
        heapq.heapify(self.heap)

    def show_tasks(self):
        """
        Wyświetla aktualną zawartość kolejki priorytetowej.
        """
        print("Aktualne zadania w kolejce:")
        for priority, created_time, max_time, name in sorted(self.heap, reverse=True):
            remaining_time = max_time - (time.time() - created_time)
            print(f"Zadanie: {name}, Priorytet: {-priority}, Pozostały czas: {remaining_time:.2f}s")

if __name__ == "__main__":
    queue = PriorityTaskQueue()

    while True:
        print("\nMenu:")
        print("1. Dodaj zadanie")
        print("2. Zmień priorytet zadania")
        print("3. Przetwórz zadanie o najwyższym priorytecie")
        print("4. Wyświetl kolejkę zadań")
        print("5. Wyjdź")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            name = input("Podaj nazwę zadania: ")
            priority = int(input("Podaj priorytet zadania (liczba całkowita): "))
            max_time = int(input("Podaj maksymalny czas życia zadania (w sekundach): "))
            queue.add_task(name, priority, max_time)
        elif choice == "2":
            name = input("Podaj nazwę zadania do zmiany priorytetu: ")
            new_priority = int(input("Podaj nowy priorytet zadania: "))
            queue.modify_priority(name, new_priority)
        elif choice == "3":
            queue.process_task()
        elif choice == "4":
            queue.show_tasks()
        elif choice == "5":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

