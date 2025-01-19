import threading
import time


def zadanie1():
    while True:
        print("Wątek 1: próbuje zdobyć blokady")
        if blokada1.acquire(timeout=1):
            try:
                print("Wątek 1: zdobył blokadę 1")
                time.sleep(1)  # Symulacja pracy
                if blokada2.acquire(timeout=1):
                    try:
                        print("Wątek 1: zdobył blokadę 2")
                        break  # Sukces - przerwanie pętli
                    finally:
                        blokada2.release()
            finally:
                blokada1.release()
        time.sleep(0.1)  # Odpoczynek przed ponowną próbą


def zadanie2():
    while True:
        print("Wątek 2: próbuje zdobyć blokady")
        if blokada2.acquire(timeout=1):
            try:
                print("Wątek 2: zdobył blokadę 2")
                time.sleep(1)  # Symulacja pracy
                if blokada1.acquire(timeout=1):
                    try:
                        print("Wątek 2: zdobył blokadę 1")
                        break  # Sukces - przerwanie pętli
                    finally:
                        blokada1.release()
            finally:
                blokada2.release()
        time.sleep(0.1)  # Odpoczynek przed ponowną próbą
