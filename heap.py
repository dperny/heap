import math
import copy

class minheap:
    def __init__(self,capacity,array=None):
        self.size = 0
        if array is None:
            self._store = [None] * size 
        else:
            self.size = len(array)
            self._store = copy.copy(array)
            self.build_heap()
        self.capacity = capacity

    
    def build_heap(self):
        for index in range(math.floor((self.size-1)/2),-1,-1):
            self.heapify(index)

    def heapify(self,index):
        left = (2 * index) + 1
        right = (2 * index) + 2
        smallest = index
        if left < self.size:
            if self._store[left] < self._store[smallest]:
                smallest = left
        if right < self.size:
            if self._store[right] < self._store[smallest]:
                smallest = right
        if smallest != index:
            self._store[smallest],self._store[index] = self._store[index],self._store[smallest]
            self.heapify(smallest)

    def find_min(self):
        return self._store[0]

    def delete_min(self):
        if self.size < 1:
            return None
        top = self._store[0]
        self._store[0] = self._store[self.size-1]
        self.size -= 1
        self.heapify(0)
        return top

    def decrease_key(self,index,key): 
        pass

    # odds are left, evens are right
    def insert(self,value):
        index = self.size
        parent = self._parent(index)
        self._store[index] = value
        while self._store[parent] >= self._store[index]:
            self._store[parent], self._store[index] = self._store[index], self._store[parent]
            index = parent
            parent = self._parent(index)
        self.size += 1


    def merge(self,value):
        pass

    def graphviz(self,filename):
        outstring = "digraph tree{\n"
        for index in range(self.size):
            left = (2 * index) + 1
            right = (2 * index) + 2
            if left < self.size:
                outstring = (outstring + 
                '\t"{0}" -> "{1}"\n'.format(self._store[index],
                                            self._store[left]))
            if right < self.size:
                outstring = (outstring + 
                '\t"{0}" -> "{1}"\n'.format(self._store[index],
                                            self._store[right]))
        outstring = outstring + "}"
    
        with open(filename,'w') as fp:
            fp.write(outstring)

    def _parent(self,index):
        return math.floor((index-1)/2)

