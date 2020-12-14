class node(object):
    def __init__(self, key, mark=False, child=None, degree=0, p=None):
        self.key = key
        self.mark = mark
        self.child = child
        self.degree = degree
        self.p = p#parent