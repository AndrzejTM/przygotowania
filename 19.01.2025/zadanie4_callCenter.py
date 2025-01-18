'''
Napisz program symulujący działanie call center:
funkcja generująca identyfikatory połączeń w regularnych odstępach.
kolejka przechowująca przychodzące połączenia.
agenci reprezentowani przez 3 wątki, którzy pobierają połączenia
z kolejki (jeżeli jest pusta oczekują na połączenie)
'''
import threading
import queue
import time
import random

call_queue = queue.Queue()

def generate_calls():
    call_id = 1
    while True:
        time.sleep(2)
        call_queue.put(f"Call-{call_id}")
        print(f"Nowe połączenie: Call-{call_id}")
        call_id += 1

def handle_calls(agent_id):
    while True:
        if not call_queue.empty():
            call = call_queue.get()
            print(f"Agent-{agent_id} obsługuje {call}")
            time.sleep(3)
            print(f"Agent-{agent_id} zakończył {call}")
        else:
            print(f"Agent-{agent_id} czeka na połączenie...")
            time.sleep(1)

call_generator_thread = threading.Thread(target=generate_calls, daemon=True)

agents = []
for i in range(3):
    agent_thread = threading.Thread(target=handle_calls, args=(i + 1,), daemon=True)
    agents.append(agent_thread)

call_generator_thread.start()

for agent_thread in agents:
    agent_thread.start()

time.sleep(20)
print("Koniec symulacji.")
