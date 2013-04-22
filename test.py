from heap import *
array = [5,1,10,9,0,2,4,3,8,7]
store = minheap(12,array)
store.insert(6)
store.delete_min()
store.insert(0)
store.insert(4)
store.delete_min()
store.delete_min()
store.delete_min()
store.delete_min()
store.delete_min()
store.graphviz("file.dot")
