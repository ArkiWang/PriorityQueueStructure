from cmath import inf

from FibonacciHeapD.Node import node
class FibonacciHeap(object):

    def __init__(self, min=None, n=0):
        self.min = min
        self.n = n

    # insert to the left side of min node
    def Fib_Heap_Insert(self, x: node):
        if self.min == None:
            self.min = x
            self.n = 1
            self.min.left, self.min.right = self.min, self.min
        else:
            x.left = self.min.left
            self.min.left.right = x
            x.right = self.min
            self.min.left = x
            if x.key < self.min.key:
                self.min = x
        self.n += 1


    def Fib_Heap_Extract_Min(self):
        z = self.min
        if z != None:
            zc = z.child
            while zc != None and (zc == z.child or zc.right != zc):
                zc.p = None
                self.Fib_Heap_Insert(zc)
                zc = zc.right
            z.left.right = z.right
            z.right.left = z.left

            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.Consolidate()
            self.n -= 1
        return z

    def Fib_Heap_Link(self, y: node, x: node):
        y.left.right = y.right
        y.right.left = y.left
        xc = x.child
        if xc == None:
            xc = y
            xc.left, xc.right = xc, xc
        else:
            y.left = xc.left
            y.right = xc
            xc.left.right = y
            xc.left = y
        x.degree += 1
        y.mark = False

    def Consolidate(self):
        a = [None] * self.n
        w = self.min
        while w == self.min or w.right != w:
            x = w
            w = w.right
            d = x.degree
            # remove x from the double list
            x.left.right = x.right
            x.right.left = x.left
            while a[d] != None:
                y = a[d]
                if x.key > y.key:
                    x, y = y, x
                self.Fib_Heap_Link(y, x)
                a[d] = None
                d += 1
            a[d] = x
        self.min = None
        for i in range(self.n):
            if a[i] != None:
                self.Fib_Heap_Insert(a[i])


    def Make_Fib_Heap(self):
        self.n = 0
        self.min = None

    def Cut(self, x: node, y: node):
        if x == y.child:
            if x.right == x:
                y.child = None
            else:
                y.child = x.right
                x.right.right.left = y.child
                y.child.left = x.left
        else:
            x.left.right = x.right
            x.right.left = x.left
        x.p = None
        x.mark = False
        self.Fib_Heap_Insert(x)

    def Cascading_Cut(self, y: node):
        z = y.p
        if z is not None:
            if y.mark == False:
                y.mark = True
            else:
                self.Cut(y, z)
                self.Cascading_Cut(z)

    def Fib_Heap_Decrease_Key(self, x: node, k: int):
        if k > x.key:
            print("new key is greater than current key")
        x.key = k
        y = x.p
        if y != None and x.key < y.key:
            self.Cut(x, y)
            self.Cascading_Cut(y)
        if x.key < self.min.key:
            self.min = x

    def Fib_Heap_Delete(self, x: node):
        self.Fib_Heap_Decrease_Key(x, -inf)
        self.Fib_Heap_Extract_Min()




























