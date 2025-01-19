import threading
import time


def zadanie1():
    print("Wątek 1: próbuje zdobyć blokadę 1")
    with blokada1:
        print("Wątek 1: zdobył blokadę 1")
        time.sleep(1)  # Symulacja pracy
        print("Wątek 1: próbuje zdobyć blokadę 2")
        with blokada2:
            print("Wątek 1: zdobył blokadę 2")


def zadanie2():
    print("Wątek 2: próbuje zdobyć blokadę 1")  # Zmiana kolejności zdobywania blokad
    with blokada1:
        print("Wątek 2: zdobył blokadę 1")
        time.sleep(1)  # Symulacja pracy
        print("Wątek 2: próbuje zdobyć blokadę 2")
        with blokada2:
            print("Wątek 2: zdobył blokadę 2")
