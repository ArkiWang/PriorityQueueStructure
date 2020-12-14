from numpy import argmin

from Node import node
class FibonacciHeap(object):
    def __init__(self, min=None, n=0, root_list=[]):
        self.min = min
        self.n = n
        self.root_list = root_list

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
        if h2.key < h1.key:
            tmp = h1
            h1 = h2
            h2 =tmp
        h = h1
        h.child.extend(h2)
        h2.p = h
        h.degree = h1 + 1
        return h

    def Fib_Heap_Extract_Min(self):
        z = self.min
        if z != None:
            for c in z.child:
                self.root_list.append(c)
                c.p = None
            self.root_list.remove(z)
            """
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.Consolidate()
            """
            if len(self.root_list) == 0:
                self.min = None
            else:
                self.min = min(self.root_list)
                self.Consolidate()

            self.n -= 1
        return z

    def Fib_Heap_Link(self, y: node, x: node):
        self.root_list.remove(y)
        x.child.append(y)
        x.degree += 1
        y.mark = False

    def Consolidate(self):
        a = [None] * self.n
        for w in self.root_list:
            x = w
            d = x.degree
            while a[d] != None:
                y = a[d]
                if x.key > y.key:
                    #self.exchange(x, y)
                    tmp = x
                    x = y
                    y = tmp
                self.Fib_Heap_Link(y, x)
                a[d] = None
                d += 1
            a[d] = x
        self.min = None
        for i in range(self.n):
            if a[i] != None:
                if self.min == None:
                    self.root_list = [a[i]]
                    self.min = a[i]
                else:
                    self.root_list.append(a[i])
                    if a[i].key < self.min.key:
                        self.min = a[i]

    def Make_Fib_Heap(self):
        self.n = 0
        self.min = None

    def update_degree(self):
        for p in self.root_list:
            p.degree = len(p.child)

    def insert(self, x: int):
        x = node(x)
        self.Fib_Heap_Insert(x)
        self.update_degree()
        degrees = {}
        for e in self.root_list:
            if e.degree not in degrees:
                degrees[e.degree] = [e]
            else:
                tmp = degrees.get(e.degree)
                tmp.append(e)
                degrees[e.degree] = tmp
        new_root_list = []
        for key in degrees.keys():
            union_list = degrees.get(key)
            while len(union_list) > 1:
                h1 = union_list.pop()
                h2 = union_list.pop()
                h = self.Fib_Heap_Union(h1, h2)
                union_list.append(h)
            new_root_list.extend(union_list)
        self.root_list = new_root_list


















