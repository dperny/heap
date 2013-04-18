from heap import *
array = [5,1,6,9,0,2,4,3,8,7]
store = minheap(len(array),array)
store.graphviz("file.dot")
