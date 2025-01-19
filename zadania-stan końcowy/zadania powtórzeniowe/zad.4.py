import threading
import queue
import time
import random


class CallCenter:
    def __init__(self, num_agents):
        """Inicjalizuje call center z podaną liczbą agentów."""
        self.call_queue = queue.Queue()  # Kolejka do przechowywania połączeń
        self.num_agents = num_agents  # Liczba agentów
        self.stop_event = threading.Event()  # Zatrzymanie symulacji

    def generate_calls(self, interval):
        """Generuje identyfikatory połączeń w regularnych odstępach czasu."""
        call_id = 1
        while not self.stop_event.is_set():
            self.call_queue.put(f"Połączenie-{call_id}")
            print(f"Nowe połączenie: Połączenie-{call_id}")
            call_id += 1
            time.sleep(interval)

    def agent_work(self, agent_id):
        """Agenci obsługujący połączenia z kolejki."""
        while not self.stop_event.is_set():
            try:
                # Pobierz połączenie z kolejki z oczekiwaniem
                call = self.call_queue.get(timeout=1)  # Timeout, by agent mógł się zatrzymać
                print(f"Agent-{agent_id} obsługuje: {call}")
                time.sleep(random.uniform(1, 3))  # Symulacja czasu obsługi połączenia
                print(f"Agent-{agent_id} zakończył obsługę: {call}")
                self.call_queue.task_done()
            except queue.Empty:
                # Jeśli kolejka jest pusta, agent czeka na nowe połączenie
                pass

    def start(self, call_interval):
        """Uruchamia generowanie połączeń i agentów."""
        self.stop_event.clear()

        # Uruchom wątek generujący połączenia
        generator_thread = threading.Thread(target=self.generate_calls, args=(call_interval,))
        generator_thread.daemon = True
        generator_thread.start()

        # Uruchom wątki agentów
        agent_threads = []
        for i in range(self.num_agents):
            thread = threading.Thread(target=self.agent_work, args=(i + 1,))
            thread.daemon = True
            thread.start()
            agent_threads.append(thread)

        # Pozwól symulacji działać przez pewien czas
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nZatrzymanie symulacji...")
            self.stop_event.set()
            generator_thread.join()  # Zatrzymanie generatora połączeń
            for thread in agent_threads:
                thread.join()  # Zatrzymanie agentów
            print("Symulacja zakończona.")


# Uruchomienie symulacji
if __name__ == "__main__":
    call_center = CallCenter(num_agents=3)
    call_interval = 2  # Interwał generowania połączeń w sekundach
    call_center.start(call_interval)
