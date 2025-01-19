import threading

class EmptyStackException(Exception):
    """Wyjątek zgłaszany, gdy próbujemy pobrać element z pustego stosu."""
    pass

class ThreadSafeStack:
    def __init__(self):
        """Inicjalizuje pusty stos i lock do synchronizacji."""
        self.stack = []
        self.lock = threading.Lock()

    def push(self, value):
        """Dodaje element na stos."""
        with self.lock:
            self.stack.append(value)
            print(f"Push: {value} (stos: {self.stack})")

    def pop(self):
        """Usuwa i zwraca element ze szczytu stosu. Zgłasza wyjątek, jeśli stos jest pusty."""
        with self.lock:
            if not self.stack:
                raise EmptyStackException("Stos jest pusty!")
            value = self.stack.pop()
            print(f"Pop: {value} (stos: {self.stack})")
            return value

    def peek(self):
        """Zwraca element ze szczytu stosu bez usuwania go. Zgłasza wyjątek, jeśli stos jest pusty."""
        with self.lock:
            if not self.stack:
                raise EmptyStackException("Stos jest pusty!")
            value = self.stack[-1]
            print(f"Peek: {value} (stos: {self.stack})")
            return value

# Funkcje do współbieżnej pracy z wątkami
def thread_function_push(stack, values):
    """Funkcja dodająca elementy na stos w wątku."""
    for value in values:
        stack.push(value)

def thread_function_pop(stack, count):
    """Funkcja usuwająca elementy ze stosu w wątku."""
    for _ in range(count):
        try:
            stack.pop()
        except EmptyStackException as e:
            print(f"Wyjątek: {e}")

# Test współbieżnego dostępu
if __name__ == "__main__":
    stack = ThreadSafeStack()

    # Wątki do operacji push
    thread1 = threading.Thread(target=thread_function_push, args=(stack, [1, 2, 3]))
    thread2 = threading.Thread(target=thread_function_push, args=(stack, [4, 5, 6]))

    # Wątki do operacji pop
    thread3 = threading.Thread(target=thread_function_pop, args=(stack, 4))
    thread4 = threading.Thread(target=thread_function_pop, args=(stack, 4))

    # Uruchamiamy wątki
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Czekamy na zakończenie wątków
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print("Wszystkie operacje zakończone.")
