class node(object):
    def __init__(self, key, mark=False, child=None, left=None, right=None, degree=0, p=None):
        self.key = key
        self.mark = mark
        self.child = child
        self.left = left
        self.right = right
        self.degree = degree
        self.p = p#parent