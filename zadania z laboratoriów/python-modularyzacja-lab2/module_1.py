class Task:
    def __init__(self, name, priority, time_added):
        self.name = name  # Nazwa zadania
        self.priority = priority  # Priorytet (mniejsza liczba oznacza wyższy priorytet)
        self.time_added = time_added  # Czas dodania zadania (timestamp)

    def __lt__(self, other):
        # Zdefiniowanie porównania dla zadań (do obsługi kolejki priorytetowej)
        # Priorytet jest najważniejszy, a jeśli priorytet jest taki sam, to porównujemy czas
        if self.priority == other.priority:
            return self.time_added < other.time_added
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(name={self.name}, priority={self.priority}, time_added={self.time_added})"