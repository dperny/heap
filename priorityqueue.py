from heap import *

class PriorityQueue:
    """A python3 class implementing a naive priority queue

    Uses an array of linked-list based queues. enqueues are O(1),
    dequeues are O(m) where m is the number of priority levels, and removing
    the lowest priority item is O(m)

    becomes bounded, because priority levels are set on initialization
    """

    def __init__(self,capacity,levels):
        self._store = minheap(capacity)
        self._capacity = capacity
        self.size = 0

    def enqueue(self,packet):
        """adds an item to the queue. if the queue is full, 
        removes the lowest priority item and return that item
        else returns None"""

        # enqueue into the queue based on the priority value and the of the packet
        rval = self._store.insert(packet) 
        if rval is None:
            self.size += 1
        return rval
        
    def dequeue(self):
        """removes the highest priority item from the queue"""
        self.size -= 1
        return self._store.delete_min()


    def _discard(self):
        """private function that removes the lowest priority item

            not used in the heap-based PriorityQueue"""
        for i in range(len(self._store)):
            if not self._store[i].isEmpty():
                rval = self._store[i].discard()
                break
        self.size -= 1
        return rval

    def extract(self):
        """not useful in the heap-based PriorityQueue"""
        rlist = []
        for i in range(len(self._store)):
            rlist.append(self._store[i].extract())
        return rlist

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
