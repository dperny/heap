from heap import *

class interpreter:
    def __init__(self,filename):
        self.store = MinHeap()
        self._filename = filename + ".dot"
    
    def cinput(self,action):
        action = action.split(" ")
        if action[0] == "i":
            self.insert(int(action[1]))
        elif action[0] == "f":
            self.find(int(action[1]))
        elif action[0] == "d":
            self.delete(int(action[1]))
        elif action[0] == "t":
            self.test()
        elif action[0] == "s":
            self.swap(int(action[1]),int(action[2]))
        elif action[0] == "v":
            self.visualize()
        elif action[0] == "r":
            self.rotate(int(action[1]))
        elif action[0] == "l":
            self.load(action[1])
        elif action[0] == "q":
            self.quit()
            return False
        return True
        
    def insert(self,value):
        pass
    """
        selfstore.insert(value)
        print("{0} was inserted!".format(value))
        """
    
    def find(self,value):
        pass
    
    def delete(self,value):
        pass

    def test(self):
        pass
    """
        if self.store.verify():
            print("tree is not broken")
        else:
            print("tree is broken")
            """
    
    def swap(self,value,fault):
        pass

    def visualize(self):
        self.store.graphviz(self._filename)
        subprocess.call("dot -Tpng -O " + self._filename,shell=True)
        subprocess.call("eog "+self._filename+".png",shell=True)

    def rotate(self,value):
        pass

    def load(self,filename):
        outlist = []
        with open(filename) as fp:
            for line in fp:
                tokens = line.split()
                tokens = [int(i) for i in tokens]
                outlist = outlist + tokens
        for value in outlist:
            self.insert(value)

    def quit(self):
        subprocess.call("make clean",shell=True)

def main():
    cli = interpreter(filename)
    status = True
    while status:
        status = cli.cinput(input("> "))

if __name__ == '__main__':
    main()
