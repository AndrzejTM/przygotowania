import threading
import random
import time

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.lock = threading.Lock()
        self.active = True  # Flaga kontrolująca działanie klientów

    def withdraw(self, client_id, amount):
        with self.lock:  # Synchronizacja dostępu do zasobów
            if not self.active:  # Jeśli flaga jest False, kończymy działanie
                return
            print(f"Klient {client_id} próbuje wypłacić {amount} zł.")
            if self.balance >= amount:
                self.balance -= amount
                print(f"Klient {client_id}: Wypłacono {amount} zł. Pozostałe saldo: {self.balance} zł.")
                if self.balance <= 0:
                    print("Saldo wynosi 0 zł. Zatrzymujemy operacje.")
                    self.active = False  # Zatrzymujemy działanie klientów
            else:
                print(f"Klient {client_id}: Brak wystarczających środków. Saldo: {self.balance} zł.")

# Funkcja symulująca działania klientów
def client_thread(account, client_id):
    while account.active:  # Działanie wątku tylko, gdy konto jest aktywne
        amount = random.randint(10, 50)  # Losowa kwota wypłaty
        account.withdraw(client_id, amount)
        time.sleep(random.uniform(0.5, 2))  # Losowy czas przerwy między operacjami

# Główna część programu
if __name__ == "__main__":
    # Inicjalizacja konta bankowego
    initial_balance = 100
    account = BankAccount(initial_balance)

    # Tworzenie wątków dla klientów
    threads = []
    for i in range(5):  # 5 klientów
        t = threading.Thread(target=client_thread, args=(account, i + 1))
        threads.append(t)
        t.start()

    # Czekamy na zakończenie działania wątków
    for t in threads:
        t.join()  # Dołączamy wątki, aby upewnić się, że wszystkie zakończyły działanie

    print("Symulacja zakończona.")
