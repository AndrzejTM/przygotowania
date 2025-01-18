'''
    Zadanie 1
    Zaimplementuj program, który odwraca podany tekst za pomocą stosu.
    Program powinien działać w taki sposób, że każdy znak tekstu jest
    dodawany na stos, a następnie wyjmowany ze stosu, aby utworzyć
    odwrócony tekst.

    Zadanie 2
    Zaimplementuj program, który symuluje kolejkę w sklepie. Klienci
    są dodawani do kolejki, a następnie obsługiwani w kolejności
    przybycia (FIFO). Po obsłużeniu klient jest usuwany z kolejki.

    Zadanie 3
    Zaimplementuj system zarządzania zadaniami z wykorzystaniem
    kolejki priorytetowej, który umożliwia dynamiczne zmienianie
    priorytetów zadań. Zadania o wyższym priorytecie są przetwarzane
    szybciej. System powinien obsługiwać:
    - dodawanie zadań (nazwa, priorytet, czas)
    - modyfikacja priorytetów
    - podniesienie wartości priorytetu wraz z upływem czasu

    Zadanie dodatkowe:
    Do zadania 3 dodaj limit czasu po, którym zadanie ulegnie usunięciu
    z kolejki w razie jego niewykonania.


    ________________________________________________________________________
    Czas może być określony jako krok czasowy bądź czas systemowy:

    from datetime import datetime
    current_time = datetime.now()

    Do symulowania czasu trwania zadania można użyć
    import time
    time.sleep()

    Do implementacji zadań można skorzystac z list i ich funkcjonalności:
    - list.pop()
    - list.append()
    - list.sort()
'''


