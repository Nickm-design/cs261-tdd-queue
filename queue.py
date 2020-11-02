# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# YOUR NAME

# Hint: pip3 install llist
from pyllist import sllist

class Queue:

    def __init__(self, data=None):
        self.data = sllist()

    def enqueue(self, value):
        self.data.append(value)
        
    def dequeue(self):
        return self.data.pop()

