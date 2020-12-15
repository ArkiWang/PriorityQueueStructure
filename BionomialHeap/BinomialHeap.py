from cmath import inf

from FibonacciHeap.Node import node
class BinomialHeap(object):
    def __init__(self, n=0, k=-1, root_list=None, min=None):
        self.n = n#nodes
        self.root_list = root_list
        self.min = min

    def insert(self, x: int):
        x = node(x)
        if self.root_list == None:
            self.root_list = [x]
        else:self.root_list.append(x)
        if self.min == None or self.min.key > x.key:
            self.min = x
        self.n += 1
        self.merge()

    #when order/degree of n1 and n2 are the same
    def merge_helper(self, n1: node, n2: node):
        if n1.key < n2.key:
            self.root_list.remove(n2)
            child = n1.child
            n1.child = n2
            n2.sibling = child
        else:
            self.root_list.remove(n1)
            child = n2.child
            n2.child = n1
            n1.sibling = child


    def merge(self):
        self.root_list = sorted(self.root_list, key=lambda x: x.degree)
        i = 0
        while i < len(self.root_list) - 1:
            if self.root_list[i].degree != self.root_list[i+1].degree:
                i += 1
            elif i+2 < len(self.root_list) and self.root_list[i].degree == self.root_list[i+2].degree:
                i += 1
            elif self.root_list[i].key <= self.root_list[i+1].key:
                self.root_list[i].degree += 1
                child = self.root_list[i].child
                self.root_list[i].child = self.root_list[i+1]
                self.root_list[i].child.parent = self.root_list[i]
                self.root_list[i].child.sibling = child
                self.root_list.__delitem__(i+1)
            else:
                self.root_list[i + 1].degree += 1
                child = self.root_list[i + 1].child
                self.root_list[i + 1].child = self.root_list[i]
                self.root_list[i + 1].child.parent = self.root_list[i + 1]
                self.root_list[i + 1].child.sibling = child
                self.root_list.__delitem__(i)

    def find_min(self):
        if self.root_list == None or self.n == 0:
            return None
        maxr = self.root_list[0]
        for ri in self.root_list:
            if maxr.key < ri.key:
                maxr = ri
        return maxr

    def decrease_key(self, x: node, k: int):
        x.key -= k
        while x.parent != None and x.key < x.parent.key:
            xk = x.key
            x.key = x.parent.key
            x.parent.key = xk
            x = x.parent
        if x.parent == None and x.key < self.min.key:
            self.min = x

    def delete_min(self):
        self.root_list.remove(self.min)
        child = self.min.child
        self.root_list.append(child)
        self.merge()
        while child.sibling != None:
            child = child.sibling
            self.root_list.append(child)
            self.merge()

    def delete_key(self, x: node):
        self.delete_key(x, inf)
        self.delete_min()








