'''
Zaimplementuj klasę ThreadSafeStack stos bezpieczny dla wątków
z metodami push, pop, peek, obsługujący wyjątek przy pobieraniu
 z pustego stosu, synchronizujący dostęp przy pomocy Lock.
 Następnie uruchom kilka wątków konkurencyjnie modyfikujących
 stos i zaprezentuj obsługę wyjątków.
'''
import threading


class EmptyStackException(Exception):
    """Wyjątek rzucany przy próbie pobrania elementu z pustego stosu."""
    pass


class ThreadSafeStack:
    def __init__(self):
        self._stack = []
        self._lock = threading.Lock()

    def push(self, item):
        with self._lock:
            self._stack.append(item)
            print(f"Push: {item} (stack: {self._stack})")

    def pop(self):
        with self._lock:
            if not self._stack:
                raise EmptyStackException("Pop attempted on an empty stack.")
            item = self._stack.pop()
            print(f"Pop: {item} (stack: {self._stack})")
            return item

    def peek(self):
        with self._lock:
            if not self._stack:
                raise EmptyStackException("Peek attempted on an empty stack.")
            item = self._stack[-1]
            print(f"Peek: {item} (stack: {self._stack})")
            return item

    def is_empty(self):
        with self._lock:
            return len(self._stack) == 0


def stack_operations(stack, operations):
    for op in operations:
        try:
            if op["action"] == "push":
                stack.push(op["value"])
            elif op["action"] == "pop":
                stack.pop()
            elif op["action"] == "peek":
                stack.peek()
        except EmptyStackException as e:
            print(f"Exception: {e}")


if __name__ == "__main__":

    stack = ThreadSafeStack()

    thread1_ops = [{"action": "push", "value": 10}, {"action": "push", "value": 20}, {"action": "pop"}]
    thread2_ops = [{"action": "push", "value": 30}, {"action": "pop"}, {"action": "pop"}, {"action": "pop"}]

    thread1 = threading.Thread(target=stack_operations, args=(stack, thread1_ops))
    thread2 = threading.Thread(target=stack_operations, args=(stack, thread2_ops))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Final stack state:", stack._stack)
