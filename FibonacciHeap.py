from Node import node
class FibonacciHeap(object):
    def __init__(self):
        self.min = None
        self.n = 0
        self.root_list = []

    def Fib_Heap_Insert(self, x: node):
        x.degree = 0
        x.p = None
        x.child = None
        x.mark = False
        if self.min == None:
            self.min = x
            self.n = 1
        else:
            self.root_list.append(x)
            if x.key < self.min.key:
                self.min = x
        self.n += 1

    def Fib_Heap_Union(self, h1: node, h2: node):
        h = FibonacciHeap()
        h.min = h1.min
        h.root_list.extend(h2.root_list)
        if h1.min == None or (h2.min != None and h2.key < h1.min.key):
            h.min = h2.min
        h.n = h1.n + h2.n
        return h

    def Fib_Heap_Extract_Min(self):
        z = self.min
        if z != None:
            for 


