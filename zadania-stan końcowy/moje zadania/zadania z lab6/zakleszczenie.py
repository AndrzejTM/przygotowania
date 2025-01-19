import threading
import time

# Funkcja pokazująca przykład zakleszczenia
# Dwa wątki będą próbowały zdobyć dwie blokady w różnej kolejności

def zadanie1():
    print("Wątek 1: próbuje zdobyć blokadę 1")
    with blokada1:
        print("Wątek 1: zdobył blokadę 1")
        time.sleep(1)  # Symulacja pracy
        print("Wątek 1: próbuje zdobyć blokadę 2")
        with blokada2:
            print("Wątek 1: zdobył blokadę 2")


def zadanie2():
    print("Wątek 2: próbuje zdobyć blokadę 2")
    with blokada2:
        print("Wątek 2: zdobył blokadę 2")
        time.sleep(1)  # Symulacja pracy
        print("Wątek 2: próbuje zdobyć blokadę 1")
        with blokada1:
            print("Wątek 2: zdobył blokadę 1")

# Tworzymy dwie blokady
blokada1 = threading.Lock()
blokada2 = threading.Lock()

# Tworzymy dwa wątki
watek1 = threading.Thread(target=zadanie1)
watek2 = threading.Thread(target=zadanie2)

# Uruchamiamy wątki
watek1.start()
watek2.start()

# Czekamy na zakończenie wątków
watek1.join()
watek2.join()

print("Program zakończony")

