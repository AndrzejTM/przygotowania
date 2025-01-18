import threading


class EmptyQueueException(Exception):
    """Wyjątek rzucany przy próbie pobrania elementu z pustej kolejki."""
    pass


class ThreadSafeQueue:
    def __init__(self):
        self._queue = []
        self._lock = threading.Lock()

    def enqueue(self, item):
        with self._lock:
            self._queue.append(item)
            print(f"Enqueue: {item} (queue: {self._queue})")

    def dequeue(self):
        with self._lock:
            if not self._queue:
                raise EmptyQueueException("Dequeue attempted on an empty queue.")
            item = self._queue.pop(0)
            print(f"Dequeue: {item} (queue: {self._queue})")
            return item

    def peek(self):
        with self._lock:
            if not self._queue:
                raise EmptyQueueException("Peek attempted on an empty queue.")
            item = self._queue[0]
            print(f"Peek: {item} (queue: {self._queue})")
            return item

    def is_empty(self):
        with self._lock:
            return len(self._queue) == 0


def queue_operations(queue, operations):
    for op in operations:
        try:
            if op["action"] == "enqueue":
                queue.enqueue(op["value"])
            elif op["action"] == "dequeue":
                queue.dequeue()
            elif op["action"] == "peek":
                queue.peek()
        except EmptyQueueException as e:
            print(f"Exception: {e}")


if __name__ == "__main__":
    queue = ThreadSafeQueue()

    thread1_ops = [{"action": "enqueue", "value": 10}, {"action": "enqueue", "value": 20}, {"action": "dequeue"}]
    thread2_ops = [{"action": "enqueue", "value": 30}, {"action": "dequeue"}, {"action": "dequeue"}, {"action": "dequeue"}]

    thread1 = threading.Thread(target=queue_operations, args=(queue, thread1_ops))
    thread2 = threading.Thread(target=queue_operations, args=(queue, thread2_ops))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Final queue state:", queue._queue)
