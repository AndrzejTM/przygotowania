class Stack:
    def __init__(self):  # Tworzy pusty stos
        self.items = []

    def push(self, item):  # Dodaje element na stos
        self.items.append(item)

    def pop(self):  # Usuwa i zwraca element z wierzchu stosu
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):  # Sprawdza, czy stos jest pusty
        return len(self.items) == 0

    def size(self):  # Zwraca liczbę elementów na stosie
        return len(self.items)


def reverse_text_using_stack(text):
    stack = Stack()

    # Dodawanie znaków na stos
    for char in text:
        stack.push(char)

    # Wyjmowanie znaków ze stosu, aby odwrócić tekst
    reversed_text = ''
    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text

text = ("Programowanie")
reversed_text = reverse_text_using_stack(text)
print(reversed_text)
