from heap import *
array = [5,1,10,9,0,2,4,3,8,7]
store = minheap(12,array)
store.insert(6)
store.graphviz("file.dot")
