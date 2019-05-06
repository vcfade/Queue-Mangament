"""
update this file to implement the following already declared methods:
- enqueue: Should add a member to the list
- dequeue: Should remove and return an element from the top or the bottom of the list (depending on the list mode: FIFO or LIFO)
- get_all: should return the entire list as it is
- size: Should return the total size of the list
"""

from random import randint

class Queue:

    def __init__(self, mode='FIFO'):
        self._queue = ['bob']
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = mode

    def enqueue(self, item):
        if self._mode == 'FIFO':
            self._queue.append(item)
            pass
        elif self._mode == 'LIFO':
            self._queue.insert(0, item)
            pass

    def dequeue(self):
        if self._queue:
            deq = self._queue.pop(0)
            return deq

        pass

    def get_all(self):

        return self._queue


    def size(self):

        return len(self._queue)