import math

class minheap:
    def __init__(self,size,array=None):
        if array is not None: 
            assert size == len(array)
        self.size = size
        if array is None:
            self._store = [None] * size 
        else:
            self._store = array
            self.build_heap()

    
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

    def find_max(self):
        pass

    def delete_max(self):
        pass

    def increase_key(self):
        pass

    def insert(self,value):
        pass

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
