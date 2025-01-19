class TaskManager:
    def __init__(self):
        self.task_queue = []  # Kopiec do przechowywania zadań

    def add_task(self, name, priority, time_added=None):
        """Dodaje zadanie do kolejki priorytetowej"""
        if time_added is None:
            time_added = time.time()  # Aktualny czas (w sekundach)
        task = Task(name, priority, time_added)
        heapq.heappush(self.task_queue, task)
        print(f"Zadanie '{name}' dodane do kolejki z priorytetem {priority}.")

    def modify_priority(self, name, new_priority):
        """Modyfikuje priorytet zadania, usuwając je z kolejki i ponownie dodając"""
        found_task = None
        for task in self.task_queue:
            if task.name == name:
                found_task = task
                break

        if found_task:
            # Usuwamy zadanie z kolejki (usunięcie i ponowne dodanie)
            self.task_queue.remove(found_task)
            heapq.heapify(self.task_queue)
            # Dodajemy je ponownie z nowym priorytetem
            self.add_task(name, new_priority, found_task.time_added)
            print(f"Priorytet zadania '{name}' został zmieniony na {new_priority}.")
        else:
            print(f"Zadanie o nazwie '{name}' nie zostało znalezione.")

    def promote_task(self, name):
        """Podnosi priorytet zadania w zależności od upływającego czasu"""
        found_task = None
        for task in self.task_queue:
            if task.name == name:
                found_task = task
                break

        if found_task:
            new_priority = max(1, found_task.priority - 1)  # Zwiększamy priorytet (zmniejszamy liczbę)
            self.modify_priority(name, new_priority)
            print(f"Priorytet zadania '{name}' został podniesiony do {new_priority}.")
        else:
            print(f"Zadanie o nazwie '{name}' nie zostało znalezione.")

    def process_task(self):
        """Przetwarza zadanie o najwyższym priorytecie"""
        if self.task_queue:
            task = heapq.heappop(self.task_queue)
            print(f"Przetwarzamy zadanie: '{task.name}' z priorytetem {task.priority}.")
        else:
            print("Brak zadań w kolejce do przetworzenia.")

    def display_tasks(self):
        """Wyświetla wszystkie zadania w kolejce"""
        if self.task_queue:
            print("Zadania w kolejce:")
            for task in self.task_queue:
                print(task)
        else:
            print("Brak zadań w kolejce.")